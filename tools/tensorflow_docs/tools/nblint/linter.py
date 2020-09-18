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
r"""Import lint tests, run lints, and report status.

A `Linter` instance imports lint tests from a style file into a structured queue
that are then run on notebook files. Depending on condition and scope options,
these are executed for the entire notebook or for each text and code cell.

A `LinterStatus` instance is returned when lint tests are run on a file. While
a single `Linter` instance can be run on multiple files, a `LinterStatus` is
associated with a single notebook file. It maintains the pass/fail state for
each lint test on the file. Additionally, `LinterStatus` implements the
formatting required to print the report that the console.
"""
import collections
import io
import pathlib
import sys
import traceback

from typing import Any, Callable, Dict, List, NamedTuple, Optional, Set, Tuple

from tensorflow_docs.tools.nbfmt import notebook_utils
from tensorflow_docs.tools.nblint import decorator


# Custom type for a dictionary containing the lint styles.
LintDict = Dict[decorator.Options.Scope, Dict[decorator.Options.Cond,
                                              List[decorator.Lint]]]


class Linter:
  """Manages the collection of lints to execute on a notebook.

  Lint assertions are imported by style modules and dispatched by condition and
  scope. A Linter can be run on multiple notebooks.

  Attributes:
    verbose: Boolean to print more details to console. Default is False.
  """

  class RunLintStatus(NamedTuple):
    """The return status and metadata from an executed lint function.

    Attributes:
      is_success: Boolean
      lint: `decorator.Lint` associated with this status.
      lint_args: Dict of args passed to lint function.
      cond_fail_msg: Optional string to print in failure message.
      fix_fn: Optional Callable to run that fixes the lint failure.
      fix_args: List of arguments passed to the `fix_fn` Callable.
    """
    is_success: bool
    lint: decorator.Lint
    lint_args: Dict[str, Any]
    cond_fail_msg: Optional[str] = None
    fix_fn: Optional[Callable[[], None]] = None
    fix_args: List[Any] = []

  def __init__(self, verbose: bool = False):
    self.verbose: bool = verbose

  def _load_notebook(self, path: pathlib.Path) -> Tuple[Dict[str, Any], str]:
    """Load and parse JSON data from a notebook file.

    Args:
      path: A `pathlib.Path` of a Jupyter notebook.

    Returns:
      Dict: Contains data of the parsed JSON notebook.
      String: The entire JSON source code of the notebook.
    """
    data, source = notebook_utils.load_notebook(path)

    if not data:
      sys.exit(1)  # load_notebook prints warning.

    return data, source

  def _run_lint(self, lint: decorator.Lint, lint_args: Dict[str, Any],
                status: "LinterStatus") -> "Linter.RunLintStatus":
    """Run lint and capture any stderr output for the status display.

    Args:
      lint: `decorator.Lint` containg the assertion, scope, and condition.
      lint_args: Nested dictionary of args to pass the lint callback function.
      status: The `LinterStatus` to add individual entries for group members.

    Returns:
      Linter.RunLintStatus: Return status and metadata for this lint function.
    """

    cond_fail_msg = None
    fix_fn = None
    fix_args = []
    try:
      is_success = lint.run(lint_args)
    except decorator.LintFailError as err:
      is_success = False
      fix_fn = err.fix_fn
      fix_args = err.fix_args
      if err.always_show:
        # Grab stack trace and carry on.
        f = io.StringIO()
        traceback.print_exc(file=f)
        trace = f.getvalue()
        # Add any non-conditional failure messages to queue. Will de-dup.
        status.log_lint_message(err.message, lint, verbose_msg=trace)
      else:
        # Defer logging a conditional message until the group status is known.
        cond_fail_msg = err.message

    return self.RunLintStatus(is_success, lint, lint_args, cond_fail_msg,
                              fix_fn, fix_args)

  def _run_lint_group(self, lint: decorator.Lint, lint_args: Dict[str, Any],
                      data: Dict[str, Any],
                      status: "LinterStatus") -> Tuple[bool, Set[str]]:
    """Run lint over all cells with scope and return cumulative pass/fail.

    Args:
      lint: `decorator.Lint` containg the assertion, scope, and condition.
      lint_args: Nested dictionary of args to pass the lint callback function.
      data: `dict` containing data of entire parse notebook.
      status: The `LinterStatus` to add individual entries for group members.

    Returns:
      Boolean: True if lint passes for all/any cells, otherwise False.
      Set: Deduplicated list of failure message strings.

    Raises:
      Exception: Unsupported lint condition in `decorator.Options.Cond`.
    """
    scope: decorator.Options.Scope = lint.scope
    # Return value of each (scoped) cell in notebook.
    is_success_list: List[bool] = []
    # All conditional failure messages from lint function (deduplicated).
    cond_fail_message_list: Set[str] = set()

    for cell_idx, cell in enumerate(data.get("cells")):
      # Evict notebook cells outside of scope.
      cell_type = cell.get("cell_type")
      if scope is decorator.Options.Scope.TEXT and cell_type != "markdown":
        continue
      elif scope is decorator.Options.Scope.CODE and cell_type != "code":
        continue

      # Add cell-specific data to args passed to lint callback.
      lint_args["cell_data"] = cell
      lint_args["cell_source"] = "".join(cell["source"])

      # Execute lint on cell and collect result.
      run_status = self._run_lint(lint, lint_args, status)
      is_success_list.append(run_status.is_success)
      if run_status.cond_fail_msg:
        cond_fail_message_list.add(run_status.cond_fail_msg)

      # All lint runs get a status entry. Group success is a separate entry.
      name = f"{lint.name}__cell_{cell_idx}"
      status.add_entry(
          lint, run_status, name=name, group=lint.name, is_group_entry=True)

    # Return True/False success for entire cell group.
    if lint.cond is decorator.Options.Cond.ANY:
      return any(is_success_list), cond_fail_message_list
    elif lint.cond is decorator.Options.Cond.ALL:
      return all(is_success_list), cond_fail_message_list
    else:
      raise Exception("Unsupported lint condition.")

  def run(self, path: pathlib.Path, lint_dict: LintDict,
          user_args_dict: Dict[str, Any]) -> "LinterStatus":
    """Multiple hooks provided to run tests at specific points.

    Args:
      path: `pathlib.Path` of notebook to run lints against.
      lint_dict: A dictionary containing the lint styles.
      user_args_dict: Dictionary of user-defined args passed to lint callback.

    Returns:
      LinterStatus: Provides status and reporting of lint tests for a notebook.
    """
    data, source = self._load_notebook(path)
    if not data:
      return False

    # Args passed to lint callback function.
    lint_args = {
        "cell_data": None,  # Added per-cell in _run_lint_group.
        "cell_source": None,  # Added per-cell in _run_lint_group.
        "file_data": data,
        "file_source": source,
        "path": path,
        "user": user_args_dict
    }

    status = LinterStatus(path, verbose=self.verbose)

    # File-level scope.
    # Lint run once for the file.
    for lint in lint_dict[decorator.Options.Scope.FILE][
        decorator.Options.Cond.ANY]:
      run_status = self._run_lint(lint, lint_args, status)
      status.add_entry(lint, run_status)

    # Cell-level scope.
    # These lints run on each cell, then return a cumulative result.
    for scope in [
        decorator.Options.Scope.CELLS, decorator.Options.Scope.CODE,
        decorator.Options.Scope.TEXT
    ]:
      for cond in decorator.Options.Cond:
        lints = lint_dict[scope][cond]
        for lint in lints:
          # Run lint group and create a separate group status.
          is_success, cond_fail_msgs = self._run_lint_group(
              lint, lint_args, data, status)
          run_status = Linter.RunLintStatus(is_success, lint, lint_args)
          status.add_entry(lint, run_status, group=lint.name)
          if not is_success:
            # Once group status is known, log any conditional messages.
            for msg in cond_fail_msgs:
              # Grab stack trace and carry on.
              f = io.StringIO()
              traceback.print_exc(file=f)
              trace = f.getvalue()
              # Add any non-conditional failure messages to queue. Will de-dup.
              status.log_lint_message(msg, lint, verbose_msg=trace)

    return status


class LinterStatus:
  """Provides status and reporting of lint tests for a notebook.

  A new `LinterStatus` object is returned when `Linter.run` is executed on a
  given notebook. A `LinterStatus` object represents a run of all lints for a
  single notebook file. Multiple notebook files require multiple `LinterStatus`
  objects. Though multiple status objects can be created by the same `Linter`.

  The `LinterStatus` instance manages `LintStatusEntry` objects. These are added
  in the `Linter.run` for each lint test. Some entries may be a part of a larger
  lint group that represents a collective pass/fail status.

  A `LinterStatus` instance is also reponsible for printing status reports for
  entries to the console to display to the user.

  Attributes:
    path: `pathlib.Path` of notebook that lints were run against.
    verbose: Boolean to print more details to console. Default is False.
    is_success: Boolean status of entire lint report: True if all tests pass,
      otherwise False.
  """

  class LintStatusEntry(NamedTuple):
    """Represents the status of a lint tested against a single section.

    Depending on the scope of the lint, one lint can create multiple
    `LintStatusEntry` objects. For example, if tested against all notebook
    cells, one status entry would be created for each cell it is run on. This
    would also create a group entry representing the cumulative conditional
    test: any/all.

    Groups are determined by a shared a group name. If an entry is designed with
    True for `is_group_entry`, that means it's a member (child) of the group.
    The cumulative status is the one member of the group that is set to False
    for `is_group_entry`.

    Attributes:
      lint: `decorator.Lint` associated with this status.
      run_status: `Linter.RunLintStatus` return status for lint.
      name: Optional name of the status entry for reports. Default to lint name.
      group: Optional string of shared group name for multiple entries.
      is_group_entry: Boolean. If in group, True if entry is memmber/child of
        group, and Falsw if it represents the collective status of a group.
    """
    lint: decorator.Lint
    run_status: Linter.RunLintStatus
    name: str
    group: Optional[str]
    is_group_entry: bool

  def __init__(self, path: pathlib.Path, verbose: bool = False) -> None:
    self.path: pathlib.Path = path
    self.verbose: bool = verbose
    # Contains all status entries.
    self._status_list: List[self.LintStatusEntry] = []
    # Deduplicated stderr messages printed within lint functions.
    self._lint_messages: Set[str] = set()

  def add_entry(self,
                lint,
                run_status,
                name=None,
                group=None,
                is_group_entry=False):
    """Add a new `LintStatusEntry` to report.

    Args:
      lint: `decorator.Lint` associated with this status.
      run_status: `Linter.RunLintStatus`
      name: Optional name of the status entry for reports. Default to lint name.
      group: Optional string of shared group name for multiple entries.
      is_group_entry: Boolean. If in group, True if entry is memmber/child of
        group, and Falsw if it represents the collective status of a group.
    """
    if not isinstance(run_status.is_success, bool):
      raise TypeError(
          f"Lint status must return Boolean, got: {run_status.is_success}")
    name = name if name else lint.name
    entry = self.LintStatusEntry(lint, run_status, name, group, is_group_entry)
    self._status_list.append(entry)

  @property
  def is_success(self):
    """Represents the status of entire lint report.

    Returns:
      Boolean: True if all top-level status entries pass, otherwise False.
    """
    status = True
    for entry in self._status_list:
      if not entry.is_group_entry and not entry.run_status.is_success:
        status = False
        break
    return status

  def log_lint_message(self,
                       msg: str,
                       lint: decorator.Lint,
                       verbose_msg: Optional[str] = None) -> None:
    """Add message to lint message queue.

    Args:
      msg: String message captured from stderr.
      lint: `decorator.Lint` associated with this message.
      verbose_msg: String to add to next line, displayed with `--verbose` flag.
    """
    prefix = f"\033[33m[{lint.style}::{lint.name}]\033[00m"  # Yellow
    log_line = f"{prefix} {msg}"
    if self.verbose and verbose_msg:
      log_line += f"\n{verbose_msg}"
    self._lint_messages.add(log_line)

  def _format_lint_messages(self):
    """Pretty-print stderr messages logged from within lint functions.

    Returns:
      String: Contains list of stderr messages.
    """
    output_str = ""
    if self._lint_messages:
      output_str += "\nLint log:\n"
      for msg in self._lint_messages:
        output_str += (msg + "\n")
    return output_str

  def _format_status(self, entry: "LinterStatus.LintStatusEntry") -> str:
    """Pretty-print an entry status for console (with color).

    Args:
      entry: `LintStatusEntry` with status.

    Returns:
      String: 'Pass' or 'Fail' with terminal color codes.
    """
    if entry.run_status.is_success:
      msg = "\033[32mPass\033[00m"  # Green
    else:
      if entry.is_group_entry:
        msg = "\033[33mFail\033[00m"  # Yellow: group entry
      else:
        msg = "\033[91mFail\033[00m"  # Light red: root entry
    return msg

  def __str__(self):
    """Print the entire status report of all entries to console.

    Arrange and format entries for reporting to console. If
    `LinterStatus.verbose` is True, display group member entries in addition to
    the cumulative group status. Called as: `print(linter_status)`.

    Returns:
      String containing the entire lint report.
    """
    # Sort group entries to display nested underneath parent.
    groups = {}
    # Can skip if not displaying.
    if self.verbose:
      for entry in self._status_list:
        if entry.is_group_entry:
          if entry.group in groups:
            groups[entry.group].append(entry)
          else:
            groups[entry.group] = [entry]

    # Filter top-level entries.
    root_entries = [obj for obj in self._status_list if not obj.is_group_entry]
    output = ""

    for entry in root_entries:
      # Print top-level entry.
      status = self._format_status(entry)
      name = f"{entry.lint.style}::{entry.name}"
      msg = f" | {entry.lint.message}" if entry.lint.message else ""
      output += f"{status} | {name}{msg}\n"

      # Print child entries, if applicable.
      if self.verbose and entry.group in groups:
        output += "[All results]\n"
        for child in groups[entry.group]:
          output += f"- {self._format_status(child)} | {child.name}\n"

        output += "\n"

    # Print any stderror messages from within lint functions.
    output += self._format_lint_messages()

    return output

  def fix_lints(self):
    """Fix lint errors, if possible.

    This executes all the fix callbacks passed to the `fail` function in a lint
    test. Any file changes and writes must be added to the callback since this
    is only a runner.

    Fix functions are run as `fn(lint_args, *fix_args)` and executed once for
    each unique fn-args pair. Callbacks passed the same arg are deduplicated.
    But it's not the end of the world if the same function/args are run multiple
    times since the file changes should be the same.
    """

    # Custom type for: {function: [(display_name, args), ...]}
    FixFnQueue = Dict[Callable[[], None], List[Tuple[str, List[Any]]]]
    fix_fns: FixFnQueue = collections.defaultdict(list)

    for entry in self._status_list:
      if not entry.run_status.fix_fn:
        continue

      fn = entry.run_status.fix_fn
      args = [entry.run_status.lint_args] + entry.run_status.fix_args
      display_name = f"{entry.lint.style}::{entry.lint.name}::{entry.run_status.fix_fn.__name__}"
      arg_group = (display_name, args)

      if arg_group not in fix_fns[fn]:
        fix_fns[fn].append(arg_group)

    # Execute each fix function with different arg lists.
    fn_count = 0
    for fix_fn, arg_groups in fix_fns.items():
      for arg_group in arg_groups:
        display_name, args = arg_group
        if self.verbose:
          print(f" {display_name}")
        fn_count += 1
        fix_fn(*args)

    plural = "" if fn_count == 1 else "es"
    print(f"Ran {fn_count} lint fix{plural}. (For details, use --verbose)")
