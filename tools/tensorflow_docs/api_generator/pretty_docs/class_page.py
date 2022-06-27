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
"""Page builder classes for class pages."""
import collections
import dataclasses
import itertools
import re
import textwrap
from typing import Any, Dict, List, NamedTuple, Optional

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import signature as signature_lib
from tensorflow_docs.api_generator.pretty_docs import base_page

from google.protobuf.message import Message as ProtoMessage


class ClassPageBuilder(base_page.TemplatePageBuilder):
  """Builds a markdown page from a `ClassPageInfo` instance."""
  TEMPLATE = 'templates/class.jinja'

  def __init__(self, page_info):
    super().__init__(page_info)
    # Split the methods into constructor and other methods.
    self.methods = split_methods(page_info.methods)

  def build_bases(self):
    page_info = self.page_info
    # If a class is a child class, add which classes it inherits from.
    parts = []
    if self.page_info.bases:
      parts.append('\nInherits From: ')

      link_template = '[`{short_name}`]({url})'
      parts.append(', '.join(
          link_template.format(**base._asdict()) for base in page_info.bases))
      parts.append('\n')

    return ''.join(parts)

  def build_constructor(self):
    page_info = self.page_info

    # If the class has a constructor, build its signature.
    # The signature will contain the class name followed by the arguments it
    # takes.
    parts = []
    if self.methods.constructor is not None:
      parts.append(
          base_page.build_signature(
              name=page_info.full_name,
              signature=self.methods.constructor.signature,
              decorators=self.methods.constructor.decorators))
      parts.append('\n\n')

    return ''.join(parts)

  def build_class_docstring(self):

    parts = merge_class_and_constructor_docstring(self.page_info,
                                                  self.methods.constructor)

    parts.append('\n\n')

    return ''.join(parts)

  def build_attr_block(self):
    parts = []
    if self.page_info.attr_block is not None:
      parts.append(
          base_page.format_docstring(
              self.page_info.attr_block,
              table_title_template='<h2 class="add-link">{title}</h2>'))
      parts.append('\n\n')
    return ''.join(parts)

  def build_method_section(self, method):
    return _build_method_section(method)

  def build_other_member_section(self):
    if self.page_info.other_members:
      return base_page.build_other_members(
          self.page_info.other_members,
          title='<h2 class="add-link">Class Variables</h2>',
      )
    else:
      return ''


class ClassPageInfo(base_page.PageInfo):
  """Collects docs for a class page.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    attributes: A dict mapping from "name" to a docstring
    bases: A list of `base_page.MemberInfo` objects pointing to the docs for the
      parent classes.
    methods: A list of `MethodInfo` objects documenting the class' methods.
    classes: A list of `base_page.MemberInfo` objects pointing to docs for any
      nested classes.
    other_members: A list of `base_page.MemberInfo` objects documenting any
      other object's defined inside the class object (mostly enum style fields).
    attr_block: A `TitleBlock` containing information about the Attributes of
      the class.
    inheritable_header: A header that may be placed on a base-class.
  """
  DEFAULT_BUILDER_CLASS = ClassPageBuilder

  def __init__(self, *, api_node, **kwargs):
    """Initialize a ClassPageInfo.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """
    super().__init__(api_node, **kwargs)

    self._namedtuplefields = collections.OrderedDict()
    if issubclass(api_node.py_object, tuple):
      namedtuple_attrs = ('_asdict', '_fields', '_make', '_replace')
      if all(hasattr(api_node.py_object, attr) for attr in namedtuple_attrs):
        for name in api_node.py_object._fields:
          self._namedtuplefields[name] = None

    self._properties = collections.OrderedDict()
    self._bases = None
    self._methods = []
    self._classes = []
    self._other_members = []
    self.attr_block = None

  @property
  def bases(self):
    """Returns a list of `base_page.MemberInfo` objects pointing to the class' parents."""
    return self._bases

  @property
  def inheritable_header(self) -> Optional[str]:
    header = doc_controls.get_inheritable_header(self.py_object)
    if header is not None:
      header = textwrap.dedent(header)
    return header

  def set_attr_block(self, attr_block):
    assert self.attr_block is None
    self.attr_block = attr_block

  def _set_bases(self):
    """Builds the `bases` attribute, to document this class' parent-classes.

    This method sets the `bases` to a list of `base_page.MemberInfo` objects
    point to the
    doc pages for the class' parents.
    """
    bases = []
    for base in self.py_object.__mro__[1:]:
      base_api_node = self.parser_config.api_tree.node_for_object(base)
      if base_api_node is None:
        continue
      base_full_name = base_api_node.full_name
      base_doc = parser.parse_md_docstring(base, base_full_name,
                                           self.parser_config, self._extra_docs)
      base_url = self.parser_config.reference_resolver.reference_to_url(
          base_full_name)

      link_info = base_page.MemberInfo(
          short_name=base_full_name.split('.')[-1],
          full_name=base_full_name,
          py_object=base,
          doc=base_doc,
          url=base_url)
      bases.append(link_info)

    self._bases = bases

  def _add_property(self, member_info: base_page.MemberInfo):
    """Adds an entry to the `properties` list.

    Args:
      member_info: a `base_page.MemberInfo` describing the property.
    """
    doc = member_info.doc
    # Clarify the default namedtuple docs-strings.
    if re.match('Alias for field number [0-9]+', doc.brief):
      new_brief = f'A `namedtuple` {doc.brief.lower()}'
      doc = doc._replace(docstring_parts=[], brief=new_brief)

    new_parts = [doc.brief]
    # Strip args/returns/raises from property
    new_parts.extend([
        str(part)
        for part in doc.docstring_parts
        if not isinstance(part, parser.TitleBlock)
    ])
    new_parts.append('')
    desc = '\n'.join(new_parts)

    if member_info.short_name in self._namedtuplefields:
      self._namedtuplefields[member_info.short_name] = desc
    else:
      self._properties[member_info.short_name] = desc

  @property
  def methods(self):
    """Returns a list of `MethodInfo` describing the class' methods."""
    return self._methods

  def _add_method(
      self,
      member_info: base_page.MemberInfo,
      defining_class: Optional[type],  # pylint: disable=g-bare-generic
  ) -> None:
    """Adds a `MethodInfo` entry to the `methods` list.

    Args:
      member_info: a `base_page.MemberInfo` describing the method.
      defining_class: The `type` object where this method is defined.
    """
    if defining_class is None:
      return

    # Omit methods defined by namedtuple.
    original_method = defining_class.__dict__[member_info.short_name]
    if (hasattr(original_method, '__module__') and
        (original_method.__module__ or '').startswith('namedtuple')):
      return

    # Some methods are often overridden without documentation. Because it's
    # obvious what they do, don't include them in the docs if there's no
    # docstring.
    if (not member_info.doc.brief.strip() and
        member_info.short_name in ['__del__', '__copy__']):
      return

    # If the current class py_object is a dataclass then use the class object
    # instead of the __init__ method object because __init__ is a
    # generated method on dataclasses (unless the definition used init=False)
    # and `api_generator.get_source.get_source` doesn't work on generated
    # methods (as the source file doesn't exist) which is required for
    # signature generation.
    if (dataclasses.is_dataclass(self.py_object) and
        member_info.short_name == '__init__' and
        self.py_object.__dataclass_params__.init):
      is_dataclass = True
      py_obj = self.py_object
    else:
      is_dataclass = False
      py_obj = member_info.py_object

    func_type = signature_lib.get_method_type(original_method,
                                              member_info.short_name,
                                              is_dataclass)
    signature = signature_lib.generate_signature(
        py_obj, self.parser_config, func_type=func_type)

    decorators = signature_lib.extract_decorators(member_info.py_object)

    defined_in = parser.get_defined_in(member_info.py_object,
                                       self.parser_config)

    method_info = MethodInfo.from_member_info(member_info, signature,
                                              decorators, defined_in)
    self._methods.append(method_info)

  @property
  def classes(self):
    """Returns a list of `base_page.MemberInfo` pointing to any nested classes."""
    return sorted(self._classes, key=lambda x: x.short_name)

  def get_metadata_html(self) -> str:
    meta_data = parser.Metadata(self.full_name)
    for item in itertools.chain(self.classes, self.methods, self.other_members):
      meta_data.append(item)

    return meta_data.build_html()

  def _add_class(self, member_info):
    """Adds a `base_page.MemberInfo` for a nested class to `classes` list.

    Args:
      member_info: a `base_page.MemberInfo` describing the class.
    """
    self._classes.append(member_info)

  @property
  def other_members(self):
    """Returns a list of `base_page.MemberInfo` describing any other contents."""
    return self._other_members

  def _add_other_member(self, member_info: base_page.MemberInfo):
    """Adds an `base_page.MemberInfo` entry to the `other_members` list.

    Args:
      member_info: a `base_page.MemberInfo` describing the object.
    """
    self.other_members.append(member_info)

  def _add_member(
      self,
      member_info: base_page.MemberInfo,
      defining_class: Optional[type],  # pylint: disable=g-bare-generic
  ) -> None:
    """Adds a member to the class page."""
    obj_type = obj_type_lib.ObjType.get(member_info.py_object)

    if obj_type is obj_type_lib.ObjType.PROPERTY:
      self._add_property(member_info)
    elif obj_type is obj_type_lib.ObjType.CLASS:
      if defining_class is None:
        return
      self._add_class(member_info)
    elif obj_type is obj_type_lib.ObjType.CALLABLE:
      self._add_method(member_info, defining_class)
    elif obj_type is obj_type_lib.ObjType.OTHER:
      # Exclude members defined by protobuf that are useless
      if issubclass(self.py_object, ProtoMessage):
        if (member_info.short_name.endswith('_FIELD_NUMBER') or
            member_info.short_name in ['__slots__', 'DESCRIPTOR']):
          return

      self._add_other_member(member_info)

  def collect_docs(self):
    """Collects information necessary specifically for a class's doc page.

    Mainly, this is details about the class's members.
    """
    py_class = self.py_object

    self._set_bases()

    class_path_node = self.parser_config.path_tree[self.api_node.path]
    for _, path_node in sorted(class_path_node.children.items()):
      # Don't document anything that is defined in object or by protobuf.
      defining_class = parser.get_defining_class(py_class, path_node.short_name)
      if defining_class in [object, type, tuple, BaseException, Exception]:
        continue

      # The following condition excludes most protobuf-defined symbols.
      if (defining_class and
          defining_class.__name__ in ['CMessage', 'Message', 'MessageMeta']):
        continue

      if doc_controls.should_skip_class_attr(py_class, path_node.short_name):
        continue

      child_doc = parser.parse_md_docstring(path_node.py_object, self.full_name,
                                            self.parser_config,
                                            self._extra_docs)

      child_url = self.parser_config.reference_resolver.reference_to_url(
          path_node.full_name)

      member_info = base_page.MemberInfo(path_node.short_name,
                                         path_node.full_name,
                                         path_node.py_object, child_doc,
                                         child_url)
      self._add_member(member_info, defining_class)

    self.set_attr_block(self._augment_attributes(self.doc.docstring_parts))

  def _augment_attributes(
      self, docstring_parts: List[Any]) -> Optional[parser.TitleBlock]:
    """Augments and deletes the "Attr" block of the docstring.

    The augmented block is returned and then added to the markdown page by
    pretty_docs.py. The existing Attribute block is deleted from the docstring.

    Merges `namedtuple` fields and properties into the attrs block.

    + `namedtuple` fields first, in order.
    + Then the docstring `Attr:` block.
    + Then any `properties` or `dataclass` fields not mentioned above.

    Args:
      docstring_parts: A list of docstring parts.

    Returns:
      Augmented "Attr" block.
    """

    attribute_block = None

    for attr_block_index, part in enumerate(docstring_parts):
      if isinstance(part, parser.TitleBlock) and part.title.startswith('Attr'):
        raw_attrs = collections.OrderedDict(part.items)
        break
    else:
      # Didn't find the attributes block, there may still be attributes so
      # add a placeholder for them at the end.
      raw_attrs = collections.OrderedDict()
      attr_block_index = len(docstring_parts)
      docstring_parts.append(None)

    attrs = collections.OrderedDict()
    # namedtuple fields first, in order.
    for name, desc in self._namedtuplefields.items():
      # If a namedtuple field has been filtered out, it's description will
      # not have been set in loop in `collect_docs`, so skip fields with `None`
      # as the description.
      if desc is not None:
        attrs[name] = desc
    # the contents of the `Attrs:` block from the docstring
    attrs.update(raw_attrs)

    # properties and dataclass fields last.
    for name, desc in self._properties.items():
      # Don't overwrite existing items
      attrs.setdefault(name, desc)

    if dataclasses.is_dataclass(self.py_object):
      for name, desc in self._dataclass_fields().items():
        # Don't overwrite existing items
        attrs.setdefault(name, desc)

    if attrs:
      attribute_block = parser.TitleBlock(
          title='Attributes', text='', items=list(attrs.items()))

    # Delete the Attrs block if it exists or delete the placeholder.
    del docstring_parts[attr_block_index]

    return attribute_block

  def _dataclass_fields(self):
    fields = {
        name: 'Dataclass field'
        for name in self.py_object.__dataclass_fields__.keys()
        if not name.startswith('_')
    }

    return fields


class MethodInfo(NamedTuple):
  """Described a method."""
  short_name: str
  full_name: str
  py_object: Any
  doc: parser.DocstringInfo
  url: str
  signature: signature_lib.TfSignature
  decorators: List[str]
  defined_in: Optional[parser.FileLocation]

  @classmethod
  def from_member_info(cls, method_info: base_page.MemberInfo,
                       signature: signature_lib.TfSignature,
                       decorators: List[str],
                       defined_in: Optional[parser.FileLocation]):
    """Upgrades a `base_page.MemberInfo` to a `MethodInfo`."""
    return cls(
        **method_info._asdict(),
        signature=signature,
        decorators=decorators,
        defined_in=defined_in)


class Methods(NamedTuple):
  info_dict: Dict[str, MethodInfo]
  constructor: MethodInfo


def split_methods(methods: List[MethodInfo]) -> Methods:
  """Splits the given methods list into constructors and the remaining methods.

  If both `__init__` and `__new__` exist on the class, then prefer `__init__`
  as the constructor over `__new__` to document.

  Args:
    methods: List of all the methods on the `ClassPageInfo` object.

  Returns:
    A `DocumentMethods` object containing a {method_name: method object}
    dictionary and a constructor object.
  """

  # Create a method_name to methods object dictionary.
  methods = sorted(methods, key=_method_sort)
  method_info_dict = {method.short_name: method for method in methods}

  # Pop the constructors from the dictionary.
  init_constructor = method_info_dict.pop('__init__', None)
  new_constructor = method_info_dict.pop('__new__', None)

  constructor = None
  # Prefers `__init__` over `__new__` as the constructor to document.
  if init_constructor is not None:
    constructor = init_constructor
  elif new_constructor is not None:
    constructor = new_constructor

  return Methods(info_dict=method_info_dict, constructor=constructor)


def merge_blocks(class_page_info: ClassPageInfo, ctor_info: MethodInfo):
  """Helper function to merge TitleBlock in constructor and class docstring."""

  # Get the class docstring. `.doc.docstring_parts` contain the entire
  # docstring except for the one-line docstring that's compulsory.
  class_doc = list(class_page_info.doc.docstring_parts)

  # If constructor doesn't exist, return the class docstring as it is.
  if ctor_info is None:
    return class_doc

  # Get the constructor's docstring parts.
  constructor_doc = ctor_info.doc.docstring_parts

  # If `Args`/`Arguments` and `Raises` already exist in the class docstring,
  # then record them and don't lift those sections from the constructor.
  existing_items_in_class = []
  for item in class_doc:
    if isinstance(item, parser.TitleBlock):
      title = item.title
      if title.startswith(('Args', 'Arguments')):
        title = 'Arg'
      existing_items_in_class.append(title)

  # Extract the `Arguments`/`Args` from the constructor's docstring.
  # A constructor won't contain `Args` and `Arguments` section at once.
  # It can contain either one of these so check for both.
  for block in constructor_doc:
    if isinstance(block, parser.TitleBlock):
      # If the block doesn't exist in class docstring, then lift the block.
      if (block.title.startswith(('Args', 'Arguments', 'Raises')) and
          not block.title.startswith(tuple(existing_items_in_class))):
        class_doc.append(block)
  return class_doc


def merge_class_and_constructor_docstring(
    class_page_info: ClassPageInfo,
    ctor_info: MethodInfo,
) -> List[str]:
  """Merges the class and the constructor docstrings.

  While merging, the following rules are followed:

  * Only `Arguments` and `Raises` blocks from constructor are uplifted to the
    class docstring. Rest of the stuff is ignored since it doesn't add much
    value and in some cases the information is repeated.

  * The `Raises` block is added to the end of the classes docstring.

  * The `Arguments` or `Args` block is inserted before the `Attributes` section.
    If `Attributes` section does not exist in the class docstring then add it
    to the end.

  * If the constructor does not exist on the class, then the class docstring
    is returned as it is.

  Args:
    class_page_info: Object containing information about the class.
    ctor_info: Object containing information about the constructor of the class.

  Returns:
    A list of strings containing the merged docstring.
  """

  def _create_class_doc(doc):
    updated_doc = []
    for item in doc:
      updated_doc.append(
          base_page.format_docstring(
              item, table_title_template='<h2 class="add-link">{title}</h2>'))
    return updated_doc

  class_doc = merge_blocks(class_page_info, ctor_info)

  return _create_class_doc(class_doc)


def _method_sort(method):
  """Create a sort-key tuple for a method based on its name."""
  # All private methods will be at the end of the list in an alphabetically
  # sorted order. All dunder methods will be above private methods and below
  # public methods. Public methods will be at the top in an alphabetically
  # sorted order.
  method_name = method.short_name
  if method_name.startswith('__'):
    return (1, method_name)
  if method_name.startswith('_'):
    return (2, method_name)
  return (-1, method_name)


def _build_method_section(method_info, heading_level=3):
  """Generates a markdown section for a method.

  Args:
    method_info: A `MethodInfo` object.
    heading_level: An Int, which HTML heading level to use.

  Returns:
    A markdown string.
  """
  parts = []
  heading = ('<h{heading_level} id="{short_name}">'
             '<code>{short_name}</code>'
             '</h{heading_level}>\n\n')
  parts.append(
      heading.format(heading_level=heading_level, **method_info._asdict()))

  if method_info.defined_in:
    parts.append(base_page.small_source_link(method_info.defined_in))

  if method_info.signature is not None:
    parts.append(
        base_page.build_signature(
            name=method_info.short_name,
            signature=method_info.signature,
            decorators=method_info.decorators))

  parts.append(method_info.doc.brief + '\n')

  parts.append(base_page.build_top_compat(method_info, h_level=4))

  for item in method_info.doc.docstring_parts:
    parts.append(
        base_page.format_docstring(
            item, table_title_template=None, anchors=False))

  parts.append(base_page.build_bottom_compat(method_info, h_level=4))

  parts.append('\n\n')
  return ''.join(parts)
