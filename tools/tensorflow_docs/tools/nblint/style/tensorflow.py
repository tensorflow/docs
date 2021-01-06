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
r"""Lint assertions for notebooks published on tensorflow.org.

These lints are a non-exhaustive implemention of style rules found in the
TensorFlow documentation and style guides. See:

- https://www.tensorflow.org/community/contribute/docs
- https://www.tensorflow.org/community/contribute/docs_style

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
import urllib

from tensorflow_docs.tools.nblint import fix
from tensorflow_docs.tools.nblint.decorator import fail
from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options


# Acceptable copyright heading for notebooks following this style.
copyrights_re = [
    r"Copyright 20[1-9][0-9] The TensorFlow\s.*?\s?Authors",
    r"Copyright 20[1-9][0-9] Google"
]


@lint(message="Copyright required", scope=Options.Scope.TEXT)
def copyright_check(args):
  cell_source = args["cell_source"]
  return any(re.search(pattern, cell_source) for pattern in copyrights_re)


license_re = re.compile("#@title Licensed under the Apache License")


@lint(
    message="Apache license cell is required",
    scope=Options.Scope.CODE,
    cond=Options.Cond.ANY)
def license_check(args):
  if license_re.search(args["cell_source"]):
    return True
  else:
    template_url = "https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb"
    fail(f"License cell missing or doesn't follow template: {template_url}")


@lint(scope=Options.Scope.FILE)
def not_translation(args):
  if "site" not in args["path"].parents:
    return True
  else:
    return "site/en" in args["path"].parents


# Button checks

is_button_cell_re = re.compile(r"class.*tfo-notebook-buttons")


def get_arg_or_fail(user_args, arg_name, arg_fmt):
  """Get value of the user-defined arg passed at the command-line.

  Args:
    user_args: Dict containing user-defined args passed at command-line.
    arg_name: String name of user-defined arg.
    arg_fmt: String format of expected user-defined arg.

  Returns:
    Value of arg passed to command-line. If the arg does not exist, raise a
    failure, log a message, and skip the lint function.
  """
  if arg_name in user_args:
    return user_args.get(arg_name)
  else:
    fail(
        f"Requires user-argument '{arg_name}': nblint --arg={arg_name}:{arg_fmt} ...",
        always_show=True)


def split_doc_path(filepath):
  """Return paths for docs root prefix directory and the relative path to file.

  Given a full path to notebook file, standalone or within an established
  documentation directory layout, split the provided path into two:
  1. a path reprsenting the prefix directory to the docs root (if it exists),
  2. the relative path to the file from the docs root directory.
  If in an unknown docs directory layout, return an empty prefix path and the
  full path of the original argument.

  For example:
  "site/en/notebook.ipynb" => ("site/en", "notebook.ipynb")
  "tensorflow/docs/notebook.ipynb" => ("docs", "notebook.ipynb")
  "unknown/path/notebook.ipynb" => ("", "unknown/path/notebook.ipynb")

  Args:
    filepath: `pathlib.Path` to a documentation notebook.

  Returns:
    pathlib.Path: The path of the doc root prefix directory., if applicable.
    pathlib.Path: The relative path to notebook from the prefix directory.
  """
  fp_full = filepath.resolve()  # Check full path for sub-elements.

  def split_path_on_dir(fp, dirname, offset=1):
    parts = fp.parts
    idx = parts.index(dirname)
    docs_dir = pathlib.Path(*parts[idx:idx + offset])
    rel_path = fp.relative_to(*parts[:idx + offset])
    return docs_dir, rel_path

  if "site" in fp_full.parts:
    return split_path_on_dir(fp_full, "site", offset=2)  # site/<lang>/
  elif "docs" in fp_full.parts:
    return split_path_on_dir(fp_full, "docs")
  elif "g3doc" in fp_full.parts:
    idx = fp_full.parts.index("g3doc")
    if fp_full.parts[idx + 1] == "en":
      offset = 2
    else:
      offset = 1
    return split_path_on_dir(fp_full, "g3doc", offset=offset)
  else:
    # Unknown setup. Return empty root and unsplit path.
    return pathlib.Path(), filepath


@lint(
    message="Missing or malformed URL in Colab button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_colab(args):
  """Test that the URL in the Colab button matches the file path."""
  cell_source = args["cell_source"]
  repo = get_arg_or_fail(args["user"], "repo", "<org/name>")
  docs_dir, rel_path = split_doc_path(args["path"])

  # Buttons use OSS URLs.
  if str(docs_dir) == "g3doc/en":
    docs_dir = pathlib.Path("site/en")

  base_url = f"colab.research.google.com/github/{repo}/blob/master"
  this_url = "https://" + str(base_url / docs_dir / rel_path)

  if is_button_cell_re.search(cell_source) and cell_source.find(this_url) != -1:
    return True
  else:
    fail(
        f"Colab button URL doesn't match: {this_url}",
        fix=fix.regex_between_groups_replace_all,
        fix_args=[r"(href.*)http.*?(\\\".*colab_logo_32px.png)", this_url])


@lint(
    message="Missing or malformed URL in Download button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_download(args):
  """Test that the URL in the Download button matches the file path."""
  cell_source = args["cell_source"]
  repo = get_arg_or_fail(args["user"], "repo", "<org/name>")
  repo_name = pathlib.Path(repo.split("/")[1])
  docs_dir, rel_path = split_doc_path(args["path"])

  if "r1" in rel_path.parts:
    return True  # No download button for TF 1.x docs.

  # Buttons use OSS URLs.
  if str(docs_dir) == "g3doc/en":
    docs_dir = pathlib.Path("site/en")

  this_url = urllib.parse.urljoin(
      "https://storage.googleapis.com",
      str(f"tensorflow_docs/{repo_name}" / docs_dir / rel_path))

  if is_button_cell_re.search(cell_source) and cell_source.find(this_url) != -1:
    return True
  else:
    fail(
        f"Download button URL doesn't match: {this_url}",
        fix=fix.regex_between_groups_replace_all,
        fix_args=[r"(href.*)http.*?(\\\".*download_logo_32px.png)", this_url])


@lint(
    message="Missing or malformed URL in GitHub button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_github(args):
  """Test that the URL in the GitHub button matches the file path."""
  cell_source = args["cell_source"]
  repo = get_arg_or_fail(args["user"], "repo", "<org/name>")
  docs_dir, rel_path = split_doc_path(args["path"])

  # Buttons use OSS URLs.
  if str(docs_dir) == "g3doc/en":
    docs_dir = pathlib.Path("site/en")

  base_url = f"github.com/{repo}/blob/master"
  this_url = "https://" + str(base_url / docs_dir / rel_path)

  if is_button_cell_re.search(cell_source) and cell_source.find(this_url) != -1:
    return True
  else:
    fail(
        f"GitHub button URL doesn't match: {this_url}",
        fix=fix.regex_between_groups_replace_all,
        fix_args=[r"(href.*)http.*?(\\\".*GitHub-Mark-32px.png)", this_url])


@lint(
    message="Missing or malformed URL in 'View on' button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_website(args):
  """Test that the website URL in the 'View on' button matches the file path.

  Because of subsites and different output directories, the exact website path
  can't be known from the file alone. But can check that the URL matches a
  correct pattern.

  Args:
    args: Nested dict of runtime arguments.

  Returns:
    Boolean: True if lint test passes, False if not.
  """
  cell_source = args["cell_source"]
  docs_dir, rel_path = split_doc_path(args["path"])

  if "r1" in rel_path.parts:
    return True  # No website button for TF 1.x docs.

  if str(docs_dir) == "site/zh-cn" or str(docs_dir) == "site/zh-tw":
    base_url = "https://tensorflow.google.cn/"
  else:
    base_url = "https://www.tensorflow.org/"

  # Construct website URL pattern based on location of this file in repo.
  url_path = rel_path.with_suffix("")
  # If run in source repo, we don't know for certain the published subsite URL.
  # Match: base/<optional-subsite-path>/notebook-path
  this_url = rf"{base_url}[\w\-/]*{url_path}"

  if is_button_cell_re.search(cell_source) and re.search(this_url, cell_source):
    return True
  else:
    # If included verbatim, bracket will fail lint. That's desired.
    url_format = f"{base_url}<OPTIONAL-SUBSITE-PATH>/{url_path}"
    fail(f"'View on' button URL doesn't match pattern: {url_format}")


@lint(
    message="Missing or malformed URL in 'TFHub' button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_hub(args):
  """Notebooks that mention tfhub.dev should have a TFHub button."""
  cell_source = args["cell_source"]
  file_source = args["file_source"]

  hub_url = "https://tfhub.dev/"

  # Only check files that mention TFHub.
  if file_source.find(hub_url) == -1:
    return True

  if is_button_cell_re.search(cell_source) and cell_source.find(hub_url) != -1:
    return True
  else:
    # If included verbatim, bracket will fail lint. That's desired.
    url_format = f"{hub_url}<MODEL-OR-COLLECTION>"
    fail(f"'TFHub' button URL doesn't match pattern: {url_format}")


@lint(
    message="Remove extra buttons from TF 1.x docs.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ALL)
def button_r1_extra(args):
  """The r1/ docs should not have website or download buttons."""
  cell_source = args["cell_source"]
  docs_dir, rel_path = split_doc_path(args["path"])

  # Only test r1/ notebooks.
  if "r1" not in rel_path.parts:
    return True
  # Only check text cells that contain the button nav bar.
  if not is_button_cell_re.search(cell_source):
    return True

  download_url = "https://storage.googleapis.com/tensorflow_docs/"
  if str(docs_dir) == "site/zh-cn" or str(docs_dir) == "site/zh-tw":
    base_url = "https://tensorflow.google.cn/"
  else:
    base_url = "https://www.tensorflow.org/"

  # Look for button URLs that shouldn't be there..
  if (re.search(f"{base_url}/(?!images)", cell_source) or
      cell_source.find(download_url) != -1):
    fail(
        "Remove the 'View on' and 'Download notebook' buttons since r1/ docs are not published."
    )
  else:
    return True
