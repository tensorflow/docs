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

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import doc_generator_visitor

from tensorflow_docs.api_generator.pretty_docs import base_page
from tensorflow_docs.api_generator.pretty_docs import function_page


class ParserTest(absltest.TestCase):

  def test_github_source_link_in_table(self):
    url = "https://github.com/tensorflow/docs/blob/master/path/to/file"
    location = parser.FileLocation(base_url=url)
    table = base_page.top_source_link(location)

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
    location = parser.FileLocation(base_url=url)
    table = base_page.top_source_link(location)

    expected = textwrap.dedent(f"""
       <table class="tfo-notebook-buttons tfo-api nocontent" align="left">

       </table>

       <a target="_blank" class="external" href="{url}">View source</a>

       """)
    self.assertEqual(expected, table)

  def test_no_source_link(self):
    location = parser.FileLocation()
    table = base_page.top_source_link(location)

    expected = textwrap.dedent("""
       <table class="tfo-notebook-buttons tfo-api nocontent" align="left">

       </table>

       """)
    self.assertEqual(expected, table)

  def _get_test_page_builder(self, search_hints):

    def test_function():
      pass

    api_node = doc_generator_visitor.ApiTreeNode(
        path=('abc',), py_object=test_function, children={})
    page_info = function_page.FunctionPageInfo(
        api_node=api_node, search_hints=search_hints)
    docstring_info = parser.DocstringInfo(
        brief='hello `tensorflow`',
        docstring_parts=['line1', 'line2'],
        compatibility={})
    page_info.set_doc(docstring_info)
    page_builder = function_page.FunctionPageBuilder(page_info)
    return page_builder

  def test_get_headers_global_hints(self):
    page_builder = self._get_test_page_builder(search_hints=True)
    result = page_builder.get_devsite_headers()

    expected = textwrap.dedent("""\
      description: hello tensorflow

      <div itemscope itemtype="http://developers.google.com/ReferenceObject">
      <meta itemprop="name" content="abc" />
      <meta itemprop="path" content="Stable" />
      </div>
      """)

    self.assertEqual(expected, result)

  def test_get_headers_global_no_hints(self):
    page_builder = self._get_test_page_builder(search_hints=False)
    result = page_builder.get_devsite_headers()

    expected = textwrap.dedent("""\
      description: hello tensorflow
      robots: noindex
      """)

    self.assertEqual(expected, result)

  def test_get_headers_local_no_hints(self):
    page_builder = self._get_test_page_builder(search_hints=True)
    result = page_builder.get_devsite_headers()

    @doc_controls.hide_from_search
    def py_object():
      pass

    page_builder.page_info.py_object = py_object

    result = page_builder.get_devsite_headers()

    expected = textwrap.dedent("""\
      description: hello tensorflow
      robots: noindex
      """)

    self.assertEqual(expected, result)


if __name__ == "__main__":
  absltest.main()
