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

import copy

import types
from typing import Optional

from absl.testing import absltest

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import generate_lib
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import reference_resolver as reference_resolver_lib
from tensorflow_docs.api_generator.pretty_docs import docs_for_object
from tensorflow_docs.api_generator.report import utils
from tensorflow_docs.api_generator.report.schema import api_report_pb2


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

  def _build_page_info(self):
    m = types.ModuleType('m')
    m.__file__ = __file__
    m.TestClass = TestClass

    generator = generate_lib.DocGenerator(
        root_title='test',
        py_modules=[('m', m)],
        code_url_prefix='https://tensorflow.org')

    parser_config = generator.run_extraction()

    api_node = doc_generator_visitor.ApiTreeNode(
        path=('m', 'TestClass'), py_object=TestClass)
    return docs_for_object.docs_for_object(
        api_node=api_node, parser_config=parser_config)

  def _make_report(self):
    page_info = self._build_page_info()

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(page_info)
    return test_api_report

  def test_fill_report_doesnt_edit_page(self):
    page1 = self._build_page_info()
    page2 = self._build_page_info()

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(page2)

    page1.api_node = None
    page1.parser_config = None

    page2.api_node = None
    page2.parser_config = None

    self.assertEqual(page1, page2)

  def test_class_raises_lint(self):
    test_api_report = self._make_report()

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'm.TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.raises_lint.num_raises_defined, 2)
        self.assertEqual(test_report.raises_lint.total_raises_in_code, 2)

  def test_method_return_lint(self):
    test_api_report = self._make_report()

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'm.TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertTrue(test_report.return_lint.returns_defined)

  def test_description_lint(self):
    test_api_report = self._make_report()

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'm.TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.desc_lint.len_brief, 2)
        self.assertEqual(test_report.desc_lint.len_long_desc, 54)

      if (test_report.symbol_name == 'm.TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.desc_lint.len_brief, 4)
        self.assertEqual(test_report.desc_lint.len_long_desc, 10)

  def test_parameter_lint(self):
    test_api_report = self._make_report()

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'm.TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_args,
                         2)
        self.assertEqual(test_report.parameter_lint.num_args_in_doc, 4)
        self.assertEqual(test_report.parameter_lint.num_args_in_code, 3)
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_attr,
                         1)
        self.assertEqual(test_report.parameter_lint.total_attr_param, 2)

      if (test_report.symbol_name == 'm.TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_args,
                         0)
        self.assertEqual(test_report.parameter_lint.num_args_in_doc, 1)
        self.assertEqual(test_report.parameter_lint.num_args_in_code, 1)
        self.assertEqual(test_report.parameter_lint.num_empty_param_desc_attr,
                         0)
        self.assertEqual(test_report.parameter_lint.total_attr_param, 0)

  def test_example_lint(self):
    test_api_report = self._make_report()

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'm.TestClass' and
          test_report.object_type == api_report_pb2.ObjectType.CLASS):
        self.assertEqual(test_report.usage_example_lint.num_doctest, 2)
        self.assertEqual(test_report.usage_example_lint.num_untested_examples,
                         1)
        self.assertEqual(
            'm',
            test_report.package_group,
        )

      if (test_report.symbol_name == 'm.TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertEqual(test_report.usage_example_lint.num_doctest, 0)
        self.assertEqual(test_report.usage_example_lint.num_untested_examples,
                         1)
        self.assertEqual('m', test_report.package_group)


if __name__ == '__main__':
  absltest.main()
