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
import pathlib
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

  def test_filter_private_symbols(self):
    module = types.ModuleType('module')
    module.a = 1
    module._b = 2

    result = public_api.filter_private_symbols(('module'), module,
                                               [('a', module.a),
                                                ('_b', module._b)])
    self.assertEqual([('a', module.a)], list(result))

  def test_private_map_filter(self):
    private_map_filter = public_api.FilterPrivateMap({'tf.test': ['mock']})
    result = private_map_filter(
        path=('tf', 'test'),
        parent='dummy',
        children=[('name1', 'thing1'), ('mock', 'thing2')])

    self.assertEqual([('name1', 'thing1')], list(result))

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

  def test_get_imported_symbols(self):
    source = """
        import sub0
        import pkg.sub1
        from pkg import sub2
        from pkg.sub3 import sub_sub1
        from pkg.sub4 import *
        from pkg import sub5 as r1
        from pkg import sub6 as r2, sub7, sub8 as r3

        """
    imported = public_api._get_imported_symbols(source)
    self.assertCountEqual(
        ['sub0', 'sub2', 'sub_sub1', 'r1', 'r2', 'sub7', 'r3'], imported)

  def test_ignore_typing(self):
    children_before = [('a', 1), ('b', 3), ('c', typing.List)]
    children_after = public_api.ignore_typing('ignored', 'ignored',
                                              children_before)
    self.assertEqual(children_after, children_before[:-1])

  def test_ignore_class_attr(self):

    class MyClass:

      def method(self):
        pass

      @doc_controls.do_not_doc_inheritable
      def hidden_method(self):
        pass

    class SubClass(MyClass):

      def hidden_method(self):
        'still hidden'

    result = public_api.filter_doc_controls_skip(
        path=('a', 'b'),
        parent=SubClass,
        children=[('method', SubClass.method),
                  ('hidden_method', SubClass.hidden_method)])

    self.assertEqual([('method', MyClass.method)], list(result))

  def test_filter_all(self):
    module = types.ModuleType('module')
    module.__all__ = ['a']
    module.a = 1
    module.b = 2

    result = public_api.filter_module_all(('module'), module, [('a', module.a),
                                                               ('b', module.b)])
    self.assertEqual([('a', module.a)], list(result))

  def test_filter_base_dirs(self):
    module = types.ModuleType('module')
    module.__file__ = '/1/2/3/module'
    module.a = 1
    module.sub1 = types.ModuleType('sub1')
    module.sub1.__file__ = '/1/2/3/4/sub1'
    module.sub2 = types.ModuleType('sub2')
    module.sub2.__file__ = '/1/2/bad/sub2'

    my_filter = public_api.FilterBaseDirs(base_dirs=[pathlib.Path('/1/2/3/')])

    result = my_filter(
        path=('module',),
        parent=module,
        children=[('a', module.a), ('sub1', module.sub1),
                  ('sub2', module.sub2)])
    self.assertEqual([('a', module.a), ('sub1', module.sub1)], list(result))

  def test_filter_base_dir_pointing_to_submodule_dir(self):
    module = types.ModuleType('module')
    module.__file__ = '/1/2/3/module'
    module.submodule = types.ModuleType('submodule')
    module.submodule.__file__ = '/1/2/3/submodule/__init__.py'

    test_filter = public_api.FilterBaseDirs(
        base_dirs=[pathlib.Path('/1/2/3/submodule')])
    result = test_filter(
        path=('module',),
        parent=module,
        children=[('submodule', module.submodule)])

    self.assertEqual([('submodule', module.submodule)], list(result))


if __name__ == '__main__':
  absltest.main()
