# Lint as: python3
# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
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
"""Tools for processing generated Java documentation."""
from typing import Any, Mapping, Sequence

Toc = Mapping[str, Sequence[Mapping[str, Any]]]


def add_package_headings(toc: Toc, root_pkg: str, labels: Mapping[str,
                                                                  str]) -> Toc:
  """Breaks up a flat structure with headings for each 1st-level package."""
  new_toc = []
  current_section = None
  for entry in toc.get('toc', []):
    new_entry = dict(entry)
    if new_entry.get('title', '').startswith(root_pkg):
      # Strip the common root_pkg from the title.
      new_title = new_entry['title'][len(root_pkg):].lstrip('.')
      # The section is labelled with the first sub-package (this.notthis.orthis)
      section, *_ = new_title.split('.')
      if section != current_section:
        # We've hit a new section, add a label if one was supplied.
        section_pkg = f'{root_pkg}.{section}' if section else root_pkg
        new_toc.append({'heading': labels.get(section_pkg, section)})
        current_section = section

      new_entry['title'] = new_title or root_pkg
    new_toc.append(new_entry)
  return {'toc': new_toc}
