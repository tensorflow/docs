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
"""Create a `pretty_docs.base_page.PageInfo` from a python object."""
from typing import Any, Dict, Optional, Type

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator.pretty_docs import base_page
from tensorflow_docs.api_generator.pretty_docs import class_page
from tensorflow_docs.api_generator.pretty_docs import function_page
from tensorflow_docs.api_generator.pretty_docs import module_page
from tensorflow_docs.api_generator.pretty_docs import type_alias_page

_DEFAULT_PAGE_BUILDER_CLASSES = {
    obj_type_lib.ObjType.CLASS: class_page.ClassPageInfo,
    obj_type_lib.ObjType.CALLABLE: function_page.FunctionPageInfo,
    obj_type_lib.ObjType.MODULE: module_page.ModulePageInfo,
    obj_type_lib.ObjType.TYPE_ALIAS: type_alias_page.TypeAliasPageInfo,
}

PageBuilderDict = Dict[obj_type_lib.ObjType, Type[base_page.PageInfo]]


def docs_for_object(
    *,
    api_node: doc_generator_visitor.ApiTreeNode,
    parser_config: config.ParserConfig,
    extra_docs: Optional[Dict[int, str]] = None,
    search_hints: bool = True,
    page_builder_classes: Optional[PageBuilderDict] = None,
) -> base_page.PageInfo:
  """Return a PageInfo object describing a given object from the TF API.

  This function resolves `tf.symbol` references in the docstrings into links
  to the appropriate location.

  Args:
    api_node: The ApiTreeNode for the object.
    parser_config: A `config.ParserConfig` object.
    extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
      that need to be added to the markdown pages created.
    search_hints: If true include metadata search hints, else include a
        "robots: noindex".
    page_builder_classes: An optional dict of `{ObjectType:Type[PageInfo]}` for
        overriding the default page builder classes.

  Returns:
    Either a subclass of `pretty_docs.base_page.PageInfo` depending on the type
    of the python object being documented.

  Raises:
    RuntimeError: If an object is encountered for which we don't know how
      to make docs.
  """
  if page_builder_classes is None:
    page_builder_classes = _DEFAULT_PAGE_BUILDER_CLASSES

  page_info_class = doc_controls.get_custom_page_builder_cls(api_node.py_object)
  if page_info_class is None:
    obj_type = obj_type_lib.ObjType.get(api_node.py_object)
    page_info_class = page_builder_classes[obj_type]

  page_info = page_info_class(
      api_node=api_node,
      search_hints=search_hints,
      extra_docs=extra_docs,
      parser_config=parser_config)

  page_info.docs_for_object()

  return page_info
