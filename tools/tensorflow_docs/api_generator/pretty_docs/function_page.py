# Lint as: python3
# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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
from typing import Any

from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import signature as signature_lib
from tensorflow_docs.api_generator.pretty_docs import base_page


class FunctionPageBuilder(base_page.TemplatePageBuilder):
  """Builds a markdown page from a `FunctionPageInfo` object."""
  TEMPLATE = 'templates/function.jinja'

  def format_docstring_part(self, part):
    ttt = '<h2 class="add-link">{title}</h2>'
    return base_page.format_docstring(part, table_title_template=ttt)

  def build_signature(self):
    return base_page.build_signature(
        name=self.page_info.full_name,
        signature=self.page_info.signature,
        decorators=self.page_info.decorators)


class FunctionPageInfo(base_page.PageInfo):
  """Collects docs For a function Page.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    signature: the parsed signature (see: generate_signature)
    decorators: A list of decorator names.
  """
  DEFAULT_BUILDER_CLASS = FunctionPageBuilder

  def __init__(self, *, full_name: str, py_object: Any, **kwargs):
    """Initialize a FunctionPageInfo.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """
    super().__init__(full_name, py_object, **kwargs)

    self._signature = None
    self._decorators = []

  @property
  def signature(self):
    return self._signature

  def collect_docs(self, parser_config):
    """Collect all information necessary to genertate the function page.

    Mainly this is details about the function signature.

    Args:
      parser_config: The config.ParserConfig for the module being documented.
    """

    assert self.signature is None
    self._signature = signature_lib.generate_signature(
        self.py_object,
        parser_config,
        func_type=signature_lib.FuncType.FUNCTION,
    )
    self._decorators = signature_lib.extract_decorators(self.py_object)

  @property
  def decorators(self):
    return list(self._decorators)

  def add_decorator(self, dec):
    self._decorators.append(dec)

  def get_metadata_html(self):
    return parser.Metadata(self.full_name).build_html()
