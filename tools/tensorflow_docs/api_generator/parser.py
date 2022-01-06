# Lint as: python3
# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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
"""Turn Python docstrings into Markdown for TensorFlow documentation."""

import collections
import dataclasses
import enum
import html
import inspect
import itertools
import os
import posixpath
import pprint
import re
import textwrap
import typing

from typing import Any, Dict, List, Tuple, Iterable, NamedTuple, Optional, Union

import astor

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator import signature as signature_lib

from google.protobuf.message import Message as ProtoMessage


@dataclasses.dataclass
class _FileLocation(object):
  """This class indicates that the object is defined in a regular file.

  This can be used for the `defined_in` slot of the `PageInfo` objects.
  """

  base_url: Optional[str] = None
  start_line: Optional[int] = None
  end_line: Optional[int] = None

  @property
  def url(self) -> Optional[str]:
    if self.start_line and self.end_line:
      if 'github.com' in self.base_url:
        return f'{self.base_url}#L{self.start_line}-L{self.end_line}'
    return self.base_url


def is_class_attr(full_name, index):
  """Check if the object's parent is a class.

  Args:
    full_name: The full name of the object, like `tf.module.symbol`.
    index: The {full_name:py_object} dictionary for the public API.

  Returns:
    True if the object is a class attribute.
  """
  parent_name = full_name.rsplit('.', 1)[0]
  if inspect.isclass(index[parent_name]):
    return True

  return False


def documentation_path(full_name, is_fragment=False):
  """Returns the file path for the documentation for the given API symbol.

  Given the fully qualified name of a library symbol, compute the path to which
  to write the documentation for that symbol (relative to a base directory).
  Documentation files are organized into directories that mirror the python
  module/class structure.

  Args:
    full_name: Fully qualified name of a library symbol.
    is_fragment: If `False` produce a page link (`tf.a.b.c` -->
      `tf/a/b/c.md`). If `True` produce fragment link, `tf.a.b.c` -->
      `tf/a/b.md#c`

  Returns:
    The file path to which to write the documentation for `full_name`.
  """
  parts = full_name.split('.')
  if is_fragment:
    parts, fragment = parts[:-1], parts[-1]

  result = posixpath.join(*parts) + '.md'

  if is_fragment:
    result = result + '#' + fragment

  return result


def _get_raw_docstring(py_object):
  """Get the docs for a given python object.

  Args:
    py_object: A python object to retrieve the docs for (class, function/method,
      or module).

  Returns:
    The docstring, or the empty string if no docstring was found.
  """

  if obj_type_lib.ObjType.get(py_object) is obj_type_lib.ObjType.TYPE_ALIAS:
    if inspect.getdoc(py_object) != inspect.getdoc(py_object.__origin__):
      result = inspect.getdoc(py_object)
    else:
      result = ''
  elif obj_type_lib.ObjType.get(py_object) is not obj_type_lib.ObjType.OTHER:
    result = inspect.getdoc(py_object) or ''
  else:
    result = ''

  if result is None:
    result = ''

  result = _StripTODOs()(result)
  result = _StripPylintAndPyformat()(result)
  result = _AddDoctestFences()(result + '\n')
  result = _DowngradeH1Keywords()(result)
  return result


class _AddDoctestFences(object):
  """Adds ``` fences around doctest caret blocks >>> that don't have them."""
  CARET_BLOCK_RE = re.compile(
      r"""
    \n                                     # After a blank line.
    (?P<indent>\ *)(?P<content>\>\>\>.*?)  # Whitespace and a triple caret.
    \n\s*?(?=\n|$)                         # Followed by a blank line""",
      re.VERBOSE | re.DOTALL)

  def _sub(self, match):
    groups = match.groupdict()
    fence = f"\n{groups['indent']}```\n"

    content = groups['indent'] + groups['content']
    return ''.join([fence, content, fence])

  def __call__(self, content):
    return self.CARET_BLOCK_RE.sub(self._sub, content)


class _StripTODOs(object):
  TODO_RE = re.compile('#? *TODO.*')

  def __call__(self, content: str) -> str:
    return self.TODO_RE.sub('', content)


class _StripPylintAndPyformat(object):
  STRIP_RE = re.compile('# *?(pylint|pyformat):.*', re.I)

  def __call__(self, content: str) -> str:
    return self.STRIP_RE.sub('', content)


class _DowngradeH1Keywords():
  """Convert keras docstring keyword format to google format."""

  KEYWORD_H1_RE = re.compile(
      r"""
    ^                 # Start of line
    (?P<indent>\s*)   # Capture leading whitespace as <indent
    \#\s*             # A literal "#" and more spaces
                      # Capture any of these keywords as <keyword>
    (?P<keyword>Args|Arguments|Returns|Raises|Yields|Examples?|Notes?)
    \s*:?             # Optional whitespace and optional ":"
    """, re.VERBOSE)

  def __call__(self, docstring):
    lines = docstring.splitlines()

    new_lines = []
    is_code = False
    for line in lines:
      if line.strip().startswith('```'):
        is_code = not is_code
      elif not is_code:
        line = self.KEYWORD_H1_RE.sub(r'\g<indent>\g<keyword>:', line)
      new_lines.append(line)

    docstring = '\n'.join(new_lines)
    return docstring


def _handle_compatibility(doc) -> Tuple[str, Dict[str, str]]:
  """Parse and remove compatibility blocks from the main docstring.

  Args:
    doc: The docstring that contains compatibility notes.

  Returns:
    A tuple of the modified doc string and a hash that maps from compatibility
    note type to the text of the note.
  """
  compatibility_notes = {}
  match_compatibility = re.compile(
      r'[ \t]*@compatibility\(([^\n]+?)\)\s*\n'
      r'(.*?)'
      r'[ \t]*@end_compatibility', re.DOTALL)
  for f in match_compatibility.finditer(doc):
    compatibility_notes[f.group(1)] = f.group(2)
  return match_compatibility.subn(r'', doc)[0], compatibility_notes


def _pairs(items):
  """Given an list of items [a,b,a,b...], generate pairs [(a,b),(a,b)...].

  Args:
    items: A list of items (length must be even)

  Returns:
    A list of pairs.
  """
  assert len(items) % 2 == 0
  return list(zip(items[::2], items[1::2]))


# Don't change the width="214px" without consulting with the devsite-team.
TABLE_TEMPLATE = textwrap.dedent("""
  <!-- Tabular view -->
   <table class="responsive fixed orange">
  <colgroup><col width="214px"><col></colgroup>
  <tr><th colspan="2">{title}</th></tr>
  {text}
  {items}
  </table>
  """)

ITEMS_TEMPLATE = textwrap.dedent("""\
  <tr>
  <td>
  {name}{anchor}
  </td>
  <td>
  {description}
  </td>
  </tr>""")

TEXT_TEMPLATE = textwrap.dedent("""\
  <tr class="alt">
  <td colspan="2">
  {text}
  </td>
  </tr>""")


@dataclasses.dataclass
class TitleBlock(object):
  """A class to parse title blocks (like `Args:`) and convert them to markdown.

  This handles the "Args/Returns/Raises" blocks and anything similar.

  These are used to extract metadata (argument descriptions, etc), and upgrade
  This `TitleBlock` to markdown.

  These blocks are delimited by indentation. There must be a blank line before
  the first `TitleBlock` in a series.

  The expected format is:

  ```
  Title:
    Freeform text
    arg1: value1
    arg2: value1
  ```

  These are represented as:

  ```
  TitleBlock(
    title = "Arguments",
    text = "Freeform text",
    items=[('arg1', 'value1'), ('arg2', 'value2')])
  ```

  The "text" and "items" fields may be empty. When both are empty the generated
  markdown only serves to upgrade the title to a <h4>.

  Attributes:
    title: The title line, without the colon.
    text: Freeform text. Anything between the `title`, and the `items`.
    items: A list of (name, value) string pairs. All items must have the same
      indentation.
  """

  _INDENTATION_REMOVAL_RE = re.compile(r'( *)(.+)')

  title: Optional[str]
  text: str
  items: Iterable[Tuple[str, str]]

  def _dedent_after_first_line(self, text):
    if '\n' not in text:
      return text

    first, remainder = text.split('\n', 1)
    remainder = textwrap.dedent(remainder)
    result = '\n'.join([first, remainder])
    return result

  def table_view(self, title_template: Optional[str] = None) -> str:
    """Returns a tabular markdown version of the TitleBlock.

    Tabular view is only for `Args`, `Returns`, `Raises` and `Attributes`. If
    anything else is encountered, redirect to list view.

    Args:
      title_template: Template for title detailing how to display it.

    Returns:
      Table containing the content to display.
    """

    if title_template is not None:
      title = title_template.format(title=self.title)
    else:
      title = self.title

    text = self.text.strip()
    if text:
      text = self._dedent_after_first_line(text)
      text = TEXT_TEMPLATE.format(text=text)

    items = []
    for name, description in self.items:
      if not description:
        description = ''
      else:
        description = description.strip('\n')
        description = self._dedent_after_first_line(description)
      item_table = ITEMS_TEMPLATE.format(
          name=f'`{name}`', anchor='', description=description)
      items.append(item_table)

    return '\n' + TABLE_TEMPLATE.format(
        title=title, text=text, items=''.join(items)) + '\n'

  def __str__(self) -> str:
    """Returns a non-tempated version of the TitleBlock."""

    sub = []
    sub.append(f'\n\n#### {self.title}:\n')
    sub.append(textwrap.dedent(self.text))
    sub.append('\n')

    for name, description in self.items:
      description = description.strip()
      if not description:
        sub.append(f'* <b>`{name}`</b>\n')
      else:
        sub.append(f'* <b>`{name}`</b>: {description}\n')

    return ''.join(sub)

  # This regex matches an entire title-block.
  BLOCK_RE = re.compile(
      r"""
      (?:^|^\n|\n\n)                  # After a blank line (non-capturing):
        (?P<title>[A-Z][\s\w]{0,20})  # Find a sentence case title, followed by
          \s*:\s*?(?=\n)              # whitespace, a colon and a new line.
      (?P<content>.*?)                # Then take everything until
        (?=\n\S|$)                    # look ahead finds a non-indented line
                                      # (a new-line followed by non-whitespace)
    """, re.VERBOSE | re.DOTALL)

  ITEM_RE = re.compile(
      r"""
      ^(\*?\*?'?"?     # Capture optional *s to allow *args, **kwargs and quotes
          \w[\w.'"]*?  # Capture a word character followed by word characters
                       # or "."s or ending quotes.
      )\s*:\s          # Allow any whitespace around the colon.""",
      re.MULTILINE | re.VERBOSE)

  @classmethod
  def split_string(cls, docstring: str):
    r"""Given a docstring split it into a list of `str` or `TitleBlock` chunks.

    For example the docstring of `tf.nn.relu`:

    '''
    Computes `max(features, 0)`.

    Args:
      features: A `Tensor`. Must be one of the following types: `float32`,
        `float64`, `int32`, `int64`, `uint8`, `int16`, `int8`, `uint16`, `half`.
      name: A name for the operation (optional).

    More freeform markdown text.
    '''

    This is parsed, and returned as:

    ```
    [
        "Computes rectified linear: `max(features, 0)`.",
        TitleBlock(
          title='Args',
          text='',
          items=[
            ('features', ' A `Tensor`. Must be...'),
            ('name', ' A name for the operation (optional).\n\n')]
        ),
        "More freeform markdown text."
    ]
    ```
    Args:
      docstring: The docstring to parse

    Returns:
      The docstring split into chunks. Each chunk produces valid markdown when
      `str` is called on it (each chunk is a python `str`, or a `TitleBlock`).
    """
    parts = []
    while docstring:
      split = re.split(cls.BLOCK_RE, docstring, maxsplit=1)
      # The first chunk in split is all text before the TitleBlock.
      before = split.pop(0)
      parts.append(before)

      # If `split` is empty, there were no other matches, and we're done.
      if not split:
        break

      # If there was a match,  split contains three items. The two capturing
      # groups in the RE, and the remainder.
      title, content, docstring = split

      # Now `content` contains the text and the name-value item pairs.
      # separate these two parts.
      content = textwrap.dedent(content)
      split = cls.ITEM_RE.split(content)
      text = split.pop(0)
      items = _pairs(split)

      title_block = cls(title=title, text=text, items=items)
      parts.append(title_block)

    return parts


class _DocstringInfo(typing.NamedTuple):
  brief: str
  docstring_parts: List[Union[TitleBlock, str]]
  compatibility: Dict[str, str]


def _get_other_member_doc(
    obj: Any,
    parser_config: config.ParserConfig,
    extra_docs: Optional[Dict[int, str]],
) -> str:
  """Returns the docs for other members of a module."""

  # An object's __doc__ attribute will mask the class'.
  my_doc = inspect.getdoc(obj)
  class_doc = inspect.getdoc(type(obj))

  description = None
  if my_doc != class_doc:
    # If they're different it's because __doc__ is set on the instance.
    if my_doc is not None:
      description = my_doc

  if description is None and extra_docs is not None:
    description = extra_docs.get(id(obj), None)

  info = None
  if isinstance(obj, dict):
    # pprint.pformat (next block) doesn't sort dicts until python 3.8
    items = [
        f' {name!r}: {value!r}'
        for name, value in sorted(obj.items(), key=repr)
    ]
    items = ',\n'.join(items)
    info = f'```\n{{\n{items}\n}}\n```'

  elif isinstance(obj, (set, frozenset)):
    # pprint.pformat (next block) doesn't sort dicts until python 3.8
    items = [f' {value!r}' for value in sorted(obj, key=repr)]
    items = ',\n'.join(items)
    info = f'```\n{{\n{items}\n}}\n```'
  elif (doc_generator_visitor.maybe_singleton(obj) or
        isinstance(obj, (list, tuple, enum.Enum))):
    # * Use pformat instead of repr so dicts and sets are sorted (deterministic)
    # * Escape ` so it doesn't break code formatting. You can't use "&#96;"
    #   here since it will diaplay as a literal. I'm not sure why <pre></pre>
    #   breaks on the site.
    info = pprint.pformat(obj).replace('`', r'\`')
    info = f'`{info}`'
  elif obj_type_lib.ObjType.get(obj) is obj_type_lib.ObjType.PROPERTY:
    info = None
  else:
    class_full_name = parser_config.reverse_index.get(id(type(obj)), None)
    if class_full_name is None:
      module = getattr(type(obj), '__module__', None)
      class_name = type(obj).__name__
      if module is None or module == 'builtins':
        class_full_name = class_name
      else:
        class_full_name = f'{module}.{class_name}'
    info = f'Instance of `{class_full_name}`'

  parts = [info, description]
  parts = [item for item in parts if item is not None]

  return '\n\n'.join(parts)


def _parse_md_docstring(
    py_object: Any,
    full_name: str,
    parser_config: config.ParserConfig,
    extra_docs: Optional[Dict[int, str]] = None,
) -> _DocstringInfo:
  """Parse the object's docstring and return a `_DocstringInfo`.

  This function clears @@'s from the docstring, and replaces `` references
  with links.

  Args:
    py_object: A python object to retrieve the docs for (class, function/method,
      or module).
    full_name: (optional) The api path to the current object, so replacements
      can depend on context.
    parser_config: An instance of `config.ParserConfig`.
    extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
      that need to be added to the markdown pages created.

  Returns:
    A _DocstringInfo object, all fields will be empty if no docstring was found.
  """

  if obj_type_lib.ObjType.get(py_object) is obj_type_lib.ObjType.OTHER:
    raw_docstring = _get_other_member_doc(
        obj=py_object, parser_config=parser_config, extra_docs=extra_docs)
  else:
    raw_docstring = _get_raw_docstring(py_object)

  raw_docstring = parser_config.reference_resolver.replace_references(
      raw_docstring, full_name)

  atat_re = re.compile(r' *@@[a-zA-Z_.0-9]+ *$')
  raw_docstring = '\n'.join(
      line for line in raw_docstring.split('\n') if not atat_re.match(line))

  docstring, compatibility = _handle_compatibility(raw_docstring)

  if 'Generated by: tensorflow/tools/api/generator' in docstring:
    docstring = ''

  # Remove the first-line "brief" docstring.
  lines = docstring.split('\n')
  brief = lines.pop(0)

  docstring = '\n'.join(lines)

  docstring_parts = TitleBlock.split_string(docstring)

  return _DocstringInfo(brief, docstring_parts, compatibility)


def _get_defining_class(py_class, name):
  for cls in inspect.getmro(py_class):
    if name in cls.__dict__:
      return cls
  return None


class MemberInfo(NamedTuple):
  """Describes an attribute of a class or module."""
  short_name: str
  full_name: str
  py_object: Any
  doc: _DocstringInfo
  url: str


class MethodInfo(NamedTuple):
  """Described a method."""
  short_name: str
  full_name: str
  py_object: Any
  doc: _DocstringInfo
  url: str
  signature: signature_lib.SignatureComponents
  decorators: List[str]
  defined_in: Optional[_FileLocation]

  @classmethod
  def from_member_info(cls, method_info: MemberInfo,
                       signature: signature_lib.SignatureComponents,
                       decorators: List[str],
                       defined_in: Optional[_FileLocation]):
    """Upgrades a `MemberInfo` to a `MethodInfo`."""
    return cls(
        **method_info._asdict(),
        signature=signature,
        decorators=decorators,
        defined_in=defined_in)


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
  """

  def __init__(
      self,
      full_name: str,
      py_object: Any,
      extra_docs: Optional[Dict[int, str]] = None,
  ):
    """Initialize a PageInfo.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
        that need to be added to the markdown pages created.
    """
    self.full_name = full_name
    self.py_object = py_object
    self._extra_docs = extra_docs

    self._defined_in = None
    self._aliases = None
    self._doc = None

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
  def doc(self) -> _DocstringInfo:
    """Returns a `_DocstringInfo` created from the object's docstring."""
    return self._doc

  def set_doc(self, doc: _DocstringInfo):
    """Sets the `doc` field.

    Args:
      doc: An instance of `_DocstringInfo`.
    """
    assert self.doc is None
    self._doc = doc


class FunctionPageInfo(PageInfo):
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
        self.full_name,
    )
    self._decorators = signature_lib.extract_decorators(self.py_object)

  @property
  def decorators(self):
    return list(self._decorators)

  def add_decorator(self, dec):
    self._decorators.append(dec)

  def get_metadata_html(self):
    return Metadata(self.full_name).build_html()


class TypeAliasPageInfo(PageInfo):
  """Collects docs For a type alias page.

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

  def __init__(self, *, full_name: str, py_object: Any, **kwargs) -> None:
    """Initialize a `TypeAliasPageInfo`.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """

    super().__init__(full_name, py_object, **kwargs)
    self._signature = None

  @property
  def signature(self):
    return self._signature

  def _custom_join(self, args: List[str], origin: str) -> str:
    """Custom join for Callable and other type hints.

    Args:
      args: Args of a type annotation object returned by `__args__`.
      origin: Origin of a type annotation object returned by `__origin__`.

    Returns:
      A joined string containing the right representation of a type annotation.
    """
    if 'Callable' in origin:
      if args[0] == '...':
        return ', '.join(args)
      else:
        return f"[{', '.join(args[:-1])}], {args[-1]}"

    return ', '.join(args)

  def _link_type_args(self, obj: Any, reverse_index: Dict[int, str],
                      linker: signature_lib.FormatArguments) -> str:
    """Recurses into typehint object and links known objects to their pages."""
    arg_full_name = reverse_index.get(id(obj), None)
    if arg_full_name is not None:
      return linker.get_link(arg_full_name)

    result = []
    if getattr(obj, '__args__', None):
      for arg in obj.__args__:
        result.append(self._link_type_args(arg, reverse_index, linker))
      origin_str = typing._type_repr(obj.__origin__)  # pylint: disable=protected-access # pytype: disable=module-attr
      result = self._custom_join(result, origin_str)
      return f'{origin_str}[{result}]'
    else:
      return typing._type_repr(obj)  # pylint: disable=protected-access # pytype: disable=module-attr

  def collect_docs(self, parser_config) -> None:
    """Collect all information necessary to genertate the function page.

    Mainly this is details about the function signature.

    For the type alias signature, the args are extracted and replaced with the
    full_name if the object is present in `parser_config.reverse_index`. They
    are also linkified to point to that symbol's page.

    For example (If generating docs for symbols in TF library):

    ```
    X = Union[int, str, bool, tf.Tensor, np.ndarray]
    ```

    In this case `tf.Tensor` will get linked to that symbol's page.
    Note: In the signature `tf.Tensor` is an object, so it will show up as
    `tensorflow.python.framework.ops.Tensor`. That's why we need to query
    `parser_config.reverse_index` to get the full_name of the object which will
    be `tf.Tensor`. Hence the signature will be:

    ```
    X = Union[int, str, bool, <a href="URL">tf.Tensor</a>, np.ndarray]
    ```

    Args:
      parser_config: The config.ParserConfig for the module being documented.
    """
    assert self.signature is None

    linker = signature_lib.FormatArguments(
        type_annotations={},
        parser_config=parser_config,
        func_full_name=self.full_name)

    sig_args = []
    if self.py_object.__origin__:
      for arg_obj in self.py_object.__args__:
        sig_args.append(
            self._link_type_args(arg_obj, parser_config.reverse_index, linker))

    sig_args_str = textwrap.indent(',\n'.join(sig_args), '    ')
    if self.py_object.__origin__:
      sig = f'{self.py_object.__origin__}[\n{sig_args_str}\n]'
    else:
      sig = repr(self.py_object)

    # pytype: enable=module-attr

    # Starting in Python 3.7, the __origin__ attribute of typing constructs
    # contains the equivalent runtime class rather than the construct itself
    # (e.g., typing.Callable.__origin__ is collections.abc.Callable).
    self._signature = sig.replace('typing.', '').replace('collections.abc.', '')

  def get_metadata_html(self) -> str:
    return Metadata(self.full_name).build_html()


class ClassPageInfo(PageInfo):
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
    bases: A list of `MemberInfo` objects pointing to the docs for the parent
      classes.
    methods: A list of `MethodInfo` objects documenting the class' methods.
    classes: A list of `MemberInfo` objects pointing to docs for any nested
      classes.
    other_members: A list of `MemberInfo` objects documenting any other object's
      defined inside the class object (mostly enum style fields).
    attr_block: A `TitleBlock` containing information about the Attributes of
      the class.
    inheritable_header: A header that may be placed on a base-class.
  """

  def __init__(self, *, full_name, py_object, **kwargs):
    """Initialize a ClassPageInfo.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """
    super().__init__(full_name, py_object, **kwargs)

    self._namedtuplefields = collections.OrderedDict()
    if issubclass(py_object, tuple):
      namedtuple_attrs = ('_asdict', '_fields', '_make', '_replace')
      if all(hasattr(py_object, attr) for attr in namedtuple_attrs):
        for name in py_object._fields:
          self._namedtuplefields[name] = None

    self._properties = collections.OrderedDict()
    self._bases = None
    self._methods = []
    self._classes = []
    self._other_members = []
    self.attr_block = None

  @property
  def bases(self):
    """Returns a list of `MemberInfo` objects pointing to the class' parents."""
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

  def _set_bases(self, parser_config):
    """Builds the `bases` attribute, to document this class' parent-classes.

    This method sets the `bases` to a list of `MemberInfo` objects point to the
    doc pages for the class' parents.

    Args:
      parser_config: An instance of `config.ParserConfig`.
    """
    bases = []
    for base in self.py_object.__mro__[1:]:
      base_full_name = parser_config.reverse_index.get(id(base), None)
      if base_full_name is None:
        continue
      base_doc = _parse_md_docstring(base, self.full_name, parser_config,
                                     self._extra_docs)
      base_url = parser_config.reference_resolver.reference_to_url(
          base_full_name)

      link_info = MemberInfo(
          short_name=base_full_name.split('.')[-1],
          full_name=base_full_name,
          py_object=base,
          doc=base_doc,
          url=base_url)
      bases.append(link_info)

    self._bases = bases

  def _add_property(self, member_info: MemberInfo):
    """Adds an entry to the `properties` list.

    Args:
      member_info: a `MemberInfo` describing the property.
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
        if not isinstance(part, TitleBlock)
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
      member_info: MemberInfo,
      defining_class: Optional[type],  # pylint: disable=g-bare-generic
      parser_config: config.ParserConfig) -> None:
    """Adds a `MethodInfo` entry to the `methods` list.

    Args:
      member_info: a `MemberInfo` describing the method.
      defining_class: The `type` object where this method is defined.
      parser_config: A `config.ParserConfig`.
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

    # If the curent class py_object is a dataclass then use the class object
    # instead of the __init__ method object because __init__ is a
    # generated method on dataclasses (unless the definition used init=False)
    # and `inspect.getsource` doesn't work on generated methods (as the source
    # file doesn't exist) which is required for signature generation.
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
        py_obj, parser_config, member_info.full_name, func_type=func_type)

    decorators = signature_lib.extract_decorators(member_info.py_object)

    defined_in = _get_defined_in(member_info.py_object, parser_config)

    method_info = MethodInfo.from_member_info(member_info, signature,
                                              decorators, defined_in)
    self._methods.append(method_info)

  @property
  def classes(self):
    """Returns a list of `MemberInfo` pointing to any nested classes."""
    return sorted(self._classes, key=lambda x: x.short_name)

  def get_metadata_html(self) -> str:
    meta_data = Metadata(self.full_name)
    for item in itertools.chain(self.classes, self.methods, self.other_members):
      meta_data.append(item)

    return meta_data.build_html()

  def _add_class(self, member_info):
    """Adds a `MemberInfo` for a nested class to `classes` list.

    Args:
      member_info: a `MemberInfo` describing the class.
    """
    self._classes.append(member_info)

  @property
  def other_members(self):
    """Returns a list of `MemberInfo` describing any other contents."""
    return self._other_members

  def _add_other_member(self, member_info: MemberInfo):
    """Adds an `MemberInfo` entry to the `other_members` list.

    Args:
      member_info: a `MemberInfo` describing the object.
    """
    self._other_members.append(member_info)

  def _add_member(
      self,
      member_info: MemberInfo,
      defining_class: Optional[type],  # pylint: disable=g-bare-generic
      parser_config: config.ParserConfig,
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
      self._add_method(member_info, defining_class, parser_config)
    elif obj_type is obj_type_lib.ObjType.OTHER:
      # Exclude members defined by protobuf that are useless
      if issubclass(self.py_object, ProtoMessage):
        if (member_info.short_name.endswith('_FIELD_NUMBER') or
            member_info.short_name in ['__slots__', 'DESCRIPTOR']):
          return

      self._add_other_member(member_info)

  def collect_docs(self, parser_config):
    """Collects information necessary specifically for a class's doc page.

    Mainly, this is details about the class's members.

    Args:
      parser_config: An instance of config.ParserConfig.
    """
    py_class = self.py_object

    self._set_bases(parser_config)

    for child_short_name in parser_config.tree[self.full_name]:
      child_full_name = '.'.join([self.full_name, child_short_name])
      child = parser_config.py_name_to_object(child_full_name)

      # Don't document anything that is defined in object or by protobuf.
      defining_class = _get_defining_class(py_class, child_short_name)
      if defining_class in [object, type, tuple, BaseException, Exception]:
        continue

      # The following condition excludes most protobuf-defined symbols.
      if (defining_class and
          defining_class.__name__ in ['CMessage', 'Message', 'MessageMeta']):
        continue

      if doc_controls.should_skip_class_attr(py_class, child_short_name):
        continue

      child_doc = _parse_md_docstring(child, self.full_name, parser_config,
                                      self._extra_docs)

      child_url = parser_config.reference_resolver.reference_to_url(
          child_full_name)

      member_info = MemberInfo(child_short_name, child_full_name, child,
                               child_doc, child_url)
      self._add_member(member_info, defining_class, parser_config)

    self.set_attr_block(self._augment_attributes(self.doc.docstring_parts))

  def _augment_attributes(self,
                          docstring_parts: List[Any]) -> Optional[TitleBlock]:
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
      if isinstance(part, TitleBlock) and part.title.startswith('Attr'):
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
      attribute_block = TitleBlock(
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


class ModulePageInfo(PageInfo):
  """Collects docs for a module page.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    classes: A list of `MemberInfo` objects pointing to docs for the classes in
      this module.
    functions: A list of `MemberInfo` objects pointing to docs for the functions
      in this module
    modules: A list of `MemberInfo` objects pointing to docs for the modules in
      this module.
    type_alias: A list of `MemberInfo` objects pointing to docs for the type
      aliases in this module.
    other_members: A list of `MemberInfo` objects documenting any other object's
      defined on the module object (mostly enum style fields).
  """

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

  def _add_module(self, member_info: MemberInfo):
    self._modules.append(member_info)

  def _add_class(self, member_info: MemberInfo):
    self._classes.append(member_info)

  def _add_function(self, member_info: MemberInfo):
    self._functions.append(member_info)

  def _add_type_alias(self, member_info: MemberInfo):
    self._type_alias.append(member_info)

  def _add_other_member(self, member_info: MemberInfo):
    self._other_members.append(member_info)

  def get_metadata_html(self):
    meta_data = Metadata(self.full_name)

    # Objects with their own pages are not added to the metadata list for the
    # module, the module only has a link to the object page. No docs.
    for item in self.other_members:
      meta_data.append(item)

    return meta_data.build_html()

  def _add_member(self, member_info: MemberInfo) -> None:
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

      member_doc = _parse_md_docstring(member, self.full_name, parser_config,
                                       self._extra_docs)

      url = parser_config.reference_resolver.reference_to_url(member_full_name)

      member_info = MemberInfo(member_short_name, member_full_name, member,
                               member_doc, url)
      self._add_member(member_info)


def docs_for_object(
    full_name: str,
    py_object: Any,
    parser_config: config.ParserConfig,
    extra_docs: Optional[Dict[int, str]] = None,
) -> PageInfo:
  """Return a PageInfo object describing a given object from the TF API.

  This function uses _parse_md_docstring to parse the docs pertaining to
  `object`.

  This function resolves '`tf.symbol`' references in the docstrings into links
  to the appropriate location. It also adds a list of alternative names for the
  symbol automatically.

  It assumes that the docs for each object live in a file given by
  `documentation_path`, and that relative links to files within the
  documentation are resolvable.

  Args:
    full_name: The fully qualified name of the symbol to be documented.
    py_object: The Python object to be documented. Its documentation is sourced
      from `py_object`'s docstring.
    parser_config: A config.ParserConfig object.
    extra_docs: Extra docs for symbols like public constants(list, tuple, etc)
      that need to be added to the markdown pages created.

  Returns:
    Either a `FunctionPageInfo`, `ClassPageInfo`, or a `ModulePageInfo`
    depending on the type of the python object being documented.

  Raises:
    RuntimeError: If an object is encountered for which we don't know how
      to make docs.
  """

  # Which other aliases exist for the object referenced by full_name?
  main_name = parser_config.reference_resolver.py_main_name(full_name)
  duplicate_names = parser_config.duplicates.get(main_name, [])
  if main_name in duplicate_names:
    duplicate_names.remove(main_name)

  obj_type = obj_type_lib.ObjType.get(py_object)
  if obj_type is obj_type_lib.ObjType.CLASS:
    page_info = ClassPageInfo(
        full_name=main_name, py_object=py_object, extra_docs=extra_docs)
  elif obj_type is obj_type_lib.ObjType.CALLABLE:
    page_info = FunctionPageInfo(
        full_name=main_name, py_object=py_object, extra_docs=extra_docs)
  elif obj_type is obj_type_lib.ObjType.MODULE:
    page_info = ModulePageInfo(
        full_name=main_name, py_object=py_object, extra_docs=extra_docs)
  elif obj_type is obj_type_lib.ObjType.TYPE_ALIAS:
    page_info = TypeAliasPageInfo(
        full_name=main_name, py_object=py_object, extra_docs=extra_docs)
  else:
    raise RuntimeError('Cannot make docs for object {full_name}: {py_object!r}')

  relative_path = os.path.relpath(
      path='.', start=os.path.dirname(documentation_path(full_name)) or '.')
  # Convert from OS-specific path to URL/POSIX path.
  relative_path = posixpath.join(*relative_path.split(os.path.sep))

  with parser_config.reference_resolver.temp_prefix(relative_path):
    page_info.set_doc(
        _parse_md_docstring(
            py_object,
            full_name,
            parser_config,
            extra_docs,
        ))

    page_info.collect_docs(parser_config)

    page_info.set_aliases(duplicate_names)

    page_info.set_defined_in(_get_defined_in(py_object, parser_config))

  return page_info


def _unwrap_obj(obj):
  while True:
    unwrapped_obj = getattr(obj, '__wrapped__', None)
    if unwrapped_obj is None:
      break
    obj = unwrapped_obj
  return obj


def _get_defined_in(
    py_object: Any,
    parser_config: config.ParserConfig) -> Optional[_FileLocation]:
  """Returns a description of where the passed in python object was defined.

  Args:
    py_object: The Python object.
    parser_config: A config.ParserConfig object.

  Returns:
    A `_FileLocation`
  """
  # Every page gets a note about where this object is defined
  base_dirs_and_prefixes = zip(parser_config.base_dir,
                               parser_config.code_url_prefix)
  try:
    obj_path = inspect.getfile(_unwrap_obj(py_object))
  except TypeError:  # getfile throws TypeError if py_object is a builtin.
    return None

  if not obj_path.endswith(('.py', '.pyc')):
    return None

  code_url_prefix = None
  for base_dir, temp_prefix in base_dirs_and_prefixes:
    rel_path = os.path.relpath(path=obj_path, start=base_dir)
    # A leading ".." indicates that the file is not inside `base_dir`, and
    # the search should continue.
    if rel_path.startswith('..'):
      continue
    else:
      code_url_prefix = temp_prefix
      # rel_path is currently a platform-specific path, so we need to convert
      # it to a posix path (for lack of a URL path).
      rel_path = posixpath.join(*rel_path.split(os.path.sep))
      break

  # No link if the file was not found in a `base_dir`, or the prefix is None.
  if code_url_prefix is None:
    return None

  try:
    lines, start_line = inspect.getsourcelines(py_object)
    end_line = start_line + len(lines) - 1
    if 'MACHINE GENERATED' in lines[0]:
      # don't link to files generated by tf_export
      return None
  except (IOError, TypeError, IndexError):
    start_line = None
    end_line = None

  # In case this is compiled, point to the original
  if rel_path.endswith('.pyc'):
    # If a PY3 __pycache__/ subdir is being used, omit it.
    rel_path = rel_path.replace('__pycache__' + os.sep, '')
    # Strip everything after the first . so that variants such as .pyc and
    # .cpython-3x.pyc or similar are all handled.
    rel_path = rel_path.partition('.')[0] + '.py'

  if re.search(r'<[\w\s]+>', rel_path):
    # Built-ins emit paths like <embedded stdlib>, <string>, etc.
    return None
  if '<attrs generated' in rel_path:
    return None

  if re.match(r'.*/gen_[^/]*\.py$', rel_path):
    return _FileLocation()
  if 'genfiles' in rel_path:
    return _FileLocation()
  elif re.match(r'.*_pb2\.py$', rel_path):
    # The _pb2.py files all appear right next to their defining .proto file.
    rel_path = rel_path[:-7] + '.proto'
    return _FileLocation(base_url=posixpath.join(code_url_prefix, rel_path))
  else:
    return _FileLocation(
        base_url=posixpath.join(code_url_prefix, rel_path),
        start_line=start_line,
        end_line=end_line)


# TODO(markdaoust): This should just parse, pretty_docs should generate the md.
def generate_global_index(library_name, index, reference_resolver):
  """Given a dict of full names to python objects, generate an index page.

  The index page generated contains a list of links for all symbols in `index`
  that have their own documentation page.

  Args:
    library_name: The name for the documented library to use in the title.
    index: A dict mapping full names to python objects.
    reference_resolver: An instance of ReferenceResolver.

  Returns:
    A string containing an index page as Markdown.
  """
  symbol_links = []
  for full_name, py_object in index.items():
    obj_type = obj_type_lib.ObjType.get(py_object)
    if obj_type in (obj_type_lib.ObjType.OTHER, obj_type_lib.ObjType.PROPERTY):
      continue
    # In Python 3, unbound methods are functions, so eliminate those.
    if obj_type is obj_type_lib.ObjType.CALLABLE:
      if is_class_attr(full_name, index):
        continue
    with reference_resolver.temp_prefix('..'):
      symbol_links.append(
          (full_name, reference_resolver.python_link(full_name, full_name)))

  lines = [f'# All symbols in {library_name}', '']
  lines.append('<!-- Insert buttons and diff -->\n')

  # Sort all the symbols once, so that the ordering is preserved when its broken
  # up into main symbols and compat symbols and sorting the sublists is not
  # required.
  symbol_links = sorted(symbol_links, key=lambda x: x[0])

  compat_v1_symbol_links = []
  compat_v2_symbol_links = []
  primary_symbol_links = []

  for symbol, link in symbol_links:
    if symbol.startswith('tf.compat.v1'):
      if 'raw_ops' not in symbol:
        compat_v1_symbol_links.append(link)
    elif symbol.startswith('tf.compat.v2'):
      compat_v2_symbol_links.append(link)
    else:
      primary_symbol_links.append(link)

  lines.append('## Primary symbols')
  for link in primary_symbol_links:
    lines.append(f'*  {link}')

  if compat_v2_symbol_links:
    lines.append('\n## Compat v2 symbols\n')
    for link in compat_v2_symbol_links:
      lines.append(f'*  {link}')

  if compat_v1_symbol_links:
    lines.append('\n## Compat v1 symbols\n')
    for link in compat_v1_symbol_links:
      lines.append(f'*  {link}')

  # TODO(markdaoust): use a _ModulePageInfo -> prety_docs.build_md_page()
  return '\n'.join(lines)


class Metadata(object):
  """A class for building a page's Metadata block.

  Attributes:
    name: The name of the page being described by the Metadata block.
    version: The source version.
  """

  def __init__(self, name, version=None, content=None):
    """Creates a Metadata builder.

    Args:
      name: The name of the page being described by the Metadata block.
      version: The source version.
      content: Content to create the metadata from.
    """

    self.name = name

    self.version = version
    if self.version is None:
      self.version = 'Stable'

    self._content = content
    if self._content is None:
      self._content = []

  def append(self, item):
    """Adds an item from the page to the Metadata block.

    Args:
      item: The parsed page section to add.
    """
    self._content.append(item.short_name)

  def build_html(self):
    """Returns the Metadata block as an Html string."""
    # Note: A schema is not a URL. It is defined with http: but doesn't resolve.
    schema = 'http://developers.google.com/ReferenceObject'
    parts = [f'<div itemscope itemtype="{schema}">']

    parts.append(f'<meta itemprop="name" content="{self.name}" />')
    parts.append(f'<meta itemprop="path" content="{self.version}" />')
    for item in self._content:
      parts.append(f'<meta itemprop="property" content="{item}"/>')

    parts.extend(['</div>', ''])

    return '\n'.join(parts)
