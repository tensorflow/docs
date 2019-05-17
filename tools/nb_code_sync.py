#!/usr/bin/env python3
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
"""Keep translated notebook code in sync with the source-of-truth notebook.

This tool attempts to make it easier to keep the community translation *code*
in sync with the en/ source-or-truth notebooks. It intentionally ignores
Markdown cells and only compares code cells. There must be the same amount of
code cells in source notebook and translation notebook.

Usage: nb_code_sync.py [--lang=en] site/lang/notebook.ipynb [...]

Useful when used with interactive git workflow to selectively add hunks:
git add --patch site/lang/notebook.ipynb
Commands:
  y: stage this hunk
  n: do not stage this hunk
  s: split this hunk
  e: edit this hunk
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import errno
import json
import os
import pathlib
import re
import sys
from absl import app
from absl import flags

flags.DEFINE_enum("lang", "en", ["en", "js", "ko", "pt", "ru", "tr", "zh-cn"],
                  "Language directory to import from.")
flags.DEFINE_string("src", None, "Source file or parent directory of source.")
flags.DEFINE_boolean("stdout", False, "Write to stdout instead of file.")
flags.DEFINE_string("site_root", None, "Root directory of site docs.")


class Notebook(object):
  """Represents a parsed .ipynb notebook file.

  Attributes:
    path: Path to the notebook file.
    data: All cells parsed from notebook.
    code_cells: Only code cells parsed from notebook.
  """

  path = None

  def __init__(self, data):
    """Inits Notebook from parsed .ipynb notebook data."""
    self.data = data
    self.code_cells = self._load_code_cells(self.data)

  @classmethod
  def from_path(cls, path):
    """Inits Notebook using path to .pynb file."""
    pth = Notebook._check_path(path)
    with open(pth) as json_data:
      data = json.load(json_data)
    nb = Notebook(data)
    nb.path = pth
    return nb

  @staticmethod
  def is_notebook(path):
    """Test of a file is an .ipynb file based on extension."""
    if not os.path.isfile(path):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    return os.path.splitext(path)[-1].lower() == ".ipynb"

  @staticmethod
  def _check_path(pth):
    if not Notebook.is_notebook(pth):
      raise Exception("Notebook must be an .ipynb file: {}".format(pth))
    path = pathlib.Path(pth)
    if not path.exists():
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    return path

  def _load_code_cells(self, data):
    # parse code cells
    code_cells = [c for c in data["cells"] if c["cell_type"] == "code"]
    # Discard last cell if empty
    cell_source = code_cells[-1]["source"]
    # remove empty strings, then test if anything is left
    if not any(cell_source):
      del code_cells[-1]
    return code_cells

  @staticmethod
  def _strip_line(line):
    """Remove comments and any trailing whitespace."""
    line = re.sub(r"^(.*?)#(.*)$", r"\1", line)
    return line.rstrip()

  @staticmethod
  def _is_source_code_equal(x_list, y_list):
    """Scrub lines of comments, remove empty lines, then compare."""
    x_list = [Notebook._strip_line(line) for line in x_list if line]
    y_list = [Notebook._strip_line(line) for line in y_list if line]
    return x_list == y_list

  def _set_cell_source(self, cell_id, source):
    for i, cell in enumerate(self.data["cells"]):
      if cell["metadata"]["id"] == cell_id:
        self.data["cells"][i]["source"] = source
        break
    else:
      # for-loop exhausted
      raise Exception("Did not find cell id '{}' in notebook.".format(cell_id))

  def update(self, notebook):
    """Update code cells that differ from the provided notebook."""
    if len(self.code_cells) != len(notebook.code_cells):
      raise Exception("Notebooks must have same amount of code cells.")
    # Iterate all cells for destination reference
    for i, src_cell in enumerate(notebook.code_cells):
      dest_cell = self.code_cells[i]
      # Compare source code after scrubbing comments.
      # Ensures translated comments are preserved until the code changes.
      if not Notebook._is_source_code_equal(src_cell["source"],
                                            dest_cell["source"]):
        self._set_cell_source(dest_cell["metadata"]["id"], src_cell["source"])

  def write(self, use_stdout=False):
    """Write notebook to file or print to screen."""
    def print_file(outfile):
      json.dump(self.data, outfile, indent=2, ensure_ascii=False)
      outfile.write("\n")  # add trailing newline

    if use_stdout:
      print_file(sys.stdout)
    else:
      with open(self.path, "w") as outfile:
        print_file(outfile)
        print("Wrote: {}".format(self.path))


def get_src_path(user_flags, notebook):
  """Get path of source notebook based on user flags or the destination file.

  Args:
    user_flags: Command-line arguments
    notebook: Destination notebook used to select source notebook.
  Returns:
    A Path of the source-of-truth notebook.
  Raises:
    FileNotFoundError: If user args for site_root or src are invalid locations.
  """
  if user_flags.site_root:
    site_root = pathlib.Path(user_flags.site_root)
  else:
    site_root = pathlib.Path(__file__).parent.parent.joinpath("site")
  if not site_root.is_dir():
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), site_root)

  if not user_flags.src:
    # Determine path from previous notebook and source language
    fp_relpath = notebook.path.relative_to(site_root)  # relative path
    fp_relpath = pathlib.Path(*fp_relpath.parts[1:])
    return site_root.joinpath(user_flags.lang, fp_relpath)
  elif os.path.isdir(user_flags.src):
    return pathlib.Path(user_flags.src) / notebook.path.name
  elif os.path.isfile(user_flags.src):
    return pathlib.Path(user_flags.src)
  else:
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                            user_flags.src)


def main(argv):
  if len(argv) < 2:
    raise app.UsageError("Missing command-line arguments.")

  for dest_path in argv[1:]:
    if not Notebook.is_notebook(dest_path):
      print("Not a notebook file, skipping: {}".format(dest_path),
            file=sys.stderr)
      continue

    dest_notebook = Notebook.from_path(dest_path)

    src_path = get_src_path(flags.FLAGS, dest_notebook)
    src_notebook = Notebook.from_path(src_path)

    dest_notebook.update(src_notebook)
    dest_notebook.write(flags.FLAGS.stdout)


if __name__ == "__main__":
  app.run(main)
