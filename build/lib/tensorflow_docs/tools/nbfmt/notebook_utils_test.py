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
"""Unit tests for notebook_utils."""

from absl.testing import absltest
from nbformat import notebooknode

from tensorflow_docs.tools.nbfmt import notebook_utils


class NotebookUtilsTest(absltest.TestCase):

  def test_copy_code_cells(self):
    source_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "markdown",
            "metadata": {
                "id": "id1"
            },
            "source": ["## Some text"]
        }, {
            "cell_type": "code",
            "metadata": {
                "id": "id2"
            },
            "source": ["# some python\n", "print('hi')"]
        }]
    })
    target_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "markdown",
            "metadata": {
                "id": "id1"
            },
            "source": ["## Different text"]
        }, {
            "cell_type": "code",
            "metadata": {
                "id": "id2"
            },
            "source": ["# some old python\n", "print 'hi'"]
        }]
    })

    stat = notebook_utils.copy_code_cells(source_notebook, target_notebook)

    # Ensure we have the expected contents (markdown untouched, code copied)
    self.assertIn("## Different text", target_notebook.cells[0]["source"])
    self.assertIn("print('hi')", target_notebook.cells[1]["source"])

    # Ensure only the code cell was updated
    self.assertEqual(1, stat.updated_cells)
    self.assertEqual(1, stat.processed_cells)

  def test_missing_target_cell(self):
    source_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell1"
            },
            "source": ["# some python\n", "print('hi')"]
        }, {
            "cell_type": "markdown",
            "metadata": {
                "id": "md1"
            },
            "source": ["## text"]
        }]
    })
    target_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell2"
            },
            "source": ["# some old python\n", "print 'hi'"]
        }]
    })

    stat = notebook_utils.copy_code_cells(source_notebook, target_notebook)

    self.assertEqual(0, stat.updated_cells)
    self.assertEqual(0, stat.processed_cells)
    self.assertEqual(["cell1"], stat.unmatched_target_cells)

  def test_missing_source_cell(self):
    source_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell1"
            },
            "source": ["# some python\n", "print('hi')"]
        }]
    })
    target_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell2"
            },
            "source": ["# some old python\n", "print 'hi'"]
        }, {
            "cell_type": "markdown",
            "metadata": {
                "id": "text1"
            },
            "source": ["## texty texty"]
        }]
    })

    stat = notebook_utils.copy_code_cells(source_notebook, target_notebook)

    self.assertEqual(0, stat.updated_cells)
    self.assertEqual(0, stat.processed_cells)
    self.assertEqual(["cell2"], stat.unmatched_source_cells)

  def test_cell_ordering(self):
    source_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell1"
            },
            "source": ["# first code\n"]
        }, {
            "cell_type": "code",
            "metadata": {
                "id": "cell2"
            },
            "source": ["# second code\n"]
        }]
    })
    target_notebook = notebooknode.NotebookNode({
        "cells": [{
            "cell_type": "code",
            "metadata": {
                "id": "cell2"
            },
            "source": ["# update me\n"]
        }, {
            "cell_type": "code",
            "metadata": {
                "id": "cell1"
            },
            "source": ["# update me\n"]
        }]
    })

    stat = notebook_utils.copy_code_cells(source_notebook, target_notebook)

    self.assertEqual(2, stat.updated_cells)
    self.assertIn("cell2", stat.out_of_order_target_cells)


if __name__ == "__main__":
  absltest.main()
