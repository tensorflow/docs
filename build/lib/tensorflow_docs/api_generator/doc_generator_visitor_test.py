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
"""Tests for tools.docs.doc_generator_visitor."""

import dataclasses
import io
import os
import textwrap
import types

from absl.testing import absltest

from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import generate_lib
from tensorflow_docs.api_generator import toc as toc_lib


class NoDunderVisitor(doc_generator_visitor.DocGeneratorVisitor):

  def __call__(self, parent_name, parent, children):
    """Drop all the dunder methods to make testing easier."""
    children = [
        (name, obj) for (name, obj) in children if not name.startswith('_')
    ]
    return super(NoDunderVisitor, self).__call__(parent_name, parent, children)


class TestDocGenerator(generate_lib.DocGenerator):

  def __init__(self, py_modules):
    kwargs = {}
    kwargs['py_modules'] = py_modules
    kwargs['root_title'] = 'TensorFlow'
    kwargs['visitor_cls'] = NoDunderVisitor
    kwargs['code_url_prefix'] = '/'
    super().__init__(**kwargs)


class DocGeneratorVisitorTest(absltest.TestCase):

  def test_call_module(self):
    visitor = doc_generator_visitor.DocGeneratorVisitor()
    visitor(
        ('doc_generator_visitor',), doc_generator_visitor,
        [('DocGeneratorVisitor', doc_generator_visitor.DocGeneratorVisitor)])

    self.assertEqual({'doc_generator_visitor': ['DocGeneratorVisitor']},
                     visitor.tree)

    self.assertEqual({
        'doc_generator_visitor': doc_generator_visitor,
        'doc_generator_visitor.DocGeneratorVisitor':
        doc_generator_visitor.DocGeneratorVisitor,
    }, visitor.index)

  def test_call_class(self):

    class ExampleClass:

      def example_method(self):
        pass

    visitor = doc_generator_visitor.DocGeneratorVisitor()
    visitor(
        parent_path=('ExampleClass',),
        parent=ExampleClass,
        children=[('example_method', ExampleClass.example_method)])

    self.assertEqual({'ExampleClass': ['example_method']}, visitor.tree)
    self.assertEqual(
        {
            'ExampleClass': ExampleClass,
            'ExampleClass.example_method': ExampleClass.example_method,
        }, visitor.index)

  def test_call_raises(self):
    visitor = doc_generator_visitor.DocGeneratorVisitor()
    with self.assertRaises(TypeError):
      visitor(('non_class_or_module',), 'non_class_or_module_object', [])

  def test_duplicates_module_class_depth(self):

    class Parent(object):

      class Nested(object):
        pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.Parent = Parent
    tf.submodule = types.ModuleType('submodule')
    tf.submodule.Parent = Parent

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    self.assertEqual(
        {
            'tf.submodule.Parent': sorted([
                'tf.Parent',
                'tf.submodule.Parent',
            ]),
            'tf.submodule.Parent.Nested': sorted([
                'tf.Parent.Nested',
                'tf.submodule.Parent.Nested',
            ]),
            'tf': ['tf'],
            'tf.submodule': ['tf.submodule'],
        },
        config.duplicates,
    )

    self.assertEqual(
        {
            'tf.Parent.Nested': 'tf.submodule.Parent.Nested',
            'tf.Parent': 'tf.submodule.Parent',
        },
        config.duplicate_of,
    )

    self.assertEqual(
        {
            id(Parent): 'tf.submodule.Parent',
            id(Parent.Nested): 'tf.submodule.Parent.Nested',
            id(tf): 'tf',
            id(tf.submodule): 'tf.submodule',
        },
        config.reverse_index,
    )

  def test_duplicates_contrib(self):

    class Parent(object):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.contrib = types.ModuleType('contrib')
    tf.submodule = types.ModuleType('submodule')
    tf.contrib.Parent = Parent
    tf.submodule.Parent = Parent

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    self.assertCountEqual(
        ['tf.contrib.Parent', 'tf.submodule.Parent'],
        config.duplicates['tf.submodule.Parent'],
    )

    self.assertEqual(
        {
            'tf.contrib.Parent': 'tf.submodule.Parent',
        },
        config.duplicate_of,
    )

    self.assertEqual(
        {
            id(tf): 'tf',
            id(tf.submodule): 'tf.submodule',
            id(Parent): 'tf.submodule.Parent',
            id(tf.contrib): 'tf.contrib',
        },
        config.reverse_index,
    )

  def test_duplicates_defining_class(self):

    class Parent(object):
      obj1 = object()

    class Child(Parent):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.Parent = Parent
    tf.Child = Child

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    self.assertCountEqual(
        ['tf.Parent.obj1', 'tf.Child.obj1'], config.duplicates['tf.Parent.obj1']
    )

    self.assertEqual(
        {
            'tf.Child.obj1': 'tf.Parent.obj1',
        },
        config.duplicate_of,
    )

    self.assertEqual(
        {
            id(tf): 'tf',
            id(Parent): 'tf.Parent',
            id(Child): 'tf.Child',
            id(Parent.obj1): 'tf.Parent.obj1',
        },
        config.reverse_index,
    )

  def test_duplicates_module_depth(self):

    class Parent(object):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.submodule = types.ModuleType('submodule')
    tf.submodule.submodule2 = types.ModuleType('submodule2')
    tf.Parent = Parent
    tf.submodule.submodule2.Parent = Parent

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    self.assertCountEqual(
        ['tf.Parent', 'tf.submodule.submodule2.Parent'],
        config.duplicates['tf.Parent'],
    )

    self.assertEqual(
        {'tf.submodule.submodule2.Parent': 'tf.Parent'}, config.duplicate_of
    )

    self.assertEqual(
        {
            id(tf): 'tf',
            id(tf.submodule): 'tf.submodule',
            id(tf.submodule.submodule2): 'tf.submodule.submodule2',
            id(Parent): 'tf.Parent',
        },
        config.reverse_index,
    )

  def test_duplicates_name(self):

    class Parent(object):
      obj1 = object()

    Parent.obj2 = Parent.obj1

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.submodule = types.ModuleType('submodule')
    tf.submodule.Parent = Parent

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    self.assertEqual(
        sorted([
            'tf.submodule.Parent.obj1',
            'tf.submodule.Parent.obj2',
        ]),
        config.duplicates['tf.submodule.Parent.obj1'],
    )

    self.assertEqual(
        {
            'tf.submodule.Parent.obj2': 'tf.submodule.Parent.obj1',
        },
        config.duplicate_of,
    )

    self.assertEqual(
        {
            id(tf): 'tf',
            id(tf.submodule): 'tf.submodule',
            id(Parent): 'tf.submodule.Parent',
            id(Parent.obj1): 'tf.submodule.Parent.obj1',
        },
        config.reverse_index,
    )

  def test_handles_duplicate_classmethods(self):

    class MyClass:

      @classmethod
      def from_value(cls, value):
        pass

    tf = types.ModuleType('fake_tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.MyClass = MyClass
    tf.sub = types.ModuleType('sub')
    tf.sub.MyClass = MyClass

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    paths = ['.'.join(p) for p in config.path_tree.keys()]

    expected = [
        '',
        'tf',
        'tf.MyClass',
        'tf.MyClass.from_value',
        'tf.sub',
        'tf.sub.MyClass',
        'tf.sub.MyClass.from_value',
    ]
    self.assertCountEqual(expected, paths)

    apis = [node.full_name for node in config.api_tree.iter_nodes()]
    expected = [
        'tf',
        'tf.sub',
        'tf.sub.MyClass',
        'tf.sub.MyClass.from_value',
    ]
    self.assertCountEqual(expected, apis)

    self.assertIs(
        config.api_tree[('tf', 'MyClass')],
        config.api_tree[('tf', 'sub', 'MyClass')],
    )
    self.assertIs(
        config.api_tree[('tf', 'MyClass', 'from_value')],
        config.api_tree[('tf', 'sub', 'MyClass', 'from_value')],
    )

  def test_handles_duplicate_singleton_attributes(self):

    class MyClass:
      simple = 1

    tf = types.ModuleType('fake_tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.MyClass = MyClass
    tf.sub = types.ModuleType('sub')
    tf.sub.MyClass = MyClass

    config = TestDocGenerator([('tf', tf)]).run_extraction()

    paths = ['.'.join(p) for p in config.path_tree.keys()]

    expected = [
        '',
        'tf',
        'tf.MyClass',
        'tf.MyClass.simple',
        'tf.sub',
        'tf.sub.MyClass',
        'tf.sub.MyClass.simple',
    ]
    self.assertCountEqual(expected, paths)

    apis = ['.'.join(p) for p in config.api_tree.keys()]
    expected = [
        '',
        'tf',
        'tf.MyClass',
        'tf.MyClass.simple',
        'tf.sub',
        'tf.sub.MyClass',
        'tf.sub.MyClass.simple',
    ]
    self.assertCountEqual(expected, apis)

    self.assertIs(
        config.api_tree[('tf', 'MyClass')],
        config.api_tree[('tf', 'sub', 'MyClass')],
    )
    self.assertIs(
        config.api_tree[('tf', 'MyClass', 'simple')],
        config.api_tree[('tf', 'sub', 'MyClass', 'simple')],
    )


class PathTreeTest(absltest.TestCase):

  def test_contains(self):
    tf = types.ModuleType('tf')
    tf.sub = types.ModuleType('sub')

    tree = doc_generator_visitor.PathTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub

    self.assertIn(('tf',), tree)
    self.assertIn(('tf', 'sub'), tree)

  def test_node_insertion(self):
    tf = types.ModuleType('tf')
    tf.sub = types.ModuleType('sub')
    tf.sub.object = object()

    tree = doc_generator_visitor.PathTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub
    tree[('tf', 'sub', 'thing')] = tf.sub.object

    node = tree[('tf', 'sub')]
    self.assertEqual(node.full_name, 'tf.sub')
    self.assertIs(node.py_object, tf.sub)
    self.assertIs(node.parent, tree[('tf',)])
    self.assertLen(node.children, 1)
    self.assertIs(node.children['thing'], tree[('tf', 'sub', 'thing')])

  def test_duplicate(self):
    tf = types.ModuleType('tf')
    tf.sub = types.ModuleType('sub')
    tf.sub.thing = object()
    tf.sub2 = types.ModuleType('sub2')
    tf.sub2.thing = tf.sub.thing

    tree = doc_generator_visitor.PathTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub
    tree[('tf', 'sub', 'thing')] = tf.sub.thing
    tree[('tf', 'sub2')] = tf.sub2
    tree[('tf', 'sub2', 'thing')] = tf.sub2.thing

    self.assertCountEqual(
        tree.nodes_for_obj(tf.sub.thing),
        [tree[('tf', 'sub', 'thing')], tree[('tf', 'sub2', 'thing')]])

  def test_duplicate_singleton(self):
    tf = types.ModuleType('tf')
    tf.sub = types.ModuleType('sub')
    tf.sub.thing = 999
    tf.sub2 = types.ModuleType('sub2')
    tf.sub2.thing = tf.sub.thing

    tree = doc_generator_visitor.PathTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub
    tree[('tf', 'sub', 'thing')] = tf.sub.thing
    tree[('tf', 'sub2')] = tf.sub2
    tree[('tf', 'sub2', 'thing')] = tf.sub2.thing

    found = tree.nodes_for_obj(tf.sub.thing)
    self.assertEqual([], found)


class ApiTreeTest(absltest.TestCase):

  def _make_fake_module(self) -> types.ModuleType:

    class Parent:

      def method1(self):
        pass

      def method2(self):
        pass

    class Child(Parent):

      def method2(self):
        pass

      def method3(self):
        pass

    class Outer(object):
      attribute = object()

      class Nested(object):
        pass

    fun1 = lambda x: x
    fun2 = lambda x: x

    tf = types.ModuleType('tf')
    tf.__file__ = __file__
    tf.seven = 7
    tf.Parent = Parent
    tf.Outer = Outer
    tf.fun1 = fun1
    tf.sub1 = types.ModuleType('sub1')
    tf.sub1.Parent = Parent
    tf.sub2 = types.ModuleType('sub2')
    tf.sub2.Child = Child
    tf.sub2.fun2 = fun2
    tf.sub1.sub2 = tf.sub2

    return tf

  def test_physical_path(self):
    tf = self._make_fake_module()

    api_tree = doc_generator_visitor.ApiTree()
    api_tree.insert(path=('tf',), py_object=tf, aliases=[('tf',)])
    api_tree.insert(
        path=('tf', 'sub2'), py_object=tf.sub2, aliases=[('tf', 'sub2')])
    api_tree.insert(
        path=('tf', 'seven'), py_object=tf.seven, aliases=[('tf', 'seven')])
    api_tree.insert(
        path=('tf', 'fun1'), py_object=tf.fun1, aliases=[('tf', 'fun1')])
    api_tree.insert(
        path=('tf', 'sub2', 'Child'),
        py_object=tf.sub2.Child,
        aliases=[('tf', 'sub2', 'Child')])

    self.assertEqual(('sub2',), api_tree[('tf', 'sub2')].physical_path)
    self.assertIsNone(api_tree[('tf', 'seven')].physical_path)
    self.assertEqual(('__main__', 'ApiTreeTest', '_make_fake_module',
                      '<locals>', '<lambda>'),
                     api_tree[('tf', 'fun1')].physical_path)
    self.assertEqual(
        ('__main__', 'ApiTreeTest', '_make_fake_module', '<locals>', 'Child'),
        api_tree[('tf', 'sub2', 'Child')].physical_path)

  def test_api_tree(self):
    tf = self._make_fake_module()

    api_tree = doc_generator_visitor.ApiTree()
    api_tree.insert(path=('tf',), py_object=tf, aliases=[('tf',)])
    api_tree.insert(
        path=('tf', 'Parent'),
        py_object=tf.Parent,
        aliases=[('tf', 'Parent'), ('tf', 'Parent2')])
    api_tree.insert(
        path=('tf', 'seven'), py_object=tf.seven, aliases=[('tf', 'seven')])

    # A node can be looked up by any alias
    self.assertIs(api_tree[('tf', 'Parent')], api_tree[('tf', 'Parent2')])
    # Nodes only show up once when iterating
    self.assertEqual([
        api_tree[('tf',)], api_tree[('tf', 'Parent')], api_tree[('tf', 'seven')]
    ], list(api_tree.iter_nodes()))
    # Test lookup by object.
    self.assertIs(api_tree[('tf', 'Parent')],
                  api_tree.node_for_object(tf.Parent))
    # You can't lookup things that maybe singletons.
    self.assertIs(api_tree[('tf', 'seven')].py_object, tf.seven)
    self.assertIsNone(api_tree.node_for_object(tf.seven))

  def test_from_path_tree(self):
    tf = self._make_fake_module()

    path_tree = doc_generator_visitor.PathTree()
    path_tree[('tf',)] = tf
    path_tree[('tf', 'Parent')] = tf.Parent
    path_tree[('tf', 'Parent2')] = tf.Parent

    result = doc_generator_visitor.ApiTree.from_path_tree(
        path_tree, score_name_fn=lambda name: name)

    expected = doc_generator_visitor.ApiTree()
    expected.insert(path=('tf',), py_object=tf, aliases=[('tf',)])
    expected.insert(
        path=('tf', 'Parent'),
        py_object=tf.Parent,
        aliases=[('tf', 'Parent'), ('tf', 'Parent2')])

    result = sorted(result.iter_nodes(), key=lambda node: node.path)
    expected = sorted(expected.iter_nodes(), key=lambda node: node.path)

    # Circular references make it hard to compare trees or nodes.
    for e, r in zip(result, expected):
      self.assertEqual(e.path, r.path)
      self.assertIs(e.py_object, r.py_object)
      self.assertCountEqual(e.aliases, r.aliases)
      self.assertCountEqual(e.children.keys(), r.children.keys())

  def test_api_tree_toc_integration(self):
    tf = self._make_fake_module()

    gen = TestDocGenerator([('tf', tf)])
    filters = gen.make_default_filters()
    visitor = generate_lib.extract(
        [('tf', tf)], filters=filters, visitor_cls=NoDunderVisitor
    )

    api_tree = doc_generator_visitor.ApiTree.from_path_tree(
        visitor.path_tree, visitor._score_name)

    toc = toc_lib.TocBuilder(site_path='/').build(api_tree)

    stream = io.StringIO()
    toc.write(stream)

    expected = textwrap.dedent("""\
        toc:
        - title: tf
          section:
          - title: Overview
            path: /tf
          - title: Outer
            path: /tf/Outer
          - title: Outer.Nested
            path: /tf/Outer/Nested
          - title: fun1
            path: /tf/fun1
          - title: sub1
            section:
            - title: Overview
              path: /tf/sub1
            - title: Parent
              path: /tf/sub1/Parent
          - title: sub2
            section:
            - title: Overview
              path: /tf/sub2
            - title: Child
              path: /tf/sub2/Child
            - title: fun2
              path: /tf/sub2/fun2
        """)

    self.assertEqual(expected, stream.getvalue())

  def test_non_priority_name(self):

    class Class1:
      pass

    mod = types.ModuleType('mod')
    mod.a = types.ModuleType('sub')
    mod.a.Class1 = Class1
    mod.b = mod.a

    path_tree = doc_generator_visitor.PathTree()
    path_tree[('mod',)] = mod
    path_tree[('mod', 'a')] = mod.a
    path_tree[('mod', 'a', 'Class1')] = mod.a.Class1
    path_tree[('mod', 'b')] = mod.b
    path_tree[('mod', 'b', 'Class1')] = mod.b.Class1

    def inconsistent_name_score(path):
      # `mod.a` is preferred over `mod.b`, but `b.Class1` is preferred over
      # `a.Class1`!
      scores = {
          ('mod',): 0,
          ('mod', 'a'): 0,  # prefer 'a'
          ('mod', 'b'): 1,
          ('mod', 'a', 'Class1'): 1,
          ('mod', 'b', 'Class1'): 0,  # prefer 'b.Class1'
      }
      return scores[path]

    api_tree = doc_generator_visitor.ApiTree.from_path_tree(
        path_tree, inconsistent_name_score)
    node = api_tree.node_for_object(Class1)

    # `Class1` can't choose `b.Class1` as its priority_path because
    # `a` is the priority_path for `sub`.
    self.assertEqual('mod.a.Class1', node.full_name)

if __name__ == '__main__':
  absltest.main()
