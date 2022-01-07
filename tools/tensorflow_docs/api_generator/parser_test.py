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
import dataclasses
import inspect
import os
import tempfile
import textwrap

from typing import List, Union

from absl.testing import absltest
from absl.testing import parameterized
import attr

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import reference_resolver as reference_resolver_lib
from tensorflow_docs.api_generator.pretty_docs import docs_for_object

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

    string = ('A `@tf.reference`, a member `tf.reference.foo`, and a '
              '`tf.third(what)`. '
              'This is `not a symbol`, and this is `tf.not.a.real.symbol`')

    duplicate_of = {'tf.third': 'tf.fourth'}
    index = {
        'tf.reference': HasOneMember,
        'tf.reference.foo': HasOneMember.foo,
        'tf.third': HasOneMember,
        'tf.fourth': HasOneMember
    }

    visitor = DummyVisitor(index, duplicate_of)

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'], link_prefix='../..')

    result = reference_resolver.replace_references(string)
    self.assertEqual(
        'A <a href="../../tf/reference.md">'
        '<code>@tf.reference</code></a>, '
        'a member <a href="../../tf/reference.md#foo">'
        '<code>tf.reference.foo</code></a>, '
        'and a <a href="../../tf/fourth.md">'
        '<code>tf.third(what)</code></a>. '
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'TestClass': [
            'a_method', 'class_method', 'static_method', 'a_property',
            'ChildClass', 'CLASS_MEMBER'
        ]
    }
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ExampleDataclass': []}

    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
        full_name='ExampleDataclass',
        py_object=ExampleDataclass,
        parser_config=parser_config)

    self.assertCountEqual(['a', 'b', 'c', 'x', 'y', 'z'],
                          [name for name, value in page_info.attr_block.items])

  def test_namedtuple_field_order(self):
    namedtupleclass = collections.namedtuple(
        'namedtupleclass', ['z', 'y', 'x', 'hidden', 'w', 'v', 'u'])

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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'namedtupleclass': {'u', 'v', 'w', 'x', 'y', 'z'}}
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
        full_name='namedtupleclass',
        py_object=namedtupleclass,
        parser_config=parser_config)

    self.assertIsNone(page_info._namedtuplefields['hidden'])

    # Each namedtiple field has a docstring of the form:
    #   'Alias for field number ##'. These props are returned sorted.
    def field_number(desc):
      return int(desc.split(' ')[-1])

    self.assertSequenceEqual(
        [0, 1, 2, 4, 5, 6],
        [field_number(desc) for name, desc in page_info.attr_block.items])

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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'Child': ['a_method'],
    }

    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ChildMessage': ['hidden', 'hidden2', 'hidden3', 'my_method']}

    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'TestModule': [
            'TestClass', 'test_function', 'test_function_with_args_kwargs'
        ]
    }
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'': ['test_function']}
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'': ['test_function_with_args_kwargs']}
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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

      @compatibility(two words!)
      Theano has nothing as awesome as this function.

      @tf.function

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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'], link_prefix='../..')
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree={},
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    doc_info = parser.parse_md_docstring(
        test_function_with_fancy_docstring,
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

    self.assertCountEqual(doc_info.compatibility.keys(),
                          {'numpy', 'two words!'})

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

    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
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
    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {
        'ConcreteMutableMapping': [
            '__init__', '__getitem__', '__setitem__', 'values', 'get'
        ]
    }
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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
    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {'ConcreteMutableMapping': ['pop']}
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    page_info = docs_for_object.docs_for_object(
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
    reference_resolver = reference_resolver_lib.ReferenceResolver.from_visitor(
        visitor=visitor, py_module_names=['tf'])

    tree = {cls: [method]}
    parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index={},
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

    function_info = docs_for_object.docs_for_object(
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

    parser_config = config.ParserConfig(
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

    parser_config = config.ParserConfig(
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

    parser_config = config.ParserConfig(
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



  def testIsClasssAttr(self):
    result = parser.is_class_attr('test_module.test_function',
                                  {'test_module': test_module})
    self.assertFalse(result)

    result = parser.is_class_attr('TestClass.test_function',
                                  {'TestClass': TestClass})
    self.assertTrue(result)

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


if __name__ == '__main__':
  absltest.main()
