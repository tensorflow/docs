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
from typing import List

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator import parser

from tensorflow_docs.api_generator.pretty_docs import base_page


class ModulePageBuilder(base_page.PageBuilder):
  """Builds a markdown page from a `ModulePageInfo` instance."""

  def build(self) -> str:
    """Build the page."""
    page_info = self.page_info
    parts = [f'# Module: {page_info.full_name}\n\n']

    parts.append('<!-- Insert buttons and diff -->\n')

    parts.append(base_page.top_source_link(page_info.defined_in))
    parts.append('\n\n')

    # First line of the docstring i.e. a brief introduction about the symbol.
    parts.append(page_info.doc.brief + '\n\n')

    parts.append(base_page.build_collapsable_aliases(page_info.aliases))

    parts.append(base_page.build_top_compat(page_info, h_level=2))

    # All lines in the docstring, expect the brief introduction.
    for item in page_info.doc.docstring_parts:
      parts.append(base_page.format_docstring(item, table_title_template=None))

    parts.append(base_page.build_bottom_compat(page_info, h_level=2))

    parts.append('\n\n')

    custom_content = doc_controls.get_custom_page_content(page_info.py_object)
    if custom_content is not None:
      parts.append(custom_content)
      return ''.join(parts)

    if page_info.modules:
      parts.append('## Modules\n\n')
      parts.extend(
          _build_module_parts(
              module_parts=page_info.modules,
              template='[`{short_name}`]({url}) module'))

    if page_info.classes:
      parts.append('## Classes\n\n')
      parts.extend(
          _build_module_parts(
              module_parts=page_info.classes,
              template='[`class {short_name}`]({url})'))

    if page_info.functions:
      parts.append('## Functions\n\n')
      parts.extend(
          _build_module_parts(
              module_parts=page_info.functions,
              template='[`{short_name}(...)`]({url})'))

    if page_info.type_alias:
      parts.append('## Type Aliases\n\n')
      parts.extend(
          _build_module_parts(
              module_parts=page_info.type_alias,
              template='[`{short_name}`]({url})'))

    if page_info.other_members:
      parts.append(
          base_page.build_other_members(
              page_info.other_members,
              title='<h2 class="add-link">Other Members</h2>',
          ))

    return ''.join(parts)


class ModulePageInfo(base_page.PageInfo):
  """Collects docs for a module page.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    classes: A list of `base_page.MemberInfo` objects pointing to docs for the
      classes in this module.
    functions: A list of `base_page.MemberInfo` objects pointing to docs for the
      functions in this module
    modules: A list of `base_page.MemberInfo` objects pointing to docs for the
      modules in this module.
    type_alias: A list of `base_page.MemberInfo` objects pointing to docs for
      the type aliases in this module.
    other_members: A list of `base_page.MemberInfo` objects documenting any
      other object's defined on the module object (mostly enum style fields).
  """
  DEFAULT_BUILDER_CLASS = ModulePageBuilder

  def __init__(self, *, full_name, py_object, **kwargs):
    """Initialize a `ModulePageInfo`.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """
    super().__init__(full_name, py_object, **kwargs)

    self._modules = []
    self._classes = []
    self._functions = []
    self._other_members = []
    self._type_alias = []

  @property
  def modules(self):
    return self._modules

  @property
  def functions(self):
    return self._functions

  @property
  def classes(self):
    return self._classes

  @property
  def type_alias(self):
    return self._type_alias

  @property
  def other_members(self):
    return self._other_members

  def _add_module(self, member_info: base_page.MemberInfo):
    self._modules.append(member_info)

  def _add_class(self, member_info: base_page.MemberInfo):
    self._classes.append(member_info)

  def _add_function(self, member_info: base_page.MemberInfo):
    self._functions.append(member_info)

  def _add_type_alias(self, member_info: base_page.MemberInfo):
    self._type_alias.append(member_info)

  def _add_other_member(self, member_info: base_page.MemberInfo):
    self.other_members.append(member_info)

  def get_metadata_html(self):
    meta_data = parser.Metadata(self.full_name)

    # Objects with their own pages are not added to the metadata list for the
    # module, the module only has a link to the object page. No docs.
    for item in self.other_members:
      meta_data.append(item)

    return meta_data.build_html()

  def _add_member(self, member_info: base_page.MemberInfo) -> None:
    """Adds members of the modules to the respective lists."""
    obj_type = obj_type_lib.ObjType.get(member_info.py_object)
    if obj_type is obj_type_lib.ObjType.MODULE:
      self._add_module(member_info)
    elif obj_type is obj_type_lib.ObjType.CLASS:
      self._add_class(member_info)
    elif obj_type is obj_type_lib.ObjType.CALLABLE:
      self._add_function(member_info)
    elif obj_type is obj_type_lib.ObjType.TYPE_ALIAS:
      self._add_type_alias(member_info)
    elif obj_type is obj_type_lib.ObjType.OTHER:
      self._add_other_member(member_info)

  def collect_docs(self, parser_config):
    """Collect information necessary specifically for a module's doc page.

    Mainly this is information about the members of the module.

    Args:
      parser_config: An instance of config.ParserConfig.
    """

    member_names = parser_config.tree.get(self.full_name, [])
    for member_short_name in member_names:

      if member_short_name in [
          '__builtins__', '__doc__', '__file__', '__name__', '__path__',
          '__package__', '__cached__', '__loader__', '__spec__',
          'absolute_import', 'division', 'print_function', 'unicode_literals'
      ]:
        continue

      if self.full_name:
        member_full_name = self.full_name + '.' + member_short_name
      else:
        member_full_name = member_short_name

      member = parser_config.py_name_to_object(member_full_name)

      member_doc = parser.parse_md_docstring(member, self.full_name,
                                             parser_config, self._extra_docs)

      url = parser_config.reference_resolver.reference_to_url(member_full_name)

      member_info = base_page.MemberInfo(member_short_name, member_full_name,
                                         member, member_doc, url)
      self._add_member(member_info)


def _build_module_parts(module_parts: List[base_page.MemberInfo],
                        template: str) -> List[str]:
  mod_str_parts = []
  for item in module_parts:
    mod_str_parts.append(template.format(**item._asdict()))
    if item.doc.brief:
      mod_str_parts.append(': ' + item.doc.brief)
    mod_str_parts.append('\n\n')
  return mod_str_parts
