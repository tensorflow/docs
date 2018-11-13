# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
"""TFDecorator-aware replacements for the inspect module."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import namedtuple
import functools
import inspect
from inspect import *  # pylint: disable=wildcard-import
import sys

import six

if sys.version_info.major < 3:
  FullArgSpec = namedtuple('FullArgSpec', [
      'args', 'varargs', 'varkw', 'defaults', 'kwonlyargs', 'kwonlydefaults',
      'annotations'
  ])

  def getfullargspec(target):
    """A python2 version of `inspect.getfullargspec`.

    Args:
      target: the target object to inspect.

    Returns:
      A `FullArgSpec`.
    """
    if isinstance(target, functools.partial):
      return _get_fullargspec_for_partial(target)
    argspecs = getargspec(target)
    fullargspecs = FullArgSpec(
        args=argspecs.args,
        varargs=argspecs.varargs,
        varkw=argspecs.keywords,
        defaults=argspecs.defaults,
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})
    return fullargspecs

  def getargspec(obj):
    """A py2 version of `inspect.getargspec`, more compatible with py3.

    Note: `getfullargspec` is recommended as the python 2/3 compatible
    replacement for this function.

    Args:
      obj: A function, partial function, or callable object.

    Returns:
      an `ArgSpec` that describes the callable's signature.

    Raises:
      ValueError: When callable's signature can not be expressed with
        ArgSpec.
      TypeError: For objects of unsupported types.
    """
    if isinstance(obj, functools.partial):
      full = _get_fullargspec_for_partial(obj)
      if full.kwonlyargs or full.annotations:
        raise ValueError('Function has keyword-only arguments or annotations, '
                         'use getfullargspec() API which can support them')

      return inspect.ArgSpec(
          args=full.args,
          varargs=full.varargs,
          keywords=full.varkw,
          defaults=full.defaults)

    try:
      return inspect.getargspec(obj)
    except TypeError:
      pass

    if isinstance(obj, type):
      try:
        return inspect.getargspec(obj.__init__)
      except TypeError:
        pass

      try:
        return inspect.getargspec(obj.__new__)
      except TypeError:
        pass

    # The `type(obj)` ensures that if a class is received we don't return
    # the signature of it's __call__ method.
    return inspect.getargspec(type(obj).__call__)

  def _get_fullargspec_for_partial(obj):
    """Implements `getargspec` for `functools.partial` objects.

    Args:
      obj: The `functools.partial` obeject

    Returns:
      An `inspect.ArgSpec`
    Raises:
      ValueError: When callable's signature can not be expressed with
        ArgSpec.
    """
    n_prune_args = len(obj.args)
    partial_keywords = obj.keywords or {}

    args, varargs, keywords, defaults = getargspec(obj.func)

    # Partial function may give default value to any argument, therefore length
    # of default value list must be len(args) to allow each argument to
    # potentially be given a default value.
    all_defaults = [None] * len(args)

    if defaults:
      all_defaults[-len(defaults):] = defaults

    # Prune the args that have a value set by partial.
    args = args[n_prune_args:]
    all_defaults = all_defaults[n_prune_args:]

    # Fill in keyword defaults provided by partial.
    for kw, default in six.iteritems(partial_keywords):
      if kw in args:
        idx = args.index(kw)
        all_defaults[idx] = default

    # Split key-word only args and defaults from others.
    # Everything from the first partial_keyword is now key-word only.
    known_kws = [kw for kw in partial_keywords if kw in args]
    if known_kws:
      stop = min([args.index(kw) for kw in known_kws])
      args, kwonlyargs = args[:stop], args[stop:]
      all_defaults, kwonlydefaults = all_defaults[:stop], all_defaults[stop:]
      kwonlydefaults = dict(zip(kwonlyargs, kwonlydefaults))
    else:
      kwonlyargs = []
      kwonlydefaults = None

    # Find first argument with default value set.
    first_default = next((idx for idx, x in enumerate(all_defaults) if x), None)
    if first_default is None:
      result_defaults = None
    else:
      result_defaults = tuple(all_defaults[first_default:])

    return FullArgSpec(
        args,
        varargs,
        keywords,
        result_defaults,
        kwonlyargs=kwonlyargs,
        kwonlydefaults=kwonlydefaults,
        annotations={})
