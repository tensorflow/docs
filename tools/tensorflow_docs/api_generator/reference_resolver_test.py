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
"""Tests for documentation parser."""

import os
import tempfile
import textwrap

from typing import Dict, List, Optional, Union

from absl.testing import absltest
from absl.testing import parameterized


from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import reference_resolver as reference_resolver_lib



class TestReferenceResolver(absltest.TestCase):
  _BASE_DIR = tempfile.mkdtemp()

  def setUp(self):
    super(TestReferenceResolver, self).setUp()
    self.workdir = os.path.join(self._BASE_DIR, self.id())
    os.makedirs(self.workdir)

  def testSaveReferenceResolver(self):
    duplicate_of = {'AClass': ['AClass2']}
    is_fragment = {
        'tf': False,
        'tf.VERSION': True,
        'tf.AClass': False,
        'tf.AClass.method': True,
        'tf.AClass2': False,
        'tf.function': False
    }
    py_module_names = {'tf': 'tensorflow'}

    resolver = reference_resolver_lib.ReferenceResolver(
        duplicate_of=duplicate_of,
        is_fragment=is_fragment,
        py_module_names=py_module_names)

    outdir = self.workdir

    filepath = os.path.join(outdir, 'resolver.json')

    resolver.to_json_file(filepath)
    resolver2 = reference_resolver_lib.ReferenceResolver.from_json_file(
        filepath)

    # There are no __slots__, so all fields are visible in __dict__.
    self.assertEqual(resolver.__dict__, resolver2.__dict__)

  def test_duplicate_fragment(self):
    duplicate_of = {
        'tf.Class2.method': 'tf.Class1.method',
        'tf.sub.Class2.method': 'tf.Class1.method',
        'tf.sub.Class2': 'tf.Class2'
    }
    is_fragment = {
        'tf.Class1.method': True,
        'tf.Class2.method': True,
        'tf.sub.Class2.method': True,
        'tf.Class1': False,
        'tf.Class2': False,
        'tf.sub.Class2': False
    }
    py_module_names = {'tf': 'tensorflow'}

    reference_resolver = reference_resolver_lib.ReferenceResolver(
        duplicate_of=duplicate_of,
        is_fragment=is_fragment,
        py_module_names=py_module_names,
        link_prefix='')

    # Method references point to the method, in the canonical class alias.
    result = reference_resolver.reference_to_url('tf.Class1.method')
    self.assertEqual('tf/Class1.md#method', result)
    result = reference_resolver.reference_to_url('tf.Class2.method')
    self.assertEqual('tf/Class2.md#method', result)
    result = reference_resolver.reference_to_url('tf.sub.Class2.method')
    self.assertEqual('tf/Class2.md#method', result)

    # Class references point to the canonical class alias
    result = reference_resolver.reference_to_url('tf.Class1')
    self.assertEqual('tf/Class1.md', result)
    result = reference_resolver.reference_to_url('tf.Class2')
    self.assertEqual('tf/Class2.md', result)
    result = reference_resolver.reference_to_url('tf.sub.Class2')
    self.assertEqual('tf/Class2.md', result)


class TestPartialSymbolAutoRef(parameterized.TestCase):
  REF_TEMPLATE = '<a href="{link}"><code>{text}</code></a>'

  @parameterized.named_parameters(
      ('basic1', 'keras.Model.fit', '../tf/keras/Model.md#fit'),
      ('duplicate_object', 'layers.Conv2D', '../tf/keras/layers/Conv2D.md'),
      ('parens', 'Model.fit(x, y, epochs=5)', '../tf/keras/Model.md#fit'),
      ('duplicate_name', 'tf.matmul', '../tf/linalg/matmul.md'),
      ('full_name', 'tf.concat', '../tf/concat.md'),
      ('normal_and_compat', 'linalg.matmul', '../tf/linalg/matmul.md'),
      ('compat_only', 'math.deprecated', None),
      ('contrib_only', 'y.z', None),
  )
  def test_partial_symbol_references(self, string, link):
    duplicate_of = {
        'tf.matmul': 'tf.linalg.matmul',
        'tf.layers.Conv2d': 'tf.keras.layers.Conv2D',
    }

    is_fragment = {
        'tf.keras.Model.fit': True,
        'tf.concat': False,
        'tf.keras.layers.Conv2D': False,
        'tf.linalg.matmul': False,
        'tf.compat.v1.math.deprecated': False,
        'tf.compat.v1.linalg.matmul': False,
        'tf.contrib.y.z': False,
    }

    py_module_names = {'tf': 'tensorflow'}

    resolver = reference_resolver_lib.ReferenceResolver(
        duplicate_of=duplicate_of,
        is_fragment=is_fragment,
        py_module_names=py_module_names,
        link_prefix='..')
    input_string = string.join('``')
    ref_string = resolver.replace_references(input_string)

    if link is None:
      expected = input_string
    else:
      expected = self.REF_TEMPLATE.format(link=link, text=string)

    self.assertEqual(expected, ref_string)


class TestIgnoreLineInBlock(parameterized.TestCase):

  @parameterized.named_parameters(
      ('ignore_backticks', ['```'], ['```'],
       '```\nFiller\n```\n```Same line```\n```python\nDowner\n```'),
      ('ignore_code_cell_output', ['<pre>{% html %}'], ['{% endhtml %}</pre>'],
       '<pre>{% html %}\nOutput\nmultiline{% endhtml %}</pre>'),
      ('ignore_backticks_and_cell_output', ['<pre>{% html %}', '```'
                                           ], ['{% endhtml %}</pre>', '```'],
       ('```\nFiller\n```\n```Same line```\n<pre>{% html %}\nOutput\nmultiline'
        '{% endhtml %}</pre>\n```python\nDowner\n```')))
  def test_ignore_lines(self, block_start, block_end, expected_ignored_lines):

    text = textwrap.dedent("""\
    ```
    Filler
    ```

    ```Same line```

    <pre>{% html %}
    Output
    multiline{% endhtml %}</pre>

    ```python
    Downer
    ```
    """)

    filters = [
        reference_resolver_lib.IgnoreLineInBlock(start, end)
        for start, end in zip(block_start, block_end)
    ]

    ignored_lines = []
    for line in text.splitlines():
      if any(filter_block(line) for filter_block in filters):
        ignored_lines.append(line)

    self.assertEqual('\n'.join(ignored_lines), expected_ignored_lines)

  def test_clean_text(self):
    text = textwrap.dedent("""\
    ```
    Ignore lines here.
    ```
    Useful information.
    Don't ignore.
    ```python
    Ignore here too.
    ```
    Stuff.
    ```Not useful.```
    """)

    filters = [reference_resolver_lib.IgnoreLineInBlock('```', '```')]

    clean_text = []
    for line in text.splitlines():
      if not any(filter_block(line) for filter_block in filters):
        clean_text.append(line)

    expected_clean_text = 'Useful information.\nDon\'t ignore.\nStuff.'

    self.assertEqual('\n'.join(clean_text), expected_clean_text)


if __name__ == '__main__':
  absltest.main()
