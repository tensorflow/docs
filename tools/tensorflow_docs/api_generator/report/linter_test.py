# Lint as: python3
# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
"""Tests for tensorflow_docs.api_generator.report.linter."""

from typing import Optional

from absl.testing import absltest

from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator.report import utils
from tensorflow_docs.api_generator.report.schema import api_report_generated_pb2 as api_report_pb2


class DummyVisitor(object):

  def __init__(self, index, duplicate_of):
    self.index = index
    self.duplicate_of = duplicate_of


class TestClass:
  """Class docstring.

  Some words here.

  Another paragraph.

  >>> x = 1
  >>> print(x)
  1
  >>> x += 2
  >>> print(x)
  3

  >>> z = 'api'
  >>> z += ' report'
  >>> print(z)
  api report

  Attributes:
    temp_a: Temporary variable a.

  A example usage here.

  ```
  y = 2
  z = y + 3
  assert z == 5
  ```
  """

  def __init__(self, temp_a, temp_b, temp_c):  # pylint: disable=g-doc-args
    """Initializes the class.

    Args:
      temp_a: Temporary variable a.
      temp_b: Temporary variable b.
      temp_c:
      temp_d:

    Raises:
      ValueError: Temp_a value not allowed.
      TypeError: Type not allowed.
    """
    self.temp_a = temp_a
    self._temp_c = temp_c

    if self.temp_a:
      raise ValueError('temp_a value not allowed.')
    else:
      raise TypeError('Type not allowed.')

  @property
  def temp_c(self):  # pylint: disable=g-missing-from-attributes
    return self._temp_c

  def method_one(self, x: str) -> Optional[str]:
    """Does some nice things.

    ```
    x = 'api'
    method_one(x)  # output == apitemp
    ```

    Args:
      x: A variable.

    Returns:
      Returns the modified variable.
    """

    if x:
      return x + 'temp'
    return None


class LinterTest(absltest.TestCase):

  def setUp(self):
    super(LinterTest, self).setUp()
    index = {
        'TestClass': TestClass,
        'TestClass.__init__': TestClass.__init__,
        'TestClass.method_one': TestClass.method_one,
        'TestClass.temp_c': TestClass.temp_c,
    }
    tree = {
        'TestClass': ['__init__', 'method_one', 'temp_c'],
    }
    reference_resolver = parser.ReferenceResolver.from_visitor(
        visitor=DummyVisitor(index=index, duplicate_of={}),
        py_module_names=['tf'],
    )
    self.parser_config = parser.ParserConfig(
        reference_resolver=reference_resolver,
        duplicates={},
        duplicate_of={},
        tree=tree,
        index=index,
        reverse_index={},
        base_dir='/',
        code_url_prefix='/')

  def test_class_raises_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.raises_lint.num_raises_defined, 2)
        self.assertEqual(test_report.raises_lint.total_raises_in_code, 2)

  def test_method_return_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertTrue(test_report.return_lint.returns_defined)

  def test_description_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.desc_lint.len_brief, 2)
        self.assertEqual(test_report.desc_lint.len_long_desc, 54)

      if (test_report.symbol_name == 'TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.desc_lint.len_brief, 4)
        self.assertEqual(test_report.desc_lint.len_long_desc, 10)

  def test_parameter_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_args,
                         2)
        self.assertEqual(test_report.parameter_lint.num_args_in_doc, 4)
        self.assertEqual(test_report.parameter_lint.num_args_in_code, 3)
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_attr,
                         1)
        self.assertEqual(test_report.parameter_lint.total_attr_param, 2)

      if (test_report.symbol_name == 'TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_args,
                         0)
        self.assertEqual(test_report.parameter_lint.num_args_in_doc, 1)
        self.assertEqual(test_report.parameter_lint.num_args_in_code, 1)
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_attr,
                         0)
        self.assertEqual(test_report.parameter_lint.total_attr_param, 0)

  def test_example_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.usage_example_lint.num_doctest, 2)
        self.assertEqual(test_report.usage_example_lint.num_untested_examples,
                         1)
        self.assertEqual(test_report.package_group, 'TestClass')

      if (test_report.symbol_name == 'TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.usage_example_lint.num_doctest, 0)
        self.assertEqual(test_report.usage_example_lint.num_untested_examples,
                         1)
        self.assertEqual(test_report.package_group, 'TestClass')


if __name__ == '__main__':
  absltest.main()
