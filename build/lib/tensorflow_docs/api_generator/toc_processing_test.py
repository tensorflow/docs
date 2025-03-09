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

from tensorflow_docs.api_generator import toc_processing


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
    actual_toc = toc_processing.add_package_headings(toc_in, ['org.tf'], labels)
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

  def test_multiple_roots(self):
    toc_in = {
        'toc': [{
            'title': 'org.tf.one',
        }, {
            'title': 'com.google.two',
        }]
    }
    roots = ['org.tf', 'com.google']
    actual_toc = toc_processing.add_package_headings(toc_in, roots, {})
    expected_toc = {
        'toc': [
            {
                'heading': 'one'
            },
            {
                'title': 'one'
            },
            {
                'heading': 'two'
            },
            {
                'title': 'two'
            },
        ]
    }
    self.assertEqual(actual_toc['toc'], expected_toc['toc'])

  def test_overlapping_packages(self):
    toc_in = {
        'toc': [{
            'title': 'org.tf.one',
            'path': '/tf/one/docs.html',
            'section': [{
                'title': 'SymbolOne',
                'path': '/tf/one/symbol.html',
            }],
        }, {
            'title':
                'org.tf.one.two',
            'path':
                '/tf/one/two/docs.html',
            'section': [{
                'title': 'SymbolOneTwo',
                'path': '/tf/one/two/SymbolOneTwo.html',
            }],
        }]
    }
    labels = {
        'org.tf.one': 'Section One',
        'org.tf.one.two': 'Section Two',
    }
    actual_toc = toc_processing.add_package_headings(toc_in, ['org.tf'], labels)
    expected_toc = {
        'toc': [{
            'heading': 'Section One',
        }, {
            'title': 'one',
            'path': '/tf/one/docs.html',
            'section': [{
                'title': 'SymbolOne',
                'path': '/tf/one/symbol.html',
            }],
        }, {
            'heading': 'Section Two',
        }, {
            'title':
                'one.two',
            'path':
                '/tf/one/two/docs.html',
            'section': [{
                'title': 'SymbolOneTwo',
                'path': '/tf/one/two/SymbolOneTwo.html',
            }],
        }]
    }
    self.assertEqual(actual_toc['toc'], expected_toc['toc'])

  def test_nesting_toc(self):
    toc_in = {
        'toc': [{
            'title': 'tf_lite.support',
            'path': '/tflite/support.html',
        }, {
            'title': 'tf_lite.support.cls',
            'path': '/tflite/support/cls.html',
        }, {
            'title': 'tf_lite.task.things',
            'path': '/tflite/task/things.html',
        }, {
            'title': 'tf_other.widgets',
            'path': '/tfother/widgets.html',
        }]
    }
    actual_toc = toc_processing.nest_toc(toc_in)
    expected_toc = {
        'toc': [{
            'title':
                'tf_lite',
            'section': [{
                'title':
                    'support',
                'path':
                    '/tflite/support.html',
                'section': [{
                    'title': 'cls',
                    'path': '/tflite/support/cls.html'
                }]
            }, {
                'title':
                    'task',
                'section': [{
                    'title': 'things',
                    'path': '/tflite/task/things.html'
                }]
            }]
        }, {
            'title': 'tf_other',
            'section': [{
                'title': 'widgets',
                'path': '/tfother/widgets.html'
            }]
        }]
    }
    self.assertEqual(actual_toc['toc'], expected_toc['toc'])

  def test_ordering(self):
    toc_in = {
        'toc': [
            {
                'title': 'org.tf.a.third'
            },
            {
                'title': 'org.tf.b.first'
            },
            {
                'title': 'com.google.c.second'
            },
            {
                'title': 'ai.google.d.unspecified'
            },
        ]
    }
    labels = ['org.tf.b', 'com.google.c', 'org.tf']
    actual_toc = toc_processing.sort_toc(toc_in, labels)
    expected_toc = {
        'toc': [
            {
                'title': 'org.tf.b.first'
            },
            {
                'title': 'com.google.c.second'
            },
            {
                'title': 'org.tf.a.third'
            },
            {
                'title': 'ai.google.d.unspecified'
            },
        ]
    }
    self.assertDictEqual(actual_toc, expected_toc)


if __name__ == '__main__':
  absltest.main()
