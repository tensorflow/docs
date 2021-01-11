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
"""Tests for MD page generator."""

import textwrap

from absl.testing import absltest

from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import pretty_docs


class ParserTest(absltest.TestCase):

  def test_github_source_link_in_table(self):
    url = "https://github.com/tensorflow/docs/blob/master/path/to/file"
    location = parser._FileLocation(url=url)
    table = pretty_docs._top_source_link(location)

    expected = textwrap.dedent(f"""
        <table class="tfo-notebook-buttons tfo-api nocontent" align="left">
        <td>
          <a target="_blank" href="{url}">
            <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
            View source on GitHub
          </a>
        </td>
        </table>

        """)
    self.assertEqual(expected, table)

  def test_other_source_link_after_table(self):
    url = "somewhere/else"
    location = parser._FileLocation(url=url)
    table = pretty_docs._top_source_link(location)

    expected = textwrap.dedent(f"""
       <table class="tfo-notebook-buttons tfo-api nocontent" align="left">

       </table>

       <a target="_blank" href="{url}">View source</a>

       """)
    self.assertEqual(expected, table)

  def test_no_source_link(self):
    location = parser._FileLocation()
    table = pretty_docs._top_source_link(location)

    expected = textwrap.dedent("""
       <table class="tfo-notebook-buttons tfo-api nocontent" align="left">

       </table>

       """)
    self.assertEqual(expected, table)


if __name__ == "__main__":
  absltest.main()
