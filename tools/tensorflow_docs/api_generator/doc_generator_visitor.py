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
"""A `traverse` visitor for processing documentation."""

import collections
import inspect

from typing import Any, Dict, List, Optional, Tuple

ApiPath = Tuple[str, ...]


def maybe_singleton(py_object: Any) -> bool:
  """Returns `True` if `py_object` might be a singleton value .

  Many immutable values in python act like singletons: small ints, some strings,
  Bools, None, the empty tuple.

  We can't rely on looking these up by their `id()` to find their name or
  duplicates.

  This function checks if the object is one of those maybe singleton values.

  Args:
    py_object: the object to check.

  Returns:
    A bool, True if the object might be a singleton.
  """
  # isinstance accepts nested tuples of types.
  immutable_types = (int, str, bytes, float, complex, bool, type(None))
  is_immutable_type = isinstance(py_object, immutable_types)

  # Check if the object is the empty tuple.
  return is_immutable_type or py_object is ()  # pylint: disable=literal-comparison


class ApiTreeNode(object):
  """Represents a single API end-point.

  Attributes:
    path: A tuple of strings containing the path to the object from the root
      like `('tf', 'losses', 'hinge')`
    obj: The python object.
    children: A dictionary from short name to `ApiTreeNode`, including the
      children nodes.
    parent: The parent node.
    short_name: The last path component
    full_name: All path components joined with "."
  """

  def __init__(self, path: ApiPath, obj: Any, parent: Optional['ApiTreeNode']):
    self.path = path
    self.py_object = obj
    self.children: Dict[str, 'ApiTreeNode'] = {}
    self.parent = parent

  @property
  def short_name(self) -> str:
    return self.path[-1]

  @property
  def full_name(self) -> str:
    return '.'.join(self.path)


class ApiTree(object):
  """Represents all api end-points as a tree.

  Items must be inserted in order, from root to leaf.

  Attributes:
    index: A dict, mapping from path tuples to `ApiTreeNode`.
    aliases: A dict, mapping from object ids to a list of all `ApiTreeNode` that
      refer to the object.
    root: The root `ApiTreeNode`
  """

  def __init__(self):
    root = ApiTreeNode(path=(), obj=None, parent=None)
    self.index: Dict[ApiPath, ApiTreeNode] = {(): root}
    self.aliases: Dict[ApiPath,
                       List[ApiTreeNode]] = collections.defaultdict(list)
    self.root: ApiTreeNode = root

  def __contains__(self, path: ApiPath) -> bool:
    """Returns `True` if path exists in the tree.

    Args:
      path: A tuple of strings, the api path to the object.

    Returns:
      True if `path` exists in the tree.
    """
    return path in self.index

  def __getitem__(self, path: ApiPath) -> ApiTreeNode:
    """Fetch an item from the tree.

    Args:
      path: A tuple of strings, the api path to the object.

    Returns:
      An `ApiTreeNode`.

    Raises:
      KeyError: If no node can be found at that path.
    """
    return self.index[path]

  def __setitem__(self, path: ApiPath, obj: Any):
    """Add an object to the tree.

    Args:
      path: A tuple of strings.
      obj: The python object.
    """
    parent_path = path[:-1]
    parent = self.index[parent_path]

    node = ApiTreeNode(path=path, obj=obj, parent=parent)

    self.index[path] = node
    if not maybe_singleton(obj):
      # We cannot use the duplicate mechanism for some constants, since e.g.,
      # id(c1) == id(c2) with c1=1, c2=1. This isn't problematic since constants
      # have no usable docstring and won't be documented automatically.
      self.aliases[id(obj)].append(node)
    parent.children[node.short_name] = node


class DocGeneratorVisitor(object):
  """A visitor that generates docs for a python object when __call__ed."""

  def __init__(self):
    """Make a visitor.

    This visitor expects to be called on each node in the api. It is passed the
    path to an object, the object, and the filtered list of the object's
    children. (see the `__call__` method for details.

    This object accumulates the various data-structures necessary to build the
    docs, including (see the property definitions for details.):

    In the decsription below "main name" is the object's preferred fully
    qualified name.

    Params:
      index: A mapping from main names to python python objects.
      tree: A mapping from main names to a list if attribute names.
      reverse_index: Mapping from python object ids to main names.
        Note that this doesn't work for python numbers, strings or tuples.
      duplicate_of: A mapping from a fully qualified names to the object's
        main name. The main names are not included as keys.
      duplicates: A mapping from main names to lists of other fully qualified
        names for the object.
    """
    self._index: Dict[str, Any] = {}
    self._tree: Dict[str, List[str]] = {}
    self._reverse_index: Dict[int, str] = None
    self._duplicates: Dict[str, List[str]] = None
    self._duplicate_of: Dict[str, str] = None

    self._api_tree = ApiTree()

  @property
  def index(self):
    """A map from fully qualified names to objects to be documented.

    The index is filled when the visitor is passed to `traverse`.

    Returns:
      The index filled by traversal.
    """
    return self._index

  @property
  def tree(self):
    """A map from fully qualified names to all its child names for traversal.

    The full name to member names map is filled when the visitor is passed to
    `traverse`.

    Returns:
      The full name to member name map filled by traversal.
    """
    return self._tree

  @property
  def reverse_index(self):
    """A map from `id(object)` to the preferred fully qualified name.

    This map only contains non-primitive objects (no numbers or strings) present
    in `index` (for primitive objects, `id()` doesn't quite do the right thing).

    It is computed when it, `duplicate_of`, or `duplicates` are first accessed.

    Returns:
      The `id(object)` to full name map.
    """
    self._maybe_find_duplicates()
    return self._reverse_index

  @property
  def duplicate_of(self):
    """A map from duplicate full names to a preferred fully qualified name.

    This map only contains names that are not themself a preferred name.

    It is computed when it, `reverse_index`, or `duplicates` are first accessed.

    Returns:
      The map from duplicate name to preferred name.
    """
    self._maybe_find_duplicates()
    return self._duplicate_of

  @property
  def duplicates(self):
    """A map from preferred full names to a list of all names for this symbol.

    This function returns a map from preferred (main) name for a symbol to a
    lexicographically sorted list of all aliases for that name (incl. the main
    name). Symbols without duplicate names do not appear in this map.

    It is computed when it, `reverse_index`, or `duplicate_of` are first
    accessed.

    Returns:
      The map from main name to list of all duplicate names.
    """
    self._maybe_find_duplicates()
    return self._duplicates

  def __call__(self, parent_path, parent, children):
    """Visitor interface, see `tensorflow/tools/common:traverse` for details.

    This method is called for each symbol found in a traversal using
    `tensorflow/tools/common:traverse`. It should not be called directly in
    user code.

    Args:
      parent_path: A tuple of strings. The fully qualified path to a symbol
        found during traversal.
      parent: The Python object referenced by `parent_name`.
      children: A list of `(name, py_object)` pairs enumerating, in alphabetical
        order, the children (as determined by `inspect.getmembers`) of
          `parent`. `name` is the local name of `py_object` in `parent`.

    Returns:
      The list of children, with any __metaclass__ removed.

    Raises:
      RuntimeError: If this visitor is called with a `parent` that is not a
        class or module.
    """
    parent_name = '.'.join(parent_path)
    self._index[parent_name] = parent
    self._tree[parent_name] = []
    if parent_path not in self._api_tree:
      self._api_tree[parent_path] = parent

    if not (inspect.ismodule(parent) or inspect.isclass(parent)):
      raise RuntimeError('Unexpected type in visitor -- '
                         f'{parent_name}: {parent!r}')

    for name, child in children:
      self._api_tree[parent_path + (name,)] = child

      full_name = '.'.join([parent_name, name]) if parent_name else name
      self._index[full_name] = child
      self._tree[parent_name].append(name)

    return children

  def _score_name(self, name):
    """Return a tuple of scores indicating how to sort for the best name.

    This function is meant to be used as the `key` to the `sorted` function.

    This returns a score tuple composed of the following scores:
      defining_class: Prefers method names pointing into the defining class,
        over a subclass (`ParentClass.method` over `Subclass.method`, if it
        referrs to the same method implementation).
      experimental: Prefers names that are not in "contrib" or "experimental".
      keras: Prefers keras names to non-keras names.
      module_length: Prefers submodules (tf.sub.thing) over the root namespace
        (tf.thing) over deeply nested paths (tf.a.b.c.thing)
      name: Fallback, sorts lexicographically on the full_name.

    Args:
      name: the full name to score, for example `tf.estimator.Estimator`

    Returns:
      A tuple of scores. When sorted the preferred name will have the lowest
      value.
    """
    parts = name.split('.')
    short_name = parts[-1]
    if len(parts) == 1:
      return (-99, -99, -99, -99, short_name)

    container = self._index.get('.'.join(parts[:-1]), name)

    defining_class_score = 1
    if inspect.isclass(container):
      if short_name in container.__dict__:
        # prefer the defining class
        defining_class_score = -1

    experimental_score = -1
    if 'contrib' in parts or any('experimental' in part for part in parts):
      experimental_score = 1

    keras_score = 1
    if 'keras' in parts:
      keras_score = -1

    while parts:
      container = self._index['.'.join(parts)]
      if inspect.ismodule(container):
        break
      parts.pop()

    module_length = len(parts)

    if len(parts) == 2:
      # `tf.submodule.thing` is better than `tf.thing`
      module_length_score = -1
    else:
      # shorter is better
      module_length_score = module_length

    return (defining_class_score, experimental_score, keras_score,
            module_length_score, name)

  def _maybe_find_duplicates(self):
    """Compute data structures containing information about duplicates.

    Find duplicates in `index` and decide on one to be the "main" name.

    Computes a reverse_index mapping each object id to its main name.

    Also computes a map `duplicate_of` from aliases to their main name (the
    main name itself has no entry in this map), and a map `duplicates` from
    main names to a lexicographically sorted list of all aliases for that name
    (incl. the main name).

    All these are computed and set as fields if they haven't already.
    """
    if self._reverse_index is not None:
      return

    # Maps the id of a symbol to its fully qualified name. For symbols that have
    # several aliases, this map contains the first one found.
    # We use id(py_object) to get a hashable value for py_object. Note all
    # objects in _index are in memory at the same time so this is safe.
    reverse_index = {}

    # Decide on main names, rewire duplicates and make a duplicate_of map
    # mapping all non-main duplicates to the main name. The main symbol
    # does not have an entry in this map.
    duplicate_of = {}

    # Duplicates maps the main symbols to the set of all duplicates of that
    # symbol (incl. itself).
    duplicates = {}

    for path, node in self._api_tree.index.items():
      if not path:
        continue
      full_name = node.full_name
      py_object = node.py_object
      object_id = id(py_object)
      if full_name in duplicates:
        continue

      aliases = self._api_tree.aliases[object_id]
      if not aliases:
        aliases = [node]

      names = [alias.full_name for alias in aliases]

      names = sorted(names)
      # Choose the main name with a lexical sort on the tuples returned by
      # by _score_name.
      main_name = min(names, key=self._score_name)

      if names:
        duplicates[main_name] = list(names)

      names.remove(main_name)
      for name in names:
        duplicate_of[name] = main_name

      # Set the reverse index to the canonical name.
      if not maybe_singleton(py_object):
        reverse_index[object_id] = main_name

    self._duplicate_of = duplicate_of
    self._duplicates = duplicates
    self._reverse_index = reverse_index
