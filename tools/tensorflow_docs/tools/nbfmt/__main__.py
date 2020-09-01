#!/usr/bin/env python3
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
r"""Format notebooks using the TensorFlow docs style.

Install the tensorflow-docs package:
$ python3 -m pip install -U [--user] git+https://github.com/tensorflow/docs

Usage:
$ python3 -m tensorflow_docs.tools.nbfmt [options] notebook.ipynb [...]

See the TensorFlow notebook template:
https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb
And the TensorFlow docs contributor guide:
https://www.tensorflow.org/community/contribute/docs
"""
import json
import os
import pathlib
import re
import sys
import textwrap

from typing import Any, Dict, Optional

from absl import app
from absl import flags

from tensorflow_docs.tools.nbfmt import notebook_utils

OSS = True

flags.DEFINE_bool("remove_outputs", False,
                  "Remove output cells from the notebook")
flags.DEFINE_integer(
    "indent", 2, "Indention level for pretty-printed JSON.", lower_bound=0)
flags.DEFINE_bool("test", False,
                  "Test if the notebook is formatted (useful for CI).")

FLAGS = flags.FLAGS


def warn(msg: str) -> None:
  """Print highlighted warning message to stderr.

  Args:
    msg: String to print to console.
  """
  # Use terminal codes to print color output to console.
  print(f" \033[33m {msg}\033[00m", file=sys.stderr)


def remove_extra_fields(data: Dict[str, Any]) -> None:
  """Deletes extra notebook fields.

  Jupyter format spec:
  https://nbformat.readthedocs.io/en/latest/format_description.html

  Args:
    data: object representing a parsed JSON notebook.
  """

  def filter_keys(data, keep_list) -> None:
    to_delete = set(data.keys()) - frozenset(keep_list)
    for key in to_delete:
      del data[key]

  # These top-level fields are required:
  filter_keys(data, ["cells", "metadata", "nbformat_minor", "nbformat"])
  # All metadata is optional according to spec, but we use some of it.
  # For example, this removes "language_info" and other editor-specific fields.
  filter_keys(data["metadata"], ["accelerator", "colab", "kernelspec"])


def _clean_code_cell(cell_data: Dict[str, Any], remove_outputs: bool) -> None:
  """Clean an individual code cell and optionally remove outputs.

  Args:
    cell_data: object representing a parsed JSON cell.
    remove_outputs: Boolean to clear cell output.
  """
  # Clean cell metadata.
  cell_meta = cell_data.get("metadata", {})
  cell_meta.pop("executionInfo", None)
  cell_meta.pop("ExecuteTime", None)

  if "colab" in cell_meta:
    cell_meta["colab"].pop("base_uri", None)

  cell_data["metadata"] = cell_meta

  if remove_outputs:
    cell_data["outputs"] = []
    cell_data["execution_count"] = None

  # Ensure outputs field exists since part of the nbformat spec.
  if cell_data.get("outputs", None) is None:
    cell_data["outputs"] = []

  # Spec allows null or int (null is Colab default).
  if cell_data.get("execution_count") == 0:
    cell_data["execution_count"] = None


def clean_cells(data: Dict[str, Any], nb_source: str,
                remove_outputs: bool) -> None:
  """Remove empty cells and clean code cells.

  Args:
    data: Object representing a parsed JSON notebook.
    nb_source: String of entire notebook contents.
    remove_outputs: Boolean True to remove code cell outputs, False to keep.
  """
  # Clear leading and trailing newlines.
  for cell in data["cells"]:
    cell_source = cell["source"]
    while cell_source and cell_source[0] == "\n":
      cell_source.pop(0)
    while cell_source and cell_source[-1] == "\n":
      cell_source.pop()
    cell["source"] = cell_source

  # remove empty cells
  data["cells"] = [cell for cell in data["cells"] if any(cell["source"])]

  # The presence of this field indicates that ouputs are already saved.
  has_outputs = True if '"output_type"' in nb_source else False

  for cell in data["cells"]:
    if cell["cell_type"] == "code":
      _clean_code_cell(cell, remove_outputs)

  if has_outputs and remove_outputs:
    warn("Removed the existing output cells.")


def update_metadata(data: Dict[str, Any],
                    filepath: Optional[pathlib.Path] = None) -> None:
  """Set notebook metadata on `data` object using TF docs style.

  Args:
    data: object representing a parsed JSON notebook.
    filepath: String of notebook filepath passed to the command-line.
  """
  metadata = data.get("metadata", {})
  colab = metadata.get("colab", {})
  # Set preferred metadata for notebook docs.
  if filepath is not None:
    colab["name"] = os.path.basename(filepath)

  colab["provenance"] = []
  colab["toc_visible"] = True
  # Use Colab default that allows saved outputs in this notebook.
  colab.pop("private_outputs", None)
  colab.pop("last_runtime", None)  # Always remove "last_runtime".
  metadata["colab"] = colab

  # kernelspec: name: display_name
  supported_kernels = {"python3": "Python 3", "swift": "Swift"}
  kernel_name = metadata.get("kernelspec", {}).get("name")

  if kernel_name not in supported_kernels:
    kernel_name = "python3"  # Notebook defaults to Python3 (same as Colab).

  # Use new dict to clear any other attributes.
  metadata["kernelspec"] = {
      "name": kernel_name,
      "display_name": supported_kernels[kernel_name]
  }

  data["metadata"] = metadata


def update_license_cell(data: Dict[str, Any]) -> None:
  """Format license cell to hide code pane from the Colab form.

  Args:
    data: object representing a parsed JSON notebook.
  """
  # This pattern in Apache and MIT license boilerplate.
  license_re = re.compile(r"#@title.*License")

  for idx, cell in enumerate(data["cells"]):
    src_text = "".join(cell["source"])

    if license_re.search(src_text):
      # Hide code pane from license form
      metadata = cell.get("metadata", {})
      metadata["cellView"] = "form"
      data["cells"][idx]["metadata"] = metadata


def main(argv):
  if len(argv) <= 1:
    raise app.UsageError("Missing arguments.")

  found_error = False  # Track errors for final return code.
  test_fail_notebooks = []
  paths, err_paths = notebook_utils.collect_notebook_paths(argv[1:])

  if err_paths:
    found_error = True
    test_fail_notebooks.extend(err_paths)

  for path in paths:
    print(f"Format notebook: {path}", file=sys.stderr)

    data, source = notebook_utils.load_notebook(path)

    if not data:
      found_error = True
      test_fail_notebooks.append(path)
      continue

    # Set top-level notebook defaults.
    data["nbformat"] = 4
    data["nbformat_minor"] = 0

    remove_extra_fields(data)  # Top-level fields.
    clean_cells(data, source, FLAGS.remove_outputs)
    update_metadata(data, filepath=path)
    update_license_cell(data)

    nbjson = json.dumps(
        data, sort_keys=True, ensure_ascii=False, indent=FLAGS.indent)

    if not OSS:
      # Serialization differences in enviroments.
      str_replaces = {"<": r"\u003c", ">": r"\u003e", "&": r"\u0026"}
      for str_from, str_to in str_replaces.items():
        nbjson = nbjson.replace(str_from, str_to)

    expected_output = (nbjson + "\n").encode("utf-8")

    if FLAGS.test:
      # Compare formatted contents with original file contents.
      src_bytes = path.read_bytes()
      if expected_output != src_bytes:
        test_fail_notebooks.append(path)
    else:
      path.write_bytes(expected_output)

  if FLAGS.test:
    if test_fail_notebooks:
      error_template = textwrap.dedent("""
      [test] The following notebooks are not formatted:
      {notebooks}
      Please install `nbfmt` and format:
      $ python3 -m pip install -U --user git+https://github.com/tensorflow/docs
      $ python3 -m tensorflow_docs.tools.nbfmt notebook.ipynb
      """)
      notebooks = "\n".join([f"- {str(fp)}" for fp in test_fail_notebooks])
      print(error_template.format(notebooks=notebooks), file=sys.stderr)
      sys.exit(1)
    else:
      print("[test] Notebooks are formatted", file=sys.stderr)
      sys.exit(0)

  if found_error:
    sys.exit(1)


if __name__ == "__main__":
  app.run(main)
