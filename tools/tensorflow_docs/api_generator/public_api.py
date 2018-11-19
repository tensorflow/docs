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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import inspect

from tensorflow_docs.api_generator import doc_controls


class PublicAPIVisitor(object):
  """Visitor to use with `traverse` to visit exactly the public TF API."""

  def __init__(self,
               visitor,
               base_dir,
               do_not_descend_map=None,
               private_map=None):
    """Constructor.

    `visitor` should be a callable suitable as a visitor for `traverse`. It will
    be called only for members of the public TensorFlow API.

    Args:
      visitor: A visitor to call for the public API.
      base_dir: The directory to take source file paths relative to.
      do_not_descend_map: A mapping from dotted path like "tf.symbol" to a list
        of names. Included names will have no children listed.
      private_map: A mapping from dotted path like "tf.symbol" to a list
        of names. Included names will not be listed at that location.
    """
    self._visitor = visitor
    self._base_dir = base_dir
    self._do_not_descend_map = do_not_descend_map or {}
    self._private_map = private_map or {}

  def _is_private(self, path, name, obj):
    """Return whether a name is private."""
    # Skip objects blocked by doc_controls.
    if doc_controls.should_skip(obj):
      return True

    # Skip modules outside of the package root.
    if inspect.ismodule(obj):
      if hasattr(obj, '__file__'):
        if not obj.__file__.startswith(self._base_dir):
          return True

    # Skip objects blocked by the private_map
    if name in self._private_map.get('.'.join(path), []):
      return True

    # Skip "_" hidden attributes
    is_dunder = name.startswith('__') and name.endswith('__')
    if name.startswith('_') and not is_dunder:
      return True

    if name in ['__base__', '__class__']:
      return True

    return False

  def __call__(self, path, parent, children):
    """Visitor interface, see `traverse` for details."""

    # Avoid long waits in cases of pretty unambiguous failure.
    if inspect.ismodule(parent) and len(path) > 10:
      raise RuntimeError(
          'Modules nested too deep:\n\n%s\n\nThis is likely a '
          'problem with an accidental public import.' % ('.'.join(path)))

    # No children if "do_not_descend" is set.
    parent_path = '.'.join(path[:-1])
    name = path[-1]
    if name in self._do_not_descend_map.get(parent_path, []):
      del children[:]

    # Remove things that are not visible.
    for child_name, child in list(children):
      if self._is_private(path, child_name, child):
        children.remove((child_name, child))

    self._visitor(path, parent, children)
