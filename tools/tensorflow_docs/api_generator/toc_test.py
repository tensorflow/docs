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

from tensorflow_docs.api_generator import toc as toc_lib
from tensorflow_docs.api_generator import doc_generator_visitor
from absl.testing import absltest


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


if __name__ == '__main__':
  absltest.main()
