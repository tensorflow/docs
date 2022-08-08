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
"""Bage builder classes for type alias pages."""
import textwrap
import typing
from typing import Any, List, Dict

from tensorflow_docs.api_generator import parser
from tensorflow_docs.api_generator import signature as signature_lib
from tensorflow_docs.api_generator.pretty_docs import base_page


class TypeAliasPageBuilder(base_page.TemplatePageBuilder):
  """Builds a markdown page from a `TypeAliasPageBuilder` object."""
  TEMPLATE = 'templates/type_alias.jinja'

  def build_signature(self):
    return base_page.build_signature(
        name=self.page_info.short_name,
        signature=self.page_info.signature,
        decorators=None,
        type_alias=True)


class TypeAliasPageInfo(base_page.PageInfo):
  """Collects docs For a type alias page.

  Attributes:
    full_name: The full, main name, of the object being documented.
    short_name: The last part of the full name.
    py_object: The object being documented.
    defined_in: A _FileLocation describing where the object was defined.
    aliases: A list of full-name for all aliases for this object.
    doc: A list of objects representing the docstring. These can all be
      converted to markdown using str().
    signature: the parsed signature (see: generate_signature)
    decorators: A list of decorator names.
  """
  DEFAULT_BUILDER_CLASS = TypeAliasPageBuilder

  def __init__(self, *, api_node, **kwargs) -> None:
    """Initialize a `TypeAliasPageInfo`.

    Args:
      full_name: The full, main name, of the object being documented.
      py_object: The object being documented.
      **kwargs: Extra arguments.
    """

    super().__init__(api_node, **kwargs)
    self._signature = None

  @property
  def signature(self):
    return self._signature

  def _custom_join(self, args: List[str], origin: str) -> str:
    """Custom join for Callable and other type hints.

    Args:
      args: Args of a type annotation object returned by `__args__`.
      origin: Origin of a type annotation object returned by `__origin__`.

    Returns:
      A joined string containing the right representation of a type annotation.
    """
    if 'Callable' in origin:
      if args[0] == '...':
        return ', '.join(args)
      else:
        return f"[{', '.join(args[:-1])}], {args[-1]}"

    return ', '.join(args)

  def _link_type_args(self, obj: Any, reverse_index: Dict[int, str],
                      linker: signature_lib.FormatArguments) -> str:
    """Recurses into typehint object and links known objects to their pages."""
    arg_full_name = reverse_index.get(id(obj), None)
    if arg_full_name is not None:
      return linker.get_link(arg_full_name)

    result = []
    if getattr(obj, '__args__', None):
      for arg in obj.__args__:
        result.append(self._link_type_args(arg, reverse_index, linker))
      origin_str = typing._type_repr(obj.__origin__)  # pylint: disable=protected-access # pytype: disable=module-attr
      result = self._custom_join(result, origin_str)
      return f'{origin_str}[{result}]'
    else:
      return typing._type_repr(obj)  # pylint: disable=protected-access # pytype: disable=module-attr

  def collect_docs(self) -> None:
    """Collect all information necessary to genertate the function page.

    Mainly this is details about the function signature.

    For the type alias signature, the args are extracted and replaced with the
    full_name if the object is present in `parser_config.reverse_index`. They
    are also linkified to point to that symbol's page.

    For example (If generating docs for symbols in TF library):

    ```
    X = Union[int, str, bool, tf.Tensor, np.ndarray]
    ```

    In this case `tf.Tensor` will get linked to that symbol's page.
    Note: In the signature `tf.Tensor` is an object, so it will show up as
    `tensorflow.python.framework.ops.Tensor`. That's why we need to query
    `parser_config.reverse_index` to get the full_name of the object which will
    be `tf.Tensor`. Hence the signature will be:

    ```
    X = Union[int, str, bool, <a href="URL">tf.Tensor</a>, np.ndarray]
    ```
    """
    assert self.signature is None

    linker = signature_lib.FormatArguments(parser_config=self.parser_config)

    sig_args = []
    if self.py_object.__origin__:
      for arg_obj in self.py_object.__args__:
        sig_args.append(
            self._link_type_args(arg_obj, self.parser_config.reverse_index,
                                 linker))

    sig_args_str = textwrap.indent(',\n'.join(sig_args), '    ')
    if self.py_object.__origin__:
      origin_str = typing._type_repr(self.py_object.__origin__)  # pylint: disable=protected-access # pytype: disable=module-attr
      sig = f'{origin_str}[\n{sig_args_str}\n]'
    else:
      sig = repr(self.py_object)

    # pytype: enable=module-attr

    # Starting in Python 3.7, the __origin__ attribute of typing constructs
    # contains the equivalent runtime class rather than the construct itself
    # (e.g., typing.Callable.__origin__ is collections.abc.Callable).
    self._signature = sig.replace('typing.', '').replace('collections.abc.', '')

  def get_metadata_html(self) -> str:
    return parser.Metadata(self.full_name).build_html()
