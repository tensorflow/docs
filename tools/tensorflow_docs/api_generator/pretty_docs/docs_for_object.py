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
"""Create a `pretty_docs.base_page.PageInfo` from a python object."""
import os
import posixpath

from typing import Any, Dict, Optional, Type

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator import parser
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
    full_name: str,
    py_object: Any,
    parser_config: config.ParserConfig,
    extra_docs: Optional[Dict[int, str]] = None,
    search_hints: bool = True,
    page_builder_classes: Optional[PageBuilderDict] = None,
) -> base_page.PageInfo:
  """Return a PageInfo object describing a given object from the TF API.

  This function resolves `tf.symbol` references in the docstrings into links
  to the appropriate location.

  Args:
    full_name: The fully qualified name of the symbol to be documented.
    py_object: The Python object to be documented. Its documentation is sourced
      from `py_object`'s docstring.
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

  # Which other aliases exist for the object referenced by full_name?
  main_name = parser_config.reference_resolver.py_main_name(full_name)
  duplicate_names = parser_config.duplicates.get(main_name, [])
  if main_name in duplicate_names:
    duplicate_names.remove(main_name)

  if page_builder_classes is None:
    page_builder_classes = _DEFAULT_PAGE_BUILDER_CLASSES

  page_info_class = doc_controls.get_custom_page_builder_cls(py_object)
  if page_info_class is None:
    obj_type = obj_type_lib.ObjType.get(py_object)
    page_info_class = page_builder_classes[obj_type]

  page_info = page_info_class(
      full_name=main_name,
      py_object=py_object,
      search_hints=search_hints,
      extra_docs=extra_docs)

  relative_path = os.path.relpath(
      path='.',
      start=os.path.dirname(parser.documentation_path(full_name)) or '.')

  # Convert from OS-specific path to URL/POSIX path.
  relative_path = posixpath.join(*relative_path.split(os.path.sep))

  with parser_config.reference_resolver.temp_prefix(relative_path):
    page_info.set_doc(
        parser.parse_md_docstring(
            py_object,
            full_name,
            parser_config,
            extra_docs,
        ))

    page_info.collect_docs(parser_config)

    page_info.set_aliases(duplicate_names)

    page_info.set_defined_in(parser.get_defined_in(py_object, parser_config))

    page_info.build()

  return page_info
