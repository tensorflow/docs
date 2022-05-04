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
import logging

from typing import Any, Dict, List, Sequence, Tuple

from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import public_api


# To see the logs pass: --logger_levels=tensorflow_docs:DEBUG --alsologtostderr
_LOGGER = logging.getLogger(__name__)

__all__ = ['traverse']


class _Traverser:
  """Crawls the public API."""

  def __init__(self, filters: Sequence[public_api.ApiFilter],
               accumulator: doc_generator_visitor.DocGeneratorVisitor):
    self.filters = list(filters)
    self.accumulator = accumulator
    self.children_cache: Dict[int, List[Tuple[str, Any]]] = {}

  def traverse(self, root, stack, path):
    """Execute the traversal."""
    new_stack = stack + [root]

    # Only traverse modules and classes
    if not inspect.isclass(root) and not inspect.ismodule(root):
      return

    _LOGGER.debug('path: %s', path)
    children = self.children_cache.get(id(root), None)
    if children is None:
      children = self.get_children(root, new_stack, path)
      self.children_cache[id(root)] = children
    else:
      _LOGGER.debug('    children (cached): %s', [n for n, c in children])

    self.accumulator(path, root, children)

    for name, child in children:
      child_path = path + (name,)
      self.traverse(child, new_stack, child_path)

  def get_children(self, root, new_stack, path) -> public_api.Children:
    """Return the children for an object."""
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

    _LOGGER.debug('    children: %s', [n for n, c in children])
    # Apply all callbacks, allowing each to filter the children
    for fil in self.filters:
      old_names = [n for n, c in children]
      children = fil(path, root, children)
      children = list(children)
      new_names = [n for n, c in children]

      if old_names != new_names:
        _LOGGER.debug('  filter: %s', fil)
        _LOGGER.debug('    children: %s', new_names)

    return children


def traverse(root, filters, accumulator, root_name) -> None:
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
    filters: A list of callables. Each taking `(path, parent, children)` as
      arguments, and returns a list of accepted children.
    accumulator: a DocGenerator to accumulate the results.
    root_name: The short-name of the root module.
  """
  _Traverser(filters, accumulator).traverse(root, [], (root_name,))
