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
r"""Example api reference docs generation script.

This script generates API reference docs for the reference doc generator.

$> pip install -U git+https://github.com/tensorflow/docs
$> python build_docs.py
"""

import os

from absl import app
from absl import flags

import tensorflow_docs
from tensorflow_docs.api_generator import generate_lib
from tensorflow_docs.api_generator import public_api

PROJECT_SHORT_NAME = 'tfdocs'
PROJECT_FULL_NAME = 'TensorFlow Docs'

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'output_dir',
    default='/tmp/generated_docs',
    help='Where to write the resulting docs to.')
flags.DEFINE_string('code_url_prefix',
                    ('https://github.com/tensorflow/docs/tree/master/tools/tensorflow_docs'),
                    'The url prefix for links to code.')

flags.DEFINE_bool('search_hints', True,
                  'Include metadata search hints in the generated files')

flags.DEFINE_string('site_path', '/api_docs/python',
                    'Path prefix in the _toc.yaml')

flags.DEFINE_bool('gen_report', False,
                  ('Generate an API report containing the health of the'
                   'docstrings of the public API.'))


def gen_api_docs():
  """Generates api docs for the tensorflow docs package."""

  # The below `del`'s are to avoid the api_gen_test to not document these.
  # Please remove these lines from your build_docs.py files when you create
  # them.
  del tensorflow_docs.google
  del tensorflow_docs.api_generator.report.schema

  doc_generator = generate_lib.DocGenerator(
      root_title=PROJECT_FULL_NAME,
      # Replace `tensorflow_docs` with your module, here.
      py_modules=[(PROJECT_SHORT_NAME, tensorflow_docs)],
      # Replace `tensorflow_docs` with your module, here.
      base_dir=os.path.dirname(tensorflow_docs.__file__),
      code_url_prefix=FLAGS.code_url_prefix,
      search_hints=FLAGS.search_hints,
      site_path=FLAGS.site_path,
      gen_report=FLAGS.gen_report,
      # This callback cleans up a lot of aliases caused by internal imports.
      callbacks=[public_api.local_definitions_filter],
  )

  doc_generator.build(FLAGS.output_dir)

  print('Output docs to: ', FLAGS.output_dir)


def main(argv):
  if argv[1:]:
    raise ValueError('Unrecognized arguments: {}'.format(argv[1:]))

  gen_api_docs()


if __name__ == '__main__':
  app.run(main)
