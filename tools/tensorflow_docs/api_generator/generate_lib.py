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

import collections
import fnmatch
import operator
import os
import shutil
import subprocess
import tempfile

import pathlib2 as pathlib
import six

from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import pretty_docs
from tensorflow_docs.api_generator import public_api
from tensorflow_docs.api_generator import py_guide_parser
from tensorflow_docs.api_generator import tf_inspect
from tensorflow_docs.api_generator import traverse

import yaml

# Used to add a collections.OrderedDict representer to yaml so that the
# dump doesn't contain !!OrderedDict yaml tags.
# Reference: https://stackoverflow.com/a/21048064
# Using a normal dict doesn't preserve the order of the input dictionary.
_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG


def dict_representer(dumper, data):
  return dumper.represent_dict(six.iteritems(data))


def dict_constructor(loader, node):
  return collections.OrderedDict(loader.construct_pairs(node))


yaml.add_representer(collections.OrderedDict, dict_representer)
yaml.add_constructor(_mapping_tag, dict_constructor)


class TocNode(object):
  """Represents a node in the TOC.

  Attributes:
    full_name: Name of the module.
    short_name: The last path component.
    py_object: Python object of the module.
    path: Path to the module's page on tensorflow.org relative to
      tensorflow.org.
    experimental: Whether the module is experimental or not.
    deprecated: Whether the module is deprecated or not.
  """

  def __init__(self, module, py_object, path):
    self._module = module
    self._py_object = py_object
    self._path = path

  @property
  def full_name(self):
    return self._module

  @property
  def short_name(self):
    return self.full_name.split('.')[-1]

  @property
  def py_object(self):
    return self._py_object

  @property
  def path(self):
    return self._path

  @property
  def experimental(self):
    return 'experimental' in self.short_name

  _DEPRECATED_STRING = 'THIS FUNCTION IS DEPRECATED'

  @property
  def deprecated(self):
    """Checks if the module is deprecated or not.

    Special case is `tf.contrib`. It doesn't have the _tf_decorator attribute
    but that module should be marked as deprecated.

    Each deprecated function has a `_tf_decorator.decorator_name` attribute.
    Check the docstring of that function to confirm if the function was
    indeed deprecated. If a different deprecation setting was used on the
    function, then "THIS FUNCTION IS DEPRECATED" substring won't be inserted
    into the docstring of that function by the decorator.

    Returns:
      True if depreacted else False.
    """

    if 'tf.contrib' in self.full_name:
      return True

    try:
      # Instead of only checking the docstring, checking for the decorator
      # provides an additional level of certainty about the correctness of the
      # the application of `status: deprecated`.
      decorator = operator.attrgetter('_tf_decorator.decorator_name')(
          self.py_object)
      if decorator == 'deprecated':
        return self._check_docstring()
    except AttributeError:
      pass

    return False

  def _check_docstring(self):
    # Only add the deprecated status if the function is deprecated. There are
    # other settings that should be ignored like deprecate_args, etc.
    docstring = self.py_object.__doc__
    return docstring is not None and self._DEPRECATED_STRING in docstring


class Module(TocNode):
  """Represents a single module and its children and submodules.

  Attributes:
    full_name: Name of the module.
    short_name: The last path component.
    py_object: Python object of the module.
    title: Title of the module in _toc.yaml
    path: Path to the module's page on tensorflow.org relative to
      tensorflow.org.
    children: List of attributes on the module.
    submodules: List of submodules in the module.
    experimental: Whether the module is experimental or not.
    deprecated: Whether the module is deprecated or not.
  """

  def __init__(self, module, py_object, path):
    super(Module, self).__init__(module, py_object, path)

    self._children = []
    self._submodules = []

  @property
  def title(self):
    if self.full_name.count('.') > 1:
      title = self.full_name.split('.')[-1]
    else:
      title = self.full_name
    return title

  @property
  def children(self):
    return sorted(
        self._children, key=lambda x: (x.full_name.upper(), x.full_name))

  @property
  def submodules(self):
    return self._submodules

  def add_children(self, children):
    if not isinstance(children, list):
      children = [children]

    self._children.extend(children)

  def add_submodule(self, sub_mod):
    self._submodules.append(sub_mod)


class ModuleChild(TocNode):
  """Represents a child of a module.

  Attributes:
    full_name: Name of the child.
    short_name: The last path component.
    py_object: Python object of the child.
    title: Title of the module in _toc.yaml
    path: Path to the module's page on tensorflow.org relative to
      tensorflow.org.
    experimental: Whether the module child is experimental or not.
    deprecated: Whether the module is deprecated or not.
  """

  def __init__(self, name, py_object, parent, path):
    self._parent = parent
    super(ModuleChild, self).__init__(name, py_object, path)

  @property
  def title(self):
    return self.full_name[len(self._parent) + 1:]


class GenerateToc(object):
  """Generates a data structure that defines the structure of _toc.yaml."""

  def __init__(self, modules):
    self._modules = modules

  def _create_graph(self):
    """Creates a graph to allow a dfs traversal on it to generate the toc.

    Each graph key contains a module and its value is an object of `Module`
    class. That module object contains a list of submodules.

    Example low-level structure of the graph is as follows:

    {
      'module1': [submodule1, submodule2],
      'submodule1': [sub1-submodule1],
      'sub1-submodule1': [],
      'submodule2': [],
      'module2': [],
      'module3': [submodule4],
      'submodule4': [sub1-submodule4],
      'sub1-submodule4': [sub1-sub1-submodule4],
      'sub1-sub1-submodule4': []
    }

    Returns:
      A tuple of (graph, base_modules). Base modules is returned because while
      creating a nested list of dictionaries, the top level should only contain
      the base modules.
    """

    # Sort the modules in case-insensitive alphabetical order.
    sorted_modules = sorted(self._modules.keys(), key=lambda a: a.lower())
    toc_base_modules = []

    toc_graph = {}
    for module in sorted_modules:
      mod = self._modules[module]

      # Add the module to the graph.
      toc_graph[module] = mod

      # If the module's name contains more than one dot, it is not a base level
      # module. Hence, add it to its parents submodules list.
      if module.count('.') > 1:
        # For example, if module is `tf.keras.applications.densenet` then its
        # parent is `tf.keras.applications`.
        parent_module = '.'.join(module.split('.')[:-1])
        parent_mod_obj = toc_graph.get(parent_module, None)
        if parent_mod_obj is not None:
          parent_mod_obj.add_submodule(mod)
      else:
        toc_base_modules.append(module)

    return toc_graph, toc_base_modules

  def _generate_children(self, mod, is_parent_deprecated):
    """Creates a list of dictionaries containing child's title and path.

    For example: The dictionary created will look this this in _toc.yaml.

    ```
    children_list = [{'title': 'Overview', 'path': '/tf/app'},
                     {'title': 'run', 'path': '/tf/app/run'}]
    ```

    The above list will get converted to the following yaml syntax.

    ```
    - title: Overview
      path: /tf/app
    - title: run
      path: /tf/app/run
    ```

    Args:
      mod: A module object.
      is_parent_deprecated: Bool, Whether the parent is deprecated or not.

    Returns:
      A list of dictionaries containing child's title and path.
    """

    children_list = []
    children_list.append(
        collections.OrderedDict([('title', 'Overview'), ('path', mod.path)]))

    for child in mod.children:
      child_yaml_content = [('title', child.title), ('path', child.path)]

      # Set `status: deprecated` only if the parent's status is not
      # deprecated.
      if child.deprecated and not is_parent_deprecated:
        child_yaml_content.insert(1, ('status', 'deprecated'))
      elif child.experimental:
        child_yaml_content.insert(1, ('status', 'experimental'))

      children_list.append(collections.OrderedDict(child_yaml_content))

    return children_list

  def _dfs(self, mod, visited, is_parent_deprecated):
    """Does a dfs traversal on the graph generated.

    This creates a nested dictionary structure which is then dumped as .yaml
    file. Each submodule's dictionary of title and path is nested under its
    parent module.

    For example, `tf.keras.app.net` will be nested under `tf.keras.app` which
    will be nested under `tf.keras`. Here's how the nested dictionaries will
    look when its dumped as .yaml.

    ```
    - title: tf.keras
      section:
      - title: Overview
        path: /tf/keras
      - title: app
        section:
        - title: Overview
          path: /tf/keras/app
        - title: net
          section:
          - title: Overview
            path: /tf/keras/app/net
    ```

    The above nested structure is what the dfs traversal will create in form
    of lists of dictionaries.

    Args:
      mod: A module object.
      visited: A dictionary of modules visited by the dfs traversal.
      is_parent_deprecated: Bool, Whether any parent is deprecated or not.

    Returns:
      A dictionary containing the nested data structure.
    """

    visited[mod.full_name] = True

    # parent_exp is set to the current module because the current module is
    # the parent for its children.
    children_list = self._generate_children(
        mod, is_parent_deprecated or mod.deprecated)

    # generate for submodules within the submodule.
    for submod in mod.submodules:
      if not visited[submod.full_name]:
        sub_mod_dict = self._dfs(submod, visited, is_parent_deprecated or
                                 mod.deprecated)
        children_list.append(sub_mod_dict)

    # If the parent module is not experimental, then add the experimental
    # status to the submodule.
    submod_yaml_content = [('title', mod.title), ('section', children_list)]

    # If the parent module is not deprecated, then add the deprecated
    # status to the submodule. If the parent is deprecated, then setting its
    # status to deprecated in _toc.yaml propagates to all its children and
    # submodules.
    if mod.deprecated and not is_parent_deprecated:
      submod_yaml_content.insert(1, ('status', 'deprecated'))
    elif mod.experimental:
      submod_yaml_content.insert(1, ('status', 'experimental'))

    return collections.OrderedDict(submod_yaml_content)

  def generate(self):
    """Generates the final toc.

    Returns:
      A list of dictionaries which will be dumped into .yaml file.
    """

    toc = []
    toc_graph, toc_base_modules = self._create_graph()
    visited = {node: False for node in toc_graph.keys()}

    # Sort in alphabetical case-insensitive order.
    toc_base_modules = sorted(toc_base_modules, key=lambda a: a.lower())
    for module in toc_base_modules:
      module_obj = toc_graph[module]
      # Generate children of the base module.
      section = self._generate_children(
          module_obj, is_parent_deprecated=module_obj.deprecated)

      # DFS traversal on the submodules.
      for sub_mod in module_obj.submodules:
        sub_mod_list = self._dfs(
            sub_mod, visited, is_parent_deprecated=module_obj.deprecated)
        section.append(sub_mod_list)

      module_yaml_content = [('title', module_obj.title), ('section', section)]
      if module_obj.deprecated:
        module_yaml_content.insert(1, ('status', 'deprecated'))
      elif module_obj.experimental:
        module_yaml_content.insert(1, ('status', 'experimental'))

      toc.append(collections.OrderedDict(module_yaml_content))

    return {'toc': toc}


def write_docs(output_dir,
               parser_config,
               yaml_toc,
               root_title='TensorFlow',
               search_hints=True,
               site_path='api_docs/python'):
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

  # Collect redirects for an api _redirects.yaml file.
  redirects = []

  # Parse and write Markdown pages, resolving cross-links (`tf.symbol`).
  for full_name in sorted(parser_config.index.keys(), key=lambda k: k.lower()):
    py_object = parser_config.index[full_name]

    if full_name in parser_config.duplicate_of:
      continue

    # Methods and some routines are documented only as part of their class.
    if not (tf_inspect.ismodule(py_object) or tf_inspect.isclass(py_object) or
            parser.is_free_function(py_object, full_name, parser_config.index)):
      continue

    # Remove the extension from the path.
    docpath, _ = os.path.splitext(parser.documentation_path(full_name))

    # For a module, remember the module for the table-of-contents
    if tf_inspect.ismodule(py_object):
      if full_name in parser_config.tree:
        mod_obj = Module(
            module=full_name,
            py_object=py_object,
            path=os.path.join('/', site_path, docpath))
        module_children[full_name] = mod_obj
    # For something else that's documented,
    # figure out what module it lives in
    else:
      subname = str(full_name)
      while True:
        subname = subname[:subname.rindex('.')]
        if tf_inspect.ismodule(parser_config.index[subname]):
          module_name = parser_config.duplicate_of.get(subname, subname)
          child_mod = ModuleChild(
              name=full_name,
              py_object=py_object,
              parent=module_name,
              path=os.path.join('/', site_path, docpath))
          module_children[module_name].add_children(child_mod)
          break

    # Generate docs for `py_object`, resolving references.
    try:
      page_info = parser.docs_for_object(full_name, py_object, parser_config)
    except:
      raise ValueError(
          'Failed to generate docs for symbol: `{}`'.format(full_name))

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
      raise OSError('Cannot write documentation for %s to %s' %
                    (full_name, directory))

    duplicates = parser_config.duplicates.get(full_name, [])
    if not duplicates:
      continue

    duplicates = [item for item in duplicates if item != full_name]

    for dup in duplicates:
      from_path = os.path.join(site_path, dup.replace('.', '/'))
      to_path = os.path.join(site_path, full_name.replace('.', '/'))
      redirects.append({
          'from': os.path.join('/', from_path),
          'to': os.path.join('/', to_path)
      })

  if redirects:
    redirects_dict = {
        'redirects': sorted(redirects, key=lambda redirect: redirect['from'])
    }

    api_redirects_path = os.path.join(output_dir, '_redirects.yaml')
    with open(api_redirects_path, 'w') as redirect_file:
      yaml.dump(redirects_dict, redirect_file, default_flow_style=False)

  if yaml_toc:
    toc_gen = GenerateToc(module_children)
    toc_dict = toc_gen.generate()

    leftnav_toc = os.path.join(output_dir, '_toc.yaml')
    with open(leftnav_toc, 'w') as toc_file:
      yaml.dump(toc_dict, toc_file, default_flow_style=False)

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
            visitor_cls=doc_generator_visitor.DocGeneratorVisitor,
            callbacks=None):
  """Walks the module contents, returns an index of all visited objects.

  The return value is an instance of `self._visitor_cls`, usually:
  `doc_generator_visitor.DocGeneratorVisitor`

  Args:
    py_modules: A list containing a single (short_name, module_object) pair.
      like `[('tf',tf)]`.
    base_dir: The package root directory. Nothing defined outside of this
      directory is documented.
    private_map: A {'path':["name"]} dictionary listing particular object
      locations that should be ignored in the doc generator.
    do_not_descend_map: A {'path':["name"]} dictionary listing particular object
      locations where the children should not be listed.
    visitor_cls: A class, typically a subclass of
      `doc_generator_visitor.DocGeneratorVisitor` that acumulates the indexes of
      obejcts to document.
    callbacks: Additional callbacks passed to `traverse`. Executed between the
      `PublicApiFilter` and the accumulator (`DocGeneratorVisitor`). The
      primary use case for these is to filter the listy of children (see:
        `public_api.local_definitions_filter`)

  Returns:
    The accumulator (`DocGeneratorVisitor`)
  """
  if callbacks is None:
    callbacks = []

  if len(py_modules) != 1:
    raise ValueError("only pass one [('name',module)] pair in py_modules")
  short_name, py_module = py_modules[0]

  api_filter = public_api.PublicAPIFilter(
      base_dir=base_dir,
      do_not_descend_map=do_not_descend_map,
      private_map=private_map)

  accumulator = visitor_cls()

  # The objects found during traversal, and their children are passed to each
  # of these visitors in sequence. Each visitor returns the list of children
  # to be passed to the next visitor.
  visitors = [api_filter, public_api.ignore_typing] + callbacks + [accumulator]

  traverse.traverse(py_module, visitors, short_name)

  return accumulator


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
    file_pattern: Only replace references in files matching file_patters, using
      `fnmatch`. Non-matching files are copied unchanged.
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
               base_dir=None,
               code_url_prefix=(),
               search_hints=True,
               site_path='api_docs/python',
               private_map=None,
               do_not_descend_map=None,
               visitor_cls=doc_generator_visitor.DocGeneratorVisitor,
               api_cache=True,
               callbacks=None):
    """Creates a doc-generator.

    Args:
      root_title: A string. The main title for the project. Like "TensorFlow"
      py_modules: The python module to document.
      base_dir: String or tuple of strings. Directories that "Defined in" links
        are generated relative to. Modules outside one of these directories are
        not documented. No `base_dir` should be inside another.
      code_url_prefix: String or tuple of strings. The prefix to add to "Defined
        in" paths. These are zipped with `base-dir`, to set the `defined_in`
        path for each file. The defined in link for `{base_dir}/path/to/file` is
        set to `{code_url_prefix}/path/to/file`.
      search_hints: Bool. Include metadata search hints at the top of each file.
      site_path: Path prefix in the "_toc.yaml"
      private_map: A {"module.path.to.object": ["names"]} dictionary. Specific
        aliases that should not be shown in the resulting docs.
      do_not_descend_map: A {"module.path.to.object": ["names"]} dictionary.
        Specific aliases that will be shown, but not expanded.
      visitor_cls: An option to override the default visitor class
        `doc_generator_visitor.DocGeneratorVisitor`.
      api_cache: Bool. Generate an api_cache file. This is used to easily add
        api links for backticked symbols (like `tf.add`) in other docs.
      callbacks: Additional callbacks passed to `traverse`. Executed between the
        `PublicApiFilter` and the accumulator (`DocGeneratorVisitor`). The
        primary use case for these is to filter the listy of children (see:
          `public_api.local_definitions_filter`)
    """
    self._root_title = root_title
    self._py_modules = py_modules
    self._short_name = py_modules[0][0]
    self._py_module = py_modules[0][1]

    if base_dir is None:
      base_dir = os.path.dirname(self._py_module.__file__)
    if isinstance(base_dir, str):
      base_dir = (base_dir,)
    self._base_dir = tuple(base_dir)
    assert self._base_dir, '`base_dir` cannot be empty'

    if isinstance(code_url_prefix, str):
      code_url_prefix = (code_url_prefix,)
    self._code_url_prefix = tuple(code_url_prefix)
    if not self._code_url_prefix:
      raise ValueError('`code_url_prefix` cannot be empty')

    if len(self._code_url_prefix) != len(base_dir):
      raise ValueError('The `base_dir` list should have the same number of '
                       'elements as the `code_url_prefix` list (they get '
                       'zipped together).')

    self._search_hints = search_hints
    self._site_path = site_path
    self._private_map = private_map or {}
    self._do_not_descend_map = do_not_descend_map or {}
    self._visitor_cls = visitor_cls
    self.api_cache = api_cache
    if callbacks is None:
      callbacks = []
    self._callbacks = callbacks

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
    """Walks the module contents, returns an index of all visited objects.

    The return value is an instance of `self._visitor_cls`, usually:
    `doc_generator_visitor.DocGeneratorVisitor`

    Returns:
    """
    return extract(
        py_modules=self._py_modules,
        base_dir=self._base_dir,
        private_map=self._private_map,
        do_not_descend_map=self._do_not_descend_map,
        visitor_cls=self._visitor_cls,
        callbacks=self._callbacks)

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

    subprocess.check_call([
        'rsync', '--recursive', '--quiet', '--delete',
        '{}/'.format(work_py_dir), output_dir
    ])
