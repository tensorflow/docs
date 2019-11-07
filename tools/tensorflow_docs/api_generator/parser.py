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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ast
import collections

import itertools
import json
import os
import re
import textwrap

from absl import logging

import astor
import six

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
  if not tf_inspect.isfunction(py_object):
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
  # For object instances, tf_inspect.getdoc does give us the docstring of their
  # type, which is not what we want. Only return the docstring if it is useful.
  if (tf_inspect.isclass(py_object) or tf_inspect.ismethod(py_object) or
      tf_inspect.isfunction(py_object) or tf_inspect.ismodule(py_object) or
      isinstance(py_object, property)):
    result = tf_inspect.getdoc(py_object) or ''
  else:
    result = ''

  return _AddDoctestFences()(result)


class _AddDoctestFences(object):
  """Adds ``` fences around doctest caret blocks >>> that don't have them."""
  CARET_BLOCK_RE = re.compile(
      r"""
    (?<=\n)\s*?\n                            # After a blank line.
    (?P<comment>\s*\#.*\n)?                  # Maybe a comment at the start.
    (?P<indent>\s*)(?P<content>\>\>\>.*?)    # Whitespace and a triple caret.
    \n\s*?(?=\n|$)                           # Followed by a blank line""",
      re.VERBOSE | re.DOTALL)

  def _sub(self, match):
    groups = match.groupdict()
    fence = '\n{}```\n'.format(groups['indent'])

    start_comment = groups['comment']
    if start_comment is None:
      start_comment = ''

    content = groups['indent'] + groups['content']
    return ''.join([fence, start_comment, content, fence])

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
        duplicate_of=visitor.duplicate_of,
        is_fragment=is_fragment,
        **kwargs)

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
        '.'.join(split_symbol[i:])
        for i in range(1, len(split_symbol) - 1)
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
      full_name: (optional) The full name of current object, so replacements
        can depend on context.

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

  def python_link(self, link_text, ref_full_name, relative_path_to_root,
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

    return '<a href="{}">{}</a>'.format(url, link_text)

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
      raise TFDocsError(
          'Cannot make link to "%s": Not in index.' % master_name)

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
      raise TFDocsError('C++ reference not understood: "%s"' % string)

    # relative_path_to_root gets you to api_docs/python, we go from there
    # to api_docs/cc, and then add ret.
    cc_relative_path = os.path.normpath(os.path.join(
        relative_path_to_root, '../cc', ret))

    return '<a href="{}"><code>{}</code></a>'.format(cc_relative_path,
                                                     link_text)


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

  def __init__(self, title, text, items):
    self.title = title
    self.text = text
    self.items = items

  def __str__(self):
    """Returns a markdown compatible version of the TitleBlock."""
    sub = []
    sub.append('\n\n#### ' + self.title + ':\n')
    sub.append(textwrap.dedent(self.text))
    sub.append('\n')
    for name, description in self.items:
      sub.append('* <b>`{}`</b>: {}'.format(name, description))
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


def _remove_first_line_indent(string):
  indent = len(re.match(r'^\s*', string).group(0))
  return '\n'.join([line[indent:] for line in string.split('\n')])


PAREN_NUMBER_RE = re.compile(r'^\(([0-9.e-]+)\)')
OBJECT_MEMORY_ADDRESS_RE = re.compile(r'<(?P<type>.+) object at 0x[\da-f]+>')


def _generate_signature(func, reverse_index):
  """Given a function, returns a list of strings representing its args.

  This function produces a list of strings representing the arguments to a
  python function. It uses tf_inspect.getfullargspec, which
  does not generalize well to Python 3.x, which is more flexible in how *args
  and **kwargs are handled. This is not a problem in TF, since we have to remain
  compatible to Python 2.7 anyway.

  This function uses `__name__` for callables if it is available. This can lead
  to poor results for functools.partial and other callable objects.

  The returned string is Python code, so if it is included in a Markdown
  document, it should be typeset as code (using backticks), or escaped.

  Args:
    func: A function, method, or functools.partial to extract the signature for.
    reverse_index: A map from object ids to canonical full names to use.

  Returns:
    A list of strings representing the argument signature of `func` as python
    code.
  """

  args_list = []

  argspec = tf_inspect.getfullargspec(func)
  first_arg_with_default = (
      len(argspec.args or []) - len(argspec.defaults or []))

  # Python documentation skips `self` when printing method signatures.
  # Note we cannot test for ismethod here since unbound methods do not register
  # as methods (in Python 3).
  first_arg = 1 if 'self' in argspec.args[:1] else 0

  # Add all args without defaults.
  for arg in argspec.args[first_arg:first_arg_with_default]:
    args_list.append(arg)

  # Add all args with defaults.
  if argspec.defaults:
    try:
      source = _remove_first_line_indent(tf_inspect.getsource(func))
      func_ast = ast.parse(source)
      ast_defaults = func_ast.body[0].args.defaults
    except IOError:  # If this is a builtin, getsource fails with IOError
      # If we cannot get the source, assume the AST would be equal to the repr
      # of the defaults.
      ast_defaults = [None] * len(argspec.defaults)
    except SyntaxError:
      # You may get a SyntaxError using pytype in python 2.
      ast_defaults = [None] * len(argspec.defaults)
    except IndexError:
      # Some python3 signatures fail in tf_inspect.getsource with IndexError
      ast_defaults = [None] * len(argspec.defaults)
    except AttributeError:
      # Some objects in tfp throw attribute errors here.
      ast_defaults = [None] * len(argspec.defaults)

    for arg, default, ast_default in zip(
        argspec.args[first_arg_with_default:], argspec.defaults, ast_defaults):
      if id(default) in reverse_index:
        default_text = reverse_index[id(default)]
      elif ast_default is not None:
        default_text = (
            astor.to_source(ast_default).rstrip('\n').replace('\t', '\\t')
            .replace('\n', '\\n').replace('"""', "'"))
        default_text = PAREN_NUMBER_RE.sub('\\1', default_text)

        if default_text != repr(default):
          # This may be an internal name. If so, handle the ones we know about.
          # TODO(wicke): This should be replaced with a lookup in the index.
          # TODO(wicke): (replace first ident with tf., check if in index)
          internal_names = {
              'ops.GraphKeys': 'tf.GraphKeys',
              '_ops.GraphKeys': 'tf.GraphKeys',
              'init_ops.zeros_initializer': 'tf.zeros_initializer',
              'init_ops.ones_initializer': 'tf.ones_initializer',
              'saver_pb2.SaverDef': 'tf.train.SaverDef',
          }
          full_name_re = '^%s(.%s)+' % (IDENTIFIER_RE, IDENTIFIER_RE)
          match = re.match(full_name_re, default_text)
          if match:
            lookup_text = default_text
            for internal_name, public_name in six.iteritems(internal_names):
              if match.group(0).startswith(internal_name):
                lookup_text = public_name + default_text[len(internal_name):]
                break
            if default_text is lookup_text:
              logging.warn(
                  'WARNING: Using default arg, failed lookup: %s, repr: %r',
                  default_text, default)
            else:
              default_text = lookup_text
      else:
        default_text = repr(default)
        # argspec.defaults can contain object memory addresses, i.e.
        # containers.MutableMapping.pop. Strip these out to avoid
        # unnecessary doc churn between invocations.
        default_text = OBJECT_MEMORY_ADDRESS_RE.sub(r'<\g<type>>', default_text)

      args_list.append('%s=%s' % (arg, default_text))

  # Add *args and *kwargs.
  if argspec.varargs:
    args_list.append('*' + argspec.varargs)
  if argspec.varkw:
    args_list.append('**' + argspec.varkw)

  return args_list


def _get_defining_class(py_class, name):
  for cls in tf_inspect.getmro(py_class):
    if name in cls.__dict__:
      return cls
  return None


class _LinkInfo(
    collections.namedtuple(
        '_LinkInfo', ['short_name', 'full_name', 'obj', 'doc', 'url'])):

  __slots__ = []

  def is_link(self):
    return True


class _OtherMemberInfo(
    collections.namedtuple('_OtherMemberInfo',
                           ['short_name', 'full_name', 'obj', 'doc'])):

  __slots__ = []

  def is_link(self):
    return False


_PropertyInfo = collections.namedtuple(
    '_PropertyInfo', ['short_name', 'full_name', 'obj', 'doc'])

_MethodInfo = collections.namedtuple('_MethodInfo', [
    'short_name',
    'full_name',
    'obj',
    'doc',
    'signature',
    'decorators',
    'defined_in',
])


class _FunctionPageInfo(object):
  """Collects docs For a function Page."""

  def __init__(self, full_name):
    self._full_name = full_name
    self._defined_in = None
    self._aliases = None
    self._doc = None

    self._signature = None
    self._decorators = []

  def for_function(self):
    return True

  def for_class(self):
    return False

  def for_module(self):
    return False

  @property
  def full_name(self):
    return self._full_name

  @property
  def short_name(self):
    return self._full_name.split('.')[-1]

  @property
  def defined_in(self):
    return self._defined_in

  def set_defined_in(self, defined_in):
    assert self.defined_in is None
    self._defined_in = defined_in

  @property
  def aliases(self):
    return self._aliases

  def set_aliases(self, aliases):
    assert self.aliases is None
    self._aliases = aliases

  @property
  def doc(self):
    return self._doc

  def set_doc(self, doc):
    assert self.doc is None
    self._doc = doc

  @property
  def signature(self):
    return self._signature

  def set_signature(self, function, reverse_index):
    """Attach the function's signature.

    Args:
      function: The python function being documented.
      reverse_index: A map from object ids in the index to full names.
    """

    assert self.signature is None
    self._signature = _generate_signature(function, reverse_index)

  @property
  def decorators(self):
    return list(self._decorators)

  def add_decorator(self, dec):
    self._decorators.append(dec)

  def get_metadata_html(self):
    return Metadata(self.full_name).build_html()


class _ClassPageInfo(object):
  """Collects docs for a class page.

  Attributes:
    full_name: The fully qualified name of the object at the master
      location. Aka `master_name`. For example: `tf.nn.sigmoid`.
    short_name: The last component of the `full_name`. For example: `sigmoid`.
    defined_in: The path to the file where this object is defined.
    aliases: The list of all fully qualified names for the locations where the
      object is visible in the public api. This includes the master location.
    doc: A `_DocstringInfo` object representing the object's docstring (can be
      created with `_parse_md_docstring`).
   bases: A list of `_LinkInfo` objects pointing to the docs for the parent
      classes.
    properties: A list of `_PropertyInfo` objects documenting the class'
      properties (attributes that use `@property`).
    methods: A list of `_MethodInfo` objects documenting the class' methods.
    classes: A list of `_LinkInfo` objects pointing to docs for any nested
      classes.
    other_members: A list of `_OtherMemberInfo` objects documenting any other
      object's defined inside the class object (mostly enum style fields).
    namedtuplefields: a list of the namedtuple fields in the class.
  """

  def __init__(self, full_name):
    self._full_name = full_name
    self._defined_in = None
    self._aliases = None
    self._doc = None
    self._namedtuplefields = None

    self._bases = None
    self._properties = []
    self._methods = []
    self._classes = []
    self._other_members = []

  def for_function(self):
    """Returns true if this object documents a function."""
    return False

  def for_class(self):
    """Returns true if this object documents a class."""
    return True

  def for_module(self):
    """Returns true if this object documents a module."""
    return False

  @property
  def full_name(self):
    """Returns the documented object's fully qualified name."""
    return self._full_name

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

  @property
  def namedtuplefields(self):
    return self._namedtuplefields

  def set_namedtuplefields(self, py_class):
    if issubclass(py_class, tuple):
      if all(
          hasattr(py_class, attr)
          for attr in ('_asdict', '_fields', '_make', '_replace')):
        self._namedtuplefields = py_class._fields

  @property
  def bases(self):
    """Returns a list of `_LinkInfo` objects pointing to the class' parents."""
    return self._bases

  def _set_bases(self, relative_path, parser_config):
    """Builds the `bases` attribute, to document this class' parent-classes.

    This method sets the `bases` to a list of `_LinkInfo` objects point to the
    doc pages for the class' parents.

    Args:
      relative_path: The relative path from the doc this object describes to
        the documentation root.
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

      link_info = _LinkInfo(short_name=base_full_name.split('.')[-1],
                            full_name=base_full_name, obj=base,
                            doc=base_doc, url=base_url)
      bases.append(link_info)

    self._bases = bases

  @property
  def properties(self):
    """Returns a list of `_PropertyInfo` describing the class' properties."""
    props_dict = {prop.short_name: prop for prop in self._properties}
    props = []
    if self.namedtuplefields:
      for field in self.namedtuplefields:
        field_prop = props_dict.pop(field, None)
        if field_prop is not None:
          props.append(field_prop)

    props.extend(sorted(props_dict.values()))

    return props

  def _add_property(self, short_name, full_name, obj, doc):
    """Adds a `_PropertyInfo` entry to the `properties` list.

    Args:
      short_name: The property's short name.
      full_name: The property's fully qualified name.
      obj: The property object itself
      doc: The property's parsed docstring, a `_DocstringInfo`.
    """
    # Hide useless namedtuple docs-trings.
    if re.match('Alias for field number [0-9]+', doc.brief):
      doc = doc._replace(docstring_parts=[], brief='')
    property_info = _PropertyInfo(short_name, full_name, obj, doc)
    self._properties.append(property_info)

  @property
  def methods(self):
    """Returns a list of `_MethodInfo` describing the class' methods."""
    return self._methods

  def _add_method(self, short_name, full_name, obj, doc, signature, decorators,
                  defined_in):
    """Adds a `_MethodInfo` entry to the `methods` list.

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
    method_info = _MethodInfo(short_name, full_name, obj, doc, signature,
                              decorators, defined_in)
    self._methods.append(method_info)

  @property
  def classes(self):
    """Returns a list of `_LinkInfo` pointing to any nested classes."""
    return self._classes

  def get_metadata_html(self):
    meta_data = Metadata(self.full_name)
    for item in itertools.chain(self.classes, self.properties, self.methods,
                                self.other_members):
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
      obj: The class object itself
      doc: The class' parsed docstring, a `_DocstringInfo`
    """
    other_member_info = _OtherMemberInfo(short_name, full_name, obj, doc)
    self._other_members.append(other_member_info)

  def collect_docs_for_class(self, py_class, parser_config):
    """Collects information necessary specifically for a class's doc page.

    Mainly, this is details about the class's members.

    Args:
      py_class: The class object being documented
      parser_config: An instance of ParserConfig.
    """
    self.set_namedtuplefields(py_class)
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
        self._add_property(short_name, child_name, child, child_doc)

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
          # If this is a (dynamically created) slot wrapper, tf_inspect will
          # raise typeerror when trying to get to the code. Ignore such
          # functions.
          continue

        child_decorators = []
        try:
          if isinstance(py_class.__dict__[short_name], classmethod):
            child_decorators.append('classmethod')
        except KeyError:
          pass

        try:
          if isinstance(py_class.__dict__[short_name], staticmethod):
            child_decorators.append('staticmethod')
        except KeyError:
          pass

        defined_in = _get_defined_in(child, parser_config)
        self._add_method(short_name, child_name, child, child_doc,
                         child_signature, child_decorators, defined_in)
      else:
        # Exclude members defined by protobuf that are useless
        if issubclass(py_class, ProtoMessage):
          if (short_name.endswith('_FIELD_NUMBER') or
              short_name in ['__slots__', 'DESCRIPTOR']):
            continue

        # TODO(wicke): We may want to also remember the object itself.
        self._add_other_member(short_name, child_name, child, child_doc)


class _ModulePageInfo(object):
  """Collects docs for a module page."""

  def __init__(self, full_name):
    self._full_name = full_name
    self._defined_in = None
    self._aliases = None
    self._doc = None

    self._modules = []
    self._classes = []
    self._functions = []
    self._other_members = []

  def for_function(self):
    return False

  def for_class(self):
    return False

  def for_module(self):
    return True

  @property
  def full_name(self):
    return self._full_name

  @property
  def short_name(self):
    return self._full_name.split('.')[-1]

  @property
  def defined_in(self):
    return self._defined_in

  def set_defined_in(self, defined_in):
    assert self.defined_in is None
    self._defined_in = defined_in

  @property
  def aliases(self):
    return self._aliases

  def set_aliases(self, aliases):
    assert self.aliases is None
    self._aliases = aliases

  @property
  def doc(self):
    return self._doc

  def set_doc(self, doc):
    assert self.doc is None
    self._doc = doc

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

  def collect_docs_for_module(self, parser_config):
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

      if name in ['__builtins__', '__doc__', '__file__',
                  '__name__', '__path__', '__package__',
                  '__cached__', '__loader__', '__spec__', 'absolute_import',
                  'division', 'print_function', 'unicode_literals']:
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
      duplicates: A `dict` mapping fully qualified names to a set of all
        aliases of this name. This is used to automatically generate a list of
        all aliases for each name.
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
    full_name: The fully qualified name of the symbol to be
      documented.
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

  # TODO(wicke): Once other pieces are ready, enable this also for partials.
  if (tf_inspect.ismethod(py_object) or tf_inspect.isfunction(py_object) or
      # Some methods in classes from extensions come in as routines.
      tf_inspect.isroutine(py_object)):
    page_info = _FunctionPageInfo(master_name)
    page_info.set_signature(py_object, parser_config.reverse_index)

  elif tf_inspect.isclass(py_object):
    page_info = _ClassPageInfo(master_name)
    page_info.collect_docs_for_class(py_object, parser_config)

  elif tf_inspect.ismodule(py_object):
    page_info = _ModulePageInfo(master_name)
    page_info.collect_docs_for_module(parser_config)

  else:
    raise RuntimeError('Cannot make docs for object %s: %r' % (full_name,
                                                               py_object))

  relative_path = os.path.relpath(
      path='.', start=os.path.dirname(documentation_path(full_name)) or '.')

  page_info.set_doc(
      _parse_md_docstring(py_object, relative_path, full_name,
                          parser_config.reference_resolver))

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


def _get_defined_in(py_object, parser_config):
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
  code_url_prefix = None
  for base_dir, temp_prefix in base_dirs_and_prefixes:
    try:
      obj_path = tf_inspect.getfile(py_object)
    except TypeError:  # getfile throws TypeError if py_object is a builtin.
      continue

    rel_path = os.path.relpath(
        path=obj_path, start=base_dir)
    # A leading ".." indicates that the file is not inside `base_dir`, and
    # the search should continue.
    if rel_path.startswith('..'):
      continue
    else:
      code_url_prefix = temp_prefix
      break

  try:
    lines, start_line = tf_inspect.getsourcelines(py_object)
    end_line = start_line + len(lines) - 1
  except IOError:
    # The source is not available.
    start_line = None
    end_line = None
  except TypeError:
    # This is a builtin, with no python-source.
    start_line = None
    end_line = None
  except IndexError:
    start_line = None
    end_line = None

  # No link if the file was not found in a `base_dir`, or the prefix is None.
  if code_url_prefix is None:
    return None

  # TODO(wicke): If this is a generated file, link to the source instead.
  # TODO(wicke): Move all generated files to a generated/ directory.
  # TODO(wicke): And make their source file predictable from the file name.

  # In case this is compiled, point to the original
  if rel_path.endswith('.pyc'):
    rel_path = rel_path[:-1]

  # Never include links outside this code base.
  if re.search(r'\b_api\b', rel_path):
    return None
  if re.search(r'\bapi/(_v2|_v1)\b', rel_path):
    return None
  if re.search(r'<[\w\s]+>', rel_path):
    # Built-ins emit paths like <embedded stdlib>, <string>, etc.
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
  for full_name, py_object in six.iteritems(index):
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
      symbol_links.append((
          full_name, reference_resolver.python_link(full_name, full_name, '.')))

  lines = ['# All symbols in %s' % library_name, '']

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
    lines.append('*  %s' % link)

  if compat_v2_symbol_links:
    lines.append('\n## Compat v2 symbols\n')
    for link in compat_v2_symbol_links:
      lines.append('*  %s' % link)

  if compat_v1_symbol_links:
    lines.append('\n## Compat v1 symbols\n')
    for link in compat_v1_symbol_links:
      lines.append('*  %s' % link)

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
    schema = 'http://developers.google.com/ReferenceObject'
    parts = ['<div itemscope itemtype="%s">' % schema]

    parts.append('<meta itemprop="name" content="%s" />' % self.name)
    parts.append('<meta itemprop="path" content="%s" />' % self.version)
    for item in self._content:
      parts.append('<meta itemprop="property" content="%s"/>' % item)

    parts.extend(['</div>', ''])

    return '\n'.join(parts)
