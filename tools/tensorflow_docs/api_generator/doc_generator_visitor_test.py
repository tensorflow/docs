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
"""Tests for tools.docs.doc_generator_visitor."""

import argparse
import os
import types

from absl.testing import absltest

from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import generate_lib


class NoDunderVisitor(doc_generator_visitor.DocGeneratorVisitor):

  def __call__(self, parent_name, parent, children):
    """Drop all the dunder methods to make testing easier."""
    children = [
        (name, obj) for (name, obj) in children if not name.startswith('_')
    ]
    return super(NoDunderVisitor, self).__call__(parent_name, parent, children)


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
    visitor = doc_generator_visitor.DocGeneratorVisitor()
    visitor(
        ('DocGeneratorVisitor',), doc_generator_visitor.DocGeneratorVisitor,
        [('index', doc_generator_visitor.DocGeneratorVisitor.reverse_index)])

    self.assertEqual({'DocGeneratorVisitor': ['index']},
                     visitor.tree)
    self.assertEqual({
        'DocGeneratorVisitor':
            doc_generator_visitor.DocGeneratorVisitor,
        'DocGeneratorVisitor.index':
            doc_generator_visitor.DocGeneratorVisitor.reverse_index
    }, visitor.index)

  def test_call_raises(self):
    visitor = doc_generator_visitor.DocGeneratorVisitor()
    with self.assertRaises(RuntimeError):
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

    visitor = generate_lib.extract(
        [('tf', tf)],
        base_dir=os.path.dirname(tf.__file__),
        private_map={},
        visitor_cls=NoDunderVisitor)

    self.assertEqual(
        {
            'tf.submodule.Parent':
                sorted([
                    'tf.Parent',
                    'tf.submodule.Parent',
                ]),
            'tf.submodule.Parent.Nested':
                sorted([
                    'tf.Parent.Nested',
                    'tf.submodule.Parent.Nested',
                ]),
            'tf': ['tf'],
            'tf.submodule': ['tf.submodule']
        }, visitor.duplicates)

    self.assertEqual({
        'tf.Parent.Nested': 'tf.submodule.Parent.Nested',
        'tf.Parent': 'tf.submodule.Parent',
    }, visitor.duplicate_of)

    self.assertEqual({
        id(Parent): 'tf.submodule.Parent',
        id(Parent.Nested): 'tf.submodule.Parent.Nested',
        id(tf): 'tf',
        id(tf.submodule): 'tf.submodule',
    }, visitor.reverse_index)

  def test_duplicates_contrib(self):

    class Parent(object):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.contrib = types.ModuleType('contrib')
    tf.submodule = types.ModuleType('submodule')
    tf.contrib.Parent = Parent
    tf.submodule.Parent = Parent

    visitor = generate_lib.extract(
        [('tf', tf)],
        base_dir=os.path.dirname(tf.__file__),
        private_map={},
        visitor_cls=NoDunderVisitor)

    self.assertEqual(
        sorted(['tf.contrib.Parent', 'tf.submodule.Parent']),
        visitor.duplicates['tf.submodule.Parent'])

    self.assertEqual({
        'tf.contrib.Parent': 'tf.submodule.Parent',
    }, visitor.duplicate_of)

    self.assertEqual({
        id(tf): 'tf',
        id(tf.submodule): 'tf.submodule',
        id(Parent): 'tf.submodule.Parent',
        id(tf.contrib): 'tf.contrib',
    }, visitor.reverse_index)

  def test_duplicates_defining_class(self):

    class Parent(object):
      obj1 = object()

    class Child(Parent):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.Parent = Parent
    tf.Child = Child

    visitor = generate_lib.extract(
        [('tf', tf)],
        base_dir=os.path.dirname(tf.__file__),
        private_map={},
        visitor_cls=NoDunderVisitor)

    self.assertEqual(
        sorted([
            'tf.Parent.obj1',
            'tf.Child.obj1',
        ]), visitor.duplicates['tf.Parent.obj1'])

    self.assertEqual({
        'tf.Child.obj1': 'tf.Parent.obj1',
    }, visitor.duplicate_of)

    self.assertEqual({
        id(tf): 'tf',
        id(Parent): 'tf.Parent',
        id(Child): 'tf.Child',
        id(Parent.obj1): 'tf.Parent.obj1',
    }, visitor.reverse_index)

  def test_duplicates_module_depth(self):

    class Parent(object):
      pass

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.submodule = types.ModuleType('submodule')
    tf.submodule.submodule2 = types.ModuleType('submodule2')
    tf.Parent = Parent
    tf.submodule.submodule2.Parent = Parent

    visitor = generate_lib.extract(
        [('tf', tf)],
        base_dir=os.path.dirname(tf.__file__),
        private_map={},
        visitor_cls=NoDunderVisitor)

    self.assertEqual(
        sorted(['tf.Parent', 'tf.submodule.submodule2.Parent']),
        visitor.duplicates['tf.Parent'])

    self.assertEqual({
        'tf.submodule.submodule2.Parent': 'tf.Parent'
    }, visitor.duplicate_of)

    self.assertEqual({
        id(tf): 'tf',
        id(tf.submodule): 'tf.submodule',
        id(tf.submodule.submodule2): 'tf.submodule.submodule2',
        id(Parent): 'tf.Parent',
    }, visitor.reverse_index)

  def test_duplicates_name(self):

    class Parent(object):
      obj1 = object()

    Parent.obj2 = Parent.obj1

    tf = types.ModuleType('tf')
    tf.__file__ = '/tmp/tf/__init__.py'
    tf.submodule = types.ModuleType('submodule')
    tf.submodule.Parent = Parent

    visitor = generate_lib.extract(
        [('tf', tf)],
        base_dir=os.path.dirname(tf.__file__),
        private_map={},
        visitor_cls=NoDunderVisitor)
    self.assertEqual(
        sorted([
            'tf.submodule.Parent.obj1',
            'tf.submodule.Parent.obj2',
        ]), visitor.duplicates['tf.submodule.Parent.obj1'])

    self.assertEqual({
        'tf.submodule.Parent.obj2': 'tf.submodule.Parent.obj1',
    }, visitor.duplicate_of)

    self.assertEqual({
        id(tf): 'tf',
        id(tf.submodule): 'tf.submodule',
        id(Parent): 'tf.submodule.Parent',
        id(Parent.obj1): 'tf.submodule.Parent.obj1',
    }, visitor.reverse_index)


class ApiTreeTest(absltest.TestCase):

  def test_contains(self):
    tf = argparse.Namespace()
    tf.sub = argparse.Namespace()

    tree = doc_generator_visitor.ApiTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub

    self.assertIn(('tf',), tree)
    self.assertIn(('tf', 'sub'), tree)

  def test_node_insertion(self):
    tf = argparse.Namespace()
    tf.sub = argparse.Namespace()
    tf.sub.object = object()

    tree = doc_generator_visitor.ApiTree()
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
    tf = argparse.Namespace()
    tf.sub = argparse.Namespace()
    tf.sub.thing = object()
    tf.sub2 = argparse.Namespace()
    tf.sub2.thing = tf.sub.thing

    tree = doc_generator_visitor.ApiTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub
    tree[('tf', 'sub', 'thing')] = tf.sub.thing
    tree[('tf', 'sub2')] = tf.sub2
    tree[('tf', 'sub2', 'thing')] = tf.sub2.thing

    self.assertCountEqual(
        tree.aliases[id(tf.sub.thing)],
        [tree[('tf', 'sub', 'thing')], tree[('tf', 'sub2', 'thing')]])

  def test_duplicate_singleton(self):
    tf = argparse.Namespace()
    tf.sub = argparse.Namespace()
    tf.sub.thing = 999
    tf.sub2 = argparse.Namespace()
    tf.sub2.thing = tf.sub.thing

    tree = doc_generator_visitor.ApiTree()
    tree[('tf',)] = tf
    tree[('tf', 'sub')] = tf.sub
    tree[('tf', 'sub', 'thing')] = tf.sub.thing
    tree[('tf', 'sub2')] = tf.sub2
    tree[('tf', 'sub2', 'thing')] = tf.sub2.thing

    self.assertEmpty(tree.aliases[tf.sub.thing], [])


if __name__ == '__main__':
  absltest.main()
