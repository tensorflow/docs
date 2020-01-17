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
"""Tests for py_guide_parser."""

import os
import tempfile
import textwrap

from absl.testing import absltest

from tensorflow_docs.api_generator import py_guide_parser


class TestPyGuideParser(py_guide_parser.PyGuideParser):

  def __init__(self):
    self.calls = []
    py_guide_parser.PyGuideParser.__init__(self)

  def process_title(self, line_number, title):
    self.calls.append((line_number, 'title', title))

  def process_section(self, line_number, section_title, tag):
    self.calls.append((line_number, 'section',
                       '%s : %s' % (section_title, tag)))

  def process_in_blockquote(self, line_number, line):
    self.calls.append((line_number, 'blockquote', line))
    self.replace_line(line_number, line + ' BQ')

  def process_line(self, line_number, line):
    self.calls.append((line_number, 'line', line))


class PyGuideParserTest(absltest.TestCase):
  _BASE_DIR = tempfile.mkdtemp()

  def setUp(self):
    super().setUp()
    self.workdir = os.path.join(self._BASE_DIR, self.id())
    os.makedirs(self.workdir)

  def testBasics(self):
    tmp = os.path.join(self.workdir, 'py_guide_parser_test.md')
    f = open(tmp, 'w')
    f.write(
        textwrap.dedent("""
        # a title
        a line
        ## a section
        ```shell
        in a blockquote
        ```
        out of blockquote
        """)[1:])
    f.close()
    parser = TestPyGuideParser()
    result = parser.process(tmp)
    expected = textwrap.dedent("""
        # a title
        a line
        ## a section
        ```shell BQ
        in a blockquote BQ
        ```
        out of blockquote
        """)[1:]
    self.assertEqual(expected, result)
    expected = [(0, 'title', 'a title'), (1, 'line', 'a line'),
                (2, 'section', 'a section : a_section'),
                (3, 'blockquote', '```shell'),
                (4, 'blockquote', 'in a blockquote'), (5, 'line', '```'),
                (6, 'line', 'out of blockquote'), (7, 'line', '')]
    self.assertEqual(expected, parser.calls)


if __name__ == '__main__':
  absltest.main()
