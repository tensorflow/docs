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

OSS = True

flags.DEFINE_bool(
    "preserve_outputs", None,
    "Configures the notebook to either preserve, or clear outputs."
    "- If `True`: Set the notebook to keep outputs.\n"
    "- If `False`: Set the notebook to clear outputs.\n"
    "- If unset (`None`): keep the notebook's current setting.\n"
    "  - If it's not set in the notebook, set the notebook to preserve outputs "
    "(to match the colab default).\n"
    "If a notebook is configured to clear outputs, this script will clear them "
    "when run.\n"
    "Colab respects this setting. Jupyter does not.")
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


def remove_extra_fields(data) -> None:
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


def clean_cells(data) -> None:
  """Remove empty cells and strip outputs from `data` object.

  Args:
    data: object representing a parsed JSON notebook.
  """
  remove_extra_fields(data)

  # Clear leading and trailing newlines.
  for cell in data["cells"]:
    source = cell["source"]
    while source and source[0] == "\n":
      source.pop(0)
    while source and source[-1] == "\n":
      source.pop()
    cell["source"] = source

  # remove empty cells
  data["cells"] = [cell for cell in data["cells"] if any(cell["source"])]

  # `private_outputs` will default to False. If `private_outputs` is True, then
  # the output will be removed from the notebook.
  private_outputs = (
      data.get("metadata", {}).get("colab", {}).get("private_outputs", False))

  has_outputs = False
  for cell in data["cells"]:
    if cell["cell_type"] != "code":
      continue

    # Clean cell metadata: remove the "executionInfo" block, this is what adds
    # the little user photos in Colab.
    cell_meta = cell.get("metadata", {})
    cell_meta.pop("executionInfo", None)
    cell["metadata"] = cell_meta

    # Clear any code cell outputs if notebook set to private outputs.
    if private_outputs and cell.get("outputs"):
      has_outputs = True
      # Clear code outputs
      cell["execution_count"] = 0
      cell["outputs"] = []

    # Ensure outputs field exists since part of the nbformat spec.
    if cell.get("outputs", None) is None:
      cell["outputs"] = []

    # Spec allows null or integer, but use null since it's the Colab default.
    if cell.get("execution_count") == 0:
      cell["execution_count"] = None

  if has_outputs:
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

  files = []
  for path in argv[1:]:
    path = pathlib.Path(path)
    if path.is_file():
      files.append(path)
    elif path.is_dir():
      files.extend(path.rglob("*.ipynb"))
    else:
      found_error = True
      warn(f"Invalid file or directory: {str(path)}")

  for fp in files:
    print(f"Notebook: {fp}", file=sys.stderr)

    if fp.suffix != ".ipynb":
      warn("Not an '.ipynb' file, skipping.")
      found_error = True
      test_fail_notebooks.append(fp)
      continue

    with open(fp, "r", encoding="utf-8") as f:
      try:
        data = json.load(f)
      except ValueError as err:
        print(f"  {err.__class__.__name__}: {err}", file=sys.stderr)
        warn("Unable to load JSON, skipping.")
        found_error = True
        test_fail_notebooks.append(fp)
        continue

    if FLAGS.preserve_outputs is not None:
      # Overwrite the value of `private_outputs`
      colab = data.get("metadata", {}).get("colab", {})
      colab["private_outputs"] = not FLAGS.preserve_outputs
      data["metadata"]["colab"] = colab

    # Set top-level notebook defaults.
    data["nbformat"] = 4
    data["nbformat_minor"] = 0

    clean_cells(data)
    update_metadata(data, filepath=fp)
    update_license_cell(data)

    nbjson = json.dumps(
        data, sort_keys=True, ensure_ascii=False, indent=FLAGS.indent)
    if not OSS:
      nbjson = nbjson.replace("<", r"\u003c").replace(">", r"\u003e")
    expected_output = (nbjson + "\n").encode("utf-8")

    if FLAGS.test:
      # Compare formatted contents with original file contents.
      src_bytes = fp.read_bytes()
      if expected_output != src_bytes:
        test_fail_notebooks.append(fp)
    else:
      fp.write_bytes(expected_output)

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
