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
"""Visitor restricting traversal to only the public tensorflow API."""

import ast
import inspect
import os
import pathlib
import typing
from typing import Any, Callable, List, Sequence, Tuple

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor

_TYPING_IDS = frozenset(
    id(obj)
    for obj in typing.__dict__.values()
    if not doc_generator_visitor.maybe_singleton(obj))


Children = List[Tuple[str, Any]]
ApiFilter = Callable[[Tuple[str, ...], Any, Children], Children]


def get_module_base_dirs(module) -> Tuple[pathlib.Path, ...]:
  """Returns the list of base_dirs.

  Args:
    module: A python module object.

  Returns:
    A tuple of paths. Usually 1 unless the module is a namespace package.
  """
  if not hasattr(module, '__file__'):
    return ()

  mod_file = module.__file__
  if mod_file is None:
    # namespace packages have `__file__=None` but the directory *paths* are
    # available in `__path__._path`.
    # https://www.python.org/dev/peps/pep-0451/
    # This is a **list of paths**.
    base_dirs = module.__path__._path  # pylint: disable=protected-access
  elif mod_file.endswith('__init__.py'):
    # A package directory will have an `__init__.py`,
    # accept anything in that directory.
    base_dirs = [os.path.dirname(mod_file)]
  else:
    # This is a single file module. The file is the base_dir.
    base_dirs = [mod_file]

  return tuple(pathlib.Path(b) for b in base_dirs)


def ignore_typing(path: Sequence[str], parent: Any,
                  children: Children) -> Children:
  """Removes all children that are members of the typing module.

  Arguments:
    path: A tuple of name parts forming the attribute-lookup path to this
      object. For `tf.keras.layers.Dense` path is:
        ("tf","keras","layers","Dense")
    parent: The parent object.
    children: A list of (name, value) pairs. The attributes of the patent.

  Returns:
    A filtered list of children `(name, value)` pairs.
  """
  del path
  del parent

  children = [(name, child_obj)
              for (name, child_obj) in children
              if id(child_obj) not in _TYPING_IDS]

  return children


def local_definitions_filter(path: Sequence[str], parent: Any,
                             children: Children) -> Children:
  """Filters children recursively.

  Only returns those defined in this package.

  This follows the API for visitors defined by `traverse.traverse`.

  This is a much tighter constraint than the default "base_dir" filter which
  ensures that only objects defined within the package root are documented.
  This applies a similar constraint, to each submodule.

  in the api-tree below, `Dense` is defined in `tf.keras.layers`, but imported
  into `tf.layers` and `tf.keras`.

  ```
  tf
    keras
      from tf.keras.layers import Dense
      layers
         class Dense(...)
    layers
      from tf.keras.layers import Dense
  ```

  This filter hides the `tf.layers.Dense` reference as `Dense` is not defined
  within the `tf.layers` package. The reference at `tf.keras.Dense` is still
  visible because dense is defined inside the `tf.keras` tree.

  One issue/feature to be aware of with this approach is that if you hide
  the defining module, the object will not be visible in the docs at all. For
  example, if used with the package below, `util_1` and `util_2` are never
  documented.

  ```
  my_package
    _utils    # leading `_` means private.
      def util_1
      def util_2
    subpackage
      from my_package._utils import *
  ```
  Arguments:
    path: A tuple or name parts forming the attribute-lookup path to this
      object. For `tf.keras.layers.Dense` path is:
        ("tf","keras","layers","Dense")
    parent: The parent object.
    children: A list of (name, value) pairs. The attributes of the patent.

  Returns:
    A filtered list of children `(name, value)` pairs.
  """
  del path

  if not inspect.ismodule(parent):
    return children

  filtered_children = []
  for pair in children:
    # Find the name of the module the child was defined in.
    _, child = pair
    if inspect.ismodule(child):
      maybe_submodule = child.__name__
    elif inspect.isfunction(child) or inspect.isclass(child):
      maybe_submodule = child.__module__
    else:
      maybe_submodule = parent.__name__

    # Skip if child was not defined within the parent module
    in_submodule = maybe_submodule.startswith(parent.__name__)
    if not in_submodule:
      continue

    filtered_children.append(pair)

  return filtered_children


def _get_imported_symbols(obj):
  """Returns a list of symbol names imported by the given `obj`."""

  class ImportNodeVisitor(ast.NodeVisitor):
    """An `ast.Visitor` that collects the names of imported symbols."""

    def __init__(self):
      self.imported_symbols = []

    def _add_imported_symbol(self, node):
      self.imported_symbols.extend([alias.name for alias in node.names])

    def visit_Import(self, node):  # pylint: disable=invalid-name
      self._add_imported_symbol(node)

    def visit_ImportFrom(self, node):  # pylint: disable=invalid-name
      self._add_imported_symbol(node)

  source = inspect.getsource(obj)
  tree = ast.parse(source)
  visitor = ImportNodeVisitor()
  visitor.visit(tree)
  return visitor.imported_symbols


def explicit_package_contents_filter(path: Sequence[str], parent: Any,
                                     children: Children) -> Children:
  """Filter modules to only include explicit contents.

  This function returns the children explicitly included by this module, meaning
  that it will exclude:

  *   Modules in a package not explicitly imported by the package (submodules
      are implicitly injected into their parent's namespace).
  *   Modules imported by a module that is not a package.

  This filter is useful if you explicitly define your API in the packages of
  your library, but do not expliticly define that API in the `__all__` variable
  of each module. The purpose is to make it easier to maintain that API.

  Note: This filter does work with wildcard imports, however it is generally not
  recommended to use wildcard imports.

  Args:
    path: A tuple of names forming the path to the object.
    parent: The parent object.
    children: A list of (name, value) tuples describing the attributes of the
      patent.

  Returns:
    A filtered list of children `(name, value)` pairs.
  """
  del path  # Unused
  is_parent_module = inspect.ismodule(parent)
  is_parent_package = is_parent_module and hasattr(parent, '__path__')
  if is_parent_package:
    imported_symbols = _get_imported_symbols(parent)
  filtered_children = []
  for child in children:
    name, obj = child
    if inspect.ismodule(obj):
      # Do not include modules in a package not explicitly imported by the
      # package.
      if is_parent_package and name not in imported_symbols:
        continue
      # Do not include modules imported by a module that is not a package.
      if is_parent_module and not is_parent_package:
        continue
    filtered_children.append(child)
  return filtered_children


ALLOWED_DUNDER_METHODS = frozenset([
    '__abs__', '__add__', '__and__', '__bool__', '__call__', '__concat__',
    '__contains__', '__div__', '__enter__', '__eq__', '__exit__',
    '__floordiv__', '__ge__', '__getitem__', '__gt__', '__init__', '__invert__',
    '__iter__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__',
    '__mul__', '__new__', '__ne__', '__neg__', '__pos__', '__nonzero__',
    '__or__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rfloordiv__',
    '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rsub__',
    '__rtruediv__', '__rxor__', '__sub__', '__truediv__', '__xor__',
    '__version__'
])


class PublicAPIFilter(object):
  """Visitor to use with `traverse` to filter just the public API."""

  def __init__(self, base_dir, private_map=None):
    """Constructor.

    Args:
      base_dir: The directory to take source file paths relative to.
      private_map: A mapping from dotted path like "tf.symbol" to a list of
        names. Included names will not be listed at that location.
    """
    self._base_dir = base_dir
    self._private_map = private_map or {}

  def _is_private(self, path, parent, name, obj):
    """Returns whether a name is private or not."""

    # Skip objects blocked by doc_controls.
    if doc_controls.should_skip(obj):
      return True

    if isinstance(parent, type):
      if doc_controls.should_skip_class_attr(parent, name):
        return True

    if doc_controls.should_doc_private(obj):
      return False

    if inspect.ismodule(obj):
      mod_base_dirs = get_module_base_dirs(obj)
      # This check only handles normal packages/modules. Namespace-package
      # contents will get filtered when the submodules are checked.
      if len(mod_base_dirs) == 1:
        mod_base_dir = mod_base_dirs[0]
        # Check that module is in one of the `self._base_dir`s
        if not any(base in mod_base_dir.parents for base in self._base_dir):
          return True

    # Skip objects blocked by the private_map
    if name in self._private_map.get('.'.join(path), []):
      return True

    # Skip "_" hidden attributes
    if name.startswith('_') and name not in ALLOWED_DUNDER_METHODS:
      return True

    return False

  def __call__(self, path: Sequence[str], parent: Any,
               children: Children) -> Children:
    """Visitor interface, see `traverse` for details."""

    # Avoid long waits in cases of pretty unambiguous failure.
    if inspect.ismodule(parent) and len(path) > 10:
      raise RuntimeError('Modules nested too deep:\n\n{}\n\nThis is likely a '
                         'problem with an accidental public import.'.format(
                             '.'.join(path)))

    # Remove things that are not visible.
    children = [(child_name, child_obj)
                for child_name, child_obj in list(children)
                if not self._is_private(path, parent, child_name, child_obj)]

    return children
