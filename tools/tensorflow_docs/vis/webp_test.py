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
"""Tests for tensorflow_docs.vis.webp."""

import os

from absl.testing import absltest

import numpy as np
import PIL.Image

from tensorflow_docs.vis import webp_animation


class WebpTest(absltest.TestCase):

  def test_smoke(self):
    workdir = self.create_tempdir().full_path

    img = PIL.Image.fromarray(np.zeros([10, 12, 3], dtype=np.uint8))
    anim = webp_animation.Webp()

    anim.append(img)
    anim.extend([img])
    anim.save(os.path.join(workdir, 'test.webp'))


if __name__ == '__main__':
  absltest.main()
