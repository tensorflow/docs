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
import dataclasses
import inspect
import os
import pathlib
import sys
import types
import typing
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple, Union

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import get_source

from google.protobuf.message import Message as ProtoMessage

try:
  import proto  # pylint: disable=g-import-not-at-top  # pytype: disable=import-error
except ImportError:
  proto = None


_TYPING_IDS = frozenset(
    id(obj)
    for obj in typing.__dict__.values()
    if not doc_generator_visitor.maybe_singleton(obj))


Children = Iterable[Tuple[str, Any]]
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
    base_dirs = module.__path__._path  # pylint: disable=protected-access  # pytype: disable=attribute-error
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


def _get_imported_symbols(obj: Union[str, types.ModuleType]):
  """Returns a list of symbol names imported by the given `obj`."""

  class ImportNodeVisitor(ast.NodeVisitor):
    """An `ast.Visitor` that collects the names of imported symbols."""

    def __init__(self):
      self.imported_symbols = []

    def _add_imported_symbol(self, node):
      for alias in node.names:
        name = alias.asname or alias.name
        if name == '*':
          continue
        if '.' in name:
          continue
        self.imported_symbols.append(name)

    def visit_Import(self, node):  # pylint: disable=invalid-name
      self._add_imported_symbol(node)

    def visit_ImportFrom(self, node):  # pylint: disable=invalid-name
      self._add_imported_symbol(node)

  tree = get_source.get_ast(obj)
  if tree is None:
    return []

  visitor = ImportNodeVisitor()
  visitor.visit(tree)
  return visitor.imported_symbols


def explicit_package_contents_filter(path: Sequence[str], parent: Any,
                                     children: Children) -> Children:
  """Filter submodules, only keep what's explicitly included.

  This filter only affects the visibility of **modules**. Other objects are not
  affected.

  This filter is useful if you explicitly define your API in the packages of
  your library (the __init__.py files), but do not expliticly define that API
  in the `__all__` variable of each module. The purpose is to make it easier to
  maintain that API.

  **This filter makes it so that modules are only documented where they are
  explicitly imported in an __init__.py**

  ### Packages

  Lots of imports **indirectly** inject modules into package namespaces, this
  filter helps you ignore those. Anywhere you `import pkg.sub1` it will inject
  `sub1` into the `pkg` namsspace.

  When filtering a package it only keeps modules that are **directly**
  impotrted in the package. This code, injects `[sub0, sub1, sub2, sub3, sub4,
  sub_sub1, *]` into the pkg namespace:

  pkg/__init__.py

  ```
  import sub0
  import pkg.sub1
  from pkg import sub2
  from pkg.sub3 import sub_sub1
  from pkg.sub4 import *
  ```

  But this filter will only keep the modules `[sub0, sub2, sub_sub1]` in the
  docs for `pkg`.

  ### Regular modules

  For regular modules all modules in the namespace are assumed to be
  implementation details and/or documented in their source location. For example
  in this package:

  ```
  pkg/
    __init__.py
    sub1.py
    sub2.py
  ```

  If you `import sub2` in `__init__.py` `sub2` will documented in `pkg`
  But if you `import sub2` in `sub1.py` `sub2` will not be documented in `sub1`

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
    '__abs__', '__add__', '__and__', '__array__', '__bool__', '__call__',
    '__concat__', '__contains__', '__div__', '__enter__', '__eq__', '__exit__',
    '__floordiv__', '__ge__', '__getitem__', '__gt__', '__init__', '__invert__',
    '__iter__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__',
    '__mod__', '__mul__', '__new__', '__ne__', '__neg__', '__pos__',
    '__nonzero__', '__or__', '__pow__', '__radd__', '__rand__', '__rdiv__',
    '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__',
    '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
    '__rtruediv__', '__rxor__', '__sub__', '__truediv__', '__xor__',
    '__version__'
])


@dataclasses.dataclass
class FailIfNestedTooDeep:
  max_depth: int

  def __call__(self, path: Sequence[str], parent: Any,
               children: Children) -> Children:
    if inspect.ismodule(parent) and len(path) > 10:
      raise RuntimeError('Modules nested too deep:\n\n{}\n\nThis is likely a '
                         'problem with an accidental public import.'.format(
                             '.'.join(path)))
    return children


@dataclasses.dataclass
class FilterBaseDirs:
  """A class for filtering based on a list of allowed parent directories."""
  base_dirs: Sequence[pathlib.Path]

  def __call__(self, path: Sequence[str], parent: Any,
               children: Children) -> Children:
    for name, child in children:
      if not inspect.ismodule(child):
        yield name, child
        continue
      mod_base_dirs = get_module_base_dirs(child)
      # This check only handles normal packages/modules. Namespace-package
      # contents will get filtered when the submodules are checked.
      if len(mod_base_dirs) == 1:
        mod_base_dir = mod_base_dirs[0]
        # Check that module is, or is in one of the `self._base_dir`s
        if not (any(base in mod_base_dir.parents for base in self.base_dirs) or
                mod_base_dir in self.base_dirs):
          continue
      yield name, child


@dataclasses.dataclass
class FilterPrivateMap:
  private_map: Dict[str, List[str]]

  def __call__(self, path: Sequence[str], parent: Any,
               children: Children) -> Children:
    if self.private_map is None:
      yield from children

    for name, child in children:
      if name in self.private_map.get('.'.join(path), []):
        continue
      yield (name, child)


def filter_private_symbols(path: Sequence[str], parent: Any,
                           children: Children) -> Children:
  del path
  del parent
  for name, child in children:
    # Skip "_" hidden attributes
    if name.startswith('_') and name not in ALLOWED_DUNDER_METHODS:
      if not doc_controls.should_doc_private(child):
        continue
    yield (name, child)


def filter_doc_controls_skip(path: Sequence[str], parent: Any,
                             children: Children) -> Children:
  del path
  for name, child in children:
    if doc_controls.should_skip(child):
      continue
    if isinstance(parent, type):
      if doc_controls.should_skip_class_attr(parent, name):
        continue
    yield (name, child)


def filter_module_all(path: Sequence[str], parent: Any,
                      children: Children) -> Children:
  """Filters module children based on the "__all__" arrtibute.

  Args:
    path: API to this symbol
    parent: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` filtered to respect __all__
  """
  del path
  if not (inspect.ismodule(parent) and hasattr(parent, '__all__')):
    return children
  module_all = set(parent.__all__)
  children = [(name, value) for (name, value) in children if name in module_all]

  return children


def add_proto_fields(path: Sequence[str], parent: Any,
                     children: Children) -> Children:
  """Add properties to Proto classes, so they can be documented.

  Warning: This inserts the Properties into the class so the rest of the system
  is unaffected. This patching is acceptable because there is never a reason to
  run other tensorflow code in the same process as the doc generator.

  Args:
    path: API to this symbol
    parent: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` with proto fields added as properties.
  """
  del path
  if not inspect.isclass(parent):
    return children

  real_parent = parent
  if not issubclass(parent, ProtoMessage):
    if proto is not None:
      if issubclass(parent, proto.message.Message):
        parent = parent.pb()
        children = [
            (name, value) for (name, value) in children if name != 'meta'
        ]
      else:
        return children

  descriptor = getattr(parent, 'DESCRIPTOR', None)
  if descriptor is None:
    return children
  fields = descriptor.fields
  if not fields:
    return children

  field = fields[0]
  # Make the dictionaries mapping from int types and labels to type and
  # label names.
  field_types = {
      getattr(field, name): name
      for name in dir(field)
      if name.startswith('TYPE')
  }

  labels = {
      getattr(field, name): name
      for name in dir(field)
      if name.startswith('LABEL')
  }

  field_properties = {}

  for field in fields:
    name = field.name
    doc_parts = []

    label = labels[field.label].lower().replace('label_', '')
    if label != 'optional':
      doc_parts.append(label)

    type_name = field_types[field.type]
    if type_name == 'TYPE_MESSAGE':
      type_name = field.message_type.name
    elif type_name == 'TYPE_ENUM':
      type_name = field.enum_type.name
    else:
      type_name = type_name.lower().replace('type_', '')

    doc_parts.append(type_name)
    doc_parts.append(name)
    doc = '`{}`'.format(' '.join(doc_parts))
    prop = property(fget=lambda x: x, doc=doc)
    field_properties[name] = prop

  for name, prop in field_properties.items():
    setattr(real_parent, name, prop)

  children = dict(children)
  children.update(field_properties)
  children = sorted(children.items(), key=lambda item: item[0])

  return children


def filter_builtin_modules(path: Sequence[str], parent: Any,
                           children: Children) -> Children:
  """Filters module children to remove builtin modules.

  Args:
    path: API to this symbol
    parent: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` with all builtin modules removed.
  """
  del path
  del parent
  # filter out 'builtin' modules
  filtered_children = []
  for name, child in children:
    # Do not descend into built-in modules
    if inspect.ismodule(child) and child.__name__ in sys.builtin_module_names:
      continue
    filtered_children.append((name, child))
  return filtered_children
