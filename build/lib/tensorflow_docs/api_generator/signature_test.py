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

import dataclasses
import textwrap
import types

from typing import Callable, Dict, List, Optional, Union

from absl.testing import absltest
from absl.testing import parameterized

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import generate_lib
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import reference_resolver as reference_resolver_lib
from tensorflow_docs.api_generator import signature
from tensorflow_docs.api_generator.pretty_docs import class_page
from tensorflow_docs.api_generator.pretty_docs import type_alias_page


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


class TestGenerateSignature(parameterized.TestCase, absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.known_object = object()

    m = types.ModuleType('m')
    m.__file__ = __file__
    m.extract_decorators = signature.extract_decorators
    m.submodule = types.ModuleType('submodule')
    m.submodule.known = self.known_object

    generator = generate_lib.DocGenerator(
        root_title='test',
        py_modules=[('m', m)],
        code_url_prefix='https://tensorflow.org')

    self.parser_config = generator.run_extraction()


  def test_known_object(self):

    def example_fun(arg=self.known_object):  # pylint: disable=unused-argument
      pass

    self.parser_config.reference_resolver = (
        self.parser_config.reference_resolver.with_prefix('/'))

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)

    expected = textwrap.dedent("""\
        (
            arg=<a href="/m/submodule.md#known"><code>m.submodule.known</code></a>
        )""")

    self.assertEqual(expected, str(sig))

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

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)

    expected = textwrap.dedent("""\
        (
            self, cls, a=5, b=5.0, c=None, d=True, e=&#x27;hello&#x27;, f=(1, (2, 3))
        )""")
    self.assertEqual(expected, str(sig))

  def test_dotted_name(self):
    # pylint: disable=g-bad-name

    class a:

      class b:

        class c:

          class d:

            def __init__(self, *args):
              pass

    # pylint: enable=g-bad-name

    e = {'f': 1}

    def example_fun(arg1=a.b.c.d, arg2=a.b.c.d(1, 2), arg3=e['f']):  # pylint: disable=unused-argument
      pass

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)
    expected = ('(\n    arg1=a.b.c.d, arg2=a.b.c.d(1, 2), '
                'arg3=e[&#x27;f&#x27;]\n)')
    self.assertEqual(expected, str(sig))

  def test_compulsory_kwargs_without_defaults(self):

    def example_fun(x, z, a=True, b='test', *, c, y=None, d, **kwargs) -> bool:  # pylint: disable=unused-argument
      return True

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)
    self.assertEqual(
        list(sig.parameters.keys()),
        ['x', 'z', 'a', 'b', 'c', 'y', 'd', 'kwargs'])
    expected = textwrap.dedent("""\
    (
        x, z, a=True, b=&#x27;test&#x27;, *, c, y=None, d, **kwargs
    ) -> bool""")
    self.assertEqual(expected, str(sig))

  def test_compulsory_kwargs_without_defaults_with_args(self):

    def example_fun(x, z, cls, *args, a=True, b='test', y=None, c, **kwargs):  # pylint: disable=unused-argument
      return True

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)
    self.assertEqual(
        list(sig.parameters.keys()),
        ['x', 'z', 'cls', 'args', 'a', 'b', 'y', 'c', 'kwargs'])
    self.assertEqual(
        str(sig),
        '(\n    x, z, cls, *args, a=True, b=&#x27;test&#x27;, y=None, c, **kwargs\n)'
    )

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

    sig = signature.generate_signature(
        TestMethodSig.example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.METHOD,
    )
    expected = textwrap.dedent("""\
        (
            x: List[str],
            z: int,
            a: Union[List[str], str, int] = None,
            b: str = &#x27;test&#x27;,
            *,
            y: bool = False,
            c: Callable[..., int],
            **kwargs
        ) -> None""")
    self.assertEqual(expected, str(sig))

  def test_dataclasses_type_annotations(self):

    sig = signature.generate_signature(
        ExampleDataclass,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)

    expected = textwrap.dedent("""\
      (
          x: List[str],
          z: int,
          c: List[int] = dataclasses.field(default_factory=list),
          a: Union[List[str], str, int] = None,
          b: str = &#x27;test&#x27;,
          y: bool = False
      )""")
    self.assertEqual(expected, str(sig))

  @parameterized.named_parameters(
      ('deep_objects', Union[Dict[str, Dict[bool, signature.extract_decorators]],
                             int, bool, signature.extract_decorators,
                             List[Dict[int, signature.extract_decorators]]],
       textwrap.dedent("""\
        Union[
            dict[str, dict[bool, <a href="../../../m/extract_decorators.md"><code>m.extract_decorators</code></a>]],
            int,
            bool,
            <a href="../../../m/extract_decorators.md"><code>m.extract_decorators</code></a>,
            list[dict[int, <a href="../../../m/extract_decorators.md"><code>m.extract_decorators</code></a>]]
        ]""")),
      ('callable_ellipsis_sig', Union[Callable[..., int], str],
       textwrap.dedent("""\
        Union[
            Callable[..., int],
            str
        ]""")),
      ('callable_args_sig', Union[Callable[[bool, signature.extract_decorators],
                                           float], int],
       textwrap.dedent("""\
        Union[
            Callable[[bool, <a href="../../../m/extract_decorators.md"><code>m.extract_decorators</code></a>], float],
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
    api_node = doc_generator_visitor.ApiTreeNode(
        path=tuple('tfdocs.api_generator.generate_lib.DocGenerator'.split('.')),
        py_object=alias)
    info_obj = type_alias_page.TypeAliasPageInfo(
        api_node=api_node, parser_config=self.parser_config)
    with self.parser_config.reference_resolver.temp_prefix('../../..'):
      info_obj.collect_docs()
      self.assertEqual(info_obj.signature, expected_sig)

  def _setup_class_info(self, cls):
    self.known_object = object()

    x = types.ModuleType('x')
    x.__file__ = __file__
    x.Cls = cls

    generator = generate_lib.DocGenerator(
        root_title='test',
        py_modules=[('x', x)],
        code_url_prefix='https://tensorflow.org')

    parser_config = generator.run_extraction()
    parser_config.reference_resolver = (
        parser_config.reference_resolver.with_prefix('/'))

    api_node = parser_config.api_tree['x', 'Cls']
    info = class_page.ClassPageInfo(
        api_node=api_node, parser_config=parser_config)
    info._doc = parser.DocstringInfo('doc', ['doc'], {})
    info.collect_docs()

    return info

  def test_signature_method_wrong_self_name(self):

    # Calling these classes all `Cls` confuses get_source, you need to
    # use unique names.
    class Cls1:

      def method(x):  # pylint: disable=no-self-argument
        pass

    info = self._setup_class_info(Cls1)
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_method_star_args(self):

    class Cls2:

      def method(*args):  # pylint: disable=no-method-argument
        pass

    info = self._setup_class_info(Cls2)
    self.assertEqual('(\n    *args\n)', str(info.methods[0].signature))

  def test_signature_classmethod_wrong_cls_name(self):

    class Cls3:

      @classmethod
      def method(x):  # pylint: disable=bad-classmethod-argument
        pass

    info = self._setup_class_info(Cls3)
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_staticmethod(self):

    class Cls4:

      @staticmethod
      def method(x):
        pass

    info = self._setup_class_info(Cls4)
    self.assertEqual('(\n    x\n)', str(info.methods[0].signature))

  def test_signature_new(self):

    class Cls5:

      def __new__(x):  # pylint: disable=bad-classmethod-argument
        pass

    info = self._setup_class_info(Cls5)
    self.assertEqual('()', str(info.methods[0].signature))

  def test_signature_dataclass_auto_init(self):

    @dataclasses.dataclass
    class Cls6:
      a: Optional[int]
      b: Optional[str]

    info = self._setup_class_info(Cls6)
    builder = info.DEFAULT_BUILDER_CLASS(info)

    self.assertEqual('(\n    a: Optional[int], b: Optional[str]\n)',
                     str(builder.methods.constructor.signature))

  def test_signature_dataclass_custom_init(self):

    @dataclasses.dataclass(init=False)
    class Cls7:
      a: Optional[int]
      b: Optional[str]

      def __init__(self, x: Optional[Union[int, str]]):
        self.a = int(x)
        self.b = str(x)

    info = self._setup_class_info(Cls7)
    builder = info.DEFAULT_BUILDER_CLASS(info)
    self.assertEqual('(\n    x: Optional[Union[int, str]]\n)',
                     str(builder.methods.constructor.signature))

  def test_dataclass_default_uses_ast_repr(self):

    @dataclasses.dataclass
    class MyClass:
      a: float = 1 / 9

    sig = signature.generate_signature(
        MyClass, parser_config=self.parser_config)

    expected = '(\n    a: float = (1 / 9)\n)'
    self.assertEqual(expected, str(sig))

  def test_dataclass_inheritance_sees_parent(self):
    const = 3.14159

    @dataclasses.dataclass
    class Parent:
      a: int = 60 * 60
      b: float = 1 / 9

    @dataclasses.dataclass
    class Child(Parent):
      b: float = 2 / 9
      c: float = const

    sig = signature.generate_signature(Child, parser_config=self.parser_config)
    expected = textwrap.dedent("""\
        (
            a: int = (60 * 60), b: float = (2 / 9), c: float = const
        )""")
    self.assertEqual(expected, str(sig))

  def test_extract_non_annotated(self):

    const = 1234

    class A:
      a = 60 * 60
      b = 1 / 9

    class B(A):
      b = 2 / 9
      c = const

    ast_extractor = signature._ClassDefaultAndAnnotationExtractor()
    ast_extractor.extract(B)

    self.assertEqual({
        'a': '(60 * 60)',
        'b': '(2 / 9)',
        'c': 'const'
    }, ast_extractor.defaults)


  def test_vararg_before_kwargonly_consistent_order(self):

    def my_fun(*args, a=1, **kwargs):  # pylint: disable=unused-argument
      pass

    sig = signature.generate_signature(my_fun, parser_config=self.parser_config)
    expected = '(\n    *args, a=1, **kwargs\n)'
    self.assertEqual(expected, str(sig))

  def test_class_vararg_before_kwargonly_consistent_order(self):

    class MyClass:

      def __init__(*args, a=1, **kwargs):  # pylint: disable=no-method-argument
        pass

    sig = signature.generate_signature(
        MyClass, parser_config=self.parser_config)
    expected = '(\n    *args, a=1, **kwargs\n)'
    self.assertEqual(expected, str(sig))

  def test_strip_address(self):

    class What:
      pass

    w = What()

    expected = ('<__main__.TestGenerateSignature.test_strip_address.'
                '<locals>.What object>')
    self.assertEqual(expected, signature.strip_obj_addresses(str(w)))

if __name__ == '__main__':
  absltest.main()
