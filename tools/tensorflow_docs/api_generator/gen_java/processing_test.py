# Lint as: python3
# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
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
"""Tests for Java doc processing code."""

from absl.testing import absltest

from tensorflow_docs.api_generator.gen_java import processing


class ProcessingTest(absltest.TestCase):

  def test_toc_package_sections(self):
    toc_in = {
        'toc': [{
            'title': 'org.tf',
            'path': '/tf/docs.html',
            'section': [{
                'title': 'SymbolOne',
                'path': '/tf/symbol.html',
            }],
        }, {
            'title':
                'org.tf.foo.baa',
            'path':
                '/tf/foo/baa/docs.html',
            'section': [{
                'title': 'FooBaaOne',
                'path': '/tf/foo/baa/FooOne.html',
            }],
        }, {
            'title':
                'org.tf.foo.bar',
            'path':
                '/tf/foo/bar/docs.html',
            'section': [{
                'title': 'FooBarBuilder',
                'path': '/tf/foo/bar/FooBarBuilder.html',
            }],
        }]
    }
    labels = {
        'org.tf': 'RootLabel',
        'org.tf.foo': 'FooPackage',
    }
    actual_toc = processing.add_package_headings(toc_in, 'org.tf', labels)
    expected_toc = {
        'toc': [
            {
                # New heading inserted, label from labels dict.
                'heading': 'RootLabel',
            },
            {
                'title': 'org.tf',
                'path': '/tf/docs.html',
                'section': [{
                    'title': 'SymbolOne',
                    'path': '/tf/symbol.html',
                }],
            },
            {
                # New heading inserted, label from labels dict.
                'heading': 'FooPackage',
            },
            {
                # Title has package prefix trimmed.
                'title':
                    'foo.baa',
                'path':
                    '/tf/foo/baa/docs.html',
                'section': [{
                    'title': 'FooBaaOne',
                    'path': '/tf/foo/baa/FooOne.html',
                }],
            },
            {
                # Title has package prefix trimmed. Under `foo` heading.
                'title':
                    'foo.bar',
                'path':
                    '/tf/foo/bar/docs.html',
                'section': [{
                    'title': 'FooBarBuilder',
                    'path': '/tf/foo/bar/FooBarBuilder.html',
                }],
            }
        ]
    }
    self.assertDictEqual(actual_toc, expected_toc)


if __name__ == '__main__':
  absltest.main()
