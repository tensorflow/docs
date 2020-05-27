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
r"""Lint assertions that adhere to the Google dev docs style guide.

This style module is a non-exhaustive implemention of style rules found in the
Google developer documentation style guide: https://developers.google.com/style

When adding lints, please link to the URL of the relevant style rule.
"""
import re

from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options

second_person_re = re.compile(r"\bwe\b", re.IGNORECASE)


@lint(
    message="Prefer second person 'you' instead of 'we': https://developers.google.com/style/person",
    cond=Options.Cond.ALL)
def second_person(source, cell, filepath):
  del cell, filepath  # Unused by callback
  if not second_person_re.search(source):
    return True
  else:
    return False
