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

from tensorflow_docs.tools.nblint.decorator import fail
from tensorflow_docs.tools.nblint.decorator import lint
from tensorflow_docs.tools.nblint.decorator import Options


def search_wordlist(wordlist, src_str):
  """Search for wordlist entries in text and return set of found items.

  Args:
    wordlist: Dict of word entries and recommendations to search in string.
    src_str: String to search for word entries.

  Returns:
    A dict that is a subset of entries from `wordlist` found in `src_str`.
  """
  found_words = {}
  for word in wordlist:
    # Word-boundary and ignore between path seperator '/'.
    if re.search(rf"[^/]\b{word}\b[^/]", src_str, re.IGNORECASE):
      alt_word = wordlist[word]
      if not alt_word:
        alt_word = "n/a"
      found_words[word] = alt_word
  return found_words


# Non-exhaustive list: {word: alt-word} (Use False if alt not provided.)
_INCLUSIVE_WORDLIST = {
    "blacklist": "blocked",
    "whitelist": "allowed",
    "master": "primary",
    "slave": "replica",
    "native": "built-in"
}


@lint(
    message="Use inclusive language: https://developers.google.com/style/inclusive-documentation",
    cond=Options.Cond.ALL)
def inclusive_language(args):
  """Test for words found in inclusive wordlist and recommend alternatives."""
  found_words = search_wordlist(_INCLUSIVE_WORDLIST, args["cell_source"])
  if found_words:
    words = ", ".join([f"{word} => {alt}" for word, alt in found_words.items()])
    fail(f"Use inclusive language where possible and accurate. Found: {words}")
  else:
    return True


# Non-exhaustive list: {word: alt-word} (Use False if alt not provided.)
_SECOND_PERSON_WORDLIST = {"we": "you", "we're": "you are"}


@lint(
    message="Prefer second person instead of first person: https://developers.google.com/style/person",
    cond=Options.Cond.ALL)
def second_person(args):
  """Test for first person usage in doc and recommend second person."""
  found_words = search_wordlist(_SECOND_PERSON_WORDLIST, args["cell_source"])
  if found_words:
    words = ", ".join([f"{word} => {alt}" for word, alt in found_words.items()])
    fail(f"Prefer second person instead of first person. Found: {words}")
  else:
    return True
