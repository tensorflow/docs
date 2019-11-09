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
"""A module for converting parsed doc content into markdown pages.

The adjacent `parser` module creates `PageInfo` objects, containing all data
necessary to document an element of the TensorFlow API.

This module contains one public function, which handels the conversion of these
`PageInfo` objects into a markdown string:

    md_page = build_md_page(page_info)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import textwrap

from tensorflow_docs.api_generator import doc_generator_visitor


def build_md_page(page_info):
  """Given a PageInfo object, return markdown for the page.

  Args:
    page_info: must be a `parser.FunctionPageInfo`, `parser.ClassPageInfo`, or
      `parser.ModulePageInfo`

  Returns:
    Markdown for the page

  Raises:
    ValueError: if `page_info` is an instance of an unrecognized class
  """
  if page_info.for_function():
    return _build_function_page(page_info)

  if page_info.for_class():
    return _build_class_page(page_info)

  if page_info.for_module():
    return _build_module_page(page_info)

  raise ValueError('Unknown Page Info Type: %s' % type(page_info))


def _build_function_page(page_info):
  """Given a FunctionPageInfo object Return the page as an md string."""
  parts = ['# %s\n\n' % page_info.full_name]

  parts.append('<!-- Insert buttons -->\n')

  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  parts.append('<!-- Start diff -->\n')

  parts.append(page_info.doc.brief + '\n\n')

  if page_info.aliases:
    parts.append('### Aliases:\n\n')
    parts.extend('* `%s`\n' % name for name in page_info.aliases)
    parts.append('\n\n')

  if page_info.signature is not None:
    parts.append(_build_signature(page_info))
    parts.append('\n\n')

  # This will be replaced by the "Used in: <notebooks>" whenever it is run.
  parts.append('<!-- Placeholder for "Used in" -->\n')

  parts.extend(str(item) for item in page_info.doc.docstring_parts)
  parts.append(_build_compatibility(page_info.doc.compatibility))

  return ''.join(parts)


def _build_class_page(page_info):
  """Given a ClassPageInfo object Return the page as an md string."""
  parts = ['# {page_info.full_name}\n\n'.format(page_info=page_info)]

  parts.append('<!-- Insert buttons -->\n')

  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  parts.append('## Class `%s`\n\n' % page_info.full_name.split('.')[-1])

  parts.append('<!-- Start diff -->\n')

  parts.append(page_info.doc.brief + '\n\n')

  if page_info.bases:
    parts.append('Inherits From: ')

    link_template = '[`{short_name}`]({url})'
    parts.append(', '.join(
        link_template.format(**base._asdict()) for base in page_info.bases))

  parts.append('\n\n')

  if page_info.aliases:
    parts.append('### Aliases:\n\n')
    parts.extend('* Class `%s`\n' % name for name in page_info.aliases)
    parts.append('\n\n')

  # This will be replaced by the "Used in: <notebooks>" whenever it is run.
  parts.append('<!-- Placeholder for "Used in" -->\n')

  parts.extend(str(item) for item in page_info.doc.docstring_parts)
  parts.append(_build_compatibility(page_info.doc.compatibility))

  parts.append('\n\n')

  # Sort the methods list, but make sure constructors come first.
  constructor_names = ['__init__', '__new__']
  constructors = sorted(method for method in page_info.methods
                        if method.short_name in constructor_names)
  other_methods = sorted(method for method in page_info.methods
                         if method.short_name not in constructor_names)

  if constructors:
    for method_info in constructors:
      parts.append(_build_method_section(method_info, heading_level=2))
    parts.append('\n\n')

  if page_info.classes:
    parts.append('## Child Classes\n')

    link_template = ('[`class {class_info.short_name}`]'
                     '({class_info.url})\n\n')
    class_links = sorted(
        link_template.format(class_info=class_info)
        for class_info in page_info.classes)

    parts.extend(class_links)

  if page_info.properties:
    parts.append('## Properties\n\n')
    for prop_info in page_info.properties:
      h3 = '<h3 id="{short_name}"><code>{short_name}</code></h3>\n\n'
      parts.append(h3.format(short_name=prop_info.short_name))

      parts.append(prop_info.doc.brief + '\n')
      parts.extend(str(item) for item in prop_info.doc.docstring_parts)
      parts.append(_build_compatibility(prop_info.doc.compatibility))

      parts.append('\n\n')

    parts.append('\n\n')

  if other_methods:
    parts.append('## Methods\n\n')

    for method_info in other_methods:
      parts.append(_build_method_section(method_info))
    parts.append('\n\n')

  if page_info.other_members:
    parts.append('## Class Members\n\n')

    parts.append(_other_members(page_info.other_members))

  return ''.join(parts)


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
    parts.append(_small_source_link(method_info.defined_in))

  if method_info.signature is not None:
    parts.append(_build_signature(method_info, use_full_name=False))

  parts.append(method_info.doc.brief + '\n')
  parts.extend(str(item) for item in method_info.doc.docstring_parts)
  parts.append(_build_compatibility(method_info.doc.compatibility))
  parts.append('\n\n')
  return ''.join(parts)


def _build_module_page(page_info):
  """Given a ClassPageInfo object Return the page as an md string."""
  parts = ['# Module: {full_name}\n\n'.format(full_name=page_info.full_name)]

  parts.append(_top_source_link(page_info.defined_in))
  parts.append('\n\n')

  # First line of the docstring i.e. a brief introduction about the symbol.
  parts.append(page_info.doc.brief + '\n\n')

  if page_info.aliases:
    parts.append('### Aliases:\n\n')
    parts.extend('* Module `%s`\n' % name for name in page_info.aliases)
    parts.append('\n\n')

  # All lines in the docstring, expect the brief introduction.
  parts.extend(str(item) for item in page_info.doc.docstring_parts)
  parts.append(_build_compatibility(page_info.doc.compatibility))

  parts.append('\n\n')

  if page_info.modules:
    parts.append('## Modules\n\n')
    template = '[`{short_name}`]({url}) module'

    for item in page_info.modules:
      parts.append(template.format(**item._asdict()))

      if item.doc.brief:
        parts.append(': ' + item.doc.brief)

      parts.append('\n\n')

  if page_info.classes:
    parts.append('## Classes\n\n')
    template = '[`class {short_name}`]({url})'

    for item in page_info.classes:
      parts.append(template.format(**item._asdict()))

      if item.doc.brief:
        parts.append(': ' + item.doc.brief)

      parts.append('\n\n')

  if page_info.functions:
    parts.append('## Functions\n\n')
    template = '[`{short_name}(...)`]({url})'

    for item in page_info.functions:
      parts.append(template.format(**item._asdict()))

      if item.doc.brief:
        parts.append(': ' + item.doc.brief)

      parts.append('\n\n')

  if page_info.other_members:
    # TODO(markdaoust): Document the value of the members,
    #                   at least for basic types.
    parts.append('## Other Members\n\n')

    parts.append(_other_members(page_info.other_members))

  return ''.join(parts)


def _build_signature(obj_info, use_full_name=True):
  """Returns a md code block showing the function signature."""
  # Special case tf.range, since it has an optional first argument
  if obj_info.full_name == 'tf.range':
    return ('``` python\n'
            "tf.range(limit, delta=1, dtype=None, name='range')\n"
            "tf.range(start, limit, delta=1, dtype=None, name='range')\n"
            '```\n\n')

  parts = ['``` python']
  parts.extend(['@' + dec for dec in obj_info.decorators])
  signature_template = '{name}({sig})'

  if not obj_info.signature:
    sig = ''
  elif len(obj_info.signature) == 1:
    sig = obj_info.signature[0]
  else:
    sig = ',\n'.join('    %s' % sig_item for sig_item in obj_info.signature)
    sig = '\n' + sig + '\n'

  if use_full_name:
    obj_name = obj_info.full_name
  else:
    obj_name = obj_info.short_name
  parts.append(signature_template.format(name=obj_name, sig=sig))
  parts.append('```\n\n')

  return '\n'.join(parts)


def _build_compatibility(compatibility):
  """Return the compatibility section as an md string."""
  parts = []
  sorted_keys = sorted(compatibility.keys())
  for key in sorted_keys:

    value = compatibility[key]
    # Dedent so that it does not trigger markdown code formatting.
    value = textwrap.dedent(value)
    parts.append('\n\n#### %s Compatibility\n%s\n' % (key.title(), value))

  return ''.join(parts)


GENERATED_FILE_TEMPLATE = 'Defined in generated file: `{path}`\n\n'


def _top_source_link(location):
  """Retrns a source link with Github image, like the notebook butons."""
  table_template = textwrap.dedent("""
    <table class="tfo-notebook-buttons tfo-api" align="left">
    {}</table>

    """)

  link_template = textwrap.dedent("""
    <td>
      <a target="_blank" href="{url}">
        <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
        View source on GitHub
      </a>
    </td>""")

  if location is None:
    return table_template.format('')

  if not location.url:
    return (table_template.format('') +
            GENERATED_FILE_TEMPLATE.format(path=location.rel_path))

  if 'github.com' not in location.url:
    return table_template.format('') + _small_source_link(location)

  link = link_template.format(url=location.url)
  table = table_template.format(link)
  return table


def _small_source_link(location):
  """Returns a small source link."""
  template = '<a target="_blank" href="{url}">View source</a>\n\n'

  if not location.url:
    return GENERATED_FILE_TEMPLATE.format(path=location.rel_path)

  return template.format(url=location.url)
