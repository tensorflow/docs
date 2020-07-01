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
"""Traversing Python modules and classes."""
import inspect
import sys

from google.protobuf.message import Message as ProtoMessage

__all__ = ['traverse']


def _filter_module_all(path, root, children):
  """Filters module children based on the "__all__" arrtibute.

  Args:
    path: API to this symbol
    root: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` filtered to respect __all__
  """
  del path
  if not (inspect.ismodule(root) and hasattr(root, '__all__')):
    return children
  module_all = set(root.__all__)
  children = [(name, value) for (name, value) in children if name in module_all]

  return children


def _add_proto_fields(path, root, children):
  """Add properties to Proto classes, so they can be documented.

  Warning: This inserts the Properties into the class so the rest of the system
  is unaffected. This patching is acceptable because there is never a reason to
  run other tensorflow code in the same process as the doc generator.

  Args:
    path: API to this symbol
    root: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` with proto fields added as properties.
  """
  del path
  if not inspect.isclass(root) or not issubclass(root, ProtoMessage):
    return children

  descriptor = getattr(root, 'DESCRIPTOR', None)
  if descriptor is None:
    return children
  fields = descriptor.fields
  if not fields:
    return children

  field = fields[0]
  # Make the dictionaries mapping from int types and labels to type and
  # label names.
  types = {
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

    type_name = types[field.type]
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
    setattr(root, name, prop)

  children = dict(children)
  children.update(field_properties)
  children = sorted(children.items(), key=lambda item: item[0])

  return children


def _filter_builtin_modules(path, root, children):
  """Filters module children to remove builtin modules.

  Args:
    path: API to this symbol
    root: The object
    children: A list of (name, object) pairs.

  Returns:
    `children` with all builtin modules removed.
  """
  del path
  del root
  # filter out 'builtin' modules
  filtered_children = []
  for name, child in children:
    # Do not descend into built-in modules
    if inspect.ismodule(child) and child.__name__ in sys.builtin_module_names:
      continue
    filtered_children.append((name, child))
  return filtered_children


def _traverse_internal(root, visitors, stack, path):
  """Internal helper for traverse."""
  new_stack = stack + [root]

  # Only traverse modules and classes
  if not inspect.isclass(root) and not inspect.ismodule(root):
    return

  try:
    children = inspect.getmembers(root)
  except ImportError:
    # On some Python installations, some modules do not support enumerating
    # members (six in particular), leading to import errors.
    children = []

  # Break cycles.
  filtered_children = []
  for name, child in children:
    if any(child is item for item in new_stack):  # `in`, but using `is`
      continue
    filtered_children.append((name, child))
  children = filtered_children

  # Apply all callbacks, allowing each to filter the children
  for visitor in visitors:
    children = visitor(path, root, list(children))

  for name, child in children:
    # Break cycles
    child_path = path + (name,)
    _traverse_internal(child, visitors, new_stack, child_path)


def traverse(root, visitors, root_name):
  """Recursively enumerate all members of `root`.

  Similar to the Python library function `os.path.walk`.

  Traverses the tree of Python objects starting with `root`, depth first.
  Parent-child relationships in the tree are defined by membership in modules or
  classes. The function `visit` is called with arguments
  `(path, parent, children)` for each module or class `parent` found in the tree
  of python objects starting with `root`. `path` is a string containing the name
  with which `parent` is reachable from the current context. For example, if
  `root` is a local class called `X` which contains a class `Y`, `visit` will be
  called with `('Y', X.Y, children)`).

  If `root` is not a module or class, `visit` is never called. `traverse`
  never descends into built-in modules.

  `children`, a list of `(name, object)` pairs are determined by
  `inspect.getmembers`. To avoid visiting parts of the tree, `children` can
  be modified in place, using `del` or slice assignment.

  Cycles (determined by reference equality, `is`) stop the traversal. A stack of
  objects is kept to find cycles. Objects forming cycles may appear in
  `children`, but `visit` will not be called with any object as `parent` which
  is already in the stack.

  Traversing system modules can take a long time, it is advisable to pass a
  `visit` callable which denylists such modules.

  Args:
    root: A python object with which to start the traversal.
    visitors: A list of callables. Each taking `(path, parent, children)` as
      arguments, and returns a list of accepted children.
    root_name: The short-name of the root module.
  """
  base_visitors = [
      _filter_module_all,
      _add_proto_fields,
      _filter_builtin_modules
  ]
  _traverse_internal(root, base_visitors + visitors, [], (root_name,))
