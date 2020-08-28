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
"""Utilities for generating report for a package."""

from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import pretty_docs
from tensorflow_docs.api_generator.report import linter

from tensorflow_docs.api_generator.report.schema import api_report_generated_pb2 as api_report_pb2
from google.protobuf import timestamp_pb2


class ApiReport:
  """Generates the API report for a package."""

  def __init__(self):
    self.api_report = api_report_pb2.ApiReport()

    invocation_timestamp = timestamp_pb2.Timestamp()
    invocation_timestamp.GetCurrentTime()
    self.api_report.timestamp.CopyFrom(invocation_timestamp)
    self.api_report.date = invocation_timestamp.ToJsonString()

  def _lint(
      self,
      *,
      name: str,
      object_type: api_report_pb2.ObjectType,
      page_info: parser.PageInfo,
  ) -> None:
    self.api_report.symbol_metric.add(
        symbol_name=name,
        object_type=object_type,
        parameter_lint=linter.lint_params(page_info),
        desc_lint=linter.lint_description(page_info),
        return_lint=linter.lint_returns(page_info),
        raises_lint=linter.lint_raises(page_info),
    )

  def _fill_class_metric(self, class_page_info: parser.ClassPageInfo) -> None:
    """Fills in the lint metrics for a class and its methods.

    The constructor and class's docstring is merged for linting. Class's
    `py_object` is replaced with that class's constructor's `py_object`.

    Every other method except `__init__` or `__new__` is linted separately.

    Args:
      class_page_info: A `ClassPageInfo` object containing information that's
        used to calculate metrics for the class and its methods.
    """

    methods: pretty_docs.Methods = pretty_docs.split_methods(
        class_page_info.methods)
    # Merge the constructor and class docstrings.
    class_blocks = pretty_docs.merge_blocks(class_page_info,
                                            methods.constructor)
    # Add the `Attributes` sections (if it exists) to the merged class blocks.
    if class_page_info.attr_block is not None:
      class_blocks.append(class_page_info.attr_block)
    # Replace the class py_object with constructors py_object. This is done
    # because each method is linted separately and class py_object contains the
    # source code of all its methods too.
    if methods.constructor is not None:
      class_page_info.py_object = methods.constructor.py_object
    else:
      class_page_info.py_object = None
    class_page_info.doc._replace(docstring_parts=class_blocks)

    self._lint(
        name=class_page_info.full_name,
        object_type=api_report_pb2.ObjectType.CLASS,
        page_info=class_page_info,
    )

    # Lint each method separately and add its metrics to the proto object.
    for method in methods.info_dict.values():
      self._lint(
          name=method.full_name,
          object_type=api_report_pb2.ObjectType.METHOD,
          page_info=method,
      )

  def _fill_function_metric(self, function_page_info: parser.FunctionPageInfo):
    """Fills in the lint metrics for a function.

    Args:
      function_page_info: A `FunctionPageInfo` object containing information
        that's used to calculate metrics for the function.
    """
    self._lint(
        name=function_page_info.full_name,
        object_type=api_report_pb2.ObjectType.FUNCTION,
        page_info=function_page_info,
    )

  def fill_metrics(self, page_info: parser.PageInfo) -> None:
    if isinstance(page_info, parser.ClassPageInfo):
      self._fill_class_metric(page_info)

    if isinstance(page_info, parser.FunctionPageInfo):
      self._fill_function_metric(page_info)
