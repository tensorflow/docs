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

import enum
import json
import os
import pathlib
import re
import sys
import textwrap

from typing import Any, Dict, List

from absl import app
from absl import flags

from tensorflow_docs.tools.nbfmt import notebook_utils

OSS = True

flags.DEFINE_integer(
    "indent", 2, "Indention level for pretty-printed JSON.", lower_bound=0)
flags.DEFINE_bool("oss", None, "Use OSS formatting.")
flags.DEFINE_bool("remove_outputs", False,
                  "Remove output cells from the notebook")
flags.DEFINE_bool("test", False,
                  "Test if the notebook is formatted (useful for CI).")

FLAGS = flags.FLAGS


def clean_notebook(data: Dict[str, Any], nb_source: str, filepath: pathlib.Path,
                   remove_outputs: bool, indent: int) -> bytes:
  """The main notebook formatting logic.

  Args:
    data: object representing a parsed JSON notebook.
    nb_source: JSON string of entire notebook contents.
    filepath: String of notebook filepath passed to the command-line.
    remove_outputs: Boolean to clear cell output.
    indent: Integer indicating the number of spaces to indent the JSON.

  Returns:
    A byte string for the JSON formatted notebook.
  """
  clean_root(data, filepath)  # Top-level notebook fields.
  clean_cells(data, nb_source, remove_outputs)
  update_license_cells(data)

  nbjson = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=indent)

  if not OSS:
    # Serialization differences in enviroments.
    str_replaces = {"<": r"\u003c", ">": r"\u003e", "&": r"\u0026"}
    for str_from, str_to in str_replaces.items():
      nbjson = nbjson.replace(str_from, str_to)

  return (nbjson + "\n").encode("utf-8")


def clean_root(data: Dict[str, Any], filepath: pathlib.Path) -> None:
  """Deletes extra top-level notebook fields and metadata.

  Jupyter format spec:
  https://nbformat.readthedocs.io/en/latest/format_description.html

  Args:
    data: object representing a parsed JSON notebook.
    filepath: String of notebook filepath passed to the command-line.
  """
  # These top-level fields are required:
  notebook_utils.del_entries_except(
      data, keep=["cells", "metadata", "nbformat_minor", "nbformat"])
  # All metadata is optional according to spec, but we use some of it.
  notebook_utils.del_entries_except(
      data["metadata"], keep=["accelerator", "colab", "kernelspec"])

  metadata = data.get("metadata", {})
  colab = metadata.get("colab", {})

  # Set top-level notebook defaults.
  data["nbformat"] = 4
  data["nbformat_minor"] = 0

  # Colab metadata
  notebook_utils.del_entries_except(
      colab, keep=["collapsed_sections", "name", "toc_visible"])
  colab["name"] = os.path.basename(filepath)
  colab["toc_visible"] = True
  metadata["colab"] = colab

  # Kernelspec metadata
  kernelspec = metadata.get("kernelspec", {})
  notebook_utils.del_entries_except(kernelspec, keep=["display_name", "name"])

  supported_kernels = {"python3": "Python 3", "swift": "Swift"}
  kernel_name = kernelspec.get("name")
  if kernel_name not in supported_kernels:
    kernel_name = "python3"  # Notebook defaults to Python3 (same as Colab).

  kernelspec["name"] = kernel_name
  kernelspec["display_name"] = supported_kernels[kernel_name]
  metadata["kernelspec"] = kernelspec

  data["metadata"] = metadata


def _clean_code_cell(cell_data: Dict[str, Any], remove_outputs: bool) -> None:
  """Clean an individual code cell and optionally remove outputs.

  Args:
    cell_data: object representing a parsed JSON cell.
    remove_outputs: Boolean to clear cell output.
  """
  if remove_outputs:
    cell_data["outputs"] = []
    cell_data["execution_count"] = None

  # Ensure outputs field exists since part of the nbformat spec.
  if cell_data.get("outputs", None) is None:
    cell_data["outputs"] = []

  # Spec allows null or int (null is Colab default).
  if cell_data.get("execution_count") == 0:
    cell_data["execution_count"] = None


def _clean_metadata_colab(cell_metadata: Dict[str, Any],
                          remove_outputs: bool) -> None:
  """Clean up a cell's `metadata.colab` field.

  Remove all `metadata.colab` contents except for `metadata.colab.resources`, if
  present. The Colab resources are used to embed data within the notebook and
  can be treated like output cells (kept unless explictly removed).

  Args:
    cell_metadata: object representing the parsed JSON metadata from a cell.
    remove_outputs: Boolean to clear cell output.
  """
  colab = cell_metadata.pop("colab", {})
  # If no outputs, just clear out `metadata.colab`.
  if remove_outputs:
    return

  # Clear around `resources` if not empty. Otherwise, clear out `metata.colab`.
  if colab.get("resources"):
    notebook_utils.del_entries_except(colab, keep=["resources"])
    cell_metadata["colab"] = colab


def clean_cells(data: Dict[str, Any], nb_source: str,
                remove_outputs: bool) -> None:
  """Remove empty cells and clean code cells.

  Args:
    data: Object representing a parsed JSON notebook.
    nb_source: JSON string of entire notebook contents.
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

  # Remove empty cells.
  data["cells"] = [cell for cell in data["cells"] if any(cell["source"])]

  # Clean cell metadata.
  cell_count = 0
  for cell in data["cells"]:
    cell_count += 1
    cell_metadata = cell.get("metadata", {})
    if "id" not in cell_metadata:
      cell_metadata["id"] = notebook_utils.generate_cell_id(
          cell["source"], cell_count)
    notebook_utils.del_entries_except(
        cell_metadata, keep=["id", "cellView", "colab"])
    _clean_metadata_colab(cell_metadata, remove_outputs)

    cell["metadata"] = cell_metadata

  # The presence of this field indicates that ouputs are already saved.
  has_outputs = True if '"output_type"' in nb_source else False

  for cell in data["cells"]:
    if cell["cell_type"] == "code":
      _clean_code_cell(cell, remove_outputs)

  if has_outputs and remove_outputs:
    notebook_utils.warn("Removed the existing output cells.")


def update_license_cells(data: Dict[str, Any]) -> None:
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


class Status(enum.Enum):
  PASS = 0
  FAIL = 1


def format_nb(
    *,
    notebooks: List[str],
    remove_outputs: bool = False,
    indent: int = 2,
    test: bool = False,
) -> Status:
  """Formats a notebook."""
  found_error = False  # Track errors for final return code.
  test_fail_notebooks = []
  paths, err_paths = notebook_utils.collect_notebook_paths(notebooks)

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

    # Returns formatted JSON byte string.
    expected_output = clean_notebook(data, source, path, remove_outputs, indent)

    if test:
      # Compare formatted contents with original file contents.
      src_bytes = path.read_bytes()
      if expected_output != src_bytes:
        test_fail_notebooks.append(path)
    else:
      path.write_bytes(expected_output)

  if test:
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
      return Status.FAIL
    else:
      print("[test] Notebooks are formatted", file=sys.stderr)
      return Status.PASS

  if found_error:
    return Status.FAIL

  return Status.PASS


def main(argv):
  if len(argv) <= 1:
    raise app.UsageError("Missing arguments.")

  if FLAGS.oss is not None:
    global OSS
    OSS = FLAGS.oss

  exit_code = format_nb(
      notebooks=argv[1:],
      remove_outputs=FLAGS.remove_outputs,
      indent=FLAGS.indent,
      test=FLAGS.test)
  if exit_code == Status.FAIL:
    sys.exit(1)
  else:
    sys.exit(0)


if __name__ == "__main__":
  app.run(main)
