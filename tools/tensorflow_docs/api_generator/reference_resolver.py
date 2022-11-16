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

from __future__ import annotations

import collections
import contextlib
import html
import json
import os
import posixpath
import re

from typing import Optional, Union

from tensorflow_docs.api_generator import parser


class TFDocsError(Exception):
  pass


class IgnoreLineInBlock:
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


class ReferenceResolver:
  """Class for replacing `tf.symbol` references with links."""

  # ?P<...> helps to find the match by entering the group name instead of the
  # index. For example, instead of doing match.group(1) we can do
  # match.group('brackets')
  AUTO_REFERENCE_RE = re.compile(
      r"""
      (?P<brackets>\[.*?\])|                      # match a '[]' span
      `(?P<backticks>@?[\w\(\[\)\]\{\}.,=\s]+?)`  # or a `` span
      """,
      flags=re.VERBOSE)

  def __init__(
      self,
      *,
      duplicate_of: dict[str, str],
      is_fragment: dict[str, bool],
      py_module_names: Union[list[str], dict[str, str]],
      link_prefix: Optional[str] = None,
      physical_path: Optional[dict[str, str]] = None,
  ):
    """Initializes a Reference Resolver.

    Args:
      duplicate_of: A map from duplicate names to preferred names of API
        symbols.
      is_fragment: A map from full names to bool for each symbol. If True the
        object lives at a page fragment `tf.a.b.c` --> `tf/a/b#c`. If False
        object has a page to itself: `tf.a.b.c` --> `tf/a/b/c`.
      py_module_names: A dict from short name to module name Like
        `{'tf': 'tensorflow'}`. Or [deprecated] a list of short-names like
        `['tf']`.
      link_prefix: The website to which these symbols should link to. A prefix
        is added before the links to enable cross-site linking if `link_prefix`
        is not None.
      physical_path: A mapping from the preferred full_name to the object's
        physical path.
    """
    self._duplicate_of = duplicate_of
    self._is_fragment = is_fragment
    self._physical_path = physical_path
    if isinstance(py_module_names, list):
      py_module_names = {short: short for short in py_module_names}
    self._py_module_names = py_module_names

    self._link_prefix = link_prefix

    self._all_names = set(is_fragment.keys())
    self._partial_symbols_dict = self._create_partial_symbols_dict()

  def get_main_name(self, name: str) -> Optional[str]:
    full_name = self._partial_symbols_dict.get(name, name)
    main_name = self._duplicate_of.get(full_name, full_name)
    if main_name in self._all_names:
      return main_name
    else:
      return None

  @classmethod
  def from_visitor(cls, visitor, **kwargs):
    """A factory function for building a ReferenceResolver from a visitor.

    Args:
      visitor: an instance of `DocGeneratorVisitor`
      **kwargs: all remaining args are passed to the constructor

    Returns:
      an instance of `ReferenceResolver` ()
    """
    api_tree = visitor.api_tree
    all_is_fragment = {}
    duplicate_of = {}
    physical_path = {}
    for node in api_tree.iter_nodes():
      full_name = node.full_name
      is_fragment = node.output_type() is node.OutputType.FRAGMENT
      if node.physical_path:
        physical_path[node.full_name] = '.'.join(node.physical_path)
      for alias in node.aliases:
        alias_name = '.'.join(alias)
        duplicate_of[alias_name] = full_name
        all_is_fragment[alias_name] = is_fragment

    return cls(
        duplicate_of=visitor.duplicate_of,
        is_fragment=all_is_fragment,
        physical_path=physical_path,
        **kwargs)

  def with_prefix(self, prefix):
    return type(self)(
        duplicate_of=self._duplicate_of,
        is_fragment=self._is_fragment,
        py_module_names=self._py_module_names,
        link_prefix=prefix,
    )

  @contextlib.contextmanager
  def temp_prefix(self, link_prefix):
    old_prefix = self._link_prefix
    self._link_prefix = link_prefix
    try:
      yield
    finally:
      self._link_prefix = old_prefix

  def is_fragment(self, full_name: str):
    """Returns True if the object's doc is a subsection of another page."""
    return self._is_fragment[full_name]

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
      # TODO(yashkatariya): Remove `tf.experimental.numpy` after `tf.numpy` is
      # in not in experimental namespace.
      if 'tf.experimental.numpy' in name or 'tf.numpy' in name:
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
    """Converts the ReferenceResolver to json and writes it to the specified file.

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

  def replace_references(self, string, full_name=None):
    """Replace `tf.symbol` references with links to symbol's documentation page.

    This function finds all occurrences of "`tf.symbol`" in `string`
    and replaces them with links to the documentation page
    for "symbol".


    Args:
      string: A string in which "`tf.symbol`" references should be replaced.
      full_name: (optional) The full name of current object, so replacements can
        depend on context.

    Returns:
      `string`, with "`tf.symbol`" references replaced by links.
    """

    def one_ref(match):
      return self._one_ref(match, full_name)

    fixed_lines = []

    filters = [
        IgnoreLineInBlock('<pre class="tfo-notebook-code-cell-output">',
                          '</pre>'),
        IgnoreLineInBlock('```', '```'),
        IgnoreLineInBlock(
            '<pre class="devsite-click-to-copy prettyprint lang-py">',
            '</pre>'),
        IgnoreLineInBlock('![', ')'),  # Don't replace within image's caption
    ]

    for line in string.splitlines():
      if not any(filter_block(line) for filter_block in filters):
        line = re.sub(self.AUTO_REFERENCE_RE, one_ref, line)
      fixed_lines.append(line)

    return '\n'.join(fixed_lines)

  def python_link(self, link_text: str, ref_full_name: Optional[str] = None):
    """Resolve a "`tf.symbol`" reference to a link.

    This will pick the canonical location for duplicate symbols.

    Args:
      link_text: The text of the link.
      ref_full_name: The fully qualified name of the symbol to link to.

    Returns:
      A link to the documentation page of `ref_full_name`.
    """
    if ref_full_name is None:
      ref_full_name = link_text
    link_text = html.escape(link_text, quote=True)

    url = self.reference_to_url(ref_full_name)
    url = html.escape(url, quote=True)
    return f'<a href="{url}"><code>{link_text}</code></a>'

  def py_main_name(self, full_name):
    """Return the main name for a Python symbol name."""
    return self._duplicate_of.get(full_name, full_name)

  def reference_to_url(self, ref_full_name):
    """Resolve a "`tf.symbol`" reference to a relative path.

    The input to this function should already be stripped of the '@'
    and '{}', and its output is only the link, not the full Markdown.

    If `ref_full_name` is the name of a class member, method, or property, the
    link will point to the page of the containing class, and it will include the
    method name as an anchor. For example, `tf.module.MyClass.my_method`.

    Args:
      ref_full_name: The fully qualified name of the symbol to link to.

    Returns:
      A relative path that links from the documentation page of `from_full_name`
      to the documentation page of `ref_full_name`.

    Raises:
      TFDocsError: If the symbol is not found.
    """
    if self._is_fragment.get(ref_full_name, False):
      # methods and constants get duplicated. And that's okay.
      # Use the main name of their parent.
      parent_name, short_name = ref_full_name.rsplit('.', 1)
      parent_main_name = self._duplicate_of.get(parent_name, parent_name)
      main_name = '.'.join([parent_main_name, short_name])
    else:
      main_name = self._duplicate_of.get(ref_full_name, ref_full_name)

    # Check whether this link exists
    if main_name not in self._all_names:
      raise TFDocsError(f'Cannot make link to {main_name!r}: Not in index.')

    rel_path = parser.documentation_path(main_name,
                                         self._is_fragment[main_name])

    if self._link_prefix is None:
      raise ValueError('you must set the `link_prefix`')
    url = posixpath.join(self._link_prefix, rel_path)
    return url

  def _one_ref(self, match, full_name=None):
    """Return a link for a single "`tf.symbol`" reference."""

    if match.group(1):
      # Found a '[]' group, return it unmodified.
      return match.group('brackets')

    # Found a '``' group.
    string = match.group('backticks')

    link_text = string

    # Drop everything after the *last* ( or [ to get the
    # symbol name. The last is used so complex nested or chained calls are not
    # recognized as valid links.
    string = re.sub(r'^(.*)[\(\[].*', r'\1', string)
    # Drop the optional leading `@`.
    string = re.sub(r'^@', r'', string)

    if string.startswith('compat.v1') or string.startswith('compat.v2'):
      string = 'tf.' + string
    elif string.startswith('v1') or string.startswith('v2'):
      string = 'tf.compat.' + string

    elif full_name is None or ('tf.compat.v' not in full_name and
                               'tf.contrib' not in full_name):
      string = self._partial_symbols_dict.get(string, string)

    if not string:
      return match.group(0)

    try:
      if string.startswith('tensorflow::'):
        # C++ symbol
        return self._cc_link(string, link_text)

      return self.python_link(link_text, string)
    except TFDocsError:
      pass

    return match.group(0)

  def _cc_link(self, string, link_text):
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
        posixpath.join(self._link_prefix, '../cc', ret))

    return f'<a href="{cc_relative_path}"><code>{link_text}</code></a>'
