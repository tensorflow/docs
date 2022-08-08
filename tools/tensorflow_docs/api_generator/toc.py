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
import pathlib

from typing import Any, IO, Iterator, List, Optional, Tuple, Union

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import doc_generator_visitor
from tensorflow_docs.api_generator import obj_type as obj_type_lib
from tensorflow_docs.api_generator import signature

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
  def _maybe_open(self, file: Union[os.PathLike, IO[str]]) -> Iterator[IO[str]]:
    if isinstance(file, os.PathLike):
      with open(file, 'w') as stream:
        yield stream
    else:
      stream = file
      yield stream

  def write(self, file: Union[os.PathLike, IO[str]]) -> None:
    with self._maybe_open(file) as stream:
      yaml.dump(
          self, stream=stream, default_flow_style=False, Dumper=_TocDumper)


class TocBuilder:
  """A class to build a Toc from an ApiTree."""

  def __init__(self, site_path):
    self.site_path = pathlib.Path(site_path)

  def build(self, api_tree: doc_generator_visitor.ApiTree) -> Toc:
    """Create a `Toc` from an `ApiTree`."""
    entries = []
    for child in api_tree.root.children.values():
      entries.extend(self._entries_from_api_node(child))
    return Toc(toc=entries)

  def _entries_from_api_node(
      self, api_node: doc_generator_visitor.ApiTreeNode) -> List[Entry]:

    """Converts an ApiTreeNode to a list of toc entries."""
    obj_type = api_node.obj_type

    if obj_type is obj_type_lib.ObjType.MODULE:
      return [self._make_section(api_node)]
    if obj_type is obj_type_lib.ObjType.CLASS:
      return self._flat_class_entries(api_node)
    if obj_type in [
        obj_type_lib.ObjType.CALLABLE, obj_type_lib.ObjType.TYPE_ALIAS
    ]:
      return [self._make_link(api_node)]
    else:
      return []

  def _get_docpath(self, api_path) -> pathlib.Path:
    api_path = (p.replace('.', '/') for p in api_path)
    return pathlib.Path(self.site_path, *api_path)

  def _make_link(self,
                 api_node: doc_generator_visitor.ApiTreeNode,
                 title: Optional[str] = None) -> Link:

    docpath = self._get_docpath(api_path=api_node.path)
    title = title or api_node.short_name
    return Link(
        title=title, path=str(docpath), status=self._make_status(api_node))

  def _make_section(self,
                    api_node: doc_generator_visitor.ApiTreeNode,
                    title: Optional[str] = None) -> Section:
    """Create a `toc.Section` from a module's ApiTreeNode."""
    overview = self._make_overview(api_node)
    entries = []
    for child in api_node.children.values():
      entries.extend(self._entries_from_api_node(child))
    entries = sorted(entries, key=self._section_order_key)
    entries = [overview] + entries

    status = self._make_status(api_node)
    return Section(
        title=title or api_node.short_name, section=entries, status=status)

  def _make_overview(self, api_node: doc_generator_visitor.ApiTreeNode):
    docpath = self._get_docpath(api_path=api_node.path)
    return Link(title='Overview', path=str(docpath))

  def _section_order_key(self, entry: Entry) -> Tuple[bool, str]:
    title = getattr(entry, 'title', None)
    is_section = isinstance(entry, Section)

    return (is_section, title)

  def _flat_class_entries(self,
                          api_node: doc_generator_visitor.ApiTreeNode,
                          title: Optional[str] = None) -> List[Entry]:
    """Returns entries for both `Class` and `Class.Nested`."""
    title = title or api_node.short_name
    entries = [self._make_link(api_node, title=title)]
    for name, child_node in api_node.children.items():
      if child_node.obj_type in [
          obj_type_lib.ObjType.CLASS, obj_type_lib.ObjType.MODULE
      ]:
        subtitle = f'{title}.{name}'
        entries.extend(self._flat_class_entries(child_node, title=subtitle))

    return entries

  def _make_status(self, api_node: doc_generator_visitor.ApiTreeNode):
    """Returns the toc.Status of an ApiTreeNode."""
    if self._is_deprecated(api_node):
      return Status.DEPRECATED
    if self._is_experimental(api_node):
      return Status.EXPERIMENTAL
    return None

  def _is_experimental(self, api_node: doc_generator_visitor.ApiTreeNode):
    return 'experimental' in api_node.short_name.lower()

  def _is_deprecated(self, api_node: doc_generator_visitor.ApiTreeNode):
    """Checks if an object is deprecated or not.

    Each deprecated function has a `_tf_decorator.decorator_name` attribute.
    Check the docstring of that function to confirm if the function was
    indeed deprecated. If a different deprecation setting was used on the
    function, then "THIS FUNCTION IS DEPRECATED" substring won't be inserted
    into the docstring of that function by the decorator.

    Args:
      api_node: The node to evaluate.

    Returns:
      True if depreacted else False.
    """
    if doc_controls.is_deprecated(api_node.py_object):
      return True

    decorator_list = signature.extract_decorators(api_node.py_object)
    if any('deprecat' in dec for dec in decorator_list):
      docstring = getattr(api_node.py_object, '__doc__') or ''
      return 'THIS FUNCTION IS DEPRECATED' in docstring

    return False


class FlatModulesTocBuilder(TocBuilder):
  """Builds a toc where the top level submodules are peers (not children).

  The base TocBuilder does this:

  ```
  module:
    thing1
    sub1:
      thing2
    sub2:
      thing3
  ```

  This one outputs:

  ```
  module:
    thing1
  module.sub1:
    thing2
  module.sub2:
    thing3
  ```
  """

  def build(self, api_tree: doc_generator_visitor.ApiTree) -> Toc:
    entries = []
    for module_node in api_tree.root.children.values():
      if '.' in module_node.short_name:
        entries.extend(self._entries_from_api_node(module_node))
      else:
        assert module_node.obj_type is obj_type_lib.ObjType.MODULE
        entries.extend(self._flat_module_entries(module_node))

    return Toc(toc=entries)

  def _flat_module_entries(self,
                           api_node: doc_generator_visitor.ApiTreeNode,
                           title: Optional[str] = None) -> List[Section]:
    """For top-level modules, place the submodules as peers."""
    title = title or api_node.short_name

    overview = self._make_link(api_node, title='Overview')
    entries = []
    submodule_sections = []
    for name, child_node in api_node.children.items():
      if child_node.obj_type is obj_type_lib.ObjType.MODULE:
        subtitle = f'{title}.{name}'
        submodule_sections.append(
            self._make_section(child_node, title=subtitle))
      else:
        entries.extend(self._entries_from_api_node(child_node))

    entries = sorted(entries, key=self._section_order_key)
    entries.insert(0, overview)

    submodule_sections = sorted(submodule_sections, key=self._section_order_key)

    status = self._make_status(api_node)
    module_section = Section(title=title, section=entries, status=status)
    return [module_section] + submodule_sections
