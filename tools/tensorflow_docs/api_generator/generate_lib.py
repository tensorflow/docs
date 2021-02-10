# Lint as: python3
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
"""Generate tensorflow.org style API Reference docs for a Python module."""

import collections
import fnmatch
import inspect
import os
import pathlib
import shutil
import tempfile

from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, Union

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import pretty_docs
from tensorflow_docs.api_generator import public_api
from tensorflow_docs.api_generator import traverse
from tensorflow_docs.api_generator.report import utils

import yaml

# Used to add a collections.OrderedDict representer to yaml so that the
# dump doesn't contain !!OrderedDict yaml tags.
# Reference: https://stackoverflow.com/a/21048064
# Using a normal dict doesn't preserve the order of the input dictionary.
_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG


def dict_representer(dumper, data):
  return dumper.represent_dict(data.items())


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

  def __init__(self, module: str, py_object: Any, path: str):
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
    if doc_controls.is_deprecated(self.py_object):
      return True

    if 'tf.contrib' in self.full_name:
      return True

    try:
      # Instead of only checking the docstring, checking for the decorator
      # provides an additional level of certainty about the correctness of the
      # the application of `status: deprecated`.
      decorator_list = parser.extract_decorators(self.py_object)
      if any('deprecat' in dec for dec in decorator_list):
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
    return sorted(self._children, key=lambda x: x.full_name)

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

  def generate(self) -> Dict[str, Any]:
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


def write_docs(
    *,
    output_dir: Union[str, pathlib.Path],
    parser_config: parser.ParserConfig,
    yaml_toc: bool,
    root_module_name: str,
    root_title: str = 'TensorFlow',
    search_hints: bool = True,
    site_path: str = 'api_docs/python',
    gen_redirects: bool = True,
    gen_report: bool = False,
    extra_docs: Optional[Dict[int, str]] = None,
):
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
    root_module_name: (str) the name of the root module (`tf` for tensorflow).
    root_title: The title name for the root level index.md.
    search_hints: (bool) include meta-data search hints at the top of each
      output file.
    site_path: The output path relative to the site root. Used in the
      `_toc.yaml` and `_redirects.yaml` files.
    gen_redirects: Bool which decides whether to generate _redirects.yaml file
      or not.
    gen_report: If True, a report for the library is generated by linting the
      docstrings of its public API symbols.
    extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
        that need to be added to the markdown pages created.

  Raises:
    ValueError: if `output_dir` is not an absolute path
  """
  output_dir = pathlib.Path(output_dir)
  site_path = pathlib.Path('/', site_path)

  # Make output_dir.
  if not output_dir.is_absolute():
    raise ValueError("'output_dir' must be an absolute path.\n"
                     f"    output_dir='{output_dir}'")
  output_dir.mkdir(parents=True, exist_ok=True)

  # These dictionaries are used for table-of-contents generation below
  # They will contain, after the for-loop below::
  #  - module name(string):classes and functions the module contains(list)
  module_children = {}

  # Collect redirects for an api _redirects.yaml file.
  redirects = []

  if gen_report:
    api_report_obj = utils.ApiReport()

  # Parse and write Markdown pages, resolving cross-links (`tf.symbol`).
  for full_name in sorted(parser_config.index.keys(), key=lambda k: k.lower()):
    py_object = parser_config.index[full_name]

    if full_name in parser_config.duplicate_of:
      continue

    # Methods constants are only documented only as part of their parent's page.
    if parser_config.reference_resolver.is_fragment(full_name):
      continue

    # Remove the extension from the path.
    docpath, _ = os.path.splitext(parser.documentation_path(full_name))

    # For a module, remember the module for the table-of-contents
    if inspect.ismodule(py_object):
      if full_name in parser_config.tree:
        mod_obj = Module(
            module=full_name,
            py_object=py_object,
            path=str(site_path / docpath))
        module_children[full_name] = mod_obj
    # For something else that's documented,
    # figure out what module it lives in
    else:
      subname = str(full_name)
      while True:
        subname = subname[:subname.rindex('.')]
        if inspect.ismodule(parser_config.index[subname]):
          module_name = parser_config.duplicate_of.get(subname, subname)
          child_mod = ModuleChild(
              name=full_name,
              py_object=py_object,
              parent=module_name,
              path=str(site_path / docpath))
          module_children[module_name].add_children(child_mod)
          break

    # Generate docs for `py_object`, resolving references.
    try:
      page_info = parser.docs_for_object(full_name, py_object, parser_config,
                                         extra_docs)
    except:
      raise ValueError(f'Failed to generate docs for symbol: `{full_name}`')

    if gen_report and not full_name.startswith(
        ('tf.compat.v', 'tf.keras.backend', 'tf.numpy',
         'tf.experimental.numpy')):
      api_report_obj.fill_metrics(page_info)
      continue

    path = output_dir / parser.documentation_path(full_name)
    try:
      path.parent.mkdir(exist_ok=True, parents=True)
      # This function returns unicode in PY3.
      hidden = doc_controls.should_hide_from_search(page_info.py_object)
      brief_no_backticks = page_info.doc.brief.replace('`', '').strip()
      content = []
      if brief_no_backticks:
        content.append(f'description: {brief_no_backticks}\n')

      if search_hints and not hidden:
        content.append(page_info.get_metadata_html())
      else:
        content.append('robots: noindex\n')

      content.append(pretty_docs.build_md_page(page_info))
      text = '\n'.join(content)
      path.write_text(text, encoding='utf-8')
    except OSError:
      raise OSError('Cannot write documentation for '
                    f'{full_name} to {path.parent}')

    duplicates = parser_config.duplicates.get(full_name, [])
    if not duplicates:
      continue

    duplicates = [item for item in duplicates if item != full_name]

    if gen_redirects:
      for dup in duplicates:
        from_path = site_path / dup.replace('.', '/')
        to_path = site_path / full_name.replace('.', '/')
        redirects.append({'from': str(from_path), 'to': str(to_path)})

  if gen_report:
    serialized_proto = api_report_obj.api_report.SerializeToString()
    raw_proto = output_dir / 'api_report.pb'
    raw_proto.write_bytes(serialized_proto)
    return

  if yaml_toc:
    toc_gen = GenerateToc(module_children)
    toc_dict = toc_gen.generate()

    # Replace the overview path *only* for 'TensorFlow' to
    # `/api_docs/python/tf_overview`. This will be redirected to
    # `/api_docs/python/tf`.
    toc_values = toc_dict['toc'][0]
    if toc_values['title'] == 'tf':
      section = toc_values['section'][0]
      section['path'] = str(site_path / 'tf_overview')

    leftnav_toc = output_dir / root_module_name / '_toc.yaml'
    with open(leftnav_toc, 'w') as toc_file:
      yaml.dump(toc_dict, toc_file, default_flow_style=False)

  if redirects and gen_redirects:
    if yaml_toc and toc_values['title'] == 'tf':
      redirects.append({
          'from': str(site_path / 'tf_overview'),
          'to': str(site_path / 'tf'),
      })
    redirects_dict = {
        'redirects': sorted(redirects, key=lambda redirect: redirect['from'])
    }

    api_redirects_path = output_dir / root_module_name / '_redirects.yaml'
    with open(api_redirects_path, 'w') as redirect_file:
      yaml.dump(redirects_dict, redirect_file, default_flow_style=False)

  # Write a global index containing all full names with links.
  with open(output_dir / root_module_name / 'all_symbols.md', 'w') as f:
    global_index = parser.generate_global_index(
        root_title, parser_config.index, parser_config.reference_resolver)
    if not search_hints:
      global_index = 'robots: noindex\n' + global_index
    f.write(global_index)


def add_dict_to_dict(add_from, add_to):
  for key in add_from:
    if key in add_to:
      add_to[key].extend(add_from[key])
    else:
      add_to[key] = add_from[key]


def extract(py_modules,
            base_dir,
            private_map,
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
    visitor_cls: A class, typically a subclass of
      `doc_generator_visitor.DocGeneratorVisitor` that acumulates the indexes of
      objects to document.
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
      private_map=private_map)

  accumulator = visitor_cls()

  # The objects found during traversal, and their children are passed to each
  # of these visitors in sequence. Each visitor returns the list of children
  # to be passed to the next visitor.
  visitors = [api_filter, public_api.ignore_typing] + callbacks + [accumulator]

  traverse.traverse(py_module, visitors, short_name)

  return accumulator


EXCLUDED = set(['__init__.py', 'OWNERS', 'README.txt'])


def replace_refs(
    src_dir: str,
    output_dir: str,
    reference_resolvers: List[parser.ReferenceResolver],
    api_docs_relpath: List[str],
    file_pattern: str = '*.md',
):
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
    reference_resolvers: A list of `parser.ReferenceResolver` to make the
      replacements.
    api_docs_relpath: List of relative-path strings to the api_docs from the
      src_dir for each reference_resolver.
    file_pattern: Only replace references in files matching file_patters, using
      `fnmatch`. Non-matching files are copied unchanged.
  """

  # Iterate through all the source files and process them.
  for dirpath, _, filenames in os.walk(src_dir):
    depth = os.path.relpath(src_dir, start=dirpath)
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

      for resolver, rel_path in zip(reference_resolvers, api_docs_relpath):
        # If `rel_path` is an absolute path, `depth` is just discarded.
        relative_path_to_root = os.path.join(depth, rel_path)
        content = resolver.replace_references(content, relative_path_to_root)

      with open(full_out_path, 'wb') as f:
        f.write((content + '\n').encode('utf-8'))


class DocGenerator:
  """Main entry point for generating docs."""

  def __init__(
      self,
      root_title: str,
      py_modules: Sequence[Tuple[str, Any]],
      base_dir: Optional[Sequence[Union[str, pathlib.Path]]] = None,
      code_url_prefix: Sequence[str] = (),
      search_hints: bool = True,
      site_path: str = 'api_docs/python',
      private_map: Optional[Dict[str, str]] = None,
      visitor_cls: Type[
          doc_generator_visitor.DocGeneratorVisitor] = doc_generator_visitor
      .DocGeneratorVisitor,
      api_cache: bool = True,
      callbacks: Optional[List[public_api.ApiFilter]] = None,
      yaml_toc: bool = True,
      gen_redirects: bool = True,
      gen_report: bool = False,
      extra_docs: Optional[Dict[int, str]] = None,
  ):
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
      visitor_cls: An option to override the default visitor class
        `doc_generator_visitor.DocGeneratorVisitor`.
      api_cache: Bool. Generate an api_cache file. This is used to easily add
        api links for backticked symbols (like `tf.add`) in other docs.
      callbacks: Additional callbacks passed to `traverse`. Executed between the
        `PublicApiFilter` and the accumulator (`DocGeneratorVisitor`). The
        primary use case for these is to filter the list of children (see:
          `public_api.ApiFilter` for the required signature)
      yaml_toc: Bool which decides whether to generate _toc.yaml file or not.
      gen_redirects: Bool which decides whether to generate _redirects.yaml file
        or not.
      gen_report: If True, a report for the library is generated by linting the
        docstrings of its public API symbols.
      extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
        that need to be added to the markdown pages created.
    """
    self._root_title = root_title
    self._py_modules = py_modules
    self._short_name = py_modules[0][0]
    self._py_module = py_modules[0][1]

    if base_dir is None:
      # Determine the base_dir for the module
      base_dir = public_api.get_module_base_dirs(self._py_module)
    else:
      if isinstance(base_dir, (str, pathlib.Path)):
        base_dir = (base_dir,)
      base_dir = tuple(pathlib.Path(d) for d in base_dir)
    self._base_dir = base_dir

    if not self._base_dir:
      raise ValueError('`base_dir` cannot be empty')

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
    self._visitor_cls = visitor_cls
    self.api_cache = api_cache
    if callbacks is None:
      callbacks = []
    self._callbacks = callbacks
    self._yaml_toc = yaml_toc
    self._gen_redirects = gen_redirects
    self._gen_report = gen_report
    self._extra_docs = extra_docs

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
        src_dir=str(workdir),
        output_dir=str(workdir),
        reference_resolvers=[reference_resolver],
        api_docs_relpath=['api_docs'],
        file_pattern='*.md',
    )

    # Write the api docs.
    parser_config = self.make_parser_config(visitor, reference_resolver)
    work_py_dir = workdir / 'api_docs/python'
    write_docs(
        output_dir=str(work_py_dir),
        parser_config=parser_config,
        yaml_toc=self._yaml_toc,
        root_title=self._root_title,
        root_module_name=self._short_name.replace('.', '/'),
        search_hints=self._search_hints,
        site_path=self._site_path,
        gen_redirects=self._gen_redirects,
        gen_report=self._gen_report,
        extra_docs=self._extra_docs,
    )

    if self.api_cache:
      reference_resolver.to_json_file(
          str(work_py_dir / self._short_name.replace('.', '/') /
              '_api_cache.json'))

    try:
      os.makedirs(output_dir)
    except OSError as e:
      if e.strerror != 'File exists':
        raise

    # Typical results are something like:
    #
    # out_dir/
    #    {short_name}/
    #    _redirects.yaml
    #    _toc.yaml
    #    index.md
    #    {short_name}.md
    #
    # Copy the top level files to the `{output_dir}/`, delete and replace the
    # `{output_dir}/{short_name}/` directory.

    if self._gen_report:
      glob_pattern = '*.pb'
    else:
      glob_pattern = '*'

    for work_path in work_py_dir.glob(glob_pattern):
      out_path = pathlib.Path(output_dir) / work_path.name
      out_path.parent.mkdir(exist_ok=True, parents=True)

      if work_path.is_file():
        shutil.copy2(work_path, out_path)
      elif work_path.is_dir():
        shutil.rmtree(out_path, ignore_errors=True)
        shutil.copytree(work_path, out_path)
