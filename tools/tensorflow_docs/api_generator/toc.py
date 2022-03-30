# Copyright 2022 The TensorFlow Authors. All Rights Reserved.
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
"""Classes for generating the TOC."""

import contextlib
import dataclasses
import enum
import os

from typing import Any, IO, Iterator, List, Optional, Tuple, Union

import yaml


class _TocDumper(yaml.SafeDumper):

  def ignore_aliases(self, data):
    """Don't output references for duplicated objects (usually strings)."""
    return True


def _dict_representer(dumper: yaml.SafeDumper, data: Any):
  """Represent the object as a dict created of (key, value) pairs."""
  return dumper.represent_dict(iter(data))


def _use_yaml_dict_representer(cls):
  """Register the class's as using a `_dict_representer`."""
  yaml.add_representer(cls, representer=_dict_representer, Dumper=_TocDumper)
  return cls


def _str_enum_representer(dumper: yaml.SafeDumper, data: Any):
  """Represent a str-Enum as a string."""
  return dumper.represent_str(data.value)


def _use_yaml_str_enum_representer(cls):
  """Register the class as using `_str_enum_representer`."""
  yaml.add_representer(
      cls, representer=_str_enum_representer, Dumper=_TocDumper)
  return cls


@_use_yaml_str_enum_representer
class Status(enum.Enum):
  """Represents a page status."""
  ALPHA = 'alpha'
  BETA = 'beta'
  DEPRECATED = 'deprecated'
  EXPERIMENTAL = 'experimental'
  EXTERNAL = 'external'
  LIMITED = 'limited'
  NEW = 'new'
  NIGHTLY = 'nightly'
  PREVIEW = 'preview'
  UNSUPPORTED = 'unsupported'


@_use_yaml_str_enum_representer
class HeadingStyle(enum.Enum):
  """Represents a Heading Style."""
  ACCORDION = 'accordion'
  DIVIDER = 'divider'


class Entry:
  """Base class for toc entries."""

  def replace(self, **kwargs):
    new_kwargs = dict(self)
    new_kwargs.update(kwargs)
    return type(self)(**new_kwargs)

  def __iter__(self) -> Iterator[Tuple[str, Any]]:
    """Support `dict(entry)` for yaml output."""
    for key, value in self.__dict__.items():
      if value is not None:
        yield (key, value)


@_use_yaml_dict_representer
@dataclasses.dataclass
class Heading(Entry):
  """A toc heading."""
  heading: str
  style: Optional[HeadingStyle] = None


@_use_yaml_dict_representer
@dataclasses.dataclass
class Section(Entry):
  """A toc section."""
  title: str
  section: List[Entry]
  status: Optional[Status] = None

  def __iter__(self) -> Iterator[Tuple[str, Any]]:
    """Support `dict(entry)` for yaml output."""
    yield 'title', self.title
    if self.status is not None:
      yield 'status', self.status
    yield 'section', self.section


@_use_yaml_dict_representer
@dataclasses.dataclass
class Link(Entry):
  """Represents toc page-link."""
  title: str
  path: str
  status: Optional[Status] = None

  def __iter__(self) -> Iterator[Tuple[str, Any]]:
    """Support `dict(entry)` for yaml output."""
    yield 'title', self.title
    if self.status is not None:
      yield 'status', self.status
    yield 'path', self.path


@_use_yaml_dict_representer
class Break(Entry):
  """Represents a toc whitesoace break."""

  def __init__(self):
    self.__dict__['break'] = True


@_use_yaml_dict_representer
@dataclasses.dataclass
class Toc(Entry):
  """Represents the top-level `toc` element in included files."""
  toc: List[Entry]

  @contextlib.contextmanager
  def _maybe_open(self, file: Union[os.PathLike, IO]) -> Iterator[IO]:
    if isinstance(file, os.PathLike):
      with open(file, 'w') as stream:
        yield stream
    else:
      stream = file
      yield stream

  def write(self, file: Union[os.PathLike, IO]) -> None:
    with self._maybe_open(file) as stream:
      yaml.dump(
          self, stream=stream, default_flow_style=False, Dumper=_TocDumper)
