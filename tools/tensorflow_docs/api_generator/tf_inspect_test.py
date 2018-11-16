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
"""Unit tests for tf_inspect."""

# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools

from absl.testing import absltest

from tensorflow_docs.api_generator import tf_inspect


class TfInspectTest(absltest.TestCase):

  def testGetArgSpecOnPartialPositionalArgumentOnly(self):
    """Tests getargspec on partial function with only positional arguments."""

    def func(m, n):
      return 2 * m + n

    partial_func = functools.partial(func, 7)
    argspec = tf_inspect.ArgSpec(
        args=['n'], varargs=None, keywords=None, defaults=None)

    self.assertEqual(argspec, tf_inspect.getargspec(partial_func))

  def testGetArgSpecOnPartialInvalidArgspec(self):
    """Tests getargspec on partial function that doesn't have valid argspec."""

    def func(m, n, l, k=4):
      return 2 * m + l + n * k

    partial_func = functools.partial(func, n=7)

    with self.assertRaisesRegexp(ValueError, 'Function has keyword-only.*'):
      tf_inspect.getargspec(partial_func)

  def testGetArgSpecOnPartialValidArgspec(self):
    """Tests getargspec on partial function with valid argspec."""

    def func(m, n, l, k=4):
      return 2 * m + l + n * k

    partial_func = functools.partial(func, n=7, l=2)
    argspec = tf_inspect.FullArgSpec(
        args=['m'],
        varargs=None,
        varkw=None,
        defaults=None,
        kwonlyargs=['n', 'l', 'k'],
        kwonlydefaults={
            'n': 7,
            'l': 2,
            'k': 4
        },
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))
    with self.assertRaisesRegexp(ValueError, 'Function has keyword-only.*'):
      tf_inspect.getargspec(partial_func)

  def testGetArgSpecOnPartialNoArgumentsLeft(self):
    """Tests getargspec on partial function that prunes all arguments."""

    def func(m, n):
      return 2 * m + n

    partial_func = functools.partial(func, 7, 10)
    argspec = tf_inspect.ArgSpec(
        args=[], varargs=None, keywords=None, defaults=None)

    self.assertEqual(argspec, tf_inspect.getargspec(partial_func))

  def testGetArgSpecOnPartialKeywordArgument(self):
    """Tests getargspec on partial function that prunes some arguments."""

    def func(m, n):
      return 2 * m + n

    partial_func = functools.partial(func, n=7)
    argspec = tf_inspect.FullArgSpec(
        args=['m'],
        varargs=None,
        varkw=None,
        defaults=None,
        kwonlyargs=['n'],
        kwonlydefaults={'n': 7},
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))

    with self.assertRaisesRegexp(ValueError, 'Function has keyword-only.*'):
      tf_inspect.getargspec(partial_func)

  def testGetArgSpecOnPartialKeywordArgumentWithDefaultValue(self):
    """Tests getargspec on partial function that prunes argument by keyword."""

    def func(m=1, n=2):
      return 2 * m + n

    partial_func = functools.partial(func, n=7)
    argspec = tf_inspect.FullArgSpec(
        args=['m'],
        varargs=None,
        varkw=None,
        defaults=(1,),
        kwonlyargs=['n'],
        kwonlydefaults={'n': 7},
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))

    with self.assertRaisesRegexp(ValueError, 'Function has keyword-only.*'):
      tf_inspect.getargspec(partial_func)

  def testGetArgSpecOnPartialWithVarargs(self):
    """Tests getargspec on partial function with variable arguments."""

    def func(m, *arg):
      return m + len(arg)

    partial_func = functools.partial(func, 7, 8)
    argspec = tf_inspect.ArgSpec(
        args=[], varargs='arg', keywords=None, defaults=None)

    self.assertEqual(argspec, tf_inspect.getargspec(partial_func))

  def testGetArgSpecOnPartialWithVarkwargs(self):
    """Tests getargspec on partial function with variable keyword arguments."""

    def func(m, n, **kwarg):
      return m * n + len(kwarg)

    partial_func = functools.partial(func, 7)
    argspec = tf_inspect.ArgSpec(
        args=['n'], varargs=None, keywords='kwarg', defaults=None)

    self.assertEqual(argspec, tf_inspect.getargspec(partial_func))

  def testGetArgSpecOnCallableObject(self):

    class Callable(object):

      def __call__(self, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.ArgSpec(
        args=['self', 'a', 'b', 'c'],
        varargs=None,
        keywords=None,
        defaults=(1, 'hello'))

    test_obj = Callable()
    self.assertEqual(argspec, tf_inspect.getargspec(test_obj))

  def testGetArgSpecOnInitClass(self):

    class InitClass(object):

      def __init__(self, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.ArgSpec(
        args=['self', 'a', 'b', 'c'],
        varargs=None,
        keywords=None,
        defaults=(1, 'hello'))

    self.assertEqual(argspec, tf_inspect.getargspec(InitClass))

  def testGetArgSpecOnNewClass(self):

    class NewClass(object):

      def __new__(cls, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.ArgSpec(
        args=['cls', 'a', 'b', 'c'],
        varargs=None,
        keywords=None,
        defaults=(1, 'hello'))

    self.assertEqual(argspec, tf_inspect.getargspec(NewClass))

  def testGetFullArgsSpecForPartial(self):

    def func(a, b):
      del a, b

    partial_function = functools.partial(func, 1)
    argspec = tf_inspect.FullArgSpec(
        args=['b'],
        varargs=None,
        varkw=None,
        defaults=None,
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_function))

  def testGetFullArgSpecOnPartialNoArgumentsLeft(self):
    """Tests getfullargspec on partial function that prunes all arguments."""

    def func(m, n):
      return 2 * m + n

    partial_func = functools.partial(func, 7, 10)
    argspec = tf_inspect.FullArgSpec(
        args=[],
        varargs=None,
        varkw=None,
        defaults=None,
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))

  def testGetFullArgSpecOnPartialWithVarargs(self):
    """Tests getfullargspec on partial function with variable arguments."""

    def func(m, *arg):
      return m + len(arg)

    partial_func = functools.partial(func, 7, 8)
    argspec = tf_inspect.FullArgSpec(
        args=[],
        varargs='arg',
        varkw=None,
        defaults=None,
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))

  def testGetFullArgSpecOnPartialWithVarkwargs(self):
    """Tests getfullargspec.

    Tests on partial function with variable keyword arguments.
    """

    def func(m, n, **kwarg):
      return m * n + len(kwarg)

    partial_func = functools.partial(func, 7)
    argspec = tf_inspect.FullArgSpec(
        args=['n'],
        varargs=None,
        varkw='kwarg',
        defaults=None,
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(partial_func))

  def testGetFullArgSpecOnCallableObject(self):

    class Callable(object):

      def __call__(self, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.FullArgSpec(
        args=['self', 'a', 'b', 'c'],
        varargs=None,
        varkw=None,
        defaults=(1, 'hello'),
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    test_obj = Callable()
    self.assertEqual(argspec, tf_inspect.getfullargspec(test_obj))

  def testGetFullArgSpecOnInitClass(self):

    class InitClass(object):

      def __init__(self, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.FullArgSpec(
        args=['self', 'a', 'b', 'c'],
        varargs=None,
        varkw=None,
        defaults=(1, 'hello'),
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(InitClass))

  def testGetFullArgSpecOnNewClass(self):

    class NewClass(object):

      def __new__(cls, a, b=1, c='hello'):
        pass

    argspec = tf_inspect.FullArgSpec(
        args=['cls', 'a', 'b', 'c'],
        varargs=None,
        varkw=None,
        defaults=(1, 'hello'),
        kwonlyargs=[],
        kwonlydefaults=None,
        annotations={})

    self.assertEqual(argspec, tf_inspect.getfullargspec(NewClass))


if __name__ == '__main__':
  absltest.main()
