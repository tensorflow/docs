# Lint as: python3
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
"""A module for converting parsed doc content into markdown pages.

The adjacent `parser` module creates `PageInfo` objects, containing all data
necessary to document an element of the TensorFlow API.

This module contains one public function, which handels the conversion of these
`PageInfo` objects into a markdown string:

    md_page = build_md_page(page_info)
"""

import textwrap

from typing import Dict, List, Optional, NamedTuple

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import parser

_TABLE_ITEMS = ('arg', 'return', 'raise', 'attr')


def build_md_page(page_info: parser.PageInfo, table_view: bool) -> str:
  """Given a PageInfo object, return markdown for the page.

  Args:
    page_info: must be a `parser.FunctionPageInfo`, `parser.ClassPageInfo`, or
      `parser.ModulePageInfo`
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    Markdown for the page

  Raises:
    ValueError: if `page_info` is an instance of an unrecognized class
  """
  if isinstance(page_info, parser.ClassPageInfo):
    return _build_class_page(page_info, table_view)

  if isinstance(page_info, parser.FunctionPageInfo):
    return _build_function_page(page_info, table_view)

  if isinstance(page_info, parser.ModulePageInfo):
    return _build_module_page(page_info, table_view)

  if isinstance(page_info, parser.TypeAliasPageInfo):
    return _build_type_alias_page(page_info, table_view)

  raise ValueError(f'Unknown Page Info Type: {type(page_info)}')


def _format_docstring(item,
                      table_view: bool,
                      *,
                      table_title_template: Optional[str] = None) -> str:
  """Formats TitleBlock into a table or list or a normal string.

  Args:
    item: A TitleBlock instance or a normal string.
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.
    table_title_template: Template for title detailing how to display it in the
      table.

  Returns:
    A formatted docstring.
  """

  if isinstance(item, parser.TitleBlock):
    lower_title = item.title.lower()
    if table_view and lower_title.startswith(_TABLE_ITEMS):
      return item.table_view(title_template=table_title_template)
    else:
      if 'attr' in lower_title:
        return item.list_view(title_template='\n\n## {title}\n')
      else:
        return item.list_view(title_template='\n\n#### {title}:\n')
  else:
    return str(item)


def _build_function_page(page_info: parser.FunctionPageInfo,
                         table_view: bool) -> str:
  """Constructs a markdown page given a `FunctionPageInfo` object.

  Args:
    page_info: A `FunctionPageInfo` object containing information that's used to
      create a function page.
      For example, see https://www.tensorflow.org/api_docs/python/tf/concat
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    The function markdown page.
  """

  parts = [f'# {page_info.full_name}\n\n']

  parts.append('<!-- Insert buttons and diff -->\n')

  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  parts.append(page_info.doc.brief + '\n\n')

  parts.append(_build_collapsable_aliases(page_info.aliases))

  if page_info.signature is not None:
    parts.append(_build_signature(page_info, obj_name=page_info.full_name))
    parts.append('\n\n')

  # This will be replaced by the "Used in: <notebooks>" whenever it is run.
  parts.append('<!-- Placeholder for "Used in" -->\n')

  for item in page_info.doc.docstring_parts:
    parts.append(
        _format_docstring(
            item,
            table_view,
            table_title_template='<h2 class="add-link">{title}</h2>'))

  parts.append(_build_compatibility(page_info.doc.compatibility))

  custom_content = doc_controls.get_custom_page_content(page_info.py_object)
  if custom_content is not None:
    parts.append(custom_content)

  return ''.join(parts)


def _build_type_alias_page(page_info: parser.TypeAliasPageInfo,
                           table_view: bool) -> str:
  """Constructs a markdown page given a `TypeAliasPageInfo` object.

  Args:
    page_info: A `TypeAliasPageInfo` object containing information that's used
      to create a type alias page.
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    The type alias's markdown page.
  """

  parts = [f'# {page_info.full_name}\n\n']

  parts.append('<!-- Insert buttons and diff -->\n')

  parts.append('This symbol is a **type alias**.\n\n')
  parts.append(page_info.doc.brief)
  parts.append('\n\n')

  if page_info.signature is not None:
    parts.append('#### Source:\n\n')
    parts.append(
        _build_signature(
            page_info, obj_name=page_info.short_name, type_alias=True))
    parts.append('\n\n')

  parts.append('<!-- Placeholder for "Used in" -->\n')

  for item in page_info.doc.docstring_parts:
    parts.append(
        _format_docstring(
            item,
            table_view,
            table_title_template='<h2 class="add-link">{title}</h2>'))

  return ''.join(parts)


class _Methods(NamedTuple):
  info_dict: Dict[str, parser.MethodInfo]
  constructor: parser.MethodInfo


def _split_methods(methods: List[parser.MethodInfo]) -> _Methods:
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

  return _Methods(info_dict=method_info_dict, constructor=constructor)


def _merge_class_and_constructor_docstring(
    class_page_info: parser.ClassPageInfo, ctor_info: parser.MethodInfo,
    table_view: bool) -> List[str]:
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
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    A list of strings containing the merged docstring.
  """

  def _create_class_doc(doc):
    updated_doc = []
    for item in doc:
      updated_doc.append(
          _format_docstring(
              item,
              table_view,
              table_title_template='<h2 class="add-link">{title}</h2>'))
    return updated_doc

  # Get the class docstring. `.doc.docstring_parts` contain the entire
  # docstring except for the one-line docstring that's compulsory.
  class_doc = class_page_info.doc.docstring_parts

  # If constructor doesn't exist, return the class docstring as it is.
  if ctor_info is None:
    return _create_class_doc(class_doc)

  # Get the constructor's docstring parts.
  constructor_doc = ctor_info.doc.docstring_parts

  # Extract the `Arguments`/`Args` from the constructor's docstring.
  # A constructor won't contain `Args` and `Arguments` section at once.
  # It can contain either one of these so check for both.
  for block in constructor_doc:
    if isinstance(block, parser.TitleBlock):
      if block.title.startswith(('Args', 'Arguments', 'Raises')):
        class_doc.append(block)

  return _create_class_doc(class_doc)


def _build_class_page(page_info: parser.ClassPageInfo, table_view: bool) -> str:
  """Constructs a markdown page given a `ClassPageInfo` object.

  Args:
    page_info: A `ClassPageInfo` object containing information that's used to
      create a class page. For example, see
      https://www.tensorflow.org/api_docs/python/tf/data/Dataset
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    The class markdown page.
  """

  # Add the full_name of the symbol to the page.
  parts = ['# {page_info.full_name}\n\n'.format(page_info=page_info)]

  # This is used as a marker to initiate the diffing process later down in the
  # pipeline.
  parts.append('<!-- Insert buttons and diff -->\n')

  # Add the github button.
  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  # Add the one line docstring of the class.
  parts.append(page_info.doc.brief + '\n\n')

  # If a class is a child class, add which classes it inherits from.
  if page_info.bases:
    parts.append('Inherits From: ')

    link_template = '[`{short_name}`]({url})'
    parts.append(', '.join(
        link_template.format(**base._asdict()) for base in page_info.bases))
    parts.append('\n\n')

  # Build the aliases section and keep it collapses by default.
  parts.append(_build_collapsable_aliases(page_info.aliases))

  # Split the methods into constructor and other methods.
  methods = _split_methods(page_info.methods)

  # If the class has a constructor, build its signature.
  # The signature will contain the class name followed by the arguments it
  # takes.
  if methods.constructor is not None:
    parts.append(
        _build_signature(methods.constructor, obj_name=page_info.full_name))
    parts.append('\n\n')

  # This will be replaced by the "Used in: <notebooks>" later in the pipeline.
  parts.append('<!-- Placeholder for "Used in" -->\n')

  # Merge the class and constructor docstring.
  parts.extend(
      _merge_class_and_constructor_docstring(page_info, methods.constructor,
                                             table_view))

  # Add the compatibility section to the page.
  parts.append(_build_compatibility(page_info.doc.compatibility))
  parts.append('\n\n')

  custom_content = doc_controls.get_custom_page_content(page_info.py_object)
  if custom_content is not None:
    parts.append(custom_content)
    return ''.join(parts)

  if page_info.attr_block is not None:
    parts.append(
        _format_docstring(
            page_info.attr_block,
            table_view,
            table_title_template='<h2 class="add-link">{title}</h2>'))
    parts.append('\n\n')

  # If the class has child classes, add that information to the page.
  if page_info.classes:
    parts.append('## Child Classes\n')

    link_template = ('[`class {class_info.short_name}`]'
                     '({class_info.url})\n\n')
    class_links = sorted(
        link_template.format(class_info=class_info)
        for class_info in page_info.classes)

    parts.extend(class_links)

  # If the class contains methods other than the constructor, then add them
  # to the page.
  if methods.info_dict:
    parts.append('## Methods\n\n')
    for method_name in sorted(methods.info_dict, key=_method_sort):
      parts.append(
          _build_method_section(methods.info_dict[method_name], table_view))
    parts.append('\n\n')

  # Add class variables/members if they exist to the page.
  if page_info.other_members:
    parts.append('## Class Variables\n\n')
    parts.append(_other_members(page_info.other_members))

  return ''.join(parts)


def _method_sort(method_name):
  # All dunder methods will be at the end of the list in an alphabetically
  # sorted order. Rest of the methods will be promoted to the top in an
  # alphabetically sorted order.
  if method_name.startswith('__'):
    return (1, method_name)
  return (-1, method_name)


def _other_members(other_members):
  """Returns "other_members" rendered to markdown.

  `other_members` is used for anything that is not a class, function, module,
  or method.

  Args:
    other_members: a list of (name, object) pairs.

  Returns:
    A markdown string
  """
  parts = []
  list_item = '* `{short_name}` <a id="{short_name}"></a>\n'
  list_item_with_value = ('* `{short_name} = {obj!r}` '
                          '<a id="{short_name}"></a>\n')
  for other_member in other_members:
    if doc_generator_visitor.maybe_singleton(other_member.obj):
      part = list_item_with_value.format(**other_member._asdict())
    else:
      part = list_item.format(**other_member._asdict())
    parts.append(part)

  return ''.join(parts)


def _build_method_section(method_info, table_view, heading_level=3):
  """Generates a markdown section for a method.

  Args:
    method_info: A `MethodInfo` object.
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.
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
    parts.append(_small_source_link(method_info.defined_in))

  if method_info.signature is not None:
    parts.append(_build_signature(method_info, obj_name=method_info.short_name))

  parts.append(method_info.doc.brief + '\n')

  for item in method_info.doc.docstring_parts:
    parts.append(_format_docstring(item, table_view, table_title_template=None))

  parts.append(_build_compatibility(method_info.doc.compatibility))
  parts.append('\n\n')
  return ''.join(parts)


def _build_module_parts(module_parts: List[parser.MemberInfo],
                        template: str) -> List[str]:
  mod_str_parts = []
  for item in module_parts:
    mod_str_parts.append(template.format(**item._asdict()))
    if item.doc.brief:
      mod_str_parts.append(': ' + item.doc.brief)
    mod_str_parts.append('\n\n')
  return mod_str_parts


def _build_module_page(page_info: parser.ModulePageInfo,
                       table_view: bool) -> str:
  """Constructs a markdown page given a `ModulePageInfo` object.

  Args:
    page_info: A `ModulePageInfo` object containing information that's used to
      create a module page.
      For example, see https://www.tensorflow.org/api_docs/python/tf/data
    table_view: If True, `Args`, `Returns`, `Raises` or `Attributes` will be
      converted to a tabular format while generating markdown. If False, they
      will be converted to a markdown List view.

  Returns:
    The module markdown page.
  """

  parts = [f'# Module: {page_info.full_name}\n\n']

  parts.append('<!-- Insert buttons and diff -->\n')

  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  # First line of the docstring i.e. a brief introduction about the symbol.
  parts.append(page_info.doc.brief + '\n\n')

  parts.append(_build_collapsable_aliases(page_info.aliases))

  # All lines in the docstring, expect the brief introduction.
  for item in page_info.doc.docstring_parts:
    parts.append(_format_docstring(item, table_view, table_title_template=None))

  parts.append(_build_compatibility(page_info.doc.compatibility))

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
    # TODO(markdaoust): Document the value of the members, for basic types.
    parts.append('## Other Members\n\n')
    parts.append(_other_members(page_info.other_members))

  return ''.join(parts)


DECORATOR_ALLOWLIST = {
    'classmethod',
    'staticmethod',
    'tf_contextlib.contextmanager',
    'contextlib.contextmanager',
    'tf.function',
    'types.method',
    'abc.abstractmethod',
}


def _build_signature(obj_info: parser.PageInfo,
                     obj_name: str,
                     type_alias: bool = False) -> str:
  """Returns a markdown code block containing the function signature.

  Wraps the signature and limits it to 80 characters.

  Args:
    obj_info: Object containing information about the class/method/function for
      which a signature will be created.
    obj_name: The name to use to build the signature.
    type_alias: If True, uses an `=` instead of `()` for the signature.
      For example: `TensorLike = (Union[str, tf.Tensor, int])`.
      Defaults to `False`.

  Returns:
    The signature of the object.
  """

  # Special case tf.range, since it has an optional first argument
  if obj_info.full_name == 'tf.range':
    return textwrap.dedent("""
      ```python
      tf.range(limit, delta=1, dtype=None, name='range')
      tf.range(start, limit, delta=1, dtype=None, name='range')
      ```
      """)

  full_signature = str(obj_info.signature)

  parts = [
      '<pre class="devsite-click-to-copy prettyprint lang-py '
      'tfo-signature-link">'
  ]

  if hasattr(obj_info, 'decorators'):
    parts.extend([
        f'<code>@{dec}</code>' for dec in obj_info.decorators
        if dec in DECORATOR_ALLOWLIST
    ])

  if type_alias:
    parts.append(f'<code>{obj_name} = {full_signature}')
  else:
    parts.append(f'<code>{obj_name}{full_signature}')
  parts.append('</code></pre>\n\n')

  return '\n'.join(parts)


def _build_compatibility(compatibility):
  """Return the compatibility section as an md string."""
  parts = []
  sorted_keys = sorted(compatibility.keys())
  for key in sorted_keys:

    value = compatibility[key]
    # Dedent so that it does not trigger markdown code formatting.
    value = textwrap.dedent(value)
    parts.append(f'\n\n#### {key.title()} Compatibility\n{value}\n')

  return ''.join(parts)


def _top_source_link(location):
  """Retrns a source link with Github image, like the notebook butons."""
  table_template = textwrap.dedent("""
    <table class="tfo-notebook-buttons tfo-api" align="left">
    {}
    </table>

    """)

  link_template = textwrap.dedent("""
    <td>
      <a target="_blank" href="{url}">
        <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
        View source on GitHub
      </a>
    </td>""")

  if location is None or not location.url:
    return table_template.format('')

  if 'github.com' not in location.url:
    return table_template.format('') + _small_source_link(location)

  link = link_template.format(url=location.url)
  table = table_template.format(link)
  return table


def _small_source_link(location):
  """Returns a small source link."""
  template = '<a target="_blank" href="{url}">View source</a>\n\n'

  if not location.url:
    return ''

  return template.format(url=location.url)


def _build_collapsable_aliases(aliases: List[str]) -> str:
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
