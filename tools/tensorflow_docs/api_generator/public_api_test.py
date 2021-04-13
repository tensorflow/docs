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
"""Tests for tensorflow.tools.common.public_api."""

import inspect
import types

import typing

from absl.testing import absltest
# This import is using to test
from tensorflow_docs import api_generator
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import public_api


class PublicApiTest(absltest.TestCase):

  class TestVisitor(object):

    def __init__(self):
      self.symbols = set()
      self.last_parent = None
      self.last_children = None

    def __call__(self, path, parent, children):
      self.symbols.add(path)
      self.last_parent = parent
      self.last_children = list(children)  # Make a copy to preserve state.
      return children

  def test_call_forward(self):
    visitor = self.TestVisitor()

    api_visitors = [public_api.PublicAPIFilter(base_dir='/'), visitor]

    path = ('tf', 'test')
    parent = 'dummy'
    children = [('name1', 'thing1'), ('name2', 'thing2')]

    for api_visitor in api_visitors:
      children = api_visitor(path, parent, children)

    self.assertEqual(set([(
        'tf',
        'test',
    )]), visitor.symbols)
    self.assertEqual('dummy', visitor.last_parent)
    self.assertEqual([('name1', 'thing1'), ('name2', 'thing2')],
                     visitor.last_children)

  def test_private_child_removal(self):
    visitor = self.TestVisitor()
    api_visitors = [
        public_api.PublicAPIFilter(base_dir='/'),
        visitor,
    ]

    children = [('name1', 'thing1'), ('_name2', 'thing2')]
    path = ('tf', 'test')
    parent = 'dummy'
    for api_visitor in api_visitors:
      children = api_visitor(path, parent, children)

    # Make sure the private symbols are removed before the visitor is called.
    self.assertEqual([('name1', 'thing1')], visitor.last_children)
    self.assertEqual([('name1', 'thing1')], children)

  def test_private_map_child_removal(self):
    visitor = self.TestVisitor()

    api_visitors = [
        public_api.PublicAPIFilter(
            base_dir='/', private_map={'tf.test': ['mock']}), visitor
    ]

    children = [('name1', 'thing1'), ('mock', 'thing2')]
    path = ('tf', 'test')
    parent = 'dummy'

    for api_visitor in api_visitors:
      children = api_visitor(path, parent, children)
    # Make sure private aliases are removed.
    self.assertEqual([('name1', 'thing1')], visitor.last_children)
    self.assertEqual([('name1', 'thing1')], children)

  def test_local_definitions_filter(self):
    tf = types.ModuleType('tf')
    tf.keras = types.ModuleType('tf.keras')
    tf.keras.layers = types.ModuleType('tf.keras.layers')
    tf.keras.layers.Dense = lambda: None
    tf.keras.layers.Dense.__module__ = 'tf.keras.layers'

    tf.keras.Dense = tf.keras.layers.Dense

    tf.layers = types.ModuleType('tf.layers')
    tf.layers.Dense = tf.keras.layers.Dense

    def public_members(obj):
      members = inspect.getmembers(obj)
      return [
          (name, value) for name, value in members if not name.startswith('_')
      ]

    filtered_children = public_api.local_definitions_filter(
        ('tf', 'keras', 'layers'), tf.keras.layers,
        public_members(tf.keras.layers))
    filtered_names = [name for name, _ in filtered_children]

    self.assertCountEqual(['Dense'], filtered_names)

    filtered_children = public_api.local_definitions_filter(
        ('tf', 'keras'), tf.keras, public_members(tf.keras))
    filtered_names = [name for name, _ in filtered_children]

    self.assertCountEqual(['layers', 'Dense'], filtered_names)

    filtered_children = public_api.local_definitions_filter(
        ('tf', 'layers'), tf.layers, public_members(tf.layers))
    filtered_names = [name for name, _ in filtered_children]

    self.assertCountEqual([], filtered_names)

  def test_explicit_package_contents_filter_removes_modules_not_explicitly_imported(
      self):
    path = ('tensorflow_docs', 'api_generator')
    parent = api_generator
    members = inspect.getmembers(parent)
    members.append(('inspect', inspect))

    # Assert that parent is a module and is a package, and that the members of
    # parent include a module named `inspect`.
    self.assertTrue(inspect.ismodule(parent))
    self.assertTrue(hasattr(parent, '__path__'))
    self.assertIn('inspect', [name for name, _ in members])
    self.assertTrue(inspect.ismodule(inspect))

    filtered_members = public_api.explicit_package_contents_filter(
        path, parent, members)

    # Assert that the filtered_members do not include a module named `inspect`.
    self.assertNotIn('inspect', [name for name, _ in filtered_members])

  def test_explicit_package_contents_filter_removes_modules_imported_by_modules(
      self):
    path = ('tensorflow_docs', 'api_generator', 'public_api')
    parent = public_api
    members = inspect.getmembers(parent)

    # Assert that parent is a module and not a package, and that the members of
    # parent include a module named `inspect`.
    self.assertTrue(inspect.ismodule(parent))
    self.assertFalse(hasattr(parent, '__path__'))
    self.assertIn('inspect', [name for name, _ in members])
    self.assertTrue(inspect.ismodule(inspect))

    filtered_members = public_api.explicit_package_contents_filter(
        path, parent, members)

    # Assert that the filtered_members do not include a module named `inspect`.
    self.assertNotIn('inspect', [name for name, _ in filtered_members])

  def test_ignore_typing(self):
    children_before = [('a', 1), ('b', 3), ('c', typing.List)]
    children_after = public_api.ignore_typing('ignored', 'ignored',
                                              children_before)
    self.assertEqual(children_after, children_before[:-1])

  def test_ignore_class_attr(self):

    class MyClass:

      @doc_controls.do_not_doc_inheritable
      def my_method(self):
        pass

    private = public_api.PublicAPIFilter._is_private(
        self=None,
        path=('a', 'b'),
        parent=MyClass,
        name='my_method',
        obj=MyClass.my_method)
    self.assertTrue(private)


if __name__ == '__main__':
  absltest.main()
