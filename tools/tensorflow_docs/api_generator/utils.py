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


def recursive_import(root, strict=False):
  """Recursively imports all the modules under a root package.

  Args:
    root: A python package.
    strict: Bool, if `True` raise exceptions, else just log them.

  Returns:
    A list of all imported modules.
  """

  modules = []
  for _, name, _ in pkgutil.walk_packages(
      root.__path__, prefix=root.__name__ + '.'):
    try:
      modules.append(importlib.import_module(name))
    except (ImportError, AttributeError, NotImplementedError):
      if strict:
        raise
      else:
        logging.exception('Failed to load module: %r', name)

  return modules
