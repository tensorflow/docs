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
r"""A collection of utilties for working with notebook files."""
import json
import pathlib
import sys
import textwrap

from typing import Any, Dict, List, Optional, Tuple, Union


def collect_notebook_paths(
    filepaths: List[Union[str, pathlib.Path]]
) -> Tuple[List[pathlib.Path], List[pathlib.Path]]:
  """Return list of `pathlib.Path`s for (recursive) notebook filepaths.

  Skips any file that's not an .ipynb notebook or invalid file.

  Args:
    filepaths: List file path strings passed at command-line.

  Returns:
    A list of Path objects for all notebook files.
    A list of Path objects that returned an error.
  """
  nb_paths = []
  err_nb_paths = []
  for fp in filepaths:
    path = pathlib.Path(fp)
    if path.is_dir():
      nb_paths.extend(path.rglob("*.ipynb"))
    elif path.is_file():
      if path.suffix == ".ipynb":
        nb_paths.append(path)
      else:
        print(f"Not an '.ipynb' file, skipping: {path}", file=sys.stderr)
        err_nb_paths.append(path)
    else:
      print(f"Invalid file, skipping: {path}", file=sys.stderr)
      err_nb_paths.append(path)
  return nb_paths, err_nb_paths


def load_notebook(path: pathlib.Path) -> Tuple[Optional[Dict[str, Any]], str]:
  """Load and parse JSON data from a notebook file.

  Args:
    path: A `pathlib.Path` of a Jupyter notebook.

  Returns:
    Dict: Contains data of the parsed JSON notebook, or null if can't read.
    String: The entire JSON source code of the notebook.
  """
  source = path.read_text(encoding="utf-8")
  try:
    data = json.loads(source)
    if not isinstance(data.get("cells"), list):
      data = None
      print("Invalid notebook, unable to find list of cells.", file=sys.stderr)
  except (json.JSONDecodeError, ValueError) as err:
    print(
        textwrap.dedent(f"""
      Unable to load JSON:
      {err.__class__.__name__}: {err}
      """),
        file=sys.stderr)
    data = None

  return data, source
