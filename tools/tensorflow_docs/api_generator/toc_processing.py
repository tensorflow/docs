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
import itertools
from typing import Any, Iterable, Mapping, MutableMapping, MutableSequence

# TODO(b/193033225): If possible, this should be a TypedDict. If not, using the
#   real protos might make things a little cleaner.
TocEntry = MutableMapping[str, Any]
Section = MutableSequence[TocEntry]
Toc = Mapping[str, Section]


def add_package_headings(toc: Toc, root_pkgs: Iterable[str],
                         labels: Mapping[str, str]) -> Toc:
  """Breaks up a flat structure with headings for each 1st-level package."""
  new_toc = []
  current_section = None
  for entry in sort_toc(toc, labels.keys())['toc']:
    new_entry = dict(entry)
    for root_pkg in root_pkgs:
      if new_entry.get('title', '').startswith(root_pkg):
        # Strip the common root_pkg from the title.
        new_title = new_entry['title'][len(root_pkg):].lstrip('.')
        # a, a.b, a.b.c from the remainder of the package name
        all_sections = itertools.accumulate(
            new_title.split('.'), lambda a, b: f'{a}.{b}')
        # Filter out any packages that aren't defined as labelled sections.
        candidate_sections = filter(lambda s: f'{root_pkg}.{s}' in labels,
                                    all_sections)
        # If there are more than one, pick the most specific (longest). If there
        # are none, use the bare trailing package.
        section = max(candidate_sections, key=len, default=new_title)

        if section != current_section:
          # We've hit a new section, add a label if one was supplied.
          section_pkg = f'{root_pkg}.{section}' if section else root_pkg
          new_toc.append({'heading': labels.get(section_pkg, section)})
          current_section = section

        new_entry['title'] = new_title or root_pkg
    new_toc.append(new_entry)
  return {'toc': new_toc}


def nest_toc(toc: Toc) -> Toc:
  """Nests a flat TOC into a tree structure based on common packages."""
  new_toc = []

  # We only look at the first level for flat package names.
  entries_by_title = {e['title']: e for e in toc['toc']}
  for title, entry in entries_by_title.items():
    target_entry = _nest_toc_entry(title, new_toc)

    # Populate the target entry with the original entry, sans title.
    # (pytype suppressed due to inferring .keys() as a List)
    fields = entry.keys() - {'title'}  # pytype: disable=unsupported-operands
    target_entry.update({f: entry[f] for f in fields})

    # Clean up empty sections
    if not target_entry.get('section'):
      target_entry.pop('section', None)

  return {'toc': new_toc}


def _nest_toc_entry(title: str, section: Section) -> TocEntry:
  """Nest the title (split by .) into the TOC. Creating hierarchy as needed."""
  pkg, *maybe_rest = title.split('.', 1)

  for entry in section:
    if entry.get('title') == pkg:
      target_entry = entry
      if 'section' not in target_entry:
        target_entry['section'] = []
      break
  else:
    target_entry = {'title': pkg, 'section': []}
    section.append(target_entry)

  if not maybe_rest:
    return target_entry
  else:
    rest = maybe_rest[0]
    return _nest_toc_entry(rest, target_entry['section'])


def sort_toc(toc: Toc, labels: Iterable[str]) -> Toc:
  """Pre-sort the TOC entries by `labels`."""
  new_toc = []
  remaining_entries = list(toc.get('toc', []))
  for label in labels:
    more_specific_labels = [l for l in labels if len(l) > len(label)]
    for entry in remaining_entries[:]:  # copy so we can remove() later
      title = entry.get('title', '')
      better_match_exists = any(
          [title.startswith(l) for l in more_specific_labels])
      if title.startswith(label) and not better_match_exists:
        new_toc.append(entry)
        # Remove the matched entry so it doesn't duplicate, and so we can track
        # any un-matched entries.
        remaining_entries.remove(entry)

  return {'toc': new_toc + remaining_entries}
