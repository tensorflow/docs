# TensorFlow Docs notebook tools

The `tensorflow-docs` package contains a collection of notebook tools designed
for open source documentation workflows.

[Jupyter notebooks](https://nbformat.readthedocs.io/en/latest/) are the
preferred documentation format for TensorFlow
[guides](https://www.tensorflow.org/guide) and
[tutorials](https://www.tensorflow.org/tutorials). These docs integrate with
[Google Colab](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb)
for reproducible environments, regularly tested code examples, and more
maintainable documentation.


## Install

Use `pip` to install the latest `tensorflow-docs` package directly from the
[tensorflow/docs](https://github.com/tensorflow/docs) GitHub repository:

```
$ python3 -m pip install -U --user git+https://github.com/tensorflow/docs
```


## nbfmt

A notebook formatting tool that makes Jupyter notebook source diffs consistent
and easier to review. Since notebook authoring environments differ with regards
to file output, indentation, metadata and other non-specified fields; `nbfmt`
uses opinionated defaults with a preference for the TensorFlow docs Colab
workflow. To format a notebook, install the `tensorflow-docs` package and run
the `nbfmt` tool:

```
$ python3 -m tensorflow_docs.tools.nbfmt [options] notebook.ipynb [...]

$ python3 -m tensorflow_docs.tools.nbfmt --help
```

`nbfmt` accepts directory arguments that format all child notebooks (skipping
non-notebook files).

For TensorFlow docs projects, notebooks *without* output cells are executed and
tested; notebooks *with* saved output cells are published as-is. `nbfmt`
respects the notebook state and uses the `--remove_outputs` option to explicitly
remove output cells.

The `--test` flag is for continuous integration tests. This does not format the
notebook, rather it exits with an error code if the notebook is not in an
up-to-date formatted state. See the tensorflow/docs
[GitHub Actions workflow](https://github.com/tensorflow/docs/blob/master/.github/workflows/ci.yaml)
for an example.

### Pre-commit

You can set up the `nbfmt` tool as a pre-commit check in other repos. To do
this, use a standard Git hook or use the
[https://pre-commit.com/](https://pre-commit.com/) framework to create the hook
for you.

If you want to use pre-commit to handle the hook installation for you, include
the [.pre-commit-hooks.yaml](./.pre-commit-hooks.yaml) file in your repo with
the following contents:

```
repos:
- repo: https://github.com/tensorflow/docs
  rev: pre-commit
```

Someone who clones that repo for development would then install the hook with:

```
# Install pre-commit framework
pip3 install pre-commit

# Install hooks
pre-commit install
```

## nblint

A notebook linting tool that checks documentation style rules. Used to catch
common errors and useful for CI tests. To lint a notebook, install the
`tensorflow-docs` package and run the `nblint` tool:

```
$ python3 -m tensorflow_docs.tools.nblint [options] notebook.ipynb [...]

$ python3 -m tensorflow_docs.tools.nblint --fix [options] notebook.ipynb [...]

$ python3 -m tensorflow_docs.tools.nblint --help
```

Some styles require a user-defined argument passed at the command-line. For
example, the `tensorflow` style (default) uses the `repo` argument to check links:

```
$ python3 -m tensorflow_docs.tools.nblint --arg=repo:tensorflow/docs notebook.ipynb
```

Lints are assertions that test specific sections of the notebook. These lints
are collected into
[style modules](https://github.com/tensorflow/docs/tree/master/tools/tensorflow_docs/tools/nblint/style).
`nblint` tests the `google` and `tensorflow` styles by default, and different
styles can be set with the `--styles` option:

```
$ python3 -m tensorflow_docs.tools.nblint \
    --styles=tensorflow,tensorflow_docs_l10n --arg=repo:tensorflow/docs-1l0n \
    notebook.ipynb
```

A style module may contain some lint checks that do not fit your project. You
can exclude specific lint checks with the `--exclude_lint` option:

```
$ python3 -m tensorflow_docs.tools.nblint \
    --styles=tensorflow --arg=repo:community/repo-name \
    --exclude_lint=tensorflow::copyright_check \
    --exclude_lint=tensorflow::button_website \
    ./community/notebook.ipynb
```

Some lint errors can be automatically fixed in the notebook file:

```
$ python3 -m tensorflow_docs.tools.nblint --fix \
    --arg=repo:tensorflow/docs notebook.ipynb
```

This applies the lint fixes to the notebook and overwrites the file. Not all
lint errors have an associated fix. Fixes are applied from the loaded style
modules.
