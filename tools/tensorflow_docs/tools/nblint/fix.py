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
r"""Utlities for fixing lints.

Convenience functions for writing general fix functions for style lints. Opening
and closing files, modifying contents, all should happen in the fix function
callback.

Fix functions are run as `fn(lint_args, *fix_args)` and executed once for each
unique fn-args pair. Callbacks passed the same arg are deduplicated. But it's
not the end of the world if the same function/args are run multiple times since
the file changes should be the same.
"""
import re
from typing import Any, Dict, Pattern


def regex_replace_all(args: Dict[str, Any], pattern: Pattern[str],
                      repl: str) -> None:
  """Replace regex matched content in a file.

  Args:
    args: Dict of args passed to the lint function.
    pattern: Regex pattern containing two groups to match.
    repl: Replacement text to insert between the two matched groups.
  """
  fp = args["path"]
  contents = fp.read_text(encoding="utf-8")
  contents_new = re.sub(
      pattern, rf"{repl}", contents, flags=re.MULTILINE | re.DOTALL)
  if contents_new != contents:
    fp.write_text(contents_new, encoding="utf-8")


def regex_between_groups_replace_all(args: Dict[str, Any],
                                     pattern: Pattern[str], repl: str) -> None:
  """Replace content between two matched groups in a file.

  Regex pattern must contain two groups: r'(foo).*(bar)'
  and the replacement text is inserted between these matches.

  Args:
    args: Dict of args passed to the lint function.
    pattern: Regex pattern containing two groups to match.
    repl: Replacement text to insert between the two matched groups.
  """
  regex_replace_all(args, pattern, rf"\g<1>{repl}\g<2>")
