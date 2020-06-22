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

from tensorflow_docs.tools.nblint.decorator import fail
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


# Button checks

is_button_cell_re = re.compile(r"class.*tfo-notebook-buttons")


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

  def split_path_on_dir(fp, dirname, offset=1):
    parts = fp.parts
    idx = parts.index(dirname)
    docs_dir = pathlib.Path(*parts[idx:idx + offset])
    rel_path = fp.relative_to(*parts[:idx + offset])
    return docs_dir, rel_path

  if "site" in filepath.parts:
    return split_path_on_dir(filepath, "site", offset=2)  # site/<lang>/
  elif "docs" in filepath.parts:
    return split_path_on_dir(filepath, "docs")
  elif "g3doc" in filepath.parts:
    idx = filepath.parts.index("g3doc")
    if filepath.parts[idx + 1] == "en":
      offset = 2
    else:
      offset = 1
    return split_path_on_dir(filepath, "g3doc", offset=offset)
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
  repo_name = args["user"].get("repo")  # User-defined arg
  docs_dir, rel_path = split_doc_path(args["path"])

  if not repo_name:
    fail(
        "Requires user-argument 'repo': nblint --arg=repo:<org/name> ...",
        always_show=True)

  # Construct Colab URL based on location of this file in repo.
  if str(docs_dir) == "g3doc/en":
    docs_dir = pathlib.Path("site/en")  # Test for OSS URLs.

  base_url = f"colab.research.google.com/github/{repo_name}/blob/master"
  this_url = "https://" + str(base_url / docs_dir / rel_path)

  if is_button_cell_re.search(cell_source) and cell_source.find(this_url) != -1:
    return True
  else:
    fail(f"Colab button URL doesn't match: {this_url}")


@lint(
    message="Missing or malformed URL in GitHub button.",
    scope=Options.Scope.TEXT,
    cond=Options.Cond.ANY)
def button_github(args):
  """Test that the URL in the GitHub button matches the file path."""
  cell_source = args["cell_source"]
  repo_name = args["user"].get("repo")  # User-defined arg
  docs_dir, rel_path = split_doc_path(args["path"])

  if not repo_name:
    fail(
        "Requires user-argument 'repo': nblint --arg=repo:<org/name> ...",
        always_show=True)

  # Construct GitHub URL based on location of this file in repo.
  if str(docs_dir) == "g3doc/en":
    docs_dir = pathlib.Path("site/en")  # Test for OSS URLs.

  base_url = f"github.com/{repo_name}/blob/master"
  this_url = "https://" + str(base_url / docs_dir / rel_path)

  if is_button_cell_re.search(cell_source) and cell_source.find(this_url) != -1:
    return True
  else:
    fail(f"GitHub button URL doesn't match: {this_url}")


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
    # No button since TF 1.x docs are not published on website.
    return True

  if str(docs_dir) == "site/zh-cn" or str(docs_dir) == "site/zh-tw":
    base_url = "https://tensorflow.google.cn/"
  else:
    base_url = "https://www.tensorflow.org/"

  # Construct website URL patterb based on location of this file in repo.
  url_path = rel_path.with_suffix("")
  this_url = f"{base_url}.*{url_path}"

  if is_button_cell_re.search(cell_source) and re.search(this_url, cell_source):
    return True
  else:
    fail(f"'View on' button URL doesn't match pattern: {this_url}")
