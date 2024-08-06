# Copyright 2024 The TensorFlow Authors. All Rights Reserved.
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
"""Unit tests for nbfmt."""
import pathlib
import unittest
from nbformat import notebooknode
from tensorflow_docs.tools.nbfmt import __main__ as nbfmt


class NotebookFormatTest(unittest.TestCase):

  def test_metadata_cleansing(self):
    subject_notebook = notebooknode.NotebookNode({
        "cells": [],
        "metadata": {
            "unknown": ["delete", "me"],
            "accelerator": "GPU",
            "colab": {
                "name": "/this/is/clobbered.ipynb",
                "collapsed_sections": [],
                "deleteme": "pls",
            },
            "kernelspec": {
                "display_name": "Python 2 foreverrrr",
                "name": "python2",
                "deleteme": "deldeldel",
            },
            "google": {
                "keywords": ["one", "two"],
                "image_path": "/foo/img.png",
                "more_stuff": "delete me",
            },
        },
    })

    expected_notebook = notebooknode.NotebookNode({
        "cells": [],
        "metadata": {
            "accelerator": "GPU",
            "colab": {
                "name": "test.ipynb",
                "collapsed_sections": [],
                "toc_visible": True,
            },
            "kernelspec": {
                "display_name": "Python 3",
                "name": "python3",
            },
            "google": {
                "keywords": ["one", "two"],
                "image_path": "/foo/img.png",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 0,
    })

    nbfmt.clean_root(subject_notebook, pathlib.Path("/path/test.ipynb"))
    self.assertEqual(subject_notebook, expected_notebook)


if __name__ == "__main__":
  unittest.main()
