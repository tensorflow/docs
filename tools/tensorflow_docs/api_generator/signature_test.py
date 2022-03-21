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

import dataclasses
import textwrap

from typing import Callable, Dict, List, Optional, Union

from absl.testing import absltest
from absl.testing import parameterized

from tensorflow_docs.api_generator import config
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
    reference_resolver = reference_resolver_lib.ReferenceResolver(
        duplicate_of={},
        is_fragment={
            'tfdocs.api_generator.signature.extract_decorators': False
        },
        py_module_names=[])
    self.parser_config = config.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree={},
        index={},
        reverse_index={
            id(self.known_object):
                'location.of.object.in.api',
            id(signature.extract_decorators):
                'tfdocs.api_generator.signature.extract_decorators',
        },
        base_dir='/',
        code_url_prefix='/')

  def test_known_object(self):

    def example_fun(arg=self.known_object):  # pylint: disable=unused-argument
      pass

    sig = signature.generate_signature(
        example_fun,
        parser_config=self.parser_config,
        func_type=signature.FuncType.FUNCTION)
    self.assertEqual('(\n    arg=location.of.object.in.api\n)', str(sig))

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
            dict[str, dict[bool, <a href="../../../tfdocs/api_generator/signature/extract_decorators.md"><code>tfdocs.api_generator.signature.extract_decorators</code></a>]],
            int,
            bool,
            <a href="../../../tfdocs/api_generator/signature/extract_decorators.md"><code>tfdocs.api_generator.signature.extract_decorators</code></a>,
            list[dict[int, <a href="../../../tfdocs/api_generator/signature/extract_decorators.md"><code>tfdocs.api_generator.signature.extract_decorators</code></a>]]
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
            Callable[[bool, <a href="../../../tfdocs/api_generator/signature/extract_decorators.md"><code>tfdocs.api_generator.signature.extract_decorators</code></a>], float],
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
    info_obj = type_alias_page.TypeAliasPageInfo(
        full_name='tfdocs.api_generator.generate_lib.DocGenerator',
        py_object=alias)
    with self.parser_config.reference_resolver.temp_prefix('../../..'):
      info_obj.collect_docs(self.parser_config)
      self.assertEqual(info_obj.signature, expected_sig)

  def _setup_class_info(self, cls, method_name):
    pc = self.parser_config
    pc.tree['x.Cls'] = [method_name]
    full_name = f'x.Cls.{method_name}'
    pc.index[full_name] = getattr(cls, method_name)
    pc.reference_resolver._duplicate_of[full_name] = full_name
    pc.reference_resolver._is_fragment[full_name] = True
    pc.reference_resolver._all_names.add(full_name)
    pc.reference_resolver._link_prefix = '../..'

    info = class_page.ClassPageInfo(full_name='x.Cls', py_object=cls)
    info._doc = parser.DocstringInfo('doc', ['doc'], {})
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
            a: int = (60 * 60),
            b: float = (2 / 9),
            c: float = const
        )""")
    self.assertEqual(expected, str(sig))

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
