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
"""Base classes for page construction."""
import abc
import os
import pathlib
import posixpath
import textwrap
from typing import Any, ClassVar, Dict, List, NamedTuple, Optional, Sequence, Tuple, Type

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import signature as signature_lib

import jinja2


class PageBuilder(abc.ABC):

  def __init__(self, page_info):
    self.page_info = page_info

  @abc.abstractmethod
  def build(self) -> str:
    pass


class TemplatePageBuilder(PageBuilder):
  """A Page builder implemented on a jinja template."""

  TEMPLATE = 'templates/page.jinja'
  TEMPLATE_SEARCH_PATH = tuple([str(pathlib.Path(__file__).parent)])
  JINJA_ENV = jinja2.Environment(
      trim_blocks=True,
      lstrip_blocks=True,
      loader=jinja2.FileSystemLoader(TEMPLATE_SEARCH_PATH))

  def build(self) -> str:
    template = self.JINJA_ENV.get_template(self.TEMPLATE)
    content = template.render(builder=self, page_info=self.page_info)
    return content

  def top_source_link(self):
    return top_source_link(self.page_info.defined_in)

  def build_collapsable_aliases(self):
    return build_collapsable_aliases(sorted(self.page_info.aliases))

  def top_compat(self):
    return build_top_compat(self.page_info, h_level=2)

  def bottom_compat(self):
    return build_bottom_compat(self.page_info, h_level=2)

  def format_docstring_part(self, part):
    return str(part)

  def get_devsite_headers(self):
    """Returns the list of header lines for this page."""
    hidden = doc_controls.should_hide_from_search(self.page_info.py_object)
    brief_no_backticks = self.page_info.doc.brief.replace('`', '').strip()
    headers = []
    if brief_no_backticks:
      headers.append(f'description: {brief_no_backticks}')

    if self.page_info.search_hints and not hidden:
      if headers:
        headers.append('')
      headers.append(self.page_info.get_metadata_html())
    else:
      headers.append('robots: noindex')
      headers.append('')

    result = '\n'.join(headers)
    return result


class PageInfo:
  """Base-class for api_pages objects.

  Converted to markdown by pretty_docs.py.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    search_hints: If true include metadata search hints, else include a
      "robots: noindex"
    text: The resulting page text.
    page_text: The cached result.
  """
  DEFAULT_BUILDER_CLASS: ClassVar[Type[PageBuilder]] = TemplatePageBuilder

  def __init__(
      self,
      api_node,
      extra_docs: Optional[Dict[int, str]] = None,
      search_hints: bool = True,
      parser_config=None,
  ):
    """Initialize a PageInfo.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
        that need to be added to the markdown pages created.
      search_hints: If true include metadata search hints, else include a
        "robots: noindex"

    """
    self.api_node = api_node
    self.full_name = api_node.full_name
    self.py_object = api_node.py_object
    self._extra_docs = extra_docs
    self.search_hints = search_hints
    self.parser_config = parser_config

    self._defined_in = None
    self._aliases = None
    self._doc = None
    self._page_text = None

  def collect_docs(self):
    """Collects additional information from the `config.ParserConfig`."""
    pass

  def docs_for_object(self):
    relative_path = os.path.relpath(
        path='.',
        start=os.path.dirname(parser.documentation_path(self.full_name)) or '.')

    # Convert from OS-specific path to URL/POSIX path.
    relative_path = posixpath.join(*relative_path.split(os.path.sep))

    with self.parser_config.reference_resolver.temp_prefix(relative_path):
      self.set_doc(
          parser.parse_md_docstring(
              self.py_object,
              self.full_name,
              self.parser_config,
              self._extra_docs,
          ))

      self.collect_docs()

      aliases = ['.'.join(alias) for alias in self.api_node.aliases]
      if self.full_name in aliases:
        aliases.remove(self.full_name)
      self.set_aliases(aliases)

      self.set_defined_in(
          parser.get_defined_in(self.py_object, self.parser_config))

      self._page_text = self.build()

    return self._page_text

  def build(self) -> str:
    """Builds the documentation."""
    cls = self.DEFAULT_BUILDER_CLASS
    return cls(self).build()

  @property
  def page_text(self):
    if self._page_text is None:
      self._page_text = self.build()
    return self._page_text

  def __eq__(self, other):
    if isinstance(other, PageInfo):
      return self.__dict__ == other.__dict__
    else:
      return NotImplemented

  @property
  def short_name(self):
    """Returns the documented object's short name."""
    return self.full_name.split('.')[-1]

  @property
  def defined_in(self):
    """Returns the path to the file where the documented object is defined."""
    return self._defined_in

  def set_defined_in(self, defined_in):
    """Sets the `defined_in` path."""
    assert self.defined_in is None
    self._defined_in = defined_in

  @property
  def self_link(self):
    if not self.parser_config.self_link_base:
      return None
    rel_path = parser.documentation_path(self.full_name)
    rel_path = rel_path[: -1 * len('.md')]  # strip suffix
    return f'{self.parser_config.self_link_base}/{rel_path}'

  @property
  def aliases(self):
    """Returns a list of all full names for the documented object."""
    return self._aliases

  def set_aliases(self, aliases):
    """Sets the `aliases` list.

    Args:
      aliases: A list of strings. Containing all the object's full names.
    """
    assert self.aliases is None
    self._aliases = aliases

  @property
  def doc(self) -> parser.DocstringInfo:
    """Returns a `parser.DocstringInfo` created from the object's docstring."""
    return self._doc

  def set_doc(self, doc: parser.DocstringInfo):
    """Sets the `doc` field.

    Args:
      doc: An instance of `parser.DocstringInfo`.
    """
    assert self.doc is None
    self._doc = doc


class MemberInfo(NamedTuple):
  """Describes an attribute of a class or module."""
  short_name: str
  full_name: str
  py_object: Any
  doc: parser.DocstringInfo
  url: str


_ALWAYS_TABLE_ITEMS = ('arg', 'return', 'raise', 'attr', 'yield')


def format_docstring(item,
                     *,
                     table_title_template: Optional[str] = None,
                     anchors: bool = True) -> str:
  """Formats a docstring part into a string.

  Args:
    item: A TitleBlock instance or a normal string.
    table_title_template: Template for title detailing how to display it in the
      table.

  Returns:
    A formatted docstring.
  """

  if isinstance(item, parser.TitleBlock):
    if (item.items or  # A colon-list like under args
        item.text.strip() or  # An indented block
        item.title.lower().startswith(_ALWAYS_TABLE_ITEMS)):
      return item.table_view(
          title_template=table_title_template, anchors=anchors)
    else:
      return str(item)
  else:
    return str(item)


def build_other_members(other_members: List[MemberInfo], title: str):
  """Returns "other_members" rendered to markdown.

  `other_members` is used for anything that is not a class, function, module,
  or method.

  Args:
    other_members: A list of `base_page.MemberInfo` objects.
    title: Title of the table.

  Returns:
    A markdown string
  """

  items = []

  for other_member in other_members:
    description = [other_member.doc.brief]
    for doc_part in other_member.doc.docstring_parts:
      if isinstance(doc_part, parser.TitleBlock):
        # Use list_view here because description will be part of a table.
        description.append(str(doc_part))
      else:
        description.append(doc_part)

    items.append(
        parser.ITEMS_TEMPLATE.format(
            name=other_member.short_name,
            anchor=f'<a id="{other_member.short_name}"></a>',
            description='\n'.join(description),
        ))
  return '\n' + parser.TABLE_TEMPLATE.format(
      title=title, text='', items=''.join(items))


DECORATOR_ALLOWLIST = frozenset({
    'classmethod',
    'staticmethod',
    'tf_contextlib.contextmanager',
    'contextlib.contextmanager',
    'tf.function',
    'types.method',
    'abc.abstractmethod',
})


def build_signature(name: str,
                    signature: signature_lib.TfSignature,
                    decorators: Optional[Sequence[str]],
                    type_alias: bool = False) -> str:
  """Returns a markdown code block containing the function signature.

  Wraps the signature and limits it to 80 characters.

  Args:
    name: the name to put in the template.
    signature: the signature object.
    decorators: a list of decorators to apply.
    type_alias: If True, uses an `=` instead of `()` for the signature.
      For example: `TensorLike = (Union[str, tf.Tensor, int])`. Defaults to
        `False`.

  Returns:
    The signature of the object.
  """
  if name == 'tf.range':
    # Special case tf.range, since it has an optional first argument
    return textwrap.dedent("""
      ```python
      tf.range(limit, delta=1, dtype=None, name='range')
      tf.range(start, limit, delta=1, dtype=None, name='range')
      ```
      """)

  full_signature = str(signature)

  parts = [
      '<pre class="devsite-click-to-copy prettyprint lang-py ' +
      'tfo-signature-link">'
  ]

  if decorators:
    parts.extend([
        f'<code>@{dec}</code>' for dec in decorators
        if dec in DECORATOR_ALLOWLIST
    ])

  if type_alias:
    parts.append(f'<code>{name} = {full_signature}')
  else:
    parts.append(f'<code>{name}{full_signature}')
  parts.append('</code></pre>\n\n')

  return '\n'.join(parts)


def _split_compat_top_bottom(page_info) -> Tuple[Optional[str], Dict[str, str]]:
  """Split the compatibility dict between the top and bottom sections."""
  compat: Dict[str, str] = page_info.doc.compatibility
  top_compat = None

  if ('compat.v1' in page_info.full_name or 'estimator' in page_info.full_name):
    bottom_compat = {}
    for key, value in compat.items():
      if key == 'TF2':
        top_compat = value
      else:
        bottom_compat[key] = value
  else:
    bottom_compat = compat

  return top_compat, bottom_compat


_TOP_COMPAT_TEMPLATE = """

 <section><devsite-expandable expanded>
 <h{h_level} class="showalways">Migrate to TF2</h{h_level}>

Caution: This API was designed for TensorFlow v1.
Continue reading for details on how to migrate from this API to a native
TensorFlow v2 equivalent. See the
[TensorFlow v1 to TensorFlow v2 migration guide](https://www.tensorflow.org/guide/migrate)
for instructions on how to migrate the rest of your code.

{value}

 </aside></devsite-expandable></section>

<h{h_level}>Description</h{h_level}>

"""


def build_top_compat(page_info: PageInfo, h_level: int) -> str:
  """Add the top section compatibility blocks."""
  compat, _ = _split_compat_top_bottom(page_info)
  if compat:
    value = textwrap.dedent(compat)
    return _TOP_COMPAT_TEMPLATE.format(value=value, h_level=h_level)
  else:
    return ''


_BOTTOM_COMPAT_TEMPLATE = """

 <section><devsite-expandable {expanded}>
 <h{h_level} class="showalways">{title}</h{h_level}>

{value}

 </devsite-expandable></section>

"""


def build_bottom_compat(page_info: PageInfo, h_level: int) -> str:
  """Add the bottom section compatibility blocks."""
  _, compat = _split_compat_top_bottom(page_info)

  def _tf2_key_tuple(key):
    # False sorts before True.
    return (key == 'TF2', key)

  parts = []
  for key in sorted(compat, key=_tf2_key_tuple):
    value = textwrap.dedent(compat[key])
    if key == 'TF2':
      expanded = ''
      title = 'Migrate to TF2'
    else:
      expanded = 'expanded'
      title = key + ' compatibility'
    parts.append(
        _BOTTOM_COMPAT_TEMPLATE.format(
            title=title, value=value, h_level=h_level, expanded=expanded))

  return ''.join(parts)


TABLE_HEADER = (
    '<table class="tfo-notebook-buttons tfo-api nocontent" align="left">')

_TABLE_TEMPLATE = textwrap.dedent("""
    {table_header}
    {table_content}
    </table>

    {table_footer}""")

_TABLE_LINK_TEMPLATE = textwrap.dedent("""\
    <td>
      <a target="_blank" href="{url}">
        <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
        View source on GitHub
      </a>
    </td>""")


def top_source_link(location):
  """Returns a source link with Github image, like the notebook butons."""

  table_content = ''
  table_footer = ''

  if location and location.url:
    if 'github.com' not in location.url:
      table_footer = small_source_link(location)
    else:
      table_content = _TABLE_LINK_TEMPLATE.format(url=location.url)

  table = _TABLE_TEMPLATE.format(
      table_header=TABLE_HEADER,
      table_content=table_content,
      table_footer=table_footer)

  return table


def small_source_link(location, text='View source'):
  """Returns a small source link."""
  if location.url:
    return ('<a target="_blank" class="external" '
            f'href="{location.url}">{text}</a>\n\n')
  else:
    return ''


def build_collapsable_aliases(aliases: List[str]) -> str:
  """Returns the top "Aliases" line."""

  def join_aliases(aliases: List[str]) -> str:
    return ', '.join('`{}`'.format(name) for name in aliases)

  collapsable_template = textwrap.dedent("""\
    <section class="expandable">
      <h4 class="showalways">View aliases</h4>
      <p>{content}</p>
    </section>
    """)

  main_alias_template = textwrap.dedent("""
    <b>Main aliases</b>
    <p>{content}</p>
    """)

  compat_alias_template = textwrap.dedent("""
    <b>Compat aliases for migration</b>
    <p>See
    <a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
    more details.</p>
    <p>{content}</p>
    """)

  main_aliases = []
  compat_aliases = []

  for alias in aliases:
    if '__' in alias:
      continue
    elif 'compat.v' in alias:
      compat_aliases.append(alias)
    else:
      main_aliases.append(alias)

  alias_content = ''
  if main_aliases:
    alias_content += main_alias_template.format(
        content=join_aliases(main_aliases))
  if compat_aliases:
    alias_content += compat_alias_template.format(
        content=join_aliases(compat_aliases))

  if alias_content:
    return collapsable_template.format(content=alias_content) + '\n'

  return alias_content
