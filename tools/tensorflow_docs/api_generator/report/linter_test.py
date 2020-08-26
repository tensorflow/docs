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
  """

  def __init__(self, temp_a, temp_b):
    """Initializes the class.

    Args:
      temp_a: Temporary variable a.
      temp_b: Temporary variable b.

    Raises:
      ValuesError: Temp_a value not allowed.
      TypeError: Type not allowed.
    """
    if temp_a:
      raise ValueError('temp_a value not allowed.')
    else:
      raise TypeError('Type not allowed.')

  def method_one(self, x: str) -> Optional[str]:
    """Does some nice things.

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
    }
    tree = {
        'TestClass': ['__init__', 'method_one'],
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
        self.assertEqual(test_report.raises_lint.num_raises_mismatch, 1)

  def test_method_return_lint(self):
    class_page_info = parser.docs_for_object(
        full_name='TestClass',
        py_object=TestClass,
        parser_config=self.parser_config)

    test_api_report = utils.ApiReport()
    test_api_report.fill_metrics(class_page_info)
    print(test_api_report.api_report)

    for test_report in test_api_report.api_report.symbol_metric:
      if (test_report.symbol_name == 'TestClass.method_one' and
          test_report.object_type == api_report_pb2.ObjectType.METHOD):
        self.assertTrue(test_report.return_lint.returns_defined)


if __name__ == '__main__':
  absltest.main()
