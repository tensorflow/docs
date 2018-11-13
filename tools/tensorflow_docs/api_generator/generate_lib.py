# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Generate docs for the TensorFlow Python API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import fnmatch
import os
import shutil
import subprocess
import tempfile
import six

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import pretty_docs
from tensorflow_docs.api_generator import public_api
from tensorflow_docs.api_generator import py_guide_parser
from tensorflow_docs.api_generator import tf_inspect
from tensorflow_docs.api_generator import traverse


def write_docs(output_dir,
               parser_config,
               yaml_toc,
               root_title='TensorFlow',
               search_hints=True,
               site_path=''):
  """Write previously extracted docs to disk.

  Write a docs page for each symbol included in the indices of parser_config to
  a tree of docs at `output_dir`.

  Symbols with multiple aliases will have only one page written about
  them, which is referenced for all aliases.

  Args:
    output_dir: Directory to write documentation markdown files to. Will be
      created if it doesn't exist.
    parser_config: A `parser.ParserConfig` object, containing all the necessary
      indices.
    yaml_toc: Set to `True` to generate a "_toc.yaml" file.
    root_title: The title name for the root level index.md.
    search_hints: (bool) include meta-data search hints at the top of each
      output file.
    site_path: The output path relative to the site root. Used in the
      `_toc.yaml` and `_redirects.yaml` files.

  Raises:
    ValueError: if `output_dir` is not an absolute path
  """
  # Make output_dir.
  if not os.path.isabs(output_dir):
    raise ValueError("'output_dir' must be an absolute path.\n"
                     "    output_dir='%s'" % output_dir)

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # These dictionaries are used for table-of-contents generation below
  # They will contain, after the for-loop below::
  #  - module name(string):classes and functions the module contains(list)
  module_children = {}
  #  - symbol name(string):pathname (string)
  symbol_to_file = {}

  # Collect redirects for an api _redirects.yaml file.
  redirects = []

  # Parse and write Markdown pages, resolving cross-links (`tf.symbol`).
  for full_name, py_object in six.iteritems(parser_config.index):
    parser_config.reference_resolver.current_doc_full_name = full_name

    if full_name in parser_config.duplicate_of:
      continue

    # Methods and some routines are documented only as part of their class.
    if not (tf_inspect.ismodule(py_object) or tf_inspect.isclass(py_object) or
            parser.is_free_function(py_object, full_name, parser_config.index)):
      continue

    sitepath = os.path.join('api_docs/python',
                            parser.documentation_path(full_name)[:-3])

    # For TOC, we need to store a mapping from full_name to the file
    # we're generating
    symbol_to_file[full_name] = sitepath

    # For a module, remember the module for the table-of-contents
    if tf_inspect.ismodule(py_object):
      if full_name in parser_config.tree:
        module_children.setdefault(full_name, [])

    # For something else that's documented,
    # figure out what module it lives in
    else:
      subname = str(full_name)
      while True:
        subname = subname[:subname.rindex('.')]
        if tf_inspect.ismodule(parser_config.index[subname]):
          module_children.setdefault(subname, []).append(full_name)
          break

    # Generate docs for `py_object`, resolving references.
    page_info = parser.docs_for_object(full_name, py_object, parser_config)

    path = os.path.join(output_dir, parser.documentation_path(full_name))
    directory = os.path.dirname(path)
    try:
      if not os.path.exists(directory):
        os.makedirs(directory)
      # This function returns raw bytes in PY2 or unicode in PY3.
      if search_hints:
        content = [page_info.get_metadata_html()]
      else:
        content = ['']

      content.append(pretty_docs.build_md_page(page_info))
      text = '\n'.join(content)
      if six.PY3:
        text = text.encode('utf-8')
      with open(path, 'wb') as f:
        f.write(text)
    except OSError:
      raise OSError(
          'Cannot write documentation for %s to %s' % (full_name, directory))

    duplicates = parser_config.duplicates.get(full_name, [])
    if not duplicates:
      continue

    duplicates = [item for item in duplicates if item != full_name]

    for dup in duplicates:
      from_path = os.path.join(site_path, dup.replace('.', '/'))
      to_path = os.path.join(site_path, full_name.replace('.', '/'))
      redirects.append((
          os.path.join('/', from_path),
          os.path.join('/', to_path)))

  if redirects:
    redirects = sorted(redirects)
    template = ('- from: {}\n'
                '  to: {}\n')
    redirects = [template.format(f, t) for f, t in redirects]
    api_redirects_path = os.path.join(output_dir, '_redirects.yaml')
    with open(api_redirects_path, 'w') as redirect_file:
      redirect_file.write('redirects:\n')
      redirect_file.write(''.join(redirects))

  if yaml_toc:
    # Generate table of contents

    # Put modules in alphabetical order, case-insensitive
    modules = sorted(module_children.keys(), key=lambda a: a.upper())

    leftnav_path = os.path.join(output_dir, '_toc.yaml')
    with open(leftnav_path, 'w') as f:

      # Generate header
      f.write('# Automatically generated file; please do not edit\ntoc:\n')
      for module in modules:
        indent_num = module.count('.')
        # Don't list `tf.submodule` inside `tf`
        indent_num = max(indent_num, 1)
        indent = '  '*indent_num

        if indent_num > 1:
          # tf.contrib.baysflow.entropy will be under
          #   tf.contrib->baysflow->entropy
          title = module.split('.')[-1]
        else:
          title = module

        header = [
            '- title: ' + title, '  section:', '  - title: Overview',
            '    path: ' + os.path.join('/', site_path, symbol_to_file[module])
        ]
        header = ''.join([indent+line+'\n' for line in header])
        f.write(header)

        symbols_in_module = module_children.get(module, [])
        # Sort case-insensitive, if equal sort case sensitive (upper first)
        symbols_in_module.sort(key=lambda a: (a.upper(), a))

        for full_name in symbols_in_module:
          item = [
              '  - title: ' + full_name[len(module) + 1:], '    path: ' +
              os.path.join('/', site_path, symbol_to_file[full_name])
          ]
          item = ''.join([indent+line+'\n' for line in item])
          f.write(item)

  # Write a global index containing all full names with links.
  with open(os.path.join(output_dir, 'index.md'), 'w') as f:
    f.write(
        parser.generate_global_index(root_title, parser_config.index,
                                     parser_config.reference_resolver))


def add_dict_to_dict(add_from, add_to):
  for key in add_from:
    if key in add_to:
      add_to[key].extend(add_from[key])
    else:
      add_to[key] = add_from[key]


class DocControlsAwareCrawler(public_api.PublicAPIVisitor):
  """A `docs_controls` aware API-crawler."""

  def _is_private(self, path, name, obj):
    if doc_controls.should_skip(obj):
      return True
    return super(DocControlsAwareCrawler, self)._is_private(path, name, obj)


def extract(py_modules,
            private_map,
            do_not_descend_map,
            visitor_cls=doc_generator_visitor.DocGeneratorVisitor):
  """Extract docs from tf namespace and write them to disk."""
  # Traverse the first module.
  visitor = visitor_cls(py_modules[0][0])
  api_visitor = DocControlsAwareCrawler(visitor)
  api_visitor.set_root_name(py_modules[0][0])
  add_dict_to_dict(private_map, api_visitor.private_map)
  add_dict_to_dict(do_not_descend_map, api_visitor.do_not_descend_map)

  traverse.traverse(py_modules[0][1], api_visitor)

  # Traverse all py_modules after the first:
  for module_name, module in py_modules[1:]:
    visitor.set_root_name(module_name)
    api_visitor.set_root_name(module_name)
    traverse.traverse(module, api_visitor)

  return visitor


class _GetMarkdownTitle(py_guide_parser.PyGuideParser):
  """Extract the title from a .md file."""

  def __init__(self):
    self.title = None
    py_guide_parser.PyGuideParser.__init__(self)

  def process_title(self, _, title):
    if self.title is None:  # only use the first title
      self.title = title


EXCLUDED = set(['__init__.py', 'OWNERS', 'README.txt'])


def replace_refs(src_dir,
                 output_dir,
                 reference_resolver,
                 file_pattern='*.md',
                 api_docs_relpath='api_docs'):
  """Link `tf.symbol` references found in files matching `file_pattern`.

  A matching directory structure, with the modified files is
  written to `output_dir`.

  `{"__init__.py","OWNERS","README.txt"}` are skipped.

  Files not matching `file_pattern` (using `fnmatch`) are copied with no change.

  Also, files in the `api_guides/python` directory get explicit ids set on all
  heading-2s to ensure back-links work.

  Args:
    src_dir: The directory to convert files from.
    output_dir: The root directory to write the resulting files to.
    reference_resolver: A `parser.ReferenceResolver` to make the replacements.
    file_pattern: Only replace references in files matching file_patters,
      using `fnmatch`. Non-matching files are copied unchanged.
    api_docs_relpath: Relative-path string to the api_docs, from the src_dir.
  """
  # Iterate through all the source files and process them.
  for dirpath, _, filenames in os.walk(src_dir):
    depth = os.path.relpath(src_dir, start=dirpath)
    # How to get from `dirpath` to api_docs/python/
    relative_path_to_root = os.path.join(depth, api_docs_relpath, 'python')

    # Make the directory under output_dir.
    new_dir = os.path.join(output_dir,
                           os.path.relpath(path=dirpath, start=src_dir))
    if not os.path.exists(new_dir):
      os.makedirs(new_dir)

    for base_name in filenames:
      if base_name in EXCLUDED:
        continue
      full_in_path = os.path.join(dirpath, base_name)

      # Set the `current_doc_full_name` so bad files can be reported on errors.
      reference_resolver.current_doc_full_name = full_in_path

      suffix = os.path.relpath(path=full_in_path, start=src_dir)
      full_out_path = os.path.join(output_dir, suffix)
      # Copy files that do not match the file_pattern, unmodified.
      if not fnmatch.fnmatch(base_name, file_pattern):
        if full_in_path != full_out_path:
          shutil.copyfile(full_in_path, full_out_path)
        continue

      with open(full_in_path, 'rb') as f:
        content = f.read().decode('utf-8')

      content = reference_resolver.replace_references(content,
                                                      relative_path_to_root)
      with open(full_out_path, 'wb') as f:
        f.write(content.encode('utf-8'))


class DocGenerator(object):
  """Main entry point for generating docs."""

  def __init__(self,
               root_title,
               py_modules,
               base_dir,
               code_url_prefix,
               search_hints=False,
               site_path='',
               private_map=None,
               do_not_descend_map=None,
               visitor_cls=doc_generator_visitor.DocGeneratorVisitor,
               api_cache=True):
    self._root_title = root_title
    self._py_modules = py_modules
    self._base_dir = base_dir
    self._code_url_prefix = code_url_prefix
    self._search_hints = search_hints
    self._site_path = site_path
    self._private_map = private_map or {}
    self._do_not_descend_map = do_not_descend_map or {}
    self._visitor_cls = visitor_cls
    self.api_cache = api_cache

  def py_module_names(self):
    if self._py_modules is None:
      raise RuntimeError(
          'Must call set_py_modules() before running py_module_names().')
    return [name for (name, _) in self._py_modules]

  def make_reference_resolver(self, visitor):
    return parser.ReferenceResolver.from_visitor(
        visitor, py_module_names=self.py_module_names())

  def make_parser_config(self, visitor, reference_resolver):
    return parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates=visitor.duplicates,
        duplicate_of=visitor.duplicate_of,
        tree=visitor.tree,
        index=visitor.index,
        reverse_index=visitor.reverse_index,
        base_dir=self._base_dir,
        code_url_prefix=self._code_url_prefix)

  def run_extraction(self):
    return extract(self._py_modules, self._private_map,
                   self._do_not_descend_map, self._visitor_cls)

  def build(self, output_dir):
    """Build all the docs.

    This produces python api docs:
      * generated from modules listed in `py_modules`.
      * written to '{output_dir}/api_docs/python/'


    Args:
      output_dir: Where to write the resulting docs.

    Returns:
      The number of errors encountered while processing.
    """
    workdir = tempfile.mkdtemp()

    # Extract the python api from the _py_modules
    visitor = self.run_extraction()
    reference_resolver = self.make_reference_resolver(visitor)
    # Replace all the `tf.symbol` references in the workdir.
    replace_refs(workdir, workdir, reference_resolver, file_pattern='*.md')

    # Write the api docs.
    parser_config = self.make_parser_config(visitor, reference_resolver)
    write_docs(
        output_dir=os.path.join(workdir, 'api_docs/python'),
        parser_config=parser_config,
        yaml_toc=True,
        root_title=self._root_title,
        search_hints=self._search_hints,
        site_path=self._site_path)

    if self.api_cache:
      reference_resolver.to_json_file(
          os.path.join(workdir, 'api_docs/python/_api_cache.json'))

    try:
      os.makedirs(output_dir)
    except OSError as e:
      if 'File exists' not in e:
        raise

    base_command = ['rsync', '--recursive', '--quiet', '--delete']
    for name, _ in self._py_modules:
      cmd = base_command + [
          os.path.join(workdir, 'api_docs/python/', name),
          os.path.join(workdir, 'api_docs/python/', name + '.md'), output_dir
      ]

      subprocess.check_call(cmd)

    cmd = base_command + [
        os.path.join(workdir, 'api_docs/python/', '_api_cache.json'),
        output_dir
    ]

    subprocess.check_call(cmd)
