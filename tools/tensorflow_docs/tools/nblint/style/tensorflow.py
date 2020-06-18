# Lint as: python3
# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
r"""Lint assertions that adhere to the TensorFlow documentation guide.

This style module is a non-exhaustive implemention of style rules found in the
TensorFlow documentation and style guides. See:

- https://www.tensorflow.org/community/contribute/docs
- https://www.tensorflow.org/community/contribute/docs_style

When adding lints, please link to the URL of the relevant style rule, if
applicable.

Lint callback functions are passed an `args` dict with the following entries:
  cell_data: Dict of parsed cell (cell-scope only)
  cell_source: String of cell content (cell-scope only)
  file_data: Dict of parsed notebook
  file_source: String of notebook content
  path: Filepath of notebook
  user: Dict of args passed at the command-line
"""
import re

from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options

copyright_re = re.compile(
    r"Copyright 20[1-9][0-9] The TensorFlow\s.*?\s?Authors")


@lint(message="TensorFlow copyright is required", scope=Options.Scope.TEXT)
def copyright_check(args):
  if copyright_re.search(args["cell_source"]):
    return True
  else:
    return False


license_re = re.compile("#@title Licensed under the Apache License")


@lint(
    message="Apache license is required",
    scope=Options.Scope.CODE,
    cond=Options.Cond.ANY)
def license_check(args):
  if license_re.search(args["cell_source"]):
    return True
  else:
    return False


@lint(scope=Options.Scope.FILE)
def not_translation(args):
  if "site" not in args["path"].parents:
    return True
  else:
    return "site/en" in args["path"].parents
