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
"""Utility functions."""

import importlib
import logging
import pkgutil


def _onerror(name):
  logging.exception('Failed to load package: %r', name)


def recursive_import(root, strict=False):
  """Recursively imports all the modules under a root package.

  Args:
    root: A python package.
    strict: Bool, if `True` raise exceptions, else just log them.

  Returns:
    A list of all imported modules.
  """

  modules = []

  kwargs = {}
  # If strict=False, ignore errors during `pkgutil.walk_packages`.
  if not strict:
    kwargs = {'onerror': _onerror}

  for _, name, _ in pkgutil.walk_packages(
      root.__path__, prefix=root.__name__ + '.', **kwargs):
    try:
      modules.append(importlib.import_module(name))
    # And ignore the same set of errors if import_module fails, these are not
    # triggered by walk_packages.
    except Exception:  # pylint: disable=broad-except
      if strict:
        raise
      else:
        logging.exception('Failed to load module: %r', name)

  return modules
