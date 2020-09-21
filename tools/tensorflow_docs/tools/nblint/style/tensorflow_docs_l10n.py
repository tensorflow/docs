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
import re

from tensorflow_docs.tools.nblint import fix
from tensorflow_docs.tools.nblint.decorator import fail
from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options
from tensorflow_docs.tools.nblint.style.tensorflow import is_button_cell_re
from tensorflow_docs.tools.nblint.style.tensorflow import split_doc_path


@lint(
    message="Only edit translated files. Source files are here: https://github.com/tensorflow/docs",
    scope=Options.Scope.FILE)
def is_translation(args):
  """Translations live in the site/<lang>/ directory of the docs-l10n repo."""
  path_str = str(args["path"].resolve())

  if "site/" not in path_str:
    return False
  elif "site/en/" in path_str:
    return False
  elif "site/en-snapshot/" in path_str:
    return False
  else:
    return True


# Catch tensorflow.org hostname usage in Chinese docs. Ignore false positives
# for the Google Group (../a/tensorflow.org/..), email (docs*@tensorflow.org),
# and subdomains like (blog|download|js).tensorflow.org.
has_tf_hostname_re = re.compile(
    r"(?<!/a/)(?<!@)(?<!download\.)(?<!js\.)(www\.)(blog\.)?tensorflow\.org",
    re.IGNORECASE)


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

  # Only applicable for China docs.
  if str(docs_dir) != "site/zh-cn" and str(docs_dir) != "site/zh-tw":
    return True

  if has_tf_hostname_re.search(args["cell_source"]):
    fail(
        fix=fix.regex_replace_all,
        fix_args=[has_tf_hostname_re.pattern, "tensorflow.google.cn"])
  else:
    return True


has_rtl_div_re = re.compile(r"<div\s*dir\s*=\s*[\"']rtl[\"'].*>", re.IGNORECASE)
has_copyright_re = re.compile(r"Copyright 20[1-9][0-9]")


@lint(
    message="RTL languages must wrap all text cell elements with: <div dir=\"rtl\">...</div>",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ALL)
def rtl_language_wrap(args):
  """Check that RTL languages wrap text elemenst in a directional div.

  Required for languages like Arabic to render correctly in Colab. Some care
  must be taken or any Markdown syntax within the div will break.

  Args:
    args: Nested dict of runtime arguments.

  Returns:
    Boolean: True if lint test passes, False if not.
  """
  docs_dir, _ = split_doc_path(args["path"])

  # Only applicable for RTL languages.
  if str(docs_dir) != "site/ar":
    return True

  cell_source = args["cell_source"]

  # Ignore the text cells for copyright and buttons.
  if (has_copyright_re.search(cell_source) or
      is_button_cell_re.search(cell_source)):
    return True

  if has_rtl_div_re.search(cell_source):
    return True
  else:
    fail(
        "Wrap all text elements in `<div dir=\"rtl\">...</div>` for Colab. But check this doesn't break any Markdown syntax within."
    )
