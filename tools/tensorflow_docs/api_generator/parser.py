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
import ast
import collections
import itertools
import json
import os
import re
import textwrap

from typing import Any, Dict, List, Tuple, Iterable, NamedTuple, Optional

from absl import logging

import astor

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import tf_inspect

from google.protobuf.message import Message as ProtoMessage


def is_free_function(py_object, full_name, index):
  """Check if input is a free function (and not a class- or static method).

  Args:
    py_object: The object in question.
    full_name: The full name of the object, like `tf.module.symbol`.
    index: The {full_name:py_object} dictionary for the public API.

  Returns:
    True if the object is a stand-alone function, and not part of a class
    definition.
  """
  if tf_inspect.isclass(py_object):
    return False

  if not callable(py_object):
    return False

  parent_name = full_name.rsplit('.', 1)[0]
  if tf_inspect.isclass(index[parent_name]):
    return False

  return True


# A regular expression capturing a python identifier.
IDENTIFIER_RE = r'[a-zA-Z_]\w*'


class TFDocsError(Exception):
  pass


def documentation_path(full_name, is_fragment=False):
  """Returns the file path for the documentation for the given API symbol.

  Given the fully qualified name of a library symbol, compute the path to which
  to write the documentation for that symbol (relative to a base directory).
  Documentation files are organized into directories that mirror the python
  module/class structure.

  Args:
    full_name: Fully qualified name of a library symbol.
    is_fragment: If `False` produce a direct markdown link (`tf.a.b.c` -->
      `tf/a/b/c.md`). If `True` produce fragment link, `tf.a.b.c` -->
      `tf/a/b.md#c`

  Returns:
    The file path to which to write the documentation for `full_name`.
  """
  parts = full_name.split('.')
  if is_fragment:
    parts, fragment = parts[:-1], parts[-1]

  result = os.path.join(*parts) + '.md'

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
  # For object instances, inspect.getdoc does give us the docstring of their
  # type, which is not what we want. Only return the docstring if it is useful.
  if (tf_inspect.isclass(py_object) or tf_inspect.ismethod(py_object) or
      tf_inspect.isfunction(py_object) or tf_inspect.ismodule(py_object) or
      isinstance(py_object, property)):
    result = tf_inspect.getdoc(py_object) or ''
  else:
    result = ''

  return _AddDoctestFences()(result + '\n')


class _AddDoctestFences(object):
  """Adds ``` fences around doctest caret blocks >>> that don't have them."""
  CARET_BLOCK_RE = re.compile(
      r"""
    (?<=\n)\ *\n                           # After a blank line.
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


class IgnoreLineInBlock(object):
  """Ignores the lines in a block.

  Attributes:
    block_start: Contains the start string of a block to ignore.
    block_end: Contains the end string of a block to ignore.
  """

  def __init__(self, block_start, block_end):
    self._block_start = block_start
    self._block_end = block_end
    self._in_block = False

    self._start_end_regex = re.escape(self._block_start) + r'.*?' + re.escape(
        self._block_end)

  def __call__(self, line):
    # If start and end block are on the same line, return True.
    if re.match(self._start_end_regex, line):
      return True

    if not self._in_block:
      if self._block_start in line:
        self._in_block = True

    elif self._block_end in line:
      self._in_block = False
      # True is being returned here because the last line in the block should
      # also be ignored.
      return True

    return self._in_block


# ?P<...> helps to find the match by entering the group name instead of the
# index. For example, instead of doing match.group(1) we can do
# match.group('brackets')
AUTO_REFERENCE_RE = re.compile(
    r"""
    (?P<brackets>\[.*?\])                    # find characters inside '[]'
    |
    `(?P<backticks>[\w\(\[\)\]\{\}.,=\s]+?)` # or find characters inside '``'
    """,
    flags=re.VERBOSE)


class ReferenceResolver(object):
  """Class for replacing `tf.symbol` references with Markdown links."""

  def __init__(self, duplicate_of, is_fragment, py_module_names):
    """Initializes a Reference Resolver.

    Args:
      duplicate_of: A map from duplicate names to preferred names of API
        symbols.
      is_fragment: A map from full names to bool for each symbol. If True the
        object lives at a page fragment `tf.a.b.c` --> `tf/a/b#c`. If False
        object has a page to itself: `tf.a.b.c` --> `tf/a/b/c`.
      py_module_names: A list of string names of Python modules.
    """
    self._duplicate_of = duplicate_of
    self._is_fragment = is_fragment
    self._all_names = set(is_fragment.keys())
    self._py_module_names = py_module_names
    self._partial_symbols_dict = self._create_partial_symbols_dict()

  @classmethod
  def from_visitor(cls, visitor, **kwargs):
    """A factory function for building a ReferenceResolver from a visitor.

    Args:
      visitor: an instance of `DocGeneratorVisitor`
      **kwargs: all remaining args are passed to the constructor

    Returns:
      an instance of `ReferenceResolver` ()
    """
    is_fragment = {}
    for name, obj in visitor.index.items():
      has_page = (
          tf_inspect.isclass(obj) or tf_inspect.ismodule(obj) or
          is_free_function(obj, name, visitor.index))

      is_fragment[name] = not has_page

    return cls(
        duplicate_of=visitor.duplicate_of, is_fragment=is_fragment, **kwargs)

  @classmethod
  def from_json_file(cls, filepath):
    """Initialize the reference resolver via _api_cache.json."""
    with open(filepath) as f:
      json_dict = json.load(f)

    return cls(**json_dict)

  def _partial_symbols(self, symbol):
    """Finds the partial symbols given the true symbol.

    For example, symbol: `tf.keras.layers.Conv2D`, then the partial dictionary
    returned will be:

    partials = ["tf.keras.layers.Conv2D","keras.layers.Conv2D","layers.Conv2D"]

    There should at least be one '.' in the partial symbol generated so as to
    avoid guessing for the true symbol.

    Args:
      symbol: String, representing the true symbol.

    Returns:
      A list of partial symbol names
    """

    split_symbol = symbol.split('.')
    partials = [
        '.'.join(split_symbol[i:]) for i in range(1,
                                                  len(split_symbol) - 1)
    ]
    return partials

  def _create_partial_symbols_dict(self):
    """Creates a partial symbols dictionary for all the symbols in TensorFlow.

    Returns:
      A dictionary mapping {partial_symbol: real_symbol}
    """
    partial_symbols_dict = collections.defaultdict(list)

    for name in sorted(self._all_names):
      if 'tf.compat.v' in name or 'tf.contrib' in name:
        continue
      partials = self._partial_symbols(name)
      for partial in partials:
        partial_symbols_dict[partial].append(name)

    new_partial_dict = {}
    for partial, full_names in partial_symbols_dict.items():
      if not full_names:
        continue

      full_names = [
          self._duplicate_of.get(full_name, full_name)
          for full_name in full_names
      ]

      new_partial_dict[partial] = full_names[0]

    return new_partial_dict

  def to_json_file(self, filepath):
    """Converts the RefenceResolver to json and writes it to the specified file.

    Args:
      filepath: The file path to write the json to.
    """

    try:
      os.makedirs(os.path.dirname(filepath))
    except OSError:
      pass

    json_dict = {}
    for key, value in self.__dict__.items():
      # Drop these fields, they are generated by the constructor.
      if key == '_all_names' or key == '_partial_symbols_dict':
        continue

      # Strip off any leading underscores on field names as these are not
      # recognized by the constructor.
      json_dict[key.lstrip('_')] = value

    with open(filepath, 'w') as f:
      json.dump(json_dict, f, indent=2, sort_keys=True)
      f.write('\n')

  def replace_references(self, string, relative_path_to_root, full_name=None):
    """Replace `tf.symbol` references with links to symbol's documentation page.

    This function finds all occurrences of "`tf.symbol`" in `string`
    and replaces them with markdown links to the documentation page
    for "symbol".

    `relative_path_to_root` is the relative path from the document
    that contains the "`tf.symbol`" reference to the root of the API
    documentation that is linked to. If the containing page is part of
    the same API docset, `relative_path_to_root` can be set to
    `os.path.dirname(documentation_path(name))`, where `name` is the
    python name of the object whose documentation page the reference
    lives on.

    Args:
      string: A string in which "`tf.symbol`" references should be replaced.
      relative_path_to_root: The relative path from the containing document to
        the root of the API documentation that is being linked to.
      full_name: (optional) The full name of current object, so replacements can
        depend on context.

    Returns:
      `string`, with "`tf.symbol`" references replaced by Markdown links.
    """

    def one_ref(match):
      return self._one_ref(match, relative_path_to_root, full_name)

    fixed_lines = []

    filters = [
        IgnoreLineInBlock('<pre class="tfo-notebook-code-cell-output">',
                          '{% endhtmlescape %}</pre>'),
        IgnoreLineInBlock('```', '```')
    ]

    for line in string.splitlines():
      if not any(filter_block(line) for filter_block in filters):
        line = re.sub(AUTO_REFERENCE_RE, one_ref, line)
      fixed_lines.append(line)

    return '\n'.join(fixed_lines)

  def python_link(self,
                  link_text,
                  ref_full_name,
                  relative_path_to_root,
                  code_ref=True):
    """Resolve a "`tf.symbol`" reference to a Markdown link.

    This will pick the canonical location for duplicate symbols.  The
    input to this function should already be stripped of the '@' and
    '{}'.  This function returns a Markdown link. If `code_ref` is
    true, it is assumed that this is a code reference, so the link
    text will be rendered as code (using backticks).
    `link_text` should refer to a library symbol, starting with 'tf.'.

    Args:
      link_text: The text of the Markdown link.
      ref_full_name: The fully qualified name of the symbol to link to.
      relative_path_to_root: The relative path from the location of the current
        document to the root of the API documentation.
      code_ref: If true (the default), put `link_text` in `...`.

    Returns:
      A markdown link to the documentation page of `ref_full_name`.
    """
    url = self.reference_to_url(ref_full_name, relative_path_to_root)

    if code_ref:
      link_text = link_text.join(['<code>', '</code>'])
    else:
      link_text = self._link_text_to_html(link_text)

    return f'<a href="{url}">{link_text}</a>'

  @staticmethod
  def _link_text_to_html(link_text):
    code_re = '`(.*?)`'
    return re.sub(code_re, r'<code>\1</code>', link_text)

  def py_master_name(self, full_name):
    """Return the master name for a Python symbol name."""
    return self._duplicate_of.get(full_name, full_name)

  def reference_to_url(self, ref_full_name, relative_path_to_root):
    """Resolve a "`tf.symbol`" reference to a relative path.

    The input to this function should already be stripped of the '@'
    and '{}', and its output is only the link, not the full Markdown.

    If `ref_full_name` is the name of a class member, method, or property, the
    link will point to the page of the containing class, and it will include the
    method name as an anchor. For example, `tf.module.MyClass.my_method` will be
    translated into a link to
    `os.join.path(relative_path_to_root, 'tf/module/MyClass.md#my_method')`.

    Args:
      ref_full_name: The fully qualified name of the symbol to link to.
      relative_path_to_root: The relative path from the location of the current
        document to the root of the API documentation.

    Returns:
      A relative path that links from the documentation page of `from_full_name`
      to the documentation page of `ref_full_name`.

    Raises:
      TFDocsError: If the symbol is not found.
    """
    if self._is_fragment.get(ref_full_name, False):
      # methods and constants get duplicated. And that's okay.
      # Use the master name of their parent.
      parent_name, short_name = ref_full_name.rsplit('.', 1)
      parent_master_name = self._duplicate_of.get(parent_name, parent_name)
      master_name = '.'.join([parent_master_name, short_name])
    else:
      master_name = self._duplicate_of.get(ref_full_name, ref_full_name)

    # Check whether this link exists
    if master_name not in self._all_names:
      raise TFDocsError(f'Cannot make link to {master_name!r}: Not in index.')

    ref_path = documentation_path(master_name, self._is_fragment[master_name])
    return os.path.join(relative_path_to_root, ref_path)

  def _one_ref(self, match, relative_path_to_root, full_name=None):
    """Return a link for a single "`tf.symbol`" reference."""

    if match.group(1):
      # Found a '[]' group, return it unmodified.
      return match.group('brackets')

    # Found a '``' group.
    string = match.group('backticks')

    link_text = string

    string = re.sub(r'(.*)[\(\[].*', r'\1', string)

    if string.startswith('compat.v1') or string.startswith('compat.v2'):
      string = 'tf.' + string
    elif string.startswith('v1') or string.startswith('v2'):
      string = 'tf.compat.' + string

    elif full_name is None or ('tf.compat.v' not in full_name and
                               'tf.contrib' not in full_name):
      string = self._partial_symbols_dict.get(string, string)

    try:
      if string.startswith('tensorflow::'):
        # C++ symbol
        return self._cc_link(string, link_text, relative_path_to_root)

      is_python = False
      for py_module_name in self._py_module_names:
        if string == py_module_name or string.startswith(py_module_name + '.'):
          is_python = True
          break

      if is_python:  # Python symbol
        return self.python_link(
            link_text, string, relative_path_to_root, code_ref=True)
    except TFDocsError:
      pass

    return match.group(0)

  def _cc_link(self, string, link_text, relative_path_to_root):
    """Generate a link for a `tensorflow::...` reference."""
    # TODO(joshl): Fix this hard-coding of paths.
    if string == 'tensorflow::ClientSession':
      ret = 'class/tensorflow/client-session.md'
    elif string == 'tensorflow::Scope':
      ret = 'class/tensorflow/scope.md'
    elif string == 'tensorflow::Status':
      ret = 'class/tensorflow/status.md'
    elif string == 'tensorflow::Tensor':
      ret = 'class/tensorflow/tensor.md'
    elif string == 'tensorflow::ops::Const':
      ret = 'namespace/tensorflow/ops.md#const'
    else:
      raise TFDocsError(f'C++ reference not understood: "{string}"')

    # relative_path_to_root gets you to api_docs/python, we go from there
    # to api_docs/cc, and then add ret.
    cc_relative_path = os.path.normpath(
        os.path.join(relative_path_to_root, '../cc', ret))

    return f'<a href="{cc_relative_path}"><code>{link_text}</code></a>'


# TODO(aselle): Collect these into a big list for all modules and functions
# and make a rosetta stone page.
def _handle_compatibility(doc):
  """Parse and remove compatibility blocks from the main docstring.

  Args:
    doc: The docstring that contains compatibility notes"

  Returns:
    a tuple of the modified doc string and a hash that maps from compatibility
    note type to the text of the note.
  """
  compatibility_notes = {}
  match_compatibility = re.compile(r'[ \t]*@compatibility\((\w+)\)\s*\n'
                                   r'((?:[^@\n]*\n)+)'
                                   r'\s*@end_compatibility')
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
  WHITESPACE_RE = re.compile(r'[ \n]+')

  def __init__(self, title: str, text: str, items: Iterable[Tuple[str, str]]):
    self.title = title
    self.text = text
    self.items = items

  def __str__(self) -> str:
    """Returns a markdown compatible version of the TitleBlock."""
    sub = []
    sub.append('\n\n#### ' + self.title + ':\n')
    sub.append(textwrap.dedent(self.text))
    sub.append('\n')
    for name, description in self.items:
      # Skip description if it's just whitespace
      if self.WHITESPACE_RE.fullmatch(str(description)):
        # Don't include the description if it's just whitespace.
        sub.append(f'* <b>`{name}`</b>\n')
      else:
        sub.append(f'* <b>`{name}`</b>: {description}')

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

  # This
  ITEM_RE = re.compile(
      r"""
      ^(\*?\*?          # Capture optional *s to allow *args, **kwargs.
          \w[\w.]*?     # Capture a word character followed by word characters
                        # or "."s.
      )\s*:\s           # Allow any whitespace around the colon.""",
      re.MULTILINE | re.VERBOSE)

  @classmethod
  def split_string(cls, docstring):
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

      title_block = cls(title, text, items)
      parts.append(title_block)

    return parts


_DocstringInfo = collections.namedtuple(
    '_DocstringInfo', ['brief', 'docstring_parts', 'compatibility'])


def _parse_md_docstring(py_object, relative_path_to_root, full_name,
                        reference_resolver):
  """Parse the object's docstring and return a `_DocstringInfo`.

  This function clears @@'s from the docstring, and replaces `` references
  with markdown links.

  For links within the same set of docs, the `relative_path_to_root` for a
  docstring on the page for `full_name` can be set to:

  ```python
  relative_path_to_root = os.path.relpath(
    path='.', start=os.path.dirname(documentation_path(full_name)) or '.')
  ```

  Args:
    py_object: A python object to retrieve the docs for (class, function/method,
      or module).
    relative_path_to_root: The relative path from the location of the current
      document to the root of the Python API documentation. This is used to
      compute links for "`tf.symbol`" references.
    full_name: (optional) The api path to the current object, so replacements
      can depend on context.
    reference_resolver: An instance of ReferenceResolver.

  Returns:
    A _DocstringInfo object, all fields will be empty if no docstring was found.
  """
  # TODO(wicke): If this is a partial, use the .func docstring and add a note.
  raw_docstring = _get_raw_docstring(py_object)

  raw_docstring = reference_resolver.replace_references(raw_docstring,
                                                        relative_path_to_root,
                                                        full_name)

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


class TypeAnnotationExtractor(ast.NodeVisitor):
  """Extracts the type annotations by parsing the AST of a function."""

  def __init__(self):
    self.annotation_dict = {}
    self.arguments_typehint_exists = False
    self.return_typehint_exists = False

  def visit_FunctionDef(self, node):  # pylint: disable=invalid-name
    """Visits the `FunctionDef` node in AST tree and extracts the typehints."""

    # Capture the return type annotation.
    if node.returns:
      self.annotation_dict['return'] = astor.to_source(
          node.returns).strip().replace('"""', '"')
      self.return_typehint_exists = True

    # Capture the args type annotation.
    for arg in node.args.args:
      if arg.annotation:
        self.annotation_dict[arg.arg] = astor.to_source(
            arg.annotation).strip().replace('"""', '"')
        self.arguments_typehint_exists = True

    # Capture the kwarg only args type annotation.
    for kwarg in node.args.kwonlyargs:
      if kwarg.annotation:
        self.annotation_dict[kwarg.arg] = astor.to_source(
            kwarg.annotation).strip().replace('"""', '"')
        self.arguments_typehint_exists = True


class FormatArguments(object):
  """Formats the arguments and adds type annotations if they exist."""

  _PAREN_NUMBER_RE = re.compile(r'^\(([0-9.e-]+)\)')
  _OBJECT_MEMORY_ADDRESS_RE = re.compile(r'<(?P<type>.+) object at 0x[\da-f]+>')

  def __init__(
      self,
      func_ast: Any,
      default_value_of_all_kwargs: Dict[str, Any],
      type_annotations: Dict[str, str],
      reverse_index: Dict[Any, str],
  ) -> None:
    self._func_ast = func_ast
    self._default_value_of_all_kwargs = default_value_of_all_kwargs
    self._type_annotations = type_annotations
    self._reverse_index = reverse_index

  def format_args(self, args: List[str]) -> List[str]:
    """Creates a text representation of the args in a method/function.

    Args:
      args: List of args to format.

    Returns:
      Formatted args with type annotations if they exist.
    """

    args_text_representation = []

    for arg in args:
      if arg in self._type_annotations:
        args_text_representation.append(f'{arg}: {self._type_annotations[arg]}')
      else:
        args_text_representation.append(f'{arg}')

    return args_text_representation

  def format_kwargs(self, kwargs: List[str]) -> List[str]:
    """Creates a text representation of the kwargs in a method/function.

    Args:
      kwargs: List of kwargs to format.

    Returns:
      Formatted kwargs with type annotations if they exist.
    """

    kwargs_text_representation = []

    ast_defaults = [None] * len(kwargs)
    if self._func_ast is not None:
      ast_args = self._func_ast.body[0].args  # pytype: disable=attribute-error
      ast_defaults = ast_args.defaults + ast_args.kw_defaults
      if len(ast_defaults) != len(kwargs):
        ast_defaults = [None] * len(kwargs)

    for kwarg, ast_default in zip(kwargs, ast_defaults):
      default_val_exists = kwarg in self._default_value_of_all_kwargs
      default_val = self._default_value_of_all_kwargs.get(kwarg, None)

      if id(default_val) in self._reverse_index:
        default_text = self._reverse_index[id(default_val)]
      elif ast_default is not None:
        default_text = (
            astor.to_source(ast_default).rstrip('\n').replace(
                '\t', '\\t').replace('\n', '\\n').replace('"""', "'"))
        default_text = self._PAREN_NUMBER_RE.sub('\\1', default_text)

        if default_text != repr(default_val):
          # This may be an internal name. If so, handle the ones we know about.
          internal_names = {
              'ops.GraphKeys': 'tf.GraphKeys',
              '_ops.GraphKeys': 'tf.GraphKeys',
              'init_ops.zeros_initializer': 'tf.zeros_initializer',
              'init_ops.ones_initializer': 'tf.ones_initializer',
              'saver_pb2.SaverDef': 'tf.train.SaverDef',
          }
          full_name_re = f'^{IDENTIFIER_RE}(.{IDENTIFIER_RE})+'
          match = re.match(full_name_re, default_text)
          if match:
            lookup_text = default_text
            for internal_name, public_name in internal_names.items():
              if match.group(0).startswith(internal_name):
                lookup_text = public_name + default_text[len(internal_name):]
                break
            if default_text is lookup_text:
              logging.warn(
                  'WARNING: Using default arg, failed lookup: '
                  '%s, repr: %r', default_text, repr(default_val))
            else:
              default_text = lookup_text
      # This is a kwarg without any default value. Add it to the list as an arg
      # and continue.
      elif not default_val_exists:
        kwargs_text_representation.extend(self.format_args([kwarg]))
        continue
      else:
        default_text = repr(default_val)
        # argspec.defaults can contain object memory addresses, i.e.
        # containers.MutableMapping.pop. Strip these out to avoid
        # unnecessary doc churn between invocations.
        default_text = self._OBJECT_MEMORY_ADDRESS_RE.sub(
            r'<\g<type>>', default_text)

      if kwarg in self._type_annotations:
        kwargs_text_representation.append(
            f'{kwarg}: {self._type_annotations[kwarg]} = {default_text}')
      else:
        kwargs_text_representation.append(f'{kwarg}={default_text}')

    return kwargs_text_representation


class _SignatureComponents(NamedTuple):
  """Contains the components that make up the signature of a function/method."""

  arguments: List[str]
  arguments_typehint_exists: bool
  return_typehint_exists: bool
  return_type: Optional[str] = None

  def __str__(self):
    arguments_signature = ''
    if self.arguments:
      str_signature = ',\n'.join(self.arguments)
      # If there is no type annotation on arguments, then wrap the entire
      # signature to width 80.
      if not self.arguments_typehint_exists:
        str_signature = textwrap.fill(str_signature, width=80)
      arguments_signature = '\n' + textwrap.indent(
          str_signature, prefix='    ') + '\n'

    full_signature = f'({arguments_signature})'
    if self.return_typehint_exists:
      full_signature += f' -> {self.return_type}'

    return full_signature


def _generate_signature(func: Any,
                        reverse_index: Dict[int, str]) -> _SignatureComponents:
  """Given a function, returns a list of strings representing its args.

  This function uses `__name__` for callables if it is available. This can lead
  to poor results for functools.partial and other callable objects.

  The returned string is Python code, so if it is included in a Markdown
  document, it should be typeset as code (using backticks), or escaped.

  Args:
    func: A function, method, or functools.partial to extract the signature for.
    reverse_index: A map from object ids to canonical full names to use.

  Returns:
    A `_SignatureComponents` NamedTuple.
  """

  all_args_list = []
  only_args = []
  kwargs_with_defaults = []
  default_value_of_all_kwargs = {}

  #############################################################################
  # The following conditions are handled below in code.
  # In Py3, there can be kwargs only arguments without any default value.
  # This is the syntax for kwargs with defaults:
  # ```
  # def temp(a, b=False, *, c, d=True, e):
  #  return True
  # ```
  # In the above function, `c`, `d` and `e` are kwargs only arguments.
  # In `inspect.getfullargspec`,
  #   * `kwonlyargs` and `kwonlydefaults` are used for `c`, `d` and `e`.
  #   * `argspec.defaults` is used for `b`'s default values which is False.
  #   * `b` and `a` are in `argspec.args`.
  #############################################################################

  # If the py_object doesn't have `_tf_decorator` as an attribute, then the
  # original py_object will be returned.
  argspec = tf_inspect.getfullargspec(func)
  arguments = argspec.args
  visitor = TypeAnnotationExtractor()

  try:
    func_source = textwrap.dedent(tf_inspect.getsource(func))
    func_ast = ast.parse(func_source)
    # Extract the type annotation from the parsed ast.
    visitor.visit(func_ast)
  except Exception:  # pylint: disable=broad-except
    # A wide-variety of errors can be thrown here.
    func_ast = None

  type_annotations = visitor.annotation_dict
  arguments_typehint_exists = visitor.arguments_typehint_exists
  return_typehint_exists = visitor.return_typehint_exists

  #############################################################################
  # Process the information about the func.
  #############################################################################

  # Remove `self` from the signature of a method.
  if 'self' in arguments:
    arguments = arguments[1:]
  # Assign arguments as the default value to only_args
  only_args = arguments

  # This `if` condition, deals with the `a` and `b` args from the example above.
  if argspec.defaults is not None:
    kd_length = len(argspec.defaults)
    only_args = arguments[:-kd_length]
    kwargs_with_defaults = arguments[-kd_length:]
    # update the default values for kwargs_with_defaults.
    for kwarg, val in zip(kwargs_with_defaults, argspec.defaults):
      default_value_of_all_kwargs[kwarg] = val

  # This deals with adding the default values for `c`, `d` and `e` in the
  # example above.
  if argspec.kwonlydefaults is not None:
    default_value_of_all_kwargs.update(argspec.kwonlydefaults)

  #############################################################################
  # Build the text representation of Args and Kwargs.
  #############################################################################

  formatter = FormatArguments(func_ast, default_value_of_all_kwargs,
                              type_annotations, reverse_index)

  # Only add the Args. Kwargs are added below.
  if only_args:
    all_args_list.extend(formatter.format_args(only_args))

  # Add the kwargs with defaults (`b`) in the example above.
  if kwargs_with_defaults:
    all_args_list.extend(formatter.format_kwargs(kwargs_with_defaults))

  # Add the compulsory kwargs (`c, `d, `e`) in the example above.
  # Also, add `*` since that's the syntax for compulsory kwargs in Py3.
  if argspec.kwonlyargs:
    if argspec.varargs:
      all_args_list.append('*' + argspec.varargs)
    else:
      all_args_list.append('*')

    all_args_list.extend(formatter.format_kwargs(argspec.kwonlyargs))

  # Add *args and *kwargs.
  if argspec.varargs and not argspec.kwonlyargs:
    all_args_list.append('*' + argspec.varargs)
  if argspec.varkw:
    all_args_list.append('**' + argspec.varkw)

  return _SignatureComponents(
      arguments=all_args_list,
      arguments_typehint_exists=arguments_typehint_exists,
      return_typehint_exists=return_typehint_exists,
      return_type=type_annotations.get('return', None))


def _get_defining_class(py_class, name):
  for cls in tf_inspect.getmro(py_class):
    if name in cls.__dict__:
      return cls
  return None


class _LinkInfo(
    collections.namedtuple('_LinkInfo',
                           ['short_name', 'full_name', 'obj', 'doc', 'url'])):

  __slots__ = []

  def is_link(self):
    return True


class _OtherMemberInfo(
    collections.namedtuple('_OtherMemberInfo',
                           ['short_name', 'full_name', 'obj', 'doc'])):

  __slots__ = []

  def is_link(self):
    return False


MethodInfo = collections.namedtuple('MethodInfo', [
    'short_name',
    'full_name',
    'obj',
    'doc',
    'signature',
    'decorators',
    'defined_in',
])


def extract_decorators(func: Any) -> List[str]:
  """Extracts the decorators on top of functions/methods.

  Args:
    func: The function to extract the decorators from.

  Returns:
    A List of decorators.
  """

  class ASTDecoratorExtractor(ast.NodeVisitor):

    def __init__(self):
      self.decorator_list = []

    def visit_FunctionDef(self, node):  # pylint: disable=invalid-name
      for dec in node.decorator_list:
        self.decorator_list.append(astor.to_source(dec).strip())

  visitor = ASTDecoratorExtractor()

  try:
    func_source = textwrap.dedent(tf_inspect.getsource(func))
    func_ast = ast.parse(func_source)
    visitor.visit(func_ast)
  except Exception:  # pylint: disable=broad-except
    # A wide-variety of errors can be thrown here.
    pass

  return visitor.decorator_list


class PageInfo(object):
  """Base-class for api_pages objects.

  Converted to markdown by pretty_docs.py.

  Attributes:
    full_name: The full, master name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object wqas defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
  """

  def __init__(self, full_name, py_object):
    """Initialize a PageInfo.

    Args:
      full_name: The full, master name, of the object being documented.
      py_object: The object being documented.
    """
    self.full_name = full_name
    self.py_object = py_object

    self._defined_in = None
    self._aliases = None
    self._doc = None

  @property
  def short_name(self):
    """Returns the documented object's short name."""
    return self._full_name.split('.')[-1]

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
  def doc(self):
    """Returns a `_DocstringInfo` created from the object's docstring."""
    return self._doc

  def set_doc(self, doc):
    """Sets the `doc` field.

    Args:
      doc: An instance of `_DocstringInfo`.
    """
    assert self.doc is None
    self._doc = doc


class FunctionPageInfo(PageInfo):
  """Collects docs For a function Page.

  Attributes:
    full_name: The full, master name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object wqas defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    signature: the parsed signature (see:_generate_signature)
    decorators: A list of decorator names.
  """

  def __init__(self, full_name, py_object):
    """Initialize a FunctionPageInfo.

    Args:
      full_name: The full, master name, of the object being documented.
      py_object: The object being documented.
    """
    super(FunctionPageInfo, self).__init__(full_name, py_object)

    self._signature = None
    self._decorators = []

  @property
  def signature(self):
    return self._signature

  def collect_docs(self, parser_config):
    """Collect all information necessary to genertate the function page.

    Mainly this is details about the function signature.

    Args:
      parser_config: The ParserConfig for the module being documented.
    """

    assert self.signature is None
    self._signature = _generate_signature(self.py_object,
                                          parser_config.reverse_index)
    self._decorators = extract_decorators(self.py_object)

  @property
  def decorators(self):
    return list(self._decorators)

  def add_decorator(self, dec):
    self._decorators.append(dec)

  def get_metadata_html(self):
    return Metadata(self.full_name).build_html()


class ClassPageInfo(PageInfo):
  """Collects docs for a class page.

  Attributes:
    full_name: The full, master name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object wqas defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    attributes: A dict mapping from "name" to a docstring
    bases: A list of `_LinkInfo` objects pointing to the docs for the parent
      classes.
    methods: A list of `MethodInfo` objects documenting the class' methods.
    classes: A list of `_LinkInfo` objects pointing to docs for any nested
      classes.
    other_members: A list of `_OtherMemberInfo` objects documenting any other
      object's defined inside the class object (mostly enum style fields).
  """

  def __init__(self, full_name, py_object):
    """Initialize a ClassPageInfo.

    Args:
      full_name: The full, master name, of the object being documented.
      py_object: The object being documented.
    """
    super(ClassPageInfo, self).__init__(full_name, py_object)

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

  @property
  def bases(self):
    """Returns a list of `_LinkInfo` objects pointing to the class' parents."""
    return self._bases

  def _set_bases(self, relative_path, parser_config):
    """Builds the `bases` attribute, to document this class' parent-classes.

    This method sets the `bases` to a list of `_LinkInfo` objects point to the
    doc pages for the class' parents.

    Args:
      relative_path: The relative path from the doc this object describes to the
        documentation root.
      parser_config: An instance of `ParserConfig`.
    """
    bases = []
    obj = parser_config.py_name_to_object(self.full_name)
    for base in obj.__bases__:
      base_full_name = parser_config.reverse_index.get(id(base), None)
      if base_full_name is None:
        continue
      base_doc = _parse_md_docstring(base, relative_path, self.full_name,
                                     parser_config.reference_resolver)
      base_url = parser_config.reference_resolver.reference_to_url(
          base_full_name, relative_path)

      link_info = _LinkInfo(
          short_name=base_full_name.split('.')[-1],
          full_name=base_full_name,
          obj=base,
          doc=base_doc,
          url=base_url)
      bases.append(link_info)

    self._bases = bases

  def _add_property(self, name: str, obj: property, doc: _DocstringInfo):
    """Adds an entry to the `properties` list.

    Args:
      name: The property's name.
      obj: The property object.
      doc: The property's parsed docstring, a `_DocstringInfo`.
    """
    del obj

    # Hide useless namedtuple docs-trings.
    if re.match('Alias for field number [0-9]+', doc.brief):
      doc = doc._replace(docstring_parts=[], brief='')

    new_parts = [doc.brief]
    # Strip args/returns/raises from property
    new_parts.extend([
        str(part)
        for part in doc.docstring_parts
        if not isinstance(part, TitleBlock)
    ])
    new_parts = [textwrap.indent(part, '  ') for part in new_parts]
    new_parts.append('')
    desc = '\n'.join(new_parts)

    if name in self._namedtuplefields:
      self._namedtuplefields[name] = desc
    else:
      self._properties[name] = desc

  @property
  def methods(self):
    """Returns a list of `MethodInfo` describing the class' methods."""
    return self._methods

  def _add_method(self, short_name, full_name, obj, doc, signature, decorators,
                  defined_in):
    """Adds a `MethodInfo` entry to the `methods` list.

    Args:
      short_name: The method's short name.
      full_name: The method's fully qualified name.
      obj: The method object itself
      doc: The method's parsed docstring, a `_DocstringInfo`
      signature: The method's parsed signature (see: `_generate_signature`)
      decorators: A list of strings describing the decorators that should be
        mentioned on the object's docs page.
      defined_in: A `_FileLocation` object pointing to the object source.
    """
    method_info = MethodInfo(short_name, full_name, obj, doc, signature,
                             decorators, defined_in)
    self._methods.append(method_info)

  @property
  def classes(self):
    """Returns a list of `_LinkInfo` pointing to any nested classes."""
    return self._classes

  def get_metadata_html(self) -> str:
    meta_data = Metadata(self.full_name)
    for item in itertools.chain(self.classes, self.methods, self.other_members):
      meta_data.append(item)

    return meta_data.build_html()

  def _add_class(self, short_name, full_name, obj, doc, url):
    """Adds a `_LinkInfo` for a nested class to `classes` list.

    Args:
      short_name: The class' short name.
      full_name: The class' fully qualified name.
      obj: The class object itself
      doc: The class' parsed docstring, a `_DocstringInfo`
      url: A url pointing to where the nested class is documented.
    """
    page_info = _LinkInfo(short_name, full_name, obj, doc, url)

    self._classes.append(page_info)

  @property
  def other_members(self):
    """Returns a list of `_OtherMemberInfo` describing any other contents."""
    return self._other_members

  def _add_other_member(self, short_name, full_name, obj, doc):
    """Adds an `_OtherMemberInfo` entry to the `other_members` list.

    Args:
      short_name: The class' short name.
      full_name: The class' fully qualified name.
      obj: The object
      doc: The object's docstring, a `_DocstringInfo`
    """
    other_member_info = _OtherMemberInfo(short_name, full_name, obj, doc)
    self._other_members.append(other_member_info)

  def collect_docs(self, parser_config):
    """Collects information necessary specifically for a class's doc page.

    Mainly, this is details about the class's members.

    Args:
      parser_config: An instance of ParserConfig.
    """
    py_class = self.py_object
    doc_path = documentation_path(self.full_name)
    relative_path = os.path.relpath(
        path='.', start=os.path.dirname(doc_path) or '.')

    self._set_bases(relative_path, parser_config)

    for short_name in parser_config.tree[self.full_name]:
      child_name = '.'.join([self.full_name, short_name])
      child = parser_config.py_name_to_object(child_name)

      # Don't document anything that is defined in object or by protobuf.
      defining_class = _get_defining_class(py_class, short_name)
      if defining_class in [object, type, tuple, BaseException, Exception]:
        continue

      # The following condition excludes most protobuf-defined symbols.
      if (defining_class and
          defining_class.__name__ in ['CMessage', 'Message', 'MessageMeta']):
        continue

      if doc_controls.should_skip_class_attr(py_class, short_name):
        continue

      child_doc = _parse_md_docstring(child, relative_path, self.full_name,
                                      parser_config.reference_resolver)

      if isinstance(child, property):
        self._add_property(short_name, child, child_doc)
        continue

      elif tf_inspect.isclass(child):
        if defining_class is None:
          continue
        url = parser_config.reference_resolver.reference_to_url(
            child_name, relative_path)
        self._add_class(short_name, child_name, child, child_doc, url)

      elif (tf_inspect.ismethod(child) or tf_inspect.isfunction(child) or
            tf_inspect.isroutine(child)):
        if defining_class is None:
          continue

        # Omit methods defined by namedtuple.
        original_method = defining_class.__dict__[short_name]
        if (hasattr(original_method, '__module__') and
            (original_method.__module__ or '').startswith('namedtuple')):
          continue

        # Some methods are often overridden without documentation. Because it's
        # obvious what they do, don't include them in the docs if there's no
        # docstring.
        if not child_doc.brief.strip() and short_name in [
            '__del__', '__copy__'
        ]:
          continue

        try:
          child_signature = _generate_signature(child,
                                                parser_config.reverse_index)
        except TypeError:
          # If this is a (dynamically created) slot wrapper, inspect will
          # raise typeerror when trying to get to the code. Ignore such
          # functions.
          continue

        child_decorators = extract_decorators(child)

        defined_in = _get_defined_in(child, parser_config)
        self._add_method(short_name, child_name, child, child_doc,
                         child_signature, child_decorators, defined_in)
      else:
        # Exclude members defined by protobuf that are useless
        if issubclass(py_class, ProtoMessage):
          if (short_name.endswith('_FIELD_NUMBER') or
              short_name in ['__slots__', 'DESCRIPTOR']):
            continue

        self._add_other_member(short_name, child_name, child, child_doc)

    self._augment_attributes_inplace(self.doc.docstring_parts)

  def _augment_attributes_inplace(self, docstring_parts: List[Any]) -> None:
    """Augments the "Attr" block of the docstring.

    The block is added to the end if it is not found.

    Merges `namedtuple` fields and properties into the attrs block.

    + `namedtuple` fields first, in order.
    + Then the docstring `Attr:` block.
    + Then any `properties` not mentioned above.

    Args:
      docstring_parts: A list of docstring parts. Edited in-place.
    """
    for attr_block_index, part in enumerate(docstring_parts):
      if isinstance(part, TitleBlock) and part.title.startswith('Attr'):
        raw_attrs = collections.OrderedDict(part.items)
        break
    else:
      raw_attrs = collections.OrderedDict()
      attr_block_index = len(docstring_parts)
      docstring_parts.append(None)

    attrs = collections.OrderedDict()
    # namedtuple fields first.
    attrs.update(self._namedtuplefields)
    # the contents of the `Attrs:` block from the docstring
    attrs.update(raw_attrs)
    # properties last.
    for name, desc in self._properties.items():
      # Don't overwrite existing items
      attrs.setdefault(name, desc)

    if attrs:
      docstring_parts[attr_block_index] = TitleBlock(
          title='Attributes', text='', items=attrs.items())
    else:
      del docstring_parts[attr_block_index]


class ModulePageInfo(PageInfo):
  """Collects docs for a module page.

  Attributes:
    full_name: The full, master name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object wqas defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    classes: A list of `_LinkInfo` objects pointing to docs for the classes in
      this module.
    functions: A list of `_LinkInfo` objects pointing to docs for the functions
      in this module
    modules: A list of `_LinkInfo` objects pointing to docs for the modules in
      this module.
    other_members: A list of `_OtherMemberInfo` objects documenting any other
      object's defined on the module object (mostly enum style fields).
  """

  def __init__(self, full_name, py_object):
    """Initialize a `ModulePageInfo`.

    Args:
      full_name: The full, master name, of the object being documented.
      py_object: The object being documented.
    """
    super(ModulePageInfo, self).__init__(full_name, py_object)

    self._modules = []
    self._classes = []
    self._functions = []
    self._other_members = []

  @property
  def modules(self):
    return self._modules

  def _add_module(self, short_name, full_name, obj, doc, url):
    self._modules.append(_LinkInfo(short_name, full_name, obj, doc, url))

  @property
  def classes(self):
    return self._classes

  def _add_class(self, short_name, full_name, obj, doc, url):
    self._classes.append(_LinkInfo(short_name, full_name, obj, doc, url))

  @property
  def functions(self):
    return self._functions

  def _add_function(self, short_name, full_name, obj, doc, url):
    self._functions.append(_LinkInfo(short_name, full_name, obj, doc, url))

  @property
  def other_members(self):
    return self._other_members

  def _add_other_member(self, short_name, full_name, obj, doc):
    self._other_members.append(
        _OtherMemberInfo(short_name, full_name, obj, doc))

  def get_metadata_html(self):
    meta_data = Metadata(self.full_name)

    # Objects with their own pages are not added to the metadata list for the
    # module, the module only has a link to the object page. No docs.
    for item in self.other_members:
      meta_data.append(item)

    return meta_data.build_html()

  def collect_docs(self, parser_config):
    """Collect information necessary specifically for a module's doc page.

    Mainly this is information about the members of the module.

    Args:
      parser_config: An instance of ParserConfig.
    """
    relative_path = os.path.relpath(
        path='.',
        start=os.path.dirname(documentation_path(self.full_name)) or '.')

    member_names = parser_config.tree.get(self.full_name, [])
    for name in member_names:

      if name in [
          '__builtins__', '__doc__', '__file__', '__name__', '__path__',
          '__package__', '__cached__', '__loader__', '__spec__',
          'absolute_import', 'division', 'print_function', 'unicode_literals'
      ]:
        continue

      member_full_name = self.full_name + '.' + name if self.full_name else name
      member = parser_config.py_name_to_object(member_full_name)

      member_doc = _parse_md_docstring(member, relative_path, self.full_name,
                                       parser_config.reference_resolver)

      url = parser_config.reference_resolver.reference_to_url(
          member_full_name, relative_path)

      if tf_inspect.ismodule(member):
        self._add_module(name, member_full_name, member, member_doc, url)

      elif tf_inspect.isclass(member):
        self._add_class(name, member_full_name, member, member_doc, url)

      elif tf_inspect.isfunction(member):
        self._add_function(name, member_full_name, member, member_doc, url)

      else:
        self._add_other_member(name, member_full_name, member, member_doc)


class ParserConfig(object):
  """Stores all indexes required to parse the docs."""

  def __init__(self, reference_resolver, duplicates, duplicate_of, tree, index,
               reverse_index, base_dir, code_url_prefix):
    """Object with the common config for docs_for_object() calls.

    Args:
      reference_resolver: An instance of ReferenceResolver.
      duplicates: A `dict` mapping fully qualified names to a set of all aliases
        of this name. This is used to automatically generate a list of all
        aliases for each name.
      duplicate_of: A map from duplicate names to preferred names of API
        symbols.
      tree: A `dict` mapping a fully qualified name to the names of all its
        members. Used to populate the members section of a class or module page.
      index: A `dict` mapping full names to objects.
      reverse_index: A `dict` mapping object ids to full names.
      base_dir: A base path that is stripped from file locations written to the
        docs.
      code_url_prefix: A Url to pre-pend to the links to file locations.
    """
    self.reference_resolver = reference_resolver
    self.duplicates = duplicates
    self.duplicate_of = duplicate_of
    self.tree = tree
    self.reverse_index = reverse_index
    self.index = index
    self.base_dir = base_dir
    self.code_url_prefix = code_url_prefix

  def py_name_to_object(self, full_name):
    """Return the Python object for a Python symbol name."""
    return self.index[full_name]


def docs_for_object(full_name, py_object, parser_config):
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
    parser_config: A ParserConfig object.

  Returns:
    Either a `_FunctionPageInfo`, `_ClassPageInfo`, or a `_ModulePageInfo`
    depending on the type of the python object being documented.

  Raises:
    RuntimeError: If an object is encountered for which we don't know how
      to make docs.
  """

  # Which other aliases exist for the object referenced by full_name?
  master_name = parser_config.reference_resolver.py_master_name(full_name)
  duplicate_names = parser_config.duplicates.get(master_name, [])
  if master_name in duplicate_names:
    duplicate_names.remove(master_name)

  if tf_inspect.isclass(py_object):
    page_info = ClassPageInfo(master_name, py_object)
  elif callable(py_object):
    page_info = FunctionPageInfo(master_name, py_object)
  elif tf_inspect.ismodule(py_object):
    page_info = ModulePageInfo(master_name, py_object)
  else:
    raise RuntimeError('Cannot make docs for object {full_name}: {py_object!r}')

  relative_path = os.path.relpath(
      path='.', start=os.path.dirname(documentation_path(full_name)) or '.')

  page_info.set_doc(
      _parse_md_docstring(py_object, relative_path, full_name,
                          parser_config.reference_resolver))

  page_info.collect_docs(parser_config)

  page_info.set_aliases(duplicate_names)

  page_info.set_defined_in(_get_defined_in(py_object, parser_config))

  return page_info


class _FileLocation(object):
  """This class indicates that the object is defined in a regular file.

  This can be used for the `defined_in` slot of the `PageInfo` objects.
  """
  GITHUB_LINE_NUMBER_TEMPLATE = '#L{start_line:d}-L{end_line:d}'

  def __init__(self, rel_path, url=None, start_line=None, end_line=None):
    self.rel_path = rel_path
    self.url = url
    self.start_line = start_line
    self.end_line = end_line

    github_master_re = 'github.com.*?(blob|tree)/master'
    suffix = ''
    # Only attach a line number for github URLs that are not using "master"
    if self.start_line and not re.search(github_master_re, self.url):
      if 'github.com' in self.url:
        suffix = self.GITHUB_LINE_NUMBER_TEMPLATE.format(
            start_line=self.start_line, end_line=self.end_line)

        self.url = self.url + suffix


def _get_defined_in(py_object: Any,
                    parser_config: ParserConfig) -> Optional[_FileLocation]:
  """Returns a description of where the passed in python object was defined.

  Args:
    py_object: The Python object.
    parser_config: A ParserConfig object.

  Returns:
    A `_FileLocation`
  """
  # Every page gets a note about where this object is defined
  base_dirs_and_prefixes = zip(parser_config.base_dir,
                               parser_config.code_url_prefix)
  try:
    obj_path = tf_inspect.getfile(py_object)
  except TypeError:  # getfile throws TypeError if py_object is a builtin.
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
      break

  # No link if the file was not found in a `base_dir`, or the prefix is None.
  if code_url_prefix is None:
    return None

  try:
    lines, start_line = tf_inspect.getsourcelines(py_object)
    end_line = start_line + len(lines) - 1
  except (IOError, TypeError, IndexError):
    start_line = None
    end_line = None

  # TODO(wicke): If this is a generated file, link to the source instead.
  # TODO(wicke): Move all generated files to a generated/ directory.
  # TODO(wicke): And make their source file predictable from the file name.

  # In case this is compiled, point to the original
  if rel_path.endswith('.pyc'):
    # If a PY3 __pycache__/ subdir is being used, omit it.
    rel_path = rel_path.replace('__pycache__' + os.sep, '')
    # Strip everything after the first . so that variants such as .pyc and
    # .cpython-3x.pyc or similar are all handled.
    rel_path = rel_path.partition('.')[0] + '.py'

  # Never include links outside this code base.
  if re.search(r'\b_api\b', rel_path):
    return None
  if re.search(r'\bapi/(_v2|_v1)\b', rel_path):
    return None
  if re.search(r'<[\w\s]+>', rel_path):
    # Built-ins emit paths like <embedded stdlib>, <string>, etc.
    return None
  if '<attrs generated' in rel_path:
    return None

  if re.match(r'.*/gen_[^/]*\.py$', rel_path):
    return _FileLocation(rel_path)
  if 'genfiles' in rel_path:
    return _FileLocation(rel_path)
  elif re.match(r'.*_pb2\.py$', rel_path):
    # The _pb2.py files all appear right next to their defining .proto file.

    rel_path = rel_path[:-7] + '.proto'
    return _FileLocation(
        rel_path=rel_path, url=os.path.join(code_url_prefix, rel_path))  # pylint: disable=undefined-loop-variable
  else:
    return _FileLocation(
        rel_path=rel_path,
        url=os.path.join(code_url_prefix, rel_path),
        start_line=start_line,
        end_line=end_line)  # pylint: disable=undefined-loop-variable


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
    if (tf_inspect.ismodule(py_object) or tf_inspect.isfunction(py_object) or
        tf_inspect.isclass(py_object)):
      # In Python 3, unbound methods are functions, so eliminate those.
      if tf_inspect.isfunction(py_object):
        if full_name.count('.') == 0:
          parent_name = ''
        else:
          parent_name = full_name[:full_name.rfind('.')]
        if parent_name in index and tf_inspect.isclass(index[parent_name]):
          # Skip methods (=functions with class parents).
          continue
      symbol_links.append(
          (full_name, reference_resolver.python_link(full_name, full_name,
                                                     '.')))

  lines = [f'# All symbols in {library_name}', '']

  # Sort all the symbols once, so that the ordering is preserved when its broken
  # up into master symbols and compat symbols and sorting the sublists is not
  # required.
  symbol_links = sorted(symbol_links, key=lambda x: x[0])

  compat_v1_symbol_links = []
  compat_v2_symbol_links = []
  primary_symbol_links = []

  for symbol, link in symbol_links:
    if symbol.startswith('tf.compat.v1'):
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
