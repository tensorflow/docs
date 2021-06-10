# Lint as: python3
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
"""This is a test module.

@compatibility(TF2)
test
@end_compatibility

Hello
"""


def a_function(x, y):
  """This is a function.

  @compatibility(TF2)
  test
  @end_compatibility

  @compatibility(numpy)
  test
  @end_compatibility

  It does things.

  Args:
    x: x
    y: y

  Returns:
    None
  """
  del x
  del y
  return None


class AClass:
  """This is a class.

  @compatibility(TF2)
  test
  @end_compatibility

  It does things too.

  Attributes:
   x: x
   y: x
  """

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def a_method(self, x, y):
    """Methods can have compatibility notes too.

    @compatibility(TF2)
    test
    @end_compatibility

    It does things too.

    Args:
      x: x
      y: y

    Returns:
      None
    """
    del x
    del y
    return None
