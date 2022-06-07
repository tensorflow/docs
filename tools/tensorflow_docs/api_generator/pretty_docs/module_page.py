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


class ModulePageBuilder(base_page.TemplatePageBuilder):
  """Builds a markdown page from a `ModulePageInfo` instance."""
  TEMPLATE = 'templates/module.jinja'

  def __init__(self, page_info: 'ModulePageInfo'):
    super().__init__(page_info)

  def build_other_member_section(self):
    if self.page_info.other_members:
      return base_page.build_other_members(
          self.page_info.other_members,
          title='<h2 class="add-link">Other Members</h2>',
      )
    else:
      return ''


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

  def __init__(self, *, api_node, **kwargs):
    """Initialize a `ModulePageInfo`.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """
    super().__init__(api_node, **kwargs)

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

  def collect_docs(self):
    """Collect information necessary specifically for a module's doc page.

    Mainly this is information about the members of the module.
    """
    # the path_tree has nodes for all api-paths, not just the preferred paths.
    module_path_node = self.parser_config.path_tree[self.api_node.path]
    for (_, path_node) in sorted(module_path_node.children.items()):
      member_doc = parser.parse_md_docstring(path_node.py_object,
                                             self.full_name, self.parser_config,
                                             self._extra_docs)

      url = self.parser_config.reference_resolver.reference_to_url(
          path_node.full_name)

      member_info = base_page.MemberInfo(path_node.short_name,
                                         path_node.full_name,
                                         path_node.py_object, member_doc, url)
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
