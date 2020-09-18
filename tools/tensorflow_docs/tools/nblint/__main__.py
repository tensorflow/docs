# Lint as: python3
# pylint: disable=invalid-name
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
r"""Check notebook conformance with documentation styles.

Install the tensorflow-docs package:
$ python3 -m pip install -U [--user] git+https://github.com/tensorflow/docs

Usage:
$ python3 -m tensorflow_docs.tools.nblint [options] notebook.ipynb [...]
$ python3 -m tensorflow_docs.tools.nblint --fix [options] notebook.ipynb [...]

$ python3 -m tensorflow_docs.tools.nblint --verbose \
    [--styles=google,tensorflow] notebook.ipynb [...]
$ python3 -m tensorflow_docs.tools.nblint --arg=x:foo --arg=y:bar notebook.ipynb
$ python3 -m tensorflow_docs.tools.nblint [options] \
    --exclude_lint=tensorflow::copyright_check [...] notebook.ipynb

See the TensorFlow notebook template:
https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb
And the TensorFlow docs contributor guide:
https://www.tensorflow.org/community/contribute/docs
"""

import importlib
import inspect
import sys
import textwrap

from absl import app
from absl import flags

from tensorflow_docs.tools.nbfmt import notebook_utils
from tensorflow_docs.tools.nblint import decorator
from tensorflow_docs.tools.nblint import linter


flags.DEFINE_multi_string("arg", [], "User arguments to pass to lint callback.")
flags.DEFINE_multi_string(
    "exclude_lint", [],
    "Do not check a specific lint within a style. Format: 'style::function'")
flags.DEFINE_boolean("fix", False, "Fix lint errors, if possible.")
flags.DEFINE_list("styles", ["google", "tensorflow"],
                  "Lint style modules to include.")
flags.DEFINE_boolean("verbose", False, "Display verbose output.")

FLAGS = flags.FLAGS


def _print_fails(path_list):
  """Format notebooks that failed lint and print to console.

  Args:
    path_list: A list of Path objects.
  """
  template = textwrap.dedent("""\
    The following notebook{plural} failed lint:
    {filepaths}""")
  paths = "\n".join([f" {str(fp)}" for fp in path_list])
  plural = "s" if len(paths) > 1 else ""
  print(template.format(filepaths=paths, plural=plural), file=sys.stderr)


def _is_user_defined_lint(mod_name):
  """Return a function that tests if a module member is a user-defined lint.

  Args:
    mod_name: THe string name of the module file containing the lint.

  Returns:
    Function: This returns a Boolean: True if the module member is a lint.
  """

  def is_lint(member):
    return (inspect.isfunction(member) and member.__module__ == mod_name and
            hasattr(member, "_lint"))

  return is_lint


def add_styles(styles, excluded_lints, verbose):
  """Import lint assertions from style modules.

  Style modules must exist in the `style/` directory of this package.

  Args:
    styles: A list of short names for style modules to import.
    excluded_lints: List of lint functions to skip ('style::function').
    verbose: Bool, to print more details to console. Default is False.

  Returns:
    A dictionary containing all the lint styles.
  """

  lint_dict = {
      decorator.Options.Scope.CODE: {
          decorator.Options.Cond.ALL: [],
          decorator.Options.Cond.ANY: []
      },
      decorator.Options.Scope.TEXT: {
          decorator.Options.Cond.ALL: [],
          decorator.Options.Cond.ANY: []
      },
      decorator.Options.Scope.CELLS: {
          decorator.Options.Cond.ALL: [],
          decorator.Options.Cond.ANY: []
      },
      decorator.Options.Scope.FILE: {
          decorator.Options.Cond.ANY: []  # Only one queue is relevant.
      }
  }

  for style in styles:
    mod_name = f"tensorflow_docs.tools.nblint.style.{style}"
    mod = importlib.import_module(mod_name)
    is_lint = _is_user_defined_lint(mod_name)

    # Extract Lint instance attached to function object by decorator.
    lints = [
        getattr(mem[1], "_lint") for mem in inspect.getmembers(mod, is_lint)
    ]

    # Remove lints that have been explictly excluded at the command-line.
    lints = [
        lint for lint in lints if f"{style}::{lint.name}" not in excluded_lints
    ]

    if verbose:
      lint_names = ", ".join([lint.name for lint in lints])
      print(f"From style '{mod_name}' import lints: {lint_names}\n")

    for lint in lints:
      lint.style = style
      lint_dict[lint.scope][lint.cond].append(lint)

  return lint_dict


def _parse_user_args(args_list):
  """Parse user-defined arguments passed at command-line.

  Args:
    args_list: List of strings in "key:value" format.

  Returns:
    A dictionary containing user-defined keys and values.
  """
  args_dict = {}
  for arg_str in args_list:
    parts = arg_str.split(":", 1)
    key = parts[0]
    # Command-line args are strings. If no value provided, use "True".
    val = parts[1] if len(parts) == 2 else "True"
    # Add basic string parsing into Python types.
    if val.isdigit():
      # Non-exhaustive numeric parsing, for convenience.
      val = int(val)
    elif val.lower() == "true":
      val = True
    elif val.lower() == "false":
      val = False
    args_dict[key] = val
  return args_dict


# Linter is run in both lint and fix modes. When linting, the lint status list
# is displayed and the program exits with an error on any lint failure.
# When fixing, no status is displayed and it runs through the queue of fix
# callbacks, exiting without error reguardless if everything is fixed.
def main(argv):
  if len(argv) <= 1:
    raise app.UsageError("Missing arguments.", 1)
  if not FLAGS.styles:
    raise app.UsageError("Missing styles.", 1)

  user_args = _parse_user_args(FLAGS.arg)

  nb_linter = linter.Linter(verbose=FLAGS.verbose)
  lint_dict = add_styles(FLAGS.styles, FLAGS.exclude_lint, FLAGS.verbose)

  linter_fails = []  # Track failed notebooks for final return code.

  paths, _ = notebook_utils.collect_notebook_paths(argv[1:])

  for path in paths:
    mode = "Fix" if FLAGS.fix else "Lint"
    print(f"{mode} notebook: {path}")

    status = nb_linter.run(path, lint_dict, user_args)
    if not status.is_success:
      linter_fails.append(path)

    if FLAGS.fix:
      status.fix_lints()
    else:
      print(status)

  # Fix mode always exits as success.
  if FLAGS.fix:
    sys.exit(0)

  if linter_fails:
    _print_fails(linter_fails)
    sys.exit(1)
  else:
    sys.exit(0)


if __name__ == "__main__":
  app.run(main)
