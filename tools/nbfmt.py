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

Usage:
$ nbfmt.py [options] notebook.ipynb [...]
$ find . -name "*\.ipynb" | xargs ./tools/nbfmt.py [--ignore_warn]

See the TensorFlow notebook template:
https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb
And the TensorFlow docs contributor guide:
https://www.tensorflow.org/community/contribute/docs
"""
import collections
import json
import os
import pathlib
import re
import sys
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
    "  - If it's not set in the notebook, set the notebook to perserve outputs "
    "(to match the colab default).\n"
    "If a notebook is configured to clear outputs, this script will clear them "
    "when run.\n"
    "Colab respects this setting. Juptyer does not.")
flags.DEFINE_bool("ignore_warn", False, "Overwrite notebook despite warnings.")
flags.DEFINE_integer(
    "indent", 2, "Indention level for pretty-printed JSON.", lower_bound=0)

FLAGS = flags.FLAGS

_REQUIRED_REGEXPS = {
    "copyright": r"Copyright 20[1-9][0-9] The TensorFlow\s.*?\s?Authors",
    "TF2 Version": r"(%tensorflow_version 2.x|tensorflow.compat.v2)"
}


def warn(msg: str) -> None:
  """Print highlighted warning message to stderr.

  Args:
    msg: String to print to console.
  """
  # Use terminal codes to print color output to console.
  print(f" \033[33m {msg}\033[00m", file=sys.stderr)


def delete_cells(data) -> None:
  """Remove empty cells and strip outputs from `data` object.

  Args:
    data: object representing a parsed JSON notebook.
  """
  # remove empty cells
  data["cells"] = [cell for cell in data["cells"] if any(cell["source"])]

  # `private_outputs` will default to False. If `private_outputs` is True, then
  # the output will be removed from the notebook.
  private_outputs = (
      data.get("metadata", {}).get("colab", {}).get("private_outputs", False))
  if not private_outputs:
    return

  has_outputs = False
  for idx, _ in enumerate(data["cells"]):
    cell = data["cells"][idx]
    if cell["cell_type"] == "code" and cell.get("outputs"):
      has_outputs = True
      # Clear code outputs
      data["cells"][idx]["execution_count"] = 0
      data["cells"][idx]["outputs"] = []

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
  metadata["colab"] = metadata.get("colab", {})
  # Set preferred metadata for notebook docs.
  if filepath is not None:
    metadata["colab"]["name"] = os.path.basename(filepath)

  metadata["colab"]["provenance"] = []
  metadata["colab"]["toc_visible"] = True
  data["metadata"] = metadata


def has_license_and_update(data: Dict[str, Any]) -> bool:
  """Check if license header exists anywhere in notebook and format.

  Args:
    data: object representing a parsed JSON notebook.

  Returns:
    Boolean: True if notebook contains the license header, False if it doesn't.
  """
  has_license = False
  license_header = "#@title Licensed under the Apache License"

  for idx, cell in enumerate(data["cells"]):
    src_text = "".join(cell["source"])

    if license_header in src_text:
      has_license = True
      # Hide code pane from license form
      metadata = cell.get("metadata", {})
      metadata["cellView"] = "form"
      data["cells"][idx]["metadata"] = metadata

  if not has_license:
    warn(f"Missing license: {license_header}")

  return has_license


def has_required_regexps(data: Dict[str, Any]) -> bool:
  """Check if all regexp patterns are found in a notebook.

  Args:
    data: object representing a parsed JSON notebook.

  Returns:
    Boolean: True if notebook contains all the patterns, False if it doesn't.
  """
  has_all_patterns = True

  for desc, pattern in _REQUIRED_REGEXPS.items():
    regexp = re.compile(pattern)
    has_pattern = False

    for cell in data["cells"]:
      src_text = "".join(cell["source"])
      if regexp.search(src_text):
        has_pattern = True
        break  # Found this match so skip the rest of the notebook.

    if not has_pattern:
      warn(f"Missing {desc}: {pattern}")
      has_all_patterns = False
      return False

  return has_all_patterns


def main(argv):
  if len(argv) <= 1:
    raise app.UsageError("Missing arguments.")

  did_skip = False  # Track errors for final return code.

  for arg in argv[1:]:
    fp = pathlib.Path(arg)

    print(f"Notebook: {fp}", file=sys.stderr)

    if fp.suffix != ".ipynb":
      warn("Not an '.ipynb' file, skipping.")
      did_skip = True
      continue

    with open(fp, "r", encoding="utf-8") as f:
      try:
        data = json.load(f)
      except ValueError as err:
        print(f"  {err.__class__.__name__}: {err}", file=sys.stderr)
        warn("Unable to load JSON, skipping.")
        did_skip = True
        continue

    if FLAGS.preserve_outputs is not None:
      # Overwrite the value of `private_outputs`
      colab = data.get("metadata", {}).get("colab", {})
      colab["private_outputs"] = not FLAGS.preserve_outputs
      data["metadata"]["colab"] = colab

    delete_cells(data)
    update_metadata(data, filepath=fp)
    has_license = has_license_and_update(data)
    has_patterns = has_required_regexps(data)

    if not FLAGS.ignore_warn:
      if not has_license or not has_patterns:
        print(
            "  Found warnings. Notebook not written, skipping.",
            file=sys.stderr)
        did_skip = True
        continue

    nbjson = json.dumps(
        data, sort_keys=True, ensure_ascii=False, indent=FLAGS.indent)
    if not OSS:
      nbjson = nbjson.replace("<", r"\u003c").replace(">", r"\u003e")

    with open(fp, "w", encoding="utf-8") as f:
      f.write(nbjson)
      f.write("\n")

  if did_skip:
    sys.exit(1)


if __name__ == "__main__":
  app.run(main)
