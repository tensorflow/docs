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
"""Turn Python docstrings into Markdown for TensorFlow documentation."""

import ast
import dataclasses
import enum
import functools
import html
import inspect
import re
import textwrap
import typing

from typing import Any, Dict, List, Iterable, NamedTuple, Optional, Union

import astor

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import public_api


class _TypeAnnotationExtractor(ast.NodeVisitor):
  """Extracts the type annotations by parsing the AST of a function."""

  def __init__(self):
    self.annotation_dict = {}
    self.arguments_typehint_exists = False
    self.return_typehint_exists = False

  def visit_FunctionDef(self, node) -> None:  # pylint: disable=invalid-name
    """Visits the `FunctionDef` node in AST tree and extracts the typehints."""

    # Capture the return type annotation.
    if node.returns:
      self.annotation_dict['return'] = astor.to_source(
          node.returns).strip().replace('"""', '"')
      self.return_typehint_exists = True

    # Capture the args type annotation.
    for arg in node.args.args:
      if arg.annotation:
        self.annotation_dict[arg.arg] = astor.to_source(
            arg.annotation).strip().replace('"""', '"')
        self.arguments_typehint_exists = True

    # Capture the kwarg only args type annotation.
    for kwarg in node.args.kwonlyargs:
      if kwarg.annotation:
        self.annotation_dict[kwarg.arg] = astor.to_source(
            kwarg.annotation).strip().replace('"""', '"')
        self.arguments_typehint_exists = True


class _DataclassTypeAnnotationExtractor(ast.NodeVisitor):
  """Extracts the type annotations by parsing the AST of a dataclass."""

  def __init__(self):
    self.annotation_dict = {}
    self.arguments_typehint_exists = False
    self.return_typehint_exists = False

  def visit_ClassDef(self, node) -> None:  # pylint: disable=invalid-name
    # Don't visit all nodes. Only visit top-level AnnAssign nodes so that
    # If there's an AnnAssign in a method it doesn't get picked up.
    for sub in node.body:
      if isinstance(sub, ast.AnnAssign):
        self.visit_AnnAssign(sub)

  def visit_AnnAssign(self, node) -> None:  # pylint: disable=invalid-name
    """Vists an assignment with a type annotation. Dataclasses is an example."""
    arg = astor.to_source(node.target).strip()
    anno = astor.to_source(node.annotation).strip()
    self.annotation_dict[arg] = anno
    self.arguments_typehint_exists = True


class _ASTDefaultValueExtractor(ast.NodeVisitor):
  """Extracts the default values by parsing the AST of a function."""

  _PAREN_NUMBER_RE = re.compile(r'^\((True|False|[0-9.e-]+)\)')

  def __init__(self):
    self.ast_args_defaults = {}
    self.ast_kw_only_defaults = {}

  def _preprocess(self, val) -> str:
    text_default_val = astor.to_source(val).strip().replace(
        '\t', '\\t').replace('\n', '\\n').replace('"""', "'")
    text_default_val = self._PAREN_NUMBER_RE.sub('\\1', text_default_val)
    return text_default_val

  def visit_FunctionDef(self, node) -> None:  # pylint: disable=invalid-name
    """Visits the `FunctionDef` node and extracts the default values."""

    # From https://docs.python.org/3/library/ast.html#ast.arguments:
    #   `defaults` is a list of default values for arguments that can be passed
    #   positionally. If there are fewer defaults, they correspond to the last
    #   n arguments.
    last_n_pos_args = node.args.args[-1 * len(node.args.defaults):]
    for arg, default_val in zip(last_n_pos_args, node.args.defaults):
      if default_val is not None:
        text_default_val = self._preprocess(default_val)
        self.ast_args_defaults[arg.arg] = text_default_val

    for kwarg, default_val in zip(node.args.kwonlyargs, node.args.kw_defaults):
      if default_val is not None:
        text_default_val = self._preprocess(default_val)
        self.ast_kw_only_defaults[kwarg.arg] = text_default_val


class FormatArguments(object):
  """Formats the arguments and adds type annotations if they exist."""

  _INTERNAL_NAMES = {
      'ops.GraphKeys': 'tf.GraphKeys',
      '_ops.GraphKeys': 'tf.GraphKeys',
      'init_ops.zeros_initializer': 'tf.zeros_initializer',
      'init_ops.ones_initializer': 'tf.ones_initializer',
      'saver_pb2.SaverDef': 'tf.train.SaverDef',
  }

  _OBJECT_MEMORY_ADDRESS_RE = re.compile(r'<(?P<type>.+) object at 0x[\da-f]+>')

  # A regular expression capturing a python identifier.
  _IDENTIFIER_RE = r'[a-zA-Z_]\w*'

  _INDIVIDUAL_TYPES_RE = re.compile(
      r"""
        (?P<single_type>
          ([\w.]*)
          (?=$|,| |\]|\[)
        )
      """, re.IGNORECASE | re.VERBOSE)

  _TYPING = frozenset(
      list(typing.__dict__.keys()) +
      ['int', 'str', 'bytes', 'float', 'complex', 'bool', 'None'])

  _IMMUTABLE_TYPES = frozenset([
      int, str, bytes, float, complex, bool, Ellipsis,
      type(None), tuple, frozenset
  ])

  def __init__(
      self,
      type_annotations: Dict[str, str],
      parser_config: config.ParserConfig,
      func_full_name: str,
  ) -> None:
    self._type_annotations = type_annotations
    self._reverse_index = parser_config.reverse_index
    self._reference_resolver = parser_config.reference_resolver
    # func_full_name is used to calculate the relative path.
    self._func_full_name = func_full_name

    self._is_fragment = self._reference_resolver._is_fragment.get(
        self._func_full_name, None)

  def get_link(self, obj_full_name: str) -> str:
    return self._reference_resolver.python_link(
        link_text=obj_full_name, ref_full_name=obj_full_name)

  def _extract_non_builtin_types(self, arg_obj: Any,
                                 non_builtin_types: List[Any]) -> List[Any]:
    """Extracts the non-builtin types from a type annotations object.

    Recurses if an object contains `__args__` attribute. If an object is
    an inbuilt object or an `Ellipsis` then its skipped.

    Args:
      arg_obj: Type annotation object.
      non_builtin_types: List to keep track of the non-builtin types extracted.

    Returns:
      List of non-builtin types.
    """

    annotations = getattr(arg_obj, '__args__', [arg_obj])
    if annotations is None:
      annotations = [arg_obj]

    for anno in annotations:
      if self._reverse_index.get(id(anno), None):
        non_builtin_types.append(anno)
      elif (anno in self._IMMUTABLE_TYPES or
            id(type(anno)) in public_api._TYPING_IDS):  # pylint: disable=protected-access
        continue
      elif hasattr(anno, '__args__'):
        self._extract_non_builtin_types(anno, non_builtin_types)
      else:
        non_builtin_types.append(anno)
    return non_builtin_types

  def _get_non_builtin_ast_types(self, ast_typehint: str) -> List[str]:
    """Extracts non-builtin types from a string AST type annotation.

    If the type is an inbuilt type or an `...`(Ellipsis) then its skipped.

    Args:
      ast_typehint: AST extracted type annotation.

    Returns:
      List of non-builtin ast types.
    """

    non_builtin_ast_types = []
    for single_type, _ in self._INDIVIDUAL_TYPES_RE.findall(ast_typehint):
      if (not single_type or single_type in self._TYPING or
          single_type == '...'):
        continue
      non_builtin_ast_types.append(single_type)
    return non_builtin_ast_types

  def _linkify(self, non_builtin_map: Dict[str, Any], match) -> str:
    """Links off to types that can be linked.

    Args:
      non_builtin_map: Dictionary mapping non-builtin_ast_types to
        non_builtin_type_objs
      match: Match object returned by `re.sub`.

    Returns:
      Linked type annotation if the type annotation object exists.
    """

    group = match.groupdict()
    ast_single_typehint = group['single_type']

    # If the AST type hint is a built-in type hint or an `Ellipsis`,
    # return it as is.
    if ast_single_typehint not in non_builtin_map:
      return ast_single_typehint

    if not non_builtin_map:
      return ast_single_typehint

    # Get the type object from the ast_single_typehint and lookup the object
    # in reverse_index to get its full name.
    obj_full_name = self._reverse_index.get(
        id(non_builtin_map[ast_single_typehint]), None)
    if obj_full_name is None:
      return ast_single_typehint

    return self.get_link(obj_full_name)

  def preprocess(self, ast_typehint: str, obj_anno: Any) -> str:
    """Links type annotations to its page if it exists.

    Args:
      ast_typehint: AST extracted type annotation.
      obj_anno: Type annotation object.

    Returns:
      Linked type annotation if the type annotation object exists.
    """
    # If the object annotations exists in the reverse_index, get the link
    # directly for the entire annotation.
    obj_anno_full_name = self._reverse_index.get(id(obj_anno), None)
    if obj_anno_full_name is not None:
      return self.get_link(obj_anno_full_name)

    non_builtin_ast_types = self._get_non_builtin_ast_types(ast_typehint)
    try:
      non_builtin_type_objs = self._extract_non_builtin_types(obj_anno, [])
    except RecursionError:
      non_builtin_type_objs = {}

    # If the length doesn't match then don't linkify any type annotation. This
    # is done to avoid linking to wrong pages instead of guessing.
    if len(non_builtin_type_objs) != len(non_builtin_ast_types):
      non_builtin_map = {}
    else:
      non_builtin_map = dict(zip(non_builtin_ast_types, non_builtin_type_objs))

    partial_func = functools.partial(self._linkify, non_builtin_map)
    return self._INDIVIDUAL_TYPES_RE.sub(partial_func, ast_typehint)

  def _replace_internal_names(self, default_text: str) -> str:
    full_name_re = f'^{self._IDENTIFIER_RE}(.{self._IDENTIFIER_RE})+'
    match = re.match(full_name_re, default_text)
    if match:
      for internal_name, public_name in self._INTERNAL_NAMES.items():
        if match.group(0).startswith(internal_name):
          return public_name + default_text[len(internal_name):]
    return default_text

  def format_return(self, return_anno: Any) -> str:
    return self.preprocess(self._type_annotations['return'], return_anno)

  def format_args(self, args: List[inspect.Parameter]) -> List[str]:
    """Creates a text representation of the args in a method/function.

    Args:
      args: List of args to format.

    Returns:
      Formatted args with type annotations if they exist.
    """

    args_text_repr = []

    for arg in args:
      arg_name = arg.name
      if arg_name in self._type_annotations:
        typeanno = self.preprocess(self._type_annotations[arg_name],
                                   arg.annotation)
        args_text_repr.append(f'{arg_name}: {typeanno}')
      else:
        args_text_repr.append(f'{arg_name}')

    return args_text_repr

  def format_kwargs(self, kwargs: List[inspect.Parameter],
                    ast_defaults: Dict[str, str]) -> List[str]:
    """Creates a text representation of the kwargs in a method/function.

    Args:
      kwargs: List of kwargs to format.
      ast_defaults: Default values extracted from the function's AST tree.

    Returns:
      Formatted kwargs with type annotations if they exist.
    """

    kwargs_text_repr = []

    for kwarg in kwargs:
      kname = kwarg.name
      ast_default = ast_defaults.get(kname)
      default_val = kwarg.default

      if id(default_val) in self._reverse_index:
        default_text = self._reverse_index[id(default_val)]
      elif ast_default is not None:
        default_text = ast_default
        if default_text != repr(default_val):
          default_text = self._replace_internal_names(default_text)
      # Kwarg without default value.
      elif default_val is kwarg.empty:
        kwargs_text_repr.extend(self.format_args([kwarg]))
        continue
      else:
        # Strip object memory addresses to avoid unnecessary doc churn.
        default_text = self._OBJECT_MEMORY_ADDRESS_RE.sub(
            r'<\g<type>>', repr(default_val))
      default_text = html.escape(str(default_text))

      # Format the kwargs to add the type annotation and default values.
      if kname in self._type_annotations:
        typeanno = self.preprocess(self._type_annotations[kname],
                                   kwarg.annotation)
        kwargs_text_repr.append(f'{kname}: {typeanno} = {default_text}')
      else:
        kwargs_text_repr.append(f'{kname}={default_text}')

    return kwargs_text_repr


class SignatureComponents(NamedTuple):
  """Contains the components that make up the signature of a function/method."""

  arguments: List[str]
  arguments_typehint_exists: bool
  return_typehint_exists: bool
  return_type: Optional[str] = None

  def __str__(self):
    arguments_signature = ''
    if self.arguments:
      str_signature = ',\n'.join(self.arguments)
      # If there is no type annotation on arguments, then wrap the entire
      # signature to width 80.
      if not self.arguments_typehint_exists:
        str_signature = textwrap.fill(str_signature, width=80)
      arguments_signature = '\n' + textwrap.indent(
          str_signature, prefix='    ') + '\n'

    full_signature = f'({arguments_signature})'
    if self.return_typehint_exists:
      full_signature += f' -> {self.return_type}'

    return full_signature


class FuncType(enum.Enum):
  """Enum to recognize type of function passed to `generate_signature`."""
  FUNCTION = 'function'
  METHOD = 'method'
  CLASSMETHOD = 'classmethod'


def get_method_type(method, name, is_dataclass):

  if isinstance(method, classmethod):
    func_type = FuncType.CLASSMETHOD
  elif name == '__new__':
    # __new__ acts like a regular method for this.
    # - At this point all args are visible in the signature.
    # - When used the first argument gets boound (like self).
    # - Sometimes users wrap it with a `staticmethod` but that gets ignored.
    func_type = FuncType.METHOD
  elif isinstance(method, staticmethod):
    func_type = FuncType.FUNCTION
  elif is_dataclass:
    # When building the init signature directly from a dataclass-class (for
    # the auto-generated __init__) `self` is already removed from the
    # signature.
    func_type = FuncType.FUNCTION
  else:
    func_type = FuncType.METHOD
  return func_type


def generate_signature(
    func: Any,
    parser_config: config.ParserConfig,
    func_full_name: str,
    func_type: FuncType = FuncType.FUNCTION,
) -> SignatureComponents:
  """Given a function, returns a list of strings representing its args.

  This function uses `__name__` for callables if it is available. This can lead
  to poor results for functools.partial and other callable objects.

  The returned string is Python code, so if it is included in a Markdown
  document, it should be typeset as code (using backticks), or escaped.

  Args:
    func: A function, method, or functools.partial to extract the signature for.
    parser_config: `config.ParserConfig` for the method/function whose signature is
      generated.
    func_full_name: The full name of a function whose signature is generated.
    func_type: Type of the current `func`. This is required because there isn't
      a clear distinction between function and method being passed to
      `generate_signature`. Sometimes methods are detected as function by
      `inspect`. Since we know the type of `func` when generate_signature is
      called, use that to pass the type of `func`.

  Returns:
    A `SignatureComponents` NamedTuple.
  """

  all_args_list = []

  try:
    sig = inspect.signature(func)
    sig_values = sig.parameters.values()
    return_anno = sig.return_annotation
  except (ValueError, TypeError):
    sig_values = []
    return_anno = None

  if dataclasses.is_dataclass(func):
    type_annotation_visitor = _DataclassTypeAnnotationExtractor()
  else:
    type_annotation_visitor = _TypeAnnotationExtractor()

  ast_defaults_visitor = _ASTDefaultValueExtractor()

  try:
    func_source = textwrap.dedent(inspect.getsource(func))
    func_ast = ast.parse(func_source)
    # Extract the type annotation from the parsed ast.
    type_annotation_visitor.visit(func_ast)
    ast_defaults_visitor.visit(func_ast)
  except Exception:  # pylint: disable=broad-except
    # A wide-variety of errors can be thrown here.
    pass

  type_annotations = type_annotation_visitor.annotation_dict
  arguments_typehint_exists = type_annotation_visitor.arguments_typehint_exists
  return_typehint_exists = type_annotation_visitor.return_typehint_exists

  #############################################################################
  # Process the information about the func.
  #############################################################################

  pos_only_args = []
  args = []
  kwargs = []
  only_kwargs = []
  varargs = None
  varkwargs = None

  for index, param in enumerate(sig_values):
    kind = param.kind
    default = param.default

    if (index == 0 and func_type == FuncType.METHOD and
        kind != param.VAR_POSITIONAL):
      # - Skip the first arg for regular methods.
      # - Some wrapper methods forget `self` and just use `(*args, **kwargs)`.
      #   That's still valid, don't drop `*args`.
      # - For classmethods the `cls` arg already bound here (it's not in
      #   `sig_values`).
      # - For regular functions (or staticmethods) you never need to skip.
      continue
    elif kind == param.POSITIONAL_ONLY:
      pos_only_args.append(param)
    elif default is param.empty and kind == param.POSITIONAL_OR_KEYWORD:
      args.append(param)
    elif default is not param.empty and kind == param.POSITIONAL_OR_KEYWORD:
      kwargs.append(param)
    elif kind == param.VAR_POSITIONAL:
      varargs = (index, param)
    elif kind == param.KEYWORD_ONLY:
      only_kwargs.append(param)
    elif kind == param.VAR_KEYWORD:
      varkwargs = param

  #############################################################################
  # Build the text representation of Args and Kwargs.
  #############################################################################

  formatter = FormatArguments(
      type_annotations, parser_config, func_full_name=func_full_name)

  if pos_only_args:
    all_args_list.extend(formatter.format_args(pos_only_args))
    all_args_list.append('/')

  if args:
    all_args_list.extend(formatter.format_args(args))

  if kwargs:
    all_args_list.extend(
        formatter.format_kwargs(kwargs, ast_defaults_visitor.ast_args_defaults))

  if only_kwargs:
    if varargs is None:
      all_args_list.append('*')
    all_args_list.extend(
        formatter.format_kwargs(only_kwargs,
                                ast_defaults_visitor.ast_kw_only_defaults))

  if varargs is not None:
    all_args_list.insert(varargs[0], '*' + varargs[1].name)

  if varkwargs is not None:
    all_args_list.append('**' + varkwargs.name)

  if return_anno and return_anno is not sig.empty and type_annotations.get(
      'return', None):
    return_type = formatter.format_return(return_anno)
  else:
    return_type = 'None'

  return SignatureComponents(
      arguments=all_args_list,
      arguments_typehint_exists=arguments_typehint_exists,
      return_typehint_exists=return_typehint_exists,
      return_type=return_type)

def extract_decorators(func: Any) -> List[str]:
  """Extracts the decorators on top of functions/methods.

  Args:
    func: The function to extract the decorators from.

  Returns:
    A List of decorators.
  """

  class ASTDecoratorExtractor(ast.NodeVisitor):

    def __init__(self):
      self.decorator_list = []

    def visit_FunctionDef(self, node):  # pylint: disable=invalid-name
      for dec in node.decorator_list:
        self.decorator_list.append(astor.to_source(dec).strip())

  visitor = ASTDecoratorExtractor()

  try:
    # Note: inspect.getsource doesn't include the decorator lines on classes,
    # this won't work for classes until that's fixed.
    func_source = textwrap.dedent(inspect.getsource(func))
    func_ast = ast.parse(func_source)
    visitor.visit(func_ast)
  except Exception:  # pylint: disable=broad-except
    # A wide-variety of errors can be thrown here.
    pass

  return visitor.decorator_list
