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

import pathlib
import six

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
          module_name = parser_config.duplicate_of.get(subname, subname)
          module_children.setdefault(module_name, []).append(full_name)
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
      from_path = os.path.join(site_path, 'api_docs/python',
                               dup.replace('.', '/'))
      to_path = os.path.join(site_path, 'api_docs/python',
                             full_name.replace('.', '/'))
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


def extract(py_modules,
            base_dir,
            private_map,
            do_not_descend_map,
            visitor_cls=doc_generator_visitor.DocGeneratorVisitor):
  """Extract docs from tf namespace and write them to disk."""
  # Traverse the first module.
  if len(py_modules) != 1:
    raise ValueError("only pass one [('name',module)] pair in py_modules")
  short_name, py_module = py_modules[0]
  visitor = visitor_cls()
  api_visitor = public_api.PublicAPIVisitor(
      visitor=visitor,
      base_dir=base_dir,
      do_not_descend_map=do_not_descend_map,
      private_map=private_map)

  traverse.traverse(py_module, api_visitor, short_name)

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
    """Creates a doc-generator.

    Args:
      root_title: A string. The main title for the project. Like "TensorFlow"
      py_modules: The python module to document.
      base_dir: The directory that "Defined in" links are generated relative to.
        Defined in links are not defined for objects defined outside this
        directory.
      code_url_prefix: The prefix to add to "Defined in" paths.
      search_hints: Bool. Include metadata search hints at the top of each file.
      site_path:
      private_map: A {"module.path.to.object": ["names"]} dictionary. Specific
        aliases that should not be shown in the resulting docs.
      do_not_descend_map: A {"module.path.to.object": ["names"]} dictionary.
        Specific aliases that will be shown, but not expanded.
      visitor_cls: An option to override the default visitor class
        `doc_generator_visitor.DocGeneratorVisitor`.
      api_cache: Bool. Generate an api_cache file. This is used to easily add
        api links for backticked symbols (like `tf.add`) in other docs.
    """
    self._root_title = root_title
    self._py_modules = py_modules
    self._short_name = py_modules[0][0]
    self._py_module = py_modules[0][1]
    self._base_dir = base_dir
    self._code_url_prefix = code_url_prefix
    self._search_hints = search_hints
    self._site_path = site_path
    self._private_map = private_map or {}
    self._do_not_descend_map = do_not_descend_map or {}
    self._visitor_cls = visitor_cls
    self.api_cache = api_cache

  def make_reference_resolver(self, visitor):
    return parser.ReferenceResolver.from_visitor(
        visitor, py_module_names=[self._short_name])

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
    return extract(self._py_modules, self._base_dir,
                   self._private_map, self._do_not_descend_map,
                   self._visitor_cls)

  def build(self, output_dir):
    """Build all the docs.

    This produces python api docs:
      * generated from `py_module`.
      * written to '{output_dir}/api_docs/python/'

    Args:
      output_dir: Where to write the resulting docs.
    """
    workdir = pathlib.Path(tempfile.mkdtemp())

    # Extract the python api from the _py_modules
    visitor = self.run_extraction()
    reference_resolver = self.make_reference_resolver(visitor)
    # Replace all the `tf.symbol` references in the workdir.
    replace_refs(
        str(workdir), str(workdir), reference_resolver, file_pattern='*.md')

    # Write the api docs.
    parser_config = self.make_parser_config(visitor, reference_resolver)
    work_py_dir = workdir / 'api_docs/python'
    write_docs(
        output_dir=str(work_py_dir),
        parser_config=parser_config,
        yaml_toc=True,
        root_title=self._root_title,
        search_hints=self._search_hints,
        site_path=self._site_path)

    if self.api_cache:
      reference_resolver.to_json_file(
          str(work_py_dir / self._short_name / '_api_cache.json'))

    try:
      os.makedirs(output_dir)
    except OSError as e:
      if e.strerror != 'File exists':
        raise

    cmd = ['rsync', '--recursive', '--quiet', '--delete']
    cmd.extend(str(path) for path in work_py_dir.glob('*'))
    cmd.append(output_dir)

    subprocess.check_call(cmd)
