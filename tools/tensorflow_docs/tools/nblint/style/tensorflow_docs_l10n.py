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
r"""Lint assertions specific to the tensorflow/docs-l10n repo.

When adding lints, link to the URL of the relevant style rule, if applicable.

Lint functions return a boolean: True to pass, False to fail.
For @lint options, see the docstrings in `decorator.py`.

Lint callback functions are passed an `args` dict with the following entries:
  cell_data: Dict of parsed cell (cell-scope only)
  cell_source: String of cell content (cell-scope only)
  file_data: Dict of parsed notebook
  file_source: String of notebook content
  path: Filepath of notebook
  user: Dict of args passed at the command-line
"""
import pathlib
import re

from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options
from tensorflow_docs.tools.nblint.style.tensorflow import split_doc_path


@lint(
    message="Edit en/ source files over here: https://github.com/tensorflow/docs",
    scope=Options.Scope.FILE)
def is_translation(args):
  """Only doc translations in this repo; edit source files elsewhere."""
  fp_parents = args["path"].resolve().parents

  if pathlib.Path("site") not in fp_parents:
    return True  # Not a doc translation, ignore.
  elif pathlib.Path("site/en") in fp_parents:
    return False
  elif pathlib.Path("site/en-snapshot") in fp_parents:
    return False
  else:
    return True


# Catch tensorflow.org hostname usage in Chinese docs. Ignore false positives
# for the Google Group (../a/tensorflow.org/..), email (docs*@tensorflow.org),
# and subdomains like (download|js).tensorflow.org.
has_tf_hostname_re = re.compile(
    r"(?<!/a/)(?<!@)(?<!download\.)(?<!js\.)(www\.)?tensorflow\.org")


@lint(
    message="Replace 'www.tensorflow.org' URL with 'tensorflow.google.cn' in Chinese docs.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ALL)
def china_hostname_url(args):
  """Chinese docs should use tensorflow.google.cn as the URL hostname.

  Replace hostname 'www.tensorflow.org' with 'tensorflow.google.cn'.

  Args:
    args: Nested dict of runtime arguments.

  Returns:
    Boolean: True if lint test passes, False if not.
  """
  docs_dir, _ = split_doc_path(args["path"])

  if str(docs_dir) == "site/zh-cn" or str(docs_dir) == "site/zh-tw":
    if has_tf_hostname_re.search(args["cell_source"]):
      return False
    else:
      return True
  else:
    return True
