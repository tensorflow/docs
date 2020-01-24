# lint as: python3
# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
"""This is a version of tf_inspect, without a tensorflow dependency.

See: tensorflow/python/util/tf_inspect.py

It also avoids the complexity of py2/3 compatibility by being py3 only.

Every function in inspect is wrapped to "unwrap_tf_decorator" it's argument
before applying the real inspect function.

The only exception to this is "getdoc", as decorators (@deprecated) may modify
the docstring and the doc system needs to report the decorator's docstring.
"""
import functools
import inspect


def unwrap_tf_decorator(py_object):
  """Unwraps any TF-Decorator style decoratotrs from the object.

  See `tensorflow.python.util.tf_decorator`.

  Args:
    py_object: A python object.

  Returns:
    A tuple: (decorators, unwraped_object)
  """
  decorators = []

  while True:
    decorator = getattr(py_object, '_tf_decorator', None)
    if decorator is None:
      break
    unwrapped_py_obj = getattr(decorator, 'decorated_target', None)
    if unwrapped_py_obj is None:
      break
    py_object = unwrapped_py_obj
    decorators.append(decorator)

  return decorators, py_object


def _undecorate_and_apply(inspect_fun, obj, *args, **kwargs):
  """Unwrap `tf_decorators` from obj before applying `inspect_fun`."""
  _, unwraped_obj = unwrap_tf_decorator(obj)
  return inspect_fun(unwraped_obj, *args, **kwargs)


def _wrap_inspect():
  """Wrap the functions in `inspect` with `_undecorate_and_apply`.

  Wrap all functions using "_undecortate_and_apply" so they remove
  `tf_decorators` before applying the builtin inspect functions.

  Returns:
    A dict of containing the contents of inspect.__dict__, with the functions
    wrapped.
  """
  # This is a reference to the module's __dict__, changes to it are reflected
  # in the module's contents.
  module_dict = {}

  for name, inspect_fun in inspect.getmembers(inspect):
    if name.startswith('_'):
      continue
    elif not callable(inspect_fun):
      module_dict[name] = inspect_fun
    elif name == 'getdoc':
      module_dict[name] = inspect_fun
    else:
      wrapped_fn = functools.partial(_undecorate_and_apply, inspect_fun)
      module_dict[name] = wrapped_fn

  return module_dict


globals().update(_wrap_inspect())
