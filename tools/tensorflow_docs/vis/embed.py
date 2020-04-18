# Lint as: python3
# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
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
"""Simple functions for embedding data in a notebook file."""

import base64
import mimetypes
import os
import pathlib
import textwrap

import IPython.display


def embed_data(mime: str, data: bytes) -> IPython.display.HTML:
  """Embeds data as an html tag with a data-url."""
  b64 = base64.b64encode(data).decode()
  if mime.startswith('image'):
    tag = f'<img src="data:{mime};base64,{b64}"/>'
  elif mime.startswith('video'):
    tag = textwrap.dedent(f"""
        <video width="640" height="480" controls>
          <source src="data:{mime};base64,{b64}" type="video/mp4">
          Your browser does not support the video tag.
        </video>
        """)
  else:
    raise ValueError('Images and Video only.')
  return IPython.display.HTML(tag)


def embed_file(path: os.PathLike) -> IPython.display.HTML:
  """Embeds a file in the notebook as an html tag with a data-url."""
  path = pathlib.Path(path)
  mime, unused_encoding = mimetypes.guess_type(str(path))
  data = path.read_bytes()

  return embed_data(mime, data)
