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
"""Easy notebook embedded webp animations.

```
import tensorflow_docs.vis.webp_animation as webp_animation

env = gym.make('SpaceInvaders-v0')
obs = env.reset()
done = False
n = 0

anim = webp_animation.Webp()

while not done:
  img = env.render(mode = 'rgb_array')
  anim.append(img)
  act = env.action_space.sample() # take a random action
  obs, reward, done, info = env.step(act)
  n += 1

anim.save("test.webp")
anim
```
"""

import numpy as np
import PIL.Image

from tensorflow_docs.vis import embed
import webp


class Webp(object):
  """Builds a webp animation.

  Attributes:
    frame_rate: The default frame rate for appended images.
    shape: The shape of the animation frames. Will default to the size of the
      first image if not set.
    result: The binary image data string. Once the animation has been used, it
      can no longer updated. And the result field contains the webp encoded
      data.
  """

  def __init__(self, shape=None, frame_rate=60.0, **options):
    """A notebook-embedable webp animation.

    Args:
      shape: Optional. The image_shape of the animation. Defaults to the shape
        of the first image if unset.
      frame_rate: The default frame rate for the animation.
      **options: Additional arguments passed to `WebPAnimEncoderOptions.new`.
    """
    self.frame_rate = frame_rate
    self._timestamp_ms = 0
    self._empty = True

    if options is None:
      options = {}

    self._options = webp.WebPAnimEncoderOptions.new(**options)
    self._encoder = None
    self._shape = shape
    self._result = None

  def append(self, img, dt_ms=None):
    """Append an image to the animation.

    Args:
      img: The image to add.
      dt_ms: override the animation frame rate for this frame with a frame
        length in ms.

    Raises:
      ValueError:
        * if the video has already been "assembled" (used).
        * if `img` does not match the shape of the animation.
    """
    if self._result is not None:
      raise ValueError(
          "Can't append to an animation after it has been \"assembled\" (used)."
      )
    self._empty = False

    if not isinstance(img, PIL.Image.Image):
      img = np.asarray(img)
      img = PIL.Image.fromarray(img)

    if self._shape is None:
      self._shape = img.size

    if self._encoder is None:
      self._encoder = webp.WebPAnimEncoder.new(self.shape[0], self.shape[1],
                                               self._options)

    if img.size != self.shape:
      raise ValueError("Image shape does not match video shape")

    img = webp.WebPPicture.from_pil(img)

    self._encoder.encode_frame(img, int(self._timestamp_ms))

    if dt_ms is None:
      self._timestamp_ms += 1000 * (1.0 / self.frame_rate)
    else:
      self._timestamp_ms += dt_ms

  def extend(self, imgs, dt_ms=None):
    """Extend tha animation with an iterable if images.

    Args:
      imgs: An iterable of images, to pass to `.append`.
      dt_ms: Override the animation frame rate for these frames with a frame
        length in ms.
    """
    for img in imgs:
      self.append(img, dt_ms=dt_ms)

  @property
  def result(self):
    result = self._result
    if result is None:
      anim_data = self._encoder.assemble(int(self._timestamp_ms))
      result = anim_data.buffer()
      self._result = result
    return result

  @property
  def shape(self):
    """The shape of the animation. Read only once set."""
    return self._shape

  def _repr_html_(self):
    """Notebook display hook, embed the image in an <img> tag."""
    if self._empty:
      return "Empty Animation"

    return embed.embed_data("image/webp", self.result)._repr_html_()  # pylint: disable=protected-access,

  def save(self, filename):
    """Write the webp data to a file."""
    with open(filename, "wb") as f:
      f.write(self.result)
