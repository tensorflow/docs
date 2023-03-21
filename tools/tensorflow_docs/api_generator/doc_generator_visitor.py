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
from __future__ import annotations

import collections
import dataclasses
import enum
import inspect
import logging


from typing import Any, Dict, List, Optional, NamedTuple, Sequence, Tuple

from tensorflow_docs.api_generator import obj_type as obj_type_lib


# To see the logs pass: --logger_levels=tensorflow_docs:DEBUG --alsologtostderr
_LOGGER = logging.getLogger(__name__)

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
  return is_immutable_type or (isinstance(py_object, tuple) and py_object == ())  # pylint: disable=g-explicit-bool-comparison


@dataclasses.dataclass
class PathTreeNode(object):
  """Represents a path to an object in the API, an object can have many paths.

  Attributes:
    path: A tuple of strings containing the path to the object from the root
      like `('tf', 'losses', 'hinge')`
    py_object: The python object.
    children: A dictionary from short name to `PathTreeNode`, of this node's
      children.
    parent: This node's parent. This is a tree, there can only be one.
    short_name: The last path component
    full_name: All path components joined with "."
  """
  path: ApiPath
  py_object: Any
  parent: Optional[PathTreeNode] = None
  children: Dict[str, PathTreeNode] = dataclasses.field(default_factory=dict)

  def __hash__(self):
    return id(self)

  def __repr__(self):
    return f'{type(self).__name__}({self.full_name})'

  __str__ = __repr__

  def __eq__(self, other):
    raise ValueError("Don't try to compare these")

  @property
  def short_name(self) -> str:
    return self.path[-1]

  @property
  def full_name(self) -> str:
    return '.'.join(self.path)


class PathTree(Dict[ApiPath, PathTreeNode]):
  """An index/tree of all object-paths in the API.

  Items must be inserted in order, from root to leaf.


  Attributes:
    root: The root `PathTreeNode`
  """

  def __init__(self):
    root = PathTreeNode(path=(), py_object=None, parent=None, children={})
    super().__setitem__((), root)

    self.root: PathTreeNode = root
    self._nodes_for_id: Dict[int, List[PathTreeNode]] = (
        collections.defaultdict(list))

  def __eq__(self, other):
    raise ValueError("Don't try to compare these")

  def iter_nodes(self):
    """Iterate over the nodes in BFS order."""
    stack = collections.deque([self.root])
    while stack:
      children = list(stack.popleft().children.values())
      yield from children
      stack.extend(children)

  def __contains__(self, path: ApiPath) -> bool:  # pylint: disable=useless-super-delegation
    # TODO(b/184563451): remove
    return super().__contains__(path)

  def __setitem__(self, path: ApiPath, obj: Any):
    """Add an object to the tree.

    Args:
      path: A tuple of strings.
      obj: The python object.
    """
    assert path not in self

    parent_path = path[:-1]
    parent = self[parent_path]

    node = PathTreeNode(path=path, py_object=obj, parent=parent)

    super().__setitem__(path, node)
    if not maybe_singleton(obj):
      # We cannot use the duplicate mechanism for some constants, since e.g.,
      # id(c1) == id(c2) with c1=1, c2=1. This isn't problematic since constants
      # have no usable docstring and won't be documented automatically.
      nodes = self.nodes_for_obj(obj)
      nodes.append(node)
    parent.children[node.short_name] = node

  def nodes_for_obj(self, py_object) -> List[PathTreeNode]:
    return self._nodes_for_id[id(py_object)]


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

    self.path_tree = PathTree()
    self.api_tree = None

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
    return self._reverse_index

  @property
  def duplicate_of(self):
    """A map from duplicate full names to a preferred fully qualified name.

    This map only contains names that are not themself a preferred name.

    It is computed when it, `reverse_index`, or `duplicates` are first accessed.

    Returns:
      The map from duplicate name to preferred name.
    """
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
    if parent_path not in self.path_tree:
      self.path_tree[parent_path] = parent

    if not (inspect.ismodule(parent) or inspect.isclass(parent)):
      raise TypeError('Unexpected type in visitor -- '
                      f'{parent_name}: {parent!r}')

    for name, child in children:
      child_path = parent_path + (name,)
      self.path_tree[child_path] = child

      full_name = '.'.join([parent_name, name]) if parent_name else name
      self._index[full_name] = child
      self._tree[parent_name].append(name)

    return children

  class NameScore(NamedTuple):
    defining_class_score: int
    experimental_score: int
    keras_score: int
    module_length_score: int
    path: ApiPath

  def _score_name(self, path: ApiPath) -> NameScore:
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
      path: APiPath to score, for example `('tf','estimator','Estimator')`

    Returns:
      A tuple of scores. When sorted the preferred name will have the lowest
      value.
    """
    py_object = self.path_tree[path].py_object
    if len(path) == 1:
      return self.NameScore(-99, -99, -99, -99, path)

    short_name = path[-1]
    container = self.path_tree[path[:-1]].py_object

    # Prefer the reference that is not in a class.
    defining_class_score = -1
    container_type = obj_type_lib.ObjType.get(container)
    if container_type is obj_type_lib.ObjType.CLASS:
      if short_name in container.__dict__:
        # If a alias points into a class, prefer the defining class
        defining_class_score = 0
      else:
        defining_class_score = 1

    experimental_score = -1
    if 'contrib' in path or any('experimental' in part for part in path):
      experimental_score = 1

    keras_score = 1
    if 'keras' in path:
      keras_score = -1

    if inspect.ismodule(py_object):
      # prefer short paths for modules
      module_length_score = len(path)
    else:
      module_length_score = self._get_module_length_score(path)

    return self.NameScore(
        defining_class_score=defining_class_score,
        experimental_score=experimental_score,
        keras_score=keras_score,
        module_length_score=module_length_score,
        path=path)

  def _get_module_length_score(self, path):
    partial_path = list(path)
    while partial_path:
      container = self.path_tree[tuple(partial_path[:-1])].py_object
      partial_path.pop()
      if inspect.ismodule(container):
        break

    module_length = len(partial_path)

    if module_length == 2:
      # `tf.submodule.thing` is better than `tf.thing`
      module_length_score = -1
    else:
      # shorter is better
      module_length_score = module_length

    return module_length_score

  def build(self):
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

    self.api_tree = ApiTree.from_path_tree(self.path_tree, self._score_name)

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

    for path, node in self.path_tree.items():
      if not path:
        continue
      full_name = node.full_name
      py_object = node.py_object
      object_id = id(py_object)
      if full_name in duplicates:
        continue

      aliases = self.path_tree.nodes_for_obj(py_object)
      # maybe_singleton types can't be looked up by object.
      if not aliases:
        aliases = [node]

      name_tuples = [alias.path for alias in aliases]

      # Choose the main name with a lexical sort on the tuples returned by
      # by _score_name.
      main_name_tuple = min(name_tuples, key=self._score_name)
      main_name = '.'.join(main_name_tuple)

      names = ['.'.join(name_tuple) for name_tuple in name_tuples]
      if name_tuples:
        duplicates[main_name] = sorted(names)

      for name in names:
        if name != main_name:
          duplicate_of[name] = main_name

      # Set the reverse index to the canonical name.
      if not maybe_singleton(py_object):
        reverse_index[object_id] = main_name

    self._duplicate_of = duplicate_of
    self._duplicates = duplicates
    self._reverse_index = reverse_index


@dataclasses.dataclass(repr=False)
class ApiTreeNode(PathTreeNode):
  """A node in the ApiTree."""
  aliases: List[ApiPath] = dataclasses.field(default_factory=list)
  physical_path: Optional[ApiPath] = None

  @property
  def obj_type(self) -> obj_type_lib.ObjType:
    return obj_type_lib.ObjType.get(self.py_object)

  class OutputType(enum.Enum):
    PAGE = 'page'
    FRAGMENT = 'fragment'

  def output_type(self) -> OutputType:
    obj_type = obj_type_lib.ObjType.get(self.py_object)

    if obj_type in (obj_type_lib.ObjType.CLASS, obj_type_lib.ObjType.MODULE):
      return self.OutputType.PAGE
    elif obj_type in (obj_type_lib.ObjType.CALLABLE,
                      obj_type_lib.ObjType.TYPE_ALIAS):
      assert self.parent is not None
      parent_type = obj_type_lib.ObjType.get(self.parent.py_object)
      if parent_type is obj_type_lib.ObjType.CLASS:
        return self.OutputType.FRAGMENT
      else:
        return self.OutputType.PAGE
    else:
      return self.OutputType.FRAGMENT


class ApiTree(Dict[ApiPath, ApiTreeNode]):
  """Public API index.

  Items must be inserted in order from root to leaves.

  Lookup a path-tuple to fetch a node:

  ```
  node = index[path]
  ```

  Use the `node_from_obj` method to lookup the node for a python object:

  ```
  node = index.node_from_obj(obj)
  ```

  Remember that `maybe_singleton` (numbers, strings, tuples) classes can't be
  looked up this way.

  To build a tree, nodes must be inserted in tree order starting from the root.


  Attributes:
    root: The root `ApiFileNode` of the tree.
  """

  def __init__(self):
    root = ApiTreeNode(
        path=(), py_object=None, parent=None, aliases=[()])  # type: ignore
    self.root = root
    super().__setitem__((), root)
    self._nodes = []
    self._node_for_object = {}

  def __eq__(self, other):
    raise ValueError("Don't try to compare these")

  def node_for_object(self, obj: Any) -> Optional[ApiTreeNode]:
    if maybe_singleton(obj):
      return None
    return self._node_for_object.get(id(obj), None)

  def __contains__(self, path: ApiPath) -> bool:  # pylint: disable=useless-super-delegation
    # TODO(b/184563451): remove
    return super().__contains__(path)

  def iter_nodes(self):
    """Iterate over the nodes in BFS order."""
    stack = collections.deque([self.root])
    while stack:
      children = list(stack.popleft().children.values())
      yield from children
      stack.extend(children)

  def __setitem__(self, *args, **kwargs):
    raise TypeError('Use .insert instead of setitem []')

  def insert(self, path: ApiPath, py_object: Any, aliases: List[ApiPath]):
    """Add an object to the index."""
    _LOGGER.debug('ApiTree.insert')
    _LOGGER.debug('  path: %s', path)
    _LOGGER.debug('  py_object: %s', py_object)
    _LOGGER.debug('  aliases: %s', aliases)
    assert path not in self, 'A path was inserted twice.'

    parent_path = path[:-1]
    parent = self[parent_path]

    node = ApiTreeNode(
        path=path,
        py_object=py_object,
        aliases=aliases,
        parent=parent,
        physical_path=self._get_physical_path(py_object))

    super().__setitem__(path, node)
    self._nodes.append(node)
    for alias in aliases:
      if alias == path:
        continue
      assert alias not in self
      super().__setitem__(alias, node)

    self._node_for_object[id(node.py_object)] = node

    parent.children[node.short_name] = node

  def _get_physical_path(self, py_object):
    physical_path = None
    obj_type = obj_type_lib.ObjType.get(py_object)
    if obj_type in [obj_type.CLASS, obj_type.CALLABLE]:
      try:
        physical_path = tuple(
            py_object.__module__.split('.') + py_object.__qualname__.split('.'))
      except AttributeError:
        pass
    elif obj_type is obj_type.MODULE:
      physical_path = tuple(py_object.__name__.split('.'))

    return physical_path

  @classmethod
  def from_path_tree(cls, path_tree: PathTree, score_name_fn) -> ApiTree:
    """Create an ApiTree from an PathTree.

    Args:
      path_tree: The `PathTree` to convert.
      score_name_fn: The name scoring function.

    Returns:
      an `ApiIndex`, created from `path_tree`.
    """
    self = cls()

    active_nodes = collections.deque(path_tree.root.children.values())
    while active_nodes:
      current_node = active_nodes.popleft()
      if current_node.path in self:
        continue

      duplicate_nodes = set(
          path_tree.nodes_for_obj(current_node.py_object))

      if not duplicate_nodes:
        # Singleton objects will return `[]`. So look up the parent object's
        # duplicate nodes and collect their children.
        assert current_node.parent is not None
        parent_nodes = path_tree.nodes_for_obj(current_node.parent.py_object)
        duplicate_nodes = [
            parent_node.children[current_node.short_name]
            for parent_node in parent_nodes
        ]

      parents = [
          node.parent for node in duplicate_nodes if node.parent is not None
      ]

      # Choose the priority name with a lexical sort on the tuples returned by
      # _score_name.
      if not all(parent.path in self for parent in parents):
        # rewind
        active_nodes.appendleft(current_node)
        # do each duplicate's immediate parents first.
        for parent in parents:
          if parent.path in self:
            continue
          active_nodes.appendleft(parent)
        continue
      # If we've made it here, the immediate parents of each of the paths have
      # been processed, so now we can choose its priority name.
      aliases = [node.path for node in duplicate_nodes]

      priority_path = self._choose_priority_path(aliases, score_name_fn)

      if priority_path is None:
        # How did this happen?
        # No parents in the public api -> you are not in the public API.
        continue

      self.insert(priority_path, current_node.py_object, aliases)

      active_nodes.extend(current_node.children.values())

    return self

  def _choose_priority_path(self, aliases: Sequence[ApiPath],
                            score_name_fn) -> Optional[ApiPath]:
    # Only consider a path an option for the priority_path if its parent-path
    # is the priority_path for that object.
    priority_path_options = []
    for alias in aliases:
      parent_path = alias[:-1]

      if self[parent_path].path == parent_path:
        priority_path_options.append(alias)

    try:
      return min(priority_path_options, key=score_name_fn)
    except ValueError:
      return None
