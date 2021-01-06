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
r"""Defines the @lint API used in style files to create lint tests.

Users define lints by adding the @lint decorator to test functions. A collection
of lint functions are grouped in a style module. Style modules can be
enabled/disabled at the command-line.

Lint functions must return a Boolean value: True for pass, False for fail.
Negative assertions must follow this logic, always pass True if the lint test is
considered a success.

Whether a lint assertion passes or fails depends on its scope and condition
parameters:

- The *condition* determines if a test is considered a success if it passes for
  *all* cells in the notebook, or *any* cells (just one).
- The *scope* determines where the assertion should be executed: for all
notebook
  cells, only text cells, only code, cells, or just run once per notebook.

Implementation-wise, the @lint decorator creates a `Lint` instance that is
attached to the underlying function object within the style module. When the
module is imported into the `Linter`, the `Lint` object is extracted.

"""
import enum
import functools

from typing import Any, Callable, List, Optional


class Options:
  """Options to define the condition and scope of a @lint defined assertion."""

  class Cond(enum.Enum):
    """Determines if a test is considered a success by which cells it passes.

    Attributes:
      ALL: Success if all cells pass.
      ANY: Success if any cells pass (just one). [Default]
    """
    ALL = enum.auto()
    ANY = enum.auto()

  class Scope(enum.Enum):
    """Determines where a function test is executed.

    Attributes:
      CELLS: Code and text cells. [Default]
      CODE: Code cells only.
      TEXT: Text cells only.
      FILE: Run assertion function once per file.
    """
    CELLS = enum.auto()
    CODE = enum.auto()
    TEXT = enum.auto()
    FILE = enum.auto()


class Lint:
  """Contains the function and properties defined by the @lint decorator.

  Attributes:
    run: User-defined assertion callback that returns a Boolean.
    scope: `Options.Scope` to determine where an assertion is executed.
    cond: `Options.Cond` to determine if an assertion is considered a success.
    name: Optional string name for assertion function in reports.
    message: String message to include in status report.
    style: String name of style module that defines the Lint. (Added on load.)
  """

  def __init__(self, fn, scope, cond, message=None, name=None):
    self.run = fn
    self.scope = scope
    self.cond = cond
    self.name = name if name else fn.__name__
    self.message = message.strip() if message else ""
    self.style = None  # Added on style load.


# Define a decorator with optional arguments.
def lint(fn=None, *, message=None, scope=None, cond=None):
  """Function decorator for user-defined lint assertions.

  Args:
    fn: User-defined assertion callback that returns a Boolean. See `Linter.run`
      for args passed to callback, depending on scope:
        * For cell-scope: callback(source, cell_data, path).
        * For file-scope: callback(source, all_data, path)
    message: Optional string message to include in status report.
    scope: Determines where the function should be executed, options in
      `Options.Scope`.
    cond: Determines how an assertion is considered a success, if it passes all
      cells or any cells. Options available in `Options.Cond`.

  Returns:
    Function: A wrapper around the user-defined `fn` function.
  """
  if fn is None:
    return functools.partial(lint, message=message, scope=scope, cond=cond)

  scope = scope if scope else Options.Scope.CELLS
  cond = cond if cond else Options.Cond.ANY

  @functools.wraps(fn)
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs)

  # Attach to function object to access when importing the style module.
  setattr(wrapper, "_lint", Lint(fn, scope, cond, message))
  return wrapper


class LintFailError(Exception):
  """Exception raised for lint failure with optional message.

    Attributes:
      message: String message to add to status log.
      always_show: Boolean if failure message should display in status,
        regardless if larger conditional met.
      fix_fn: Optional Callable to run that fixes the lint failure.
      fix_args: List of arguments passed to the `fix_fn` Callable.
  """

  def __init__(self,
               message: str = "Lint failure",
               always_show: bool = False,
               fix_fn: Optional[Callable[[], None]] = None,
               fix_args: Optional[List[Any]] = None):
    self.message: str = message
    self.always_show: bool = always_show
    self.fix_fn: Optional[Callable[[], None]] = fix_fn
    if fix_args is None:
      fix_args = []
    self.fix_args: List[Any] = fix_args
    super().__init__(self.message)


def fail(message: Optional[str] = None,
         always_show: bool = False,
         fix: Optional[Callable[[], None]] = None,
         fix_args: Optional[List[Any]] = None) -> None:
  """Signal within a @lint function that the test fails.

  While sufficient to simply return False from a failing @lint function, this
  function can add a message to the status log to provide the user additional
  context. Stack trace available with `--verbose` flag.

  Failure messages come in two flavors:
  - conditional: (Default) While this test may fail here, it may succeed
    elsewhere, and thus, the larger condition passes and do not dislay this
    message.
  - non-conditional (always show): Regardless if the larger condition is met,
    display this error message in the status report. For example, a
    configuration error should always display, even if the test succeeds
    elsewhere.

  A `fix` function/Callable is executed with the --fix command-line option. It
  is run as `fn(lint_args, *fix_args)` and executed once for each unique fn-args
  pair. Callbacks passed the same arg are deduplicated.

  Args:
    message: String message to add to status log.
    always_show: Boolean if failure message should display in status, reguardles
      if larger conditional met.
    fix: Optional Callable to run that fixes the lint failure.
    fix_args: Optional list of arguments passed to the `fix` Callable.

  Raises:
    LintFailError: Lint failure with optional message.
  """
  raise LintFailError(message, always_show, fix, fix_args)
