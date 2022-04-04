# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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

import io
import textwrap
import types

from absl.testing import absltest

from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import toc as toc_lib


class TestToc(absltest.TestCase):

  def test_toc_write(self):
    link = toc_lib.Link(title='A link', path='/path/to/link')
    link2 = toc_lib.Link(
        title='Another link',
        path='/path/to/link2',
        status=toc_lib.Status.EXTERNAL)

    subsection = toc_lib.Section(
        title='A subsection',
        section=[link],
        status=toc_lib.Status.EXPERIMENTAL)

    toc = toc_lib.Toc([
        # pyformat: disable
        toc_lib.Heading('Hello'),
        link,
        link2,
        toc_lib.Break(),
        subsection
    ])

    stream = io.StringIO()
    toc.write(stream)

    expected = textwrap.dedent("""\
        toc:
        - heading: Hello
        - title: A link
          path: /path/to/link
        - title: Another link
          status: external
          path: /path/to/link2
        - break: true
        - title: A subsection
          status: experimental
          section:
          - title: A link
            path: /path/to/link
        """)

    self.assertEqual(expected, stream.getvalue())

  def test_replace(self):
    link = toc_lib.Link(title='A link', path='/path/to/link')
    new_link = link.replace(status=toc_lib.Status.NEW, title='New title.')

    expected = toc_lib.Link(
        title='New title.', path='/path/to/link', status=toc_lib.Status.NEW)
    self.assertEqual(expected, new_link)

  def _make_tree(self) -> doc_generator_visitor.ApiTree:
    api_tree = doc_generator_visitor.ApiTree()
    api_tree.insert(
        path=('module',), py_object=types.ModuleType('module'), aliases=[])
    api_tree.insert(path=('module', 'func1'), py_object=lambda x: x, aliases=[])
    api_tree.insert(
        path=('module', 'Class'),
        py_object=types.new_class('Class'),
        aliases=[])
    api_tree.insert(
        path=('module', 'Class', 'method'), py_object=lambda x: x, aliases=[])
    api_tree.insert(
        path=('module', 'Class', 'NestedClass'),
        py_object=types.new_class('NestedClass'),
        aliases=[])
    api_tree.insert(
        path=('module', 'Class', 'NestedClass', 'method2'),
        py_object=lambda x: x,
        aliases=[])
    api_tree.insert(
        path=('module', 'Class', 'constant'),
        py_object='Just a string.',
        aliases=[])
    api_tree.insert(
        path=('module', 'submodule'),
        py_object=types.ModuleType('submodule'),
        aliases=[])
    api_tree.insert(
        path=('module', 'submodule', 'func2'),
        py_object=lambda x: x,
        aliases=[])
    api_tree.insert(
        path=('module', 'submodule', 'constant'),
        py_object='Another string.',
        aliases=[])
    return api_tree

  def test_toc_builder(self):
    api_tree = self._make_tree()
    builder = toc_lib.TocBuilder('/path/in/site')
    toc = builder.build(api_tree)
    stream = io.StringIO()
    toc.write(stream)

    expected = textwrap.dedent("""\
        toc:
        - title: module
          section:
          - title: Overview
            path: /path/in/site/module
          - title: Class
            path: /path/in/site/module/Class
          - title: Class.NestedClass
            path: /path/in/site/module/Class/NestedClass
          - title: func1
            path: /path/in/site/module/func1
          - title: submodule
            section:
            - title: Overview
              path: /path/in/site/module/submodule
            - title: func2
              path: /path/in/site/module/submodule/func2
        """)

    self.assertEqual(expected, stream.getvalue())

  def test_flat_modules_builder(self):
    api_tree = self._make_tree()
    builder = toc_lib.FlatModulesTocBuilder('/path/in/site')
    toc = builder.build(api_tree)
    stream = io.StringIO()
    toc.write(stream)

    expected = textwrap.dedent("""\
        toc:
        - title: module
          section:
          - title: Overview
            path: /path/in/site/module
          - title: Class
            path: /path/in/site/module/Class
          - title: Class.NestedClass
            path: /path/in/site/module/Class/NestedClass
          - title: func1
            path: /path/in/site/module/func1
        - title: module.submodule
          section:
          - title: Overview
            path: /path/in/site/module/submodule
          - title: func2
            path: /path/in/site/module/submodule/func2
        """)

    self.assertEqual(expected, stream.getvalue())


if __name__ == '__main__':
  absltest.main()
