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
import copy
import dataclasses
import enum
import functools
import html
import inspect
import re
import textwrap
import typing

from typing import Any, Callable, Dict, List, Optional, Tuple, Type

import astor

from tensorflow_docs.api_generator import config
from tensorflow_docs.api_generator import get_source
from tensorflow_docs.api_generator import public_api

EMPTY = inspect.Signature.empty


def _source_from_ast(node: ast.AST) -> str:
  return astor.to_source(node).strip().replace('"""', "'")


class _BaseDefaultAndAnnotationExtractor(ast.NodeVisitor):
  """A base class for extracting annotations and defaults from the AST."""
  _PAREN_NUMBER_RE = re.compile(r'^\((True|False|[0-9.e-]+)\)')

  def __init__(self):
    self.annotations = {}
    self.defaults = {}
    self.return_annotation = EMPTY

  def _preprocess_default(self, val: ast.AST) -> str:
    text_default_val = (
        _source_from_ast(val).replace('\t', '\\t').replace('\n', '\\n'))
    text_default_val = self._PAREN_NUMBER_RE.sub('\\1', text_default_val)
    return text_default_val

  def extract(self, obj: Any):
    obj_ast = get_source.get_ast(obj)
    if obj_ast is not None:
      self.visit(obj_ast)


class _ArgDefaultAndAnnotationExtractor(_BaseDefaultAndAnnotationExtractor):
  """Extracts the type annotations by parsing the AST of a function."""

  def visit_FunctionDef(self, node) -> None:  # pylint: disable=invalid-name
    """Visits the `FunctionDef` node in AST tree and extracts the typehints."""

    # Capture the return type annotation.
    if node.returns:
      self.return_annotation = _source_from_ast(node.returns)

    # Capture the args type annotation.
    for arg in node.args.args:
      if arg.annotation:
        self.annotations[arg.arg] = _source_from_ast(arg.annotation)
        self.arguments_typehint_exists = True

    # Capture the kwarg only args type annotation.
    for kwarg in node.args.kwonlyargs:
      if kwarg.annotation:
        self.annotations[kwarg.arg] = _source_from_ast(kwarg.annotation)
        self.arguments_typehint_exists = True

    # From https://docs.python.org/3/library/ast.html#ast.arguments:
    #   `defaults` is a list of default values for arguments that can be passed
    #   positionally. If there are fewer defaults, they correspond to the last
    #   n arguments.

    last_n_pos_args = node.args.args[-1 * len(node.args.defaults):]
    for arg, default_val in zip(last_n_pos_args, node.args.defaults):
      if default_val is not None:
        text_default_val = self._preprocess_default(default_val)
        self.defaults[arg.arg] = text_default_val

    for kwarg, default_val in zip(node.args.kwonlyargs, node.args.kw_defaults):
      if default_val is not None:
        text_default_val = self._preprocess_default(default_val)
        self.defaults[kwarg.arg] = text_default_val


class _ClassDefaultAndAnnotationExtractor(_BaseDefaultAndAnnotationExtractor):
  """Extracts the type annotations by parsing the AST of a dataclass."""

  def __init__(self):
    super().__init__()
    self.annotations = {}
    self.defaults = {}
    self.return_annotation = EMPTY

  def visit_ClassDef(self, node) -> None:  # pylint: disable=invalid-name
    # Don't visit all nodes. Only visit top-level AnnAssign nodes so that
    # If there's an AnnAssign in a method it doesn't get picked up.
    for sub in node.body:
      if isinstance(sub, ast.AnnAssign):
        self.visit_AnnAssign(sub)
      elif isinstance(sub, ast.Assign):
        self.visit_Assign(sub)

  def visit_AnnAssign(self, node) -> None:  # pylint: disable=invalid-name
    """Vists an assignment with a type annotation. Dataclasses is an example."""

    arg = _source_from_ast(node.target)
    self.annotations[arg] = _source_from_ast(node.annotation)
    if node.value is not None:
      self.defaults[arg] = self._preprocess_default(node.value)

  def visit_Assign(self, node) -> None:  # pylint: disable=invalid-name
    """Vists an assignment with a type annotation. Dataclasses is an example."""
    names = [_source_from_ast(t) for t in node.targets]
    if node.value is not None:
      val = self._preprocess_default(node.value)
      for name in names:
        self.defaults[name] = val

  def extract(self, cls):
    # Iterate over the classes in reverse order so each class overwrites it's
    # parents. Skip `object`.
    for cls in reversed(cls.__mro__[:-1]):
      super().extract(cls)


_OBJECT_MEMORY_ADDRESS_RE = re.compile(r'<(?P<type>.+?) at 0x[\da-f]+>')


def strip_obj_addresses(text):
  return _OBJECT_MEMORY_ADDRESS_RE.sub(r'<\g<type>>', text)


class FormatArguments(object):
  """Formats the arguments and adds type annotations if they exist."""

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
      parser_config: config.ParserConfig,
  ) -> None:
    self._reverse_index = parser_config.reverse_index
    self._reference_resolver = parser_config.reference_resolver

  def get_link(self,
               link_text: str,
               obj_full_name: Optional[str] = None) -> str:
    return self._reference_resolver.python_link(
        link_text=link_text, ref_full_name=obj_full_name)

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

  def maybe_add_link(self, source: str, value: Any) -> str:
    """Return a link to an object's api page if found.

    Args:
      source: The source string from the code.
      value: The value of the object.

    Returns:
      The original string with maybe an HTML link added.
    """
    cls = type(value)

    value_name = self._reverse_index.get(id(value), None)
    cls_name = self._reverse_index.get(id(cls), None)

    if cls_name is not None:
      # It's much more common for the class to be documented than the instance.
      # and the class page will provide better docs.
      before = source.split('(')[0]
      cls_short_name = cls_name.split('.')[-1]
      if before.endswith(cls_short_name):
        # Yes, this is a guess but it will usually be right.
        return self.get_link(source, cls_name)

    if value_name is not None:
      return self.get_link(value_name, value_name)

    return source

  def preprocess(self, string: str, value: Any) -> str:
    """Links type annotations to its page if it exists.

    Args:
      string: AST extracted type annotation.
      value: Type annotation object.

    Returns:
      Linked type annotation if the type annotation object exists.
    """
    # If the object annotations exists in the reverse_index, get the link
    # directly for the entire annotation.
    obj_anno_full_name = self._reverse_index.get(id(value), None)
    if obj_anno_full_name is not None:
      return self.get_link(obj_anno_full_name)

    non_builtin_ast_types = self._get_non_builtin_ast_types(string)
    try:
      non_builtin_type_objs = self._extract_non_builtin_types(value, [])
    except RecursionError:
      non_builtin_type_objs = {}

    # If the length doesn't match then don't linkify any type annotation. This
    # is done to avoid linking to wrong pages instead of guessing.
    if len(non_builtin_type_objs) != len(non_builtin_ast_types):
      non_builtin_map = {}
    else:
      non_builtin_map = dict(zip(non_builtin_ast_types, non_builtin_type_objs))

    partial_func = functools.partial(self._linkify, non_builtin_map)
    return self._INDIVIDUAL_TYPES_RE.sub(partial_func, string)

  def format_return(self, return_anno: Tuple[Any, str]) -> str:
    value, source = return_anno
    return self.preprocess(source, value)

  def format_args(self, args: List[inspect.Parameter]) -> List[str]:
    """Creates a text representation of the args in a method/function.

    Args:
      args: List of args to format.

    Returns:
      Formatted args with type annotations if they exist.
    """

    args_text_repr = []

    for arg in args:
      typeanno = None
      if arg.annotation is not EMPTY:
        value, source = arg.annotation
        if source is not None:
          typeanno = self.preprocess(source, value)

      if typeanno:
        args_text_repr.append(f'{arg.name}: {typeanno}')
      else:
        args_text_repr.append(f'{arg.name}')

    return args_text_repr

  def format_kwargs(self, kwargs: List[inspect.Parameter]) -> List[str]:
    """Creates a text representation of the kwargs in a method/function.

    Args:
      kwargs: List of kwargs to format.

    Returns:
      Formatted kwargs with type annotations if they exist.
    """

    kwargs_text_repr = []

    for kwarg in kwargs:
      default_text = None
      if kwarg.default is not EMPTY:
        default_val, default_source = kwarg.default
        if default_source is None:
          default_source = strip_obj_addresses(repr(default_val))
        default_source = html.escape(default_source)

        default_text = self.maybe_add_link(default_source, default_val)

      # Format the kwargs to add the type annotation and default values.
      typeanno = None
      if kwarg.annotation is not EMPTY:
        anno_value, anno_source = kwarg.annotation
        if anno_source is not None:
          typeanno = self.preprocess(anno_source, anno_value)

      if typeanno is not None and default_text is not None:
        kwargs_text_repr.append(f'{kwarg.name}: {typeanno} = {default_text}')
      elif default_text is not None:
        kwargs_text_repr.append(f'{kwarg.name}={default_text}')
      elif typeanno is not None:
        kwargs_text_repr.append(f'{kwarg.name}: {typeanno}')
      else:
        kwargs_text_repr.append(kwarg.name)

    return kwargs_text_repr


class TfSignature(inspect.Signature):
  """A custom version of `inspect.Signature`."""

  def __init__(self, parameters, *, return_annotation, parser_config):
    super().__init__(parameters, return_annotation=return_annotation)  # pytype: disable=wrong-arg-types  # mapping-is-not-sequence
    self.parser_config = parser_config

  def replace(self, **kwargs):
    attrs = {
        'parameters': self.parameters,
        'return_annotation': self.return_annotation,
        'parser_config': self.parser_config,
    }
    attrs.update(kwargs)
    return type(self)(**attrs)

  def __copy__(self):
    return TfSignature(
        list(self.parameters.values()),
        return_annotation=self.return_annotation,
        parser_config=self.parser_config)

  def __deepcopy__(self, memo):
    return TfSignature(
        copy.deepcopy(list(self.parameters.values()), memo),
        return_annotation=copy.deepcopy(self.return_annotation, memo),
        parser_config=copy.deepcopy(self.parser_config, memo))

  def __str__(self):
    # separate the args by type
    pos_only_args = []
    args = []
    kwargs = []
    only_kwargs = []
    varargs = None
    varkwargs = None

    for index, param in enumerate(self.parameters.values()):
      kind = param.kind
      default = param.default

      if kind == param.POSITIONAL_ONLY:
        pos_only_args.append(param)
      elif default is EMPTY and kind == param.POSITIONAL_OR_KEYWORD:
        args.append(param)
      elif default is not EMPTY and kind == param.POSITIONAL_OR_KEYWORD:
        kwargs.append(param)
      elif kind == param.VAR_POSITIONAL:
        varargs = (index, param)
      elif kind == param.KEYWORD_ONLY:
        only_kwargs.append(param)
      elif kind == param.VAR_KEYWORD:
        varkwargs = param

    # Build the text representation.
    all_args_list = []

    formatter = FormatArguments(parser_config=self.parser_config)

    if pos_only_args:
      all_args_list.extend(formatter.format_args(pos_only_args))
      all_args_list.append('/')

    if args:
      all_args_list.extend(formatter.format_args(args))

    if kwargs:
      all_args_list.extend(formatter.format_kwargs(kwargs))

    if only_kwargs:
      if varargs is None:
        all_args_list.append('*')
      all_args_list.extend(formatter.format_kwargs(only_kwargs))

    if varargs is not None:
      all_args_list.insert(varargs[0], '*' + varargs[1].name)

    if varkwargs is not None:
      all_args_list.append('**' + varkwargs.name)

    return_annotation_text = ''
    if self.return_annotation is not EMPTY:
      if EMPTY not in self.return_annotation:
        return_annotation_text = formatter.format_return(self.return_annotation)

    arguments_signature = ''
    has_any_annotations = any(
        v.annotation is not EMPTY for v in self.parameters.values())
    if all_args_list:
      str_signature = ',\n'.join(all_args_list)
      # If it fits on one line flatten it.
      if len(str_signature) + 4 < 80:
        str_signature = textwrap.fill(str_signature, width=80)

      arguments_signature = '\n' + textwrap.indent(
          str_signature, prefix='    ') + '\n'

    full_signature = f'({arguments_signature})'
    if return_annotation_text:
      full_signature = f'({arguments_signature}) -> {return_annotation_text}'
    else:
      full_signature = f'({arguments_signature})'
    return full_signature


class FuncType(enum.Enum):
  """Enum to recognize type of function passed to `generate_signature`."""
  FUNCTION = 'function'
  METHOD = 'method'
  CLASSMETHOD = 'classmethod'


def get_method_type(method, name, is_dataclass):
  """Determine the type of callable."""
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
    func_type: FuncType = FuncType.FUNCTION,
) -> TfSignature:
  """Given a function, returns a list of strings representing its args.

  This function uses `__name__` for callables if it is available. This can lead
  to poor results for functools.partial and other callable objects.

  The returned string is Python code, so if it is included in a Markdown
  document, it should be typeset as code (using backticks), or escaped.

  Args:
    func: A function, method, or functools.partial to extract the signature for.
    parser_config: `config.ParserConfig` for the method/function whose signature
      is generated.
    func_type: Type of the current `func`. This is required because there isn't
      a clear distinction between function and method being passed to
      `generate_signature`. Sometimes methods are detected as function by
      `inspect`. Since we know the type of `func` when generate_signature is
      called, use that to pass the type of `func`.

  Returns:
    A `SignatureComponents` NamedTuple.
  """
  try:
    sig = inspect.signature(func)
  except (ValueError, TypeError):
    sig = inspect.signature(lambda: None)

  params = list(sig.parameters.values())

  # Drop `self`
  if params:
    first = params[0]
    if first.kind != first.VAR_POSITIONAL:
      if func_type == FuncType.METHOD:
        # - Skip the first arg for regular methods.
        # - Some wrapper methods forget `self` and just use `(*args, **kwargs)`.
        #   That's still valid, don't drop `*args`.
        # - For classmethods the `cls` arg already bound here (it's not in
        #   `params`).
        # - For regular functions (or staticmethods) you never need to skip.
        params.pop(0)

  sig = sig.replace(parameters=params)

  if dataclasses.is_dataclass(func):
    sig = sig.replace(return_annotation=EMPTY)
    extract_fn = _extract_class_defaults_and_annotations
  else:
    extract_fn = _extract_arg_defaults_and_annotations

  (annotation_source_dict, defaults_source_dict,
   return_annotation_source) = extract_fn(func)

  # Replace everything with either `EMPTY` or (value, source) pairs.
  new_params = []
  for name, param in sig.parameters.items():
    default = param.default
    if default is not EMPTY:
      default = (default, defaults_source_dict.get(name, None))

    annotation = param.annotation
    if annotation is not EMPTY:
      annotation = (annotation, annotation_source_dict.get(name, None))

    param = param.replace(default=default, annotation=annotation)
    new_params.append(param)

  return_annotation = sig.return_annotation
  if return_annotation is not EMPTY:
    return_annotation = (return_annotation, return_annotation_source)

  sig = TfSignature(
      parameters=new_params,
      return_annotation=return_annotation,
      parser_config=parser_config)

  return sig


AnnotsDefaultsReturns = Tuple[Dict[str, str], Dict[str, str], Any]


def _extract_class_defaults_and_annotations(
    cls: Type[object]) -> AnnotsDefaultsReturns:
  """Extract ast defaults and annotations form a dataclass."""
  ast_visitor = _ClassDefaultAndAnnotationExtractor()
  ast_visitor.extract(cls)

  return (ast_visitor.annotations, ast_visitor.defaults,
          ast_visitor.return_annotation)


def _extract_arg_defaults_and_annotations(
    func: Callable[..., Any]) -> AnnotsDefaultsReturns:
  """Extract ast defaults and annotations form a standard callable."""

  ast_visitor = _ArgDefaultAndAnnotationExtractor()

  annotation_source_dict = {}
  defaults_source_dict = {}
  return_annotation_source = EMPTY

  try:
    # Extract the type annotation from the parsed ast.
    ast_visitor.extract(func)
  except Exception:  # pylint: disable=broad-except
    # A wide-variety of errors can be thrown here.
    pass
  else:
    annotation_source_dict = ast_visitor.annotations
    defaults_source_dict = ast_visitor.defaults
    return_annotation_source = ast_visitor.return_annotation

  return annotation_source_dict, defaults_source_dict, return_annotation_source


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
        self.decorator_list.append(_source_from_ast(dec))

  visitor = ASTDecoratorExtractor()

  # Note: get_source doesn't include the decorator lines on classes,
  # this won't work for classes until that's fixed.
  func_ast = get_source.get_ast(func)
  if func_ast is not None:
    visitor.visit(func_ast)

  return visitor.decorator_list
