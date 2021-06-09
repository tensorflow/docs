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
"""Tests for documentation parser."""

import collections
import inspect
import os
import sys
import tempfile
import textwrap

from typing import Callable, Dict, List, Optional, Union

from absl.testing import absltest
from absl.testing import parameterized
import attr
import dataclasses

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import parser

# The test needs a real module. `types.ModuleType()` doesn't work, as the result
# is a `builtin` module. Using "parser" here is arbitraty. The tests don't
# depend on the module contents. At this point in the process the public api
# has already been extracted.
test_module = parser


def test_function(unused_arg, unused_kwarg='default'):
  """Docstring for test function."""
  pass


def test_function_with_args_kwargs(unused_arg, *unused_args, **unused_kwargs):
  """Docstring for second test function."""
  pass


class ParentClass(object):

  @doc_controls.do_not_doc_inheritable
  def hidden_method(self):
    pass


class TestClass(ParentClass):
  """Docstring for TestClass itself.

  Attributes:
    hello: hello
  """

  def a_method(self, arg='default'):
    """Docstring for a method."""
    pass

  def hidden_method(self):
    pass

  @doc_controls.do_not_generate_docs
  def hidden_method2(self):
    pass

  class ChildClass(object):
    """Docstring for a child class."""
    pass

  @property
  def a_property(self):
    """Docstring for a property."""
    pass

  @staticmethod
  def static_method(arg):
    pass

  @classmethod
  def class_method(cls):
    pass

  CLASS_MEMBER = 'a class member'


class DummyVisitor(object):

  def __init__(self, index, duplicate_of):
    self.index = index
    self.duplicate_of = duplicate_of


class ConcreteMutableMapping(collections.MutableMapping):
  """MutableMapping subclass to repro inspect.getsource() IndexError."""

  def __init__(self):
    self._map = {}

  def __getitem__(self, key):
    return self._map[key]

  def __setitem__(self, key, value):
    self._map[key] = value

  def __delitem__(self, key):
    del self._map[key]

  def __iter__(self):
    return self._map.__iter__()

  def __len__(self):
    return len(self._map)


ConcreteNamedTuple = collections.namedtuple('ConcreteNamedTuple', ['a', 'b'])


@attr.s
class ClassUsingAttrs(object):
  member = attr.ib(type=int)


@dataclasses.dataclass
class ExampleDataclass:
  x: List[str]
  z: int
  c: List[int] = dataclasses.field(default_factory=list)
  a: Union[List[str], str, int] = None
  b: str = 'test'
  y: bool = False

  def add(self, x: int, y: int) -> int:
    q: int = x + y
    return q


class ParserTest(parameterized.TestCase):

  def test_documentation_path(self):
    self.assertEqual('test.md', parser.documentation_path('test'))
    self.assertEqual('test/module.md', parser.documentation_path('test.module'))

  def test_replace_references(self):

    class HasOneMember(object):

      def foo(self):
        pass

    string = (
        'A `tf.reference`, a member `tf.reference.foo`, and a `tf.third`. '
        'This is `not a symbol`, and this is `tf.not.a.real.symbol`')

    duplicate_of = {'tf.third': 'tf.fourth'}
    index = {
        'tf.reference': HasOneMember,
        'tf.reference.foo': HasOneMember.foo,
        'tf.third': HasOneMember,
        'tf.fourth': HasOneMember
    }

    visitor = DummyVisitor(index, duplicate_of)

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    result = reference_resolver.replace_references(string, '../..')
    self.assertEqual(
        'A <a href="../../tf/reference.md">'
        '<code>tf.reference</code></a>, '
        'a member <a href="../../tf/reference.md#foo">'
        '<code>tf.reference.foo</code></a>, '
        'and a <a href="../../tf/fourth.md">'
        '<code>tf.third</code></a>. '
        'This is `not a symbol`, and this is '
        '`tf.not.a.real.symbol`', result)

  def test_docs_for_class(self):

    index = {
        'TestClass': TestClass,
        'TestClass.a_method': TestClass.a_method,
        'TestClass.a_property': TestClass.a_property,
        'TestClass.ChildClass': TestClass.ChildClass,
        'TestClass.static_method': TestClass.static_method,
        'TestClass.class_method': TestClass.class_method,
        'TestClass.CLASS_MEMBER': TestClass.CLASS_MEMBER,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'TestClass': [
            'a_method', 'class_method', 'static_method', 'a_property',
            'ChildClass', 'CLASS_MEMBER'
        ]
    }
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='TestClass', py_object=TestClass, parser_config=parser_config)

    # Make sure the brief docstring is present
    self.assertEqual(
        inspect.getdoc(TestClass).split('\n')[0], page_info.doc.brief)

    # Make sure the method is present
    method_infos = {
        method_info.short_name: method_info for method_info in page_info.methods
    }

    self.assertIs(method_infos['a_method'].py_object, TestClass.a_method)

    # Make sure that the signature is extracted properly and omits self.
    self.assertEqual(['arg=&#x27;default&#x27;'],
                     method_infos['a_method'].signature.arguments)

    self.assertEqual(method_infos['static_method'].decorators, ['staticmethod'])
    self.assertEqual(method_infos['class_method'].decorators, ['classmethod'])

    # Make sure the property is present
    attrs = page_info.attr_block
    self.assertIsInstance(attrs, parser.TitleBlock)
    self.assertIn('a_property', [name for name, desc in attrs.items])

    # Make sure there is a link to the child class and it points the right way.
    self.assertIs(TestClass.ChildClass, page_info.classes[0].py_object)

  def test_dataclass_attributes_table(self):

    index = {
        'ExampleDataclass': ExampleDataclass,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ExampleDataclass': []}

    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='ExampleDataclass',
        py_object=ExampleDataclass,
        parser_config=parser_config)

    self.assertCountEqual(['a', 'b', 'c', 'x', 'y', 'z'],
                          [name for name, value in page_info.attr_block.items])

  def test_namedtuple_field_order(self):
    namedtupleclass = collections.namedtuple('namedtupleclass',
                                             {'z', 'y', 'x', 'w', 'v', 'u'})

    index = {
        'namedtupleclass': namedtupleclass,
        'namedtupleclass.u': namedtupleclass.u,
        'namedtupleclass.v': namedtupleclass.v,
        'namedtupleclass.w': namedtupleclass.w,
        'namedtupleclass.x': namedtupleclass.x,
        'namedtupleclass.y': namedtupleclass.y,
        'namedtupleclass.z': namedtupleclass.z,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'namedtupleclass': {'u', 'v', 'w', 'x', 'y', 'z'}}
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='namedtupleclass',
        py_object=namedtupleclass,
        parser_config=parser_config)

    # Each namedtiple field has a docstring of the form:
    #   'Alias for field number ##'. These props are returned sorted.

    def sort_key(prop_info):
      return int(prop_info.py_object.__doc__.split(' ')[-1])

    self.assertSequenceEqual(page_info._properties,
                             sorted(page_info._properties, key=sort_key))

  def test_docs_for_class_should_skip(self):

    class Parent(object):

      @doc_controls.do_not_doc_inheritable
      def a_method(self, arg='default'):
        pass

    class Child(Parent):

      def a_method(self, arg='default'):
        pass

    index = {
        'Child': Child,
        'Child.a_method': Child.a_method,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'Child': ['a_method'],
    }

    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='Child', py_object=Child, parser_config=parser_config)

    # Make sure the `a_method` is not present
    self.assertEmpty(page_info.methods)

  def test_docs_for_message_class(self):

    class CMessage(object):

      def hidden(self):
        pass

    class Message(object):

      def hidden2(self):
        pass

    class MessageMeta(object):

      def hidden3(self):
        pass

    class ChildMessage(CMessage, Message, MessageMeta):

      def my_method(self):
        pass

    index = {
        'ChildMessage': ChildMessage,
        'ChildMessage.hidden': ChildMessage.hidden,
        'ChildMessage.hidden2': ChildMessage.hidden2,
        'ChildMessage.hidden3': ChildMessage.hidden3,
        'ChildMessage.my_method': ChildMessage.my_method,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ChildMessage': ['hidden', 'hidden2', 'hidden3', 'my_method']}

    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='ChildMessage',
        py_object=ChildMessage,
        parser_config=parser_config)

    self.assertLen(page_info.methods, 1)
    self.assertEqual('my_method', page_info.methods[0].short_name)

  def test_docs_for_module(self):

    index = {
        'TestModule':
            test_module,
        'TestModule.test_function':
            test_function,
        'TestModule.test_function_with_args_kwargs':
            test_function_with_args_kwargs,
        'TestModule.TestClass':
            TestClass,
    }

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'TestModule': [
            'TestClass', 'test_function', 'test_function_with_args_kwargs'
        ]
    }
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='TestModule',
        py_object=test_module,
        parser_config=parser_config)

    # Make sure the brief docstring is present
    self.assertEqual(
        inspect.getdoc(test_module).split('\n')[0], page_info.doc.brief)

    # Make sure that the members are there
    funcs = {f_info.py_object for f_info in page_info.functions}
    self.assertEqual({test_function, test_function_with_args_kwargs}, funcs)

    classes = {cls_info.py_object for cls_info in page_info.classes}
    self.assertEqual({TestClass}, classes)

  def test_docs_for_function(self):
    index = {'test_function': test_function}

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'': ['test_function']}
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='test_function',
        py_object=test_function,
        parser_config=parser_config)

    # Make sure the brief docstring is present
    self.assertEqual(
        inspect.getdoc(test_function).split('\n')[0], page_info.doc.brief)

    # Make sure the extracted signature is good.
    self.assertEqual(['unused_arg', 'unused_kwarg=&#x27;default&#x27;'],
                     page_info.signature.arguments)

  def test_docs_for_function_with_kwargs(self):
    index = {'test_function_with_args_kwargs': test_function_with_args_kwargs}

    visitor = DummyVisitor(index=index, duplicate_of={})

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'': ['test_function_with_args_kwargs']}
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='test_function_with_args_kwargs',
        py_object=test_function_with_args_kwargs,
        parser_config=parser_config)

    # Make sure the brief docstring is present
    self.assertEqual(
        inspect.getdoc(test_function_with_args_kwargs).split('\n')[0],
        page_info.doc.brief)

    # Make sure the extracted signature is good.
    self.assertEqual(['unused_arg', '*unused_args', '**unused_kwargs'],
                     page_info.signature.arguments)

  def test_parse_md_docstring(self):

    def test_function_with_fancy_docstring(arg):
      """Function with a fancy docstring.

      And a bunch of references: `tf.reference`, another `tf.reference`,
          a member `tf.reference.foo`, and a `tf.third`.

      Args:
        arg: An argument.

      Raises:
        an exception

      Returns:
        arg: the input, and
        arg: the input, again.

      @compatibility(numpy)
      NumPy has nothing as awesome as this function.
      @end_compatibility

      @compatibility(theano)
      Theano has nothing as awesome as this function.

      Check it out.
      @end_compatibility

      """
      return arg, arg

    class HasOneMember(object):

      def foo(self):
        pass

    duplicate_of = {'tf.third': 'tf.fourth'}
    index = {
        'tf': test_module,
        'tf.fancy': test_function_with_fancy_docstring,
        'tf.reference': HasOneMember,
        'tf.reference.foo': HasOneMember.foo,
        'tf.third': HasOneMember,
        'tf.fourth': HasOneMember
    }

    visitor = DummyVisitor(index=index, duplicate_of=duplicate_of)

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree={},
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    doc_info = parser._parse_md_docstring(
        test_function_with_fancy_docstring,
        relative_path_to_root='../..',
        full_name=None,
        parser_config=parser_config)

    freeform_docstring = '\n'.join(
        part for part in doc_info.docstring_parts if isinstance(part, str))
    self.assertNotIn('@', freeform_docstring)
    self.assertNotIn('compatibility', freeform_docstring)
    self.assertNotIn('Raises:', freeform_docstring)

    title_blocks = [
        part for part in doc_info.docstring_parts if not isinstance(part, str)
    ]

    self.assertLen(title_blocks, 3)

    self.assertCountEqual(doc_info.compatibility.keys(), {'numpy', 'theano'})

    self.assertEqual(doc_info.compatibility['numpy'],
                     'NumPy has nothing as awesome as this function.\n')

  def test_downgrade_h1_docstrings(self):
    h1_docstring = textwrap.dedent("""\
      Hello.

      Some keras functions have docstrings like this.

      # Arguments
        a: a
        b: b
        c: c

      # Example

        ```
        # comment
        ```

      # Returns
        a+b+c

      # Raises
        ValueError: always
      """)
    downgrader = parser._DowngradeH1Keywords()
    doc = downgrader(h1_docstring)
    self.assertIn('\n  ```\n  # comment\n  ```', doc)
    self.assertIn('\nArguments:', doc)
    self.assertIn('\nExample:', doc)
    self.assertIn('\nReturns:', doc)
    self.assertIn('\nRaises:', doc)

  def test_generate_index(self):

    index = {
        'tf': test_module,
        'tf.TestModule': test_module,
        'tf.test_function': test_function,
        'tf.TestModule.test_function': test_function,
        'tf.TestModule.TestClass': TestClass,
        'tf.TestModule.TestClass.a_method': TestClass.a_method,
        'tf.TestModule.TestClass.a_property': TestClass.a_property,
        'tf.TestModule.TestClass.ChildClass': TestClass.ChildClass,
    }
    duplicate_of = {'tf.TestModule.test_function': 'tf.test_function'}

    visitor = DummyVisitor(index=index, duplicate_of=duplicate_of)

    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    docs = parser.generate_global_index(
        'TestLibrary', index=index, reference_resolver=reference_resolver)

    # Make sure duplicates and non-top-level symbols are in the index, but
    # methods and properties are not.
    self.assertNotIn('a_method', docs)
    self.assertNotIn('a_property', docs)
    self.assertIn('TestModule.TestClass', docs)
    self.assertIn('TestModule.TestClass.ChildClass', docs)
    self.assertIn('TestModule.test_function', docs)
    # Leading backtick to make sure it's included top-level.
    # This depends on formatting, but should be stable.
    self.assertIn('<code>tf.test_function', docs)

  def test_getsource_indexerror_resilience(self):
    """Validates that parser gracefully handles IndexErrors.

    inspect.getsource() can raise an IndexError in some cases. It's unclear
    why this happens, but it consistently repros on the `get` method of
    collections.MutableMapping subclasses.
    """

    # This isn't the full set of APIs from MutableMapping, but sufficient for
    # testing.
    index = {
        'ConcreteMutableMapping':
            ConcreteMutableMapping,
        'ConcreteMutableMapping.__init__':
            ConcreteMutableMapping.__init__,
        'ConcreteMutableMapping.__getitem__':
            ConcreteMutableMapping.__getitem__,
        'ConcreteMutableMapping.__setitem__':
            ConcreteMutableMapping.__setitem__,
        'ConcreteMutableMapping.values':
            ConcreteMutableMapping.values,
        'ConcreteMutableMapping.get':
            ConcreteMutableMapping.get
    }
    visitor = DummyVisitor(index=index, duplicate_of={})
    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'ConcreteMutableMapping': [
            '__init__', '__getitem__', '__setitem__', 'values', 'get'
        ]
    }
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='ConcreteMutableMapping',
        py_object=ConcreteMutableMapping,
        parser_config=parser_config)

    self.assertIn(ConcreteMutableMapping.get,
                  [m.py_object for m in page_info.methods])

  def test_strips_default_arg_memory_address(self):
    """Validates that parser strips memory addresses out out default argspecs.

     argspec.defaults can contain object memory addresses, which can change
     between invocations. It's desirable to strip these out to reduce churn.

     See: `help(collections.MutableMapping.pop)`
    """
    index = {
        'ConcreteMutableMapping': ConcreteMutableMapping,
        'ConcreteMutableMapping.pop': ConcreteMutableMapping.pop
    }
    visitor = DummyVisitor(index=index, duplicate_of={})
    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ConcreteMutableMapping': ['pop']}
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = parser.docs_for_object(
        full_name='ConcreteMutableMapping',
        py_object=ConcreteMutableMapping,
        parser_config=parser_config)

    pop_default_arg = page_info.methods[0].signature.arguments[1]
    self.assertNotIn('object at 0x', pop_default_arg)
    self.assertIn('&lt;object&gt;', pop_default_arg)

  @parameterized.named_parameters(
      ('mutable_mapping', 'ConcreteMutableMapping', '__contains__',
       ConcreteMutableMapping.__contains__),
      ('namedtuple', 'ConcreteNamedTuple', '__new__',
       ConcreteNamedTuple.__new__),
      ('ClassUsingAttrs_eq', 'ClassUsingAttrs', '__eq__',
       ClassUsingAttrs.__eq__),
      ('ClassUsingAttrs_init', 'ClassUsingAttrs', '__init__',
       ClassUsingAttrs.__init__),
  )
  def test_empty_defined_in(self, cls, method, py_object):
    """Validates that the parser omits the defined_in location properly.

    This test covers two cases where the parser should omit the defined_in
    location:
      1. built-ins.
      2. methods automatically generated by python attr library.

    For built-ins, if without special handling, the defined-in URL ends up like:
      http://prefix/<embedded stdlib>/_collections_abc.py

    For methods automatically generated by python attr library, if without
    special handling, the defined-in URL ends up like:
      http://prefix/<attrs generated eq ...>

    Args:
      cls: The class name to generate docs for.
      method: The class method name to generate docs for.
      py_object: The python object for the specified cls.method.
    """

    visitor = DummyVisitor(index={}, duplicate_of={})
    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {cls: [method]}
    parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index={},
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    function_info = parser.docs_for_object(
        full_name='%s.%s' % (cls, method),
        py_object=py_object,
        parser_config=parser_config)

    self.assertIsNone(function_info.defined_in)

  def test_get_other_member_doc_object_doc_attr(self):

    class A():
      """Class docs."""
      pass

    a = A()
    a.__doc__ = 'Object doc'

    parser_config = parser.ParserConfig(
        reference_resolver=None,
        duplicates={},
        duplicate_of={},
        tree={},
        index={},
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    result = parser._get_other_member_doc(a, parser_config, {})

    expected = textwrap.dedent("""\
      Instance of `__main__.A`

      Object doc""")

    self.assertEqual(expected, result)

  def test_get_other_member_doc_extra_doc(self):
    # This will get sorted.
    a = {4, 2, 1, 3}
    # You can't set __doc__ on a list or a set so use extra_docs
    doc = 'Object doc'
    extra_docs = {id(a): doc}

    result = parser._get_other_member_doc(a, None, extra_docs)

    expected = textwrap.dedent("""\
      ```
      {
       1,
       2,
       3,
       4
      }
      ```

      Object doc""")
    self.assertEqual(expected, result)

  def test_get_other_member_basic_type(self):
    a = 5
    result = parser._get_other_member_doc(a, None, {})

    self.assertEqual('`5`', result)

  def test_get_other_member_doc_unknown_class(self):

    class A():
      """Class docs."""
      pass

    a = A()

    parser_config = parser.ParserConfig(
        reference_resolver=None,
        duplicates={},
        duplicate_of={},
        tree={},
        index={},
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    result = parser._get_other_member_doc(a, parser_config, {})
    expected = textwrap.dedent("""\
      Instance of `__main__.A`""")

    self.assertEqual(expected, result)

  def test_get_other_member_doc_known_class(self):

    class A():
      """Class docs."""
      pass

    a = A()

    parser_config = parser.ParserConfig(
        reference_resolver=None,
        duplicates={},
        duplicate_of={},
        tree={},
        index={},
        reverse_index={id(A): 'tf.test.A'},
        base_dir='/',
        code_url_prefix='/')

    result = parser._get_other_member_doc(a, parser_config, {})

    self.assertEqual('Instance of `tf.test.A`', result)


class TestReferenceResolver(absltest.TestCase):
  _BASE_DIR = tempfile.mkdtemp()

  def setUp(self):
    super(TestReferenceResolver, self).setUp()
    self.workdir = os.path.join(self._BASE_DIR, self.id())
    os.makedirs(self.workdir)

  def testSaveReferenceResolver(self):
    duplicate_of = {'AClass': ['AClass2']}
    is_fragment = {
        'tf': False,
        'tf.VERSION': True,
        'tf.AClass': False,
        'tf.AClass.method': True,
        'tf.AClass2': False,
        'tf.function': False
    }
    py_module_names = ['tf', 'tfdbg']

    resolver = parser.ReferenceResolver(duplicate_of, is_fragment,
                                        py_module_names)

    outdir = self.workdir

    filepath = os.path.join(outdir, 'resolver.json')

    resolver.to_json_file(filepath)
    resolver2 = parser.ReferenceResolver.from_json_file(filepath)

    # There are no __slots__, so all fields are visible in __dict__.
    self.assertEqual(resolver.__dict__, resolver2.__dict__)

  def testIsClasssAttr(self):
    result = parser.is_class_attr('test_module.test_function',
                                  {'test_module': test_module})
    self.assertFalse(result)

    result = parser.is_class_attr('TestClass.test_function',
                                  {'TestClass': TestClass})
    self.assertTrue(result)

  def test_duplicate_fragment(self):
    duplicate_of = {
        'tf.Class2.method': 'tf.Class1.method',
        'tf.sub.Class2.method': 'tf.Class1.method',
        'tf.sub.Class2': 'tf.Class2'
    }
    is_fragment = {
        'tf.Class1.method': True,
        'tf.Class2.method': True,
        'tf.sub.Class2.method': True,
        'tf.Class1': False,
        'tf.Class2': False,
        'tf.sub.Class2': False
    }
    py_module_names = ['tf']

    reference_resolver = parser.ReferenceResolver(duplicate_of, is_fragment,
                                                  py_module_names)

    # Method references point to the method, in the canonical class alias.
    result = reference_resolver.reference_to_url('tf.Class1.method', '')
    self.assertEqual('tf/Class1.md#method', result)
    result = reference_resolver.reference_to_url('tf.Class2.method', '')
    self.assertEqual('tf/Class2.md#method', result)
    result = reference_resolver.reference_to_url('tf.sub.Class2.method', '')
    self.assertEqual('tf/Class2.md#method', result)

    # Class references point to the canonical class alias
    result = reference_resolver.reference_to_url('tf.Class1', '')
    self.assertEqual('tf/Class1.md', result)
    result = reference_resolver.reference_to_url('tf.Class2', '')
    self.assertEqual('tf/Class2.md', result)
    result = reference_resolver.reference_to_url('tf.sub.Class2', '')
    self.assertEqual('tf/Class2.md', result)


RELU_DOC = """Computes rectified linear: `max(features, 0)`

RELU is an activation

Args:
  'features': A `Tensor`. Must be one of the following types: `float32`,
    `float64`, `int32`, `int64`, `uint8`, `int16`, `int8`, `uint16`,
    `half`.
  name: A name for the operation (optional)
    Note: this is a note, not another parameter.

Examples:

  ```
  a+b=c
  ```

Returns:
  Some tensors, with the same type as the input.
  first: is the something
  second: is the something else
"""


class TestParseDocstring(absltest.TestCase):

  def test_split_title_blocks(self):
    docstring_parts = parser.TitleBlock.split_string(RELU_DOC)

    self.assertLen(docstring_parts, 7)

    args = docstring_parts[1]
    self.assertEqual(args.title, 'Args')
    self.assertEqual(args.text, '\n')
    self.assertLen(args.items, 2)
    self.assertEqual(args.items[0][0], "'features'")
    self.assertEqual(
        args.items[0][1],
        'A `Tensor`. Must be one of the following types: `float32`,\n'
        '  `float64`, `int32`, `int64`, `uint8`, `int16`, `int8`, `uint16`,\n'
        '  `half`.\n')
    self.assertEqual(args.items[1][0], 'name')
    self.assertEqual(
        args.items[1][1], 'A name for the operation (optional)\n'
        '  Note: this is a note, not another parameter.\n')

    returns = [item for item in docstring_parts if not isinstance(item, str)
              ][-1]
    self.assertEqual(returns.title, 'Returns')
    self.assertEqual(returns.text,
                     '\nSome tensors, with the same type as the input.\n')
    self.assertLen(returns.items, 2)


class TestPartialSymbolAutoRef(parameterized.TestCase):
  REF_TEMPLATE = '<a href="{link}"><code>{text}</code></a>'

  @parameterized.named_parameters(
      ('basic1', 'keras.Model.fit', '../tf/keras/Model.md#fit'),
      ('duplicate_object', 'layers.Conv2D', '../tf/keras/layers/Conv2D.md'),
      ('parens', 'Model.fit(x, y, epochs=5)', '../tf/keras/Model.md#fit'),
      ('duplicate_name', 'tf.matmul', '../tf/linalg/matmul.md'),
      ('full_name', 'tf.concat', '../tf/concat.md'),
      ('normal_and_compat', 'linalg.matmul', '../tf/linalg/matmul.md'),
      ('compat_only', 'math.deprecated', None),
      ('contrib_only', 'y.z', None),
  )
  def test_partial_symbol_references(self, string, link):
    duplicate_of = {
        'tf.matmul': 'tf.linalg.matmul',
        'tf.layers.Conv2d': 'tf.keras.layers.Conv2D',
    }

    is_fragment = {
        'tf.keras.Model.fit': True,
        'tf.concat': False,
        'tf.keras.layers.Conv2D': False,
        'tf.linalg.matmul': False,
        'tf.compat.v1.math.deprecated': False,
        'tf.compat.v1.linalg.matmul': False,
        'tf.contrib.y.z': False,
    }

    py_module_names = ['tf']

    resolver = parser.ReferenceResolver(duplicate_of, is_fragment,
                                        py_module_names)
    input_string = string.join('``')
    ref_string = resolver.replace_references(input_string, '..')

    if link is None:
      expected = input_string
    else:
      expected = self.REF_TEMPLATE.format(link=link, text=string)

    self.assertEqual(expected, ref_string)


class TestIgnoreLineInBlock(parameterized.TestCase):

  @parameterized.named_parameters(
      ('ignore_backticks', ['```'], ['```'],
       '```\nFiller\n```\n```Same line```\n```python\nDowner\n```'),
      ('ignore_code_cell_output', ['<pre>{% html %}'], ['{% endhtml %}</pre>'],
       '<pre>{% html %}\nOutput\nmultiline{% endhtml %}</pre>'),
      ('ignore_backticks_and_cell_output', ['<pre>{% html %}', '```'
                                           ], ['{% endhtml %}</pre>', '```'],
       ('```\nFiller\n```\n```Same line```\n<pre>{% html %}\nOutput\nmultiline'
        '{% endhtml %}</pre>\n```python\nDowner\n```')))
  def test_ignore_lines(self, block_start, block_end, expected_ignored_lines):

    text = textwrap.dedent("""\
    ```
    Filler
    ```

    ```Same line```

    <pre>{% html %}
    Output
    multiline{% endhtml %}</pre>

    ```python
    Downer
    ```
    """)

    filters = [
        parser.IgnoreLineInBlock(start, end)
        for start, end in zip(block_start, block_end)
    ]

    ignored_lines = []
    for line in text.splitlines():
      if any(filter_block(line) for filter_block in filters):
        ignored_lines.append(line)

    self.assertEqual('\n'.join(ignored_lines), expected_ignored_lines)

  def test_clean_text(self):
    text = textwrap.dedent("""\
    ```
    Ignore lines here.
    ```
    Useful information.
    Don't ignore.
    ```python
    Ignore here too.
    ```
    Stuff.
    ```Not useful.```
    """)

    filters = [parser.IgnoreLineInBlock('```', '```')]

    clean_text = []
    for line in text.splitlines():
      if not any(filter_block(line) for filter_block in filters):
        clean_text.append(line)

    expected_clean_text = 'Useful information.\nDon\'t ignore.\nStuff.'

    self.assertEqual('\n'.join(clean_text), expected_clean_text)

  def test_strip_todos(self):
    input_str = ("""#  TODO(blah) blah

        hello    TODO: more stuff
        middle
        goodbye  TODO
        """)

    expected = ("""

        hello
        middle
        goodbye
        """)
    strip_todos = parser._StripTODOs()
    self.assertEqual(expected, strip_todos(input_str))

  def test_strip_pylintandpyformat(self):
    input_str = textwrap.dedent("""
        hello  #  pyformat: disable
        middle  # pyformat: enable
        goodbye  TODO  # pylint: disable=g-top-imports

        # pyformat: disable
        xyz
        # pyformat: enable

        # pylint: disable=g-top-imports
        abc
        # pylint: enable=g-top-imports
        """)

    expected = textwrap.dedent("""
        hello  
        middle  
        goodbye  TODO  


        xyz



        abc

        """)
    strip_todos = parser._StripPylintAndPyformat()
    self.assertEqual(expected, strip_todos(input_str))


class TestGenerateSignature(parameterized.TestCase, absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.known_object = object()
    reference_resolver = parser.ReferenceResolver(
        duplicate_of={},
        is_fragment={'tfdocs.api_generator.parser.extract_decorators': False},
        py_module_names=[])
    self.parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree={},
        index={},
        reverse_index={
            id(self.known_object):
                'location.of.object.in.api',
            id(parser.extract_decorators):
                'tfdocs.api_generator.parser.extract_decorators',
        },
        base_dir='/',
        code_url_prefix='/')

  def test_known_object(self):

    def example_fun(arg=self.known_object):  # pylint: disable=unused-argument
      pass

    sig = parser.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)
    self.assertEqual(sig.arguments, ['arg=location.of.object.in.api'])

  def test_literals(self):

    def example_fun(
        self,
        cls,
        a=5,
        b=5.0,
        c=None,
        d=True,
        e='hello',
        f=(1, (2, 3)),
    ):  # pylint: disable=g-bad-name, unused-argument
      pass

    sig = parser.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)
    self.assertEqual(sig.arguments, [
        'self', 'cls', 'a=5', 'b=5.0', 'c=None', 'd=True',
        'e=&#x27;hello&#x27;', 'f=(1, (2, 3))'
    ])

  def test_dotted_name(self):
    # pylint: disable=g-bad-name

    class a(object):

      class b(object):

        class c(object):

          class d(object):

            def __init__(self, *args):
              pass

    # pylint: enable=g-bad-name

    e = {'f': 1}

    def example_fun(arg1=a.b.c.d, arg2=a.b.c.d(1, 2), arg3=e['f']):  # pylint: disable=unused-argument
      pass

    sig = parser.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)
    self.assertEqual(
        sig.arguments,
        ['arg1=a.b.c.d', 'arg2=a.b.c.d(1, 2)', 'arg3=e[&#x27;f&#x27;]'])

  def test_compulsory_kwargs_without_defaults(self):

    def example_fun(x, z, a=True, b='test', *, y=None, c, **kwargs) -> bool:  # pylint: disable=unused-argument
      return True

    sig = parser.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)
    self.assertEqual(sig.arguments, [
        'x', 'z', 'a=True', 'b=&#x27;test&#x27;', '*', 'y=None', 'c', '**kwargs'
    ])
    self.assertEqual(sig.return_type, 'bool')
    self.assertEqual(sig.arguments_typehint_exists, False)
    self.assertEqual(sig.return_typehint_exists, True)

  def test_compulsory_kwargs_without_defaults_with_args(self):

    def example_fun(x, z, cls, *args, a=True, b='test', y=None, c, **kwargs):  # pylint: disable=unused-argument
      return True

    sig = parser.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)
    self.assertEqual(sig.arguments, [
        'x', 'z', 'cls', '*args', 'a=True', 'b=&#x27;test&#x27;', 'y=None', 'c',
        '**kwargs'
    ])
    self.assertEqual(sig.arguments_typehint_exists, False)
    self.assertEqual(sig.return_typehint_exists, False)

  def test_type_annotations(self):
    # pylint: disable=unused-argument

    class TestMethodSig:

      def example_fun(self,
                      x: List[str],
                      z: int,
                      a: Union[List[str], str, int] = None,
                      b: str = 'test',
                      *,
                      y: bool = False,
                      c: Callable[..., int],
                      **kwargs) -> None:
        pass

    # pylint: enable=unused-argument

    sig = parser.generate_signature(
        TestMethodSig.example_fun,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.METHOD,
    )
    self.assertEqual(sig.arguments, [
        'x: List[str]',
        'z: int',
        'a: Union[List[str], str, int] = None',
        'b: str = &#x27;test&#x27;',
        '*',
        'y: bool = False',
        'c: Callable[..., int]',
        '**kwargs',
    ])
    self.assertEqual(sig.return_type, 'None')
    self.assertEqual(sig.arguments_typehint_exists, True)
    self.assertEqual(sig.return_typehint_exists, True)

  def test_dataclasses_type_annotations(self):

    sig = parser.generate_signature(
        ExampleDataclass,
        parser_config=self.parser_config,
        func_full_name='',
        func_type=parser.FuncType.FUNCTION)

    self.assertEqual(sig.arguments, [
        'x: List[str]',
        'z: int',
        'c: List[int] = &lt;factory&gt;',
        'a: Union[List[str], str, int] = None',
        'b: str = &#x27;test&#x27;',
        'y: bool = False',
    ])
    self.assertEqual(sig.return_type, 'None')
    self.assertEqual(sig.arguments_typehint_exists, True)

  @parameterized.named_parameters(
      ('deep_objects', Union[Dict[str, Dict[bool, parser.extract_decorators]],
                             int, bool, parser.extract_decorators,
                             List[Dict[int, parser.extract_decorators]]],
       textwrap.dedent("""\
        Union[
            dict[str, dict[bool, <a href="../../../tfdocs/api_generator/parser/extract_decorators.md"><code>tfdocs.api_generator.parser.extract_decorators</code></a>]],
            int,
            bool,
            <a href="../../../tfdocs/api_generator/parser/extract_decorators.md"><code>tfdocs.api_generator.parser.extract_decorators</code></a>,
            list[dict[int, <a href="../../../tfdocs/api_generator/parser/extract_decorators.md"><code>tfdocs.api_generator.parser.extract_decorators</code></a>]]
        ]""")), ('callable_ellipsis_sig', Union[Callable[..., int], str],
                 textwrap.dedent("""\
        Union[
            Callable[..., int],
            str
        ]""")),
      ('callable_args_sig', Union[Callable[[bool, parser.extract_decorators],
                                           float], int],
       textwrap.dedent("""\
        Union[
            Callable[[bool, <a href="../../../tfdocs/api_generator/parser/extract_decorators.md"><code>tfdocs.api_generator.parser.extract_decorators</code></a>], float],
            int
        ]""")),
      ('callable_without_args', Union[None, dict, str, Callable],
       textwrap.dedent("""\
        Union[
            NoneType,
            dict,
            str,
            Callable
        ]""")),
  )  # pyformat: disable
  def test_type_alias_signature(self, alias, expected_sig):
    info_obj = parser.TypeAliasPageInfo(
        full_name='tfdocs.api_generator.generate_lib.DocGenerator',
        py_object=alias)
    info_obj.collect_docs(self.parser_config)
    if sys.version_info[:2] <= (3, 6):
      # TypeAliasPageInfo.signature is built using the __origin__ attribute of
      # type annotations. Before Python 3.7, __origin__ stored typing constructs
      # (e.g., typing.List); in 3.7+, it stores the equivalent runtime class
      # (e.g., builtins.list).
      expected_sig = expected_sig.replace('dict[',
                                          'Dict[').replace('list[', 'List[')
      # For some reason, bool is missing from the deep_objects signature in 3.6.
      expected_sig = expected_sig.replace('    bool,\n', '')
    self.assertEqual(info_obj.signature, expected_sig)

  def _setup_class_info(self, cls, method_name):
    pc = self.parser_config
    pc.tree['x.Cls'] = [method_name]
    full_name = f'x.Cls.{method_name}'
    pc.index[full_name] = getattr(cls, method_name)
    pc.reference_resolver._duplicate_of[full_name] = full_name
    pc.reference_resolver._is_fragment[full_name] = True
    pc.reference_resolver._all_names.add(full_name)

    info = parser.ClassPageInfo(full_name='x.Cls', py_object=cls)
    info._doc = parser._DocstringInfo('doc', ['doc'], {})
    info.collect_docs(self.parser_config)

    return info

  def test_signature_method_wrong_self_name(self):

    # Calling these classes all `Cls` confuses inspect.getsource.
    # Use unique names.
    class Cls1:

      def method(x):  # pylint: disable=no-self-argument
        pass

    info = self._setup_class_info(Cls1, 'method')
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_method_star_args(self):

    class Cls2:

      def method(*args):  # pylint: disable=no-method-argument
        pass

    info = self._setup_class_info(Cls2, 'method')
    self.assertEqual('(\n    *args\n)', str(info.methods[0].signature))

  def test_signature_classmethod_wrong_cls_name(self):

    class Cls3:

      @classmethod
      def method(x):  # pylint: disable=bad-classmethod-argument
        pass

    info = self._setup_class_info(Cls3, 'method')
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_staticmethod(self):

    class Cls4:

      @staticmethod
      def method(x):
        pass

    info = self._setup_class_info(Cls4, 'method')
    self.assertEqual('(\n    x\n)', str(info.methods[0].signature))

  def test_signature_new(self):

    class Cls5:

      def __new__(x):  # pylint: disable=bad-classmethod-argument
        pass

    info = self._setup_class_info(Cls5, '__new__')
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_dataclass_auto_init(self):

    @dataclasses.dataclass
    class Cls6:
      a: Optional[int]
      b: Optional[str]

    info = self._setup_class_info(Cls6, '__init__')
    self.assertEqual('(\n    a: Optional[int],\n    b: Optional[str]\n)',
                     str(info.methods[0].signature))

  def test_signature_dataclass_custom_init(self):

    @dataclasses.dataclass(init=False)
    class Cls7:
      a: Optional[int]
      b: Optional[str]

      def __init__(self, x: Optional[Union[int, str]]):
        self.a = int(x)
        self.b = str(x)

    info = self._setup_class_info(Cls7, '__init__')
    self.assertEqual('(\n    x: Optional[Union[int, str]]\n)',
                     str(info.methods[0].signature))


if __name__ == '__main__':
  absltest.main()
