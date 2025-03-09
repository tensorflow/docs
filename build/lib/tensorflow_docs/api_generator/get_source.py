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
"""Simple get_source."""
import ast
import inspect
import textwrap

from typing import Any, Optional, Sequence, Tuple


def get_ast(py_object) -> Optional[ast.AST]:
  if isinstance(py_object, str):
    source = textwrap.dedent(py_object)
  else:
    source = get_source(py_object)
  if source is None:
    return None

  try:
    return ast.parse(source)
  except Exception:  # pylint: disable=broad-except
    return None


def get_source(py_object: Any) -> Optional[str]:
  if py_object is not None:
    try:
      return textwrap.dedent(inspect.getsource(py_object))
    except Exception:  # pylint: disable=broad-except
      # A wide-variety of errors can be thrown here.
      pass
  return None


def get_source_lines(
    py_object: Any) -> Tuple[Optional[Sequence[str]], Optional[int]]:
  if py_object is not None:
    try:
      return inspect.getsourcelines(py_object)
    except Exception:  # pylint: disable=broad-except
      # A wide-variety of errors can be thrown here.
      pass
  return None, None
