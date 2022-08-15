# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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
"""Utility for copying cells between notebooks."""
import pathlib
import sys
import textwrap

from absl import app
import nbformat

from tensorflow_docs.tools.nbfmt import __main__ as nbfmt
from tensorflow_docs.tools.nbfmt import notebook_utils


def process_stats(stats: notebook_utils.CellCopyStats) -> bool:
  """Displays summary stats to the user. Returns True if any warnings."""
  print(
      textwrap.dedent(f"""
      Notebook copy complete.
        - Total code cells processed: {stats.processed_cells}
        - Cells updated: {stats.updated_cells}
      """))

  has_warnings = any((
      stats.unmatched_target_cells,
      stats.unmatched_source_cells,
      stats.out_of_order_target_cells,
  ))
  if has_warnings:
    print('Warnings:')

    if stats.unmatched_target_cells:
      notebook_utils.warn(
          '- Cells in source notebook that are not in the destination: '
          f'{" ".join(stats.unmatched_target_cells)}')

    if stats.unmatched_source_cells:
      notebook_utils.warn(
          '- Cells in destination notebook that are not in the source: '
          f'{" ".join(stats.unmatched_source_cells)}')

    if stats.out_of_order_target_cells:
      notebook_utils.warn(
          '- Cells found earlier in destination notebook than source: '
          f'{" ".join(stats.out_of_order_target_cells)}')

    print()

  return has_warnings


def main(args: list[str]) -> int:
  if len(args) != 3:
    notebook_utils.warn('nbcp requires 2 notebooks as arguments:')
    notebook_utils.warn('  $ ...nbcp src_notebook.ipynb dest_notebook.ipynb'
                        ' [--nbfmt --args --supported]')
    sys.exit(1)

  src = pathlib.Path(args[1])
  dest = pathlib.Path(args[2])

  # Open files and copy cells.
  with src.open('rt') as src_fh, dest.open('rt') as dest_fh:
    dest_nb = nbformat.read(dest_fh, nbformat.NO_CONVERT)
    stats = notebook_utils.copy_code_cells(
        nbformat.read(src_fh, nbformat.NO_CONVERT), dest_nb)

  # Write over destination file.
  with dest.open('wt') as dest_fh:
    nbformat.write(dest_nb, dest_fh)

  warnings = process_stats(stats)

  # Format the notebook.
  nbfmt.main(['', str(dest)])

  return int(warnings)


if __name__ == '__main__':
  app.run(main)
