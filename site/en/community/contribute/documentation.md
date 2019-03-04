# Contribute to the TensorFlow documentation

TensorFlow welcomes contributions to documentation. Improving the documentation
is improving the TensorFlow library itself. Often, documentation is an easier
way to contribute to an open source project than writing code.

TensorFlow core has two broad categories of documentation:

*   **API documentation** — Reference docs, which are written along with the
    TensorFlow API code, and built from the same source.
    [You can view the API documentation here.](https://www.tensorflow.org/api_docs/)
*   **Narrative documentaton** -
    [Tutorials](https://www.tensorflow.org/tutorials),
    [guides](https://www.tensorflow.org/guide), and other "long-form" writing
    which is written apart from the code and kept
    [in the TensorFlow/docs repository](https://github.com/tensorflow/docs).

Other TensorFlow projects publish their documentation to this website, but
mostly keep their documentation source files in the same project repository as
the code (usually in a folder labeled `/docs/`). For details on contributing to
specific documentation projects other than core, see the `CONTRIBUTING.md` in
the project repo, or contact the maintainers of the project you are interested
in.

## API documentation

### Versions and branches

The [TensorFlow website](http://www.tensorflow.org) , at root, shows API
reference documentation for the latest stable binary. This is the documentation
you should be reading if you are using `pip install tensorflow`.

The default TensorFlow pip package is built from the stable branch `rX.X` in the
main TensorFlow repository. In contrast, to quickly publish fixes, the docs on
the website are built from the `docs/master` branch.

Old versions of the documentation are available in the `rX.X` branches. An "old
version" branch will only be created when the next version is released: e.g.,
when `r1.11` is released, we will create the `r1.10` branch.

In the rare case that there is a major update for a new feature that we do not
publish to the site in the meantime, the docs will be developed in a feature
branch, and then merged to `master` when ready.

### Authoring and editing

The following reference documentation is automatically generated from comments
in the code:

*   C++ API reference docs
*   Java API reference docs
*   Python API reference docs

To modify the reference documentation, you edit the appropriate code comments and doc strings. These are only updated with new releases, as they reflect the contents of the default installation.

Editing this documentation is editing code, so for complete information on the
code contribution workflow, see [Code contribution](#code-contribution).

<!--
The sections on writing about C++ and Python ops will go here, but they need more work.
-->

### Build process

#### Python

Building the Python documentation requires that you install the
`tensorflow_docs` repository as a pip package:

```bash
$ pip install git+https://github.com/tensorflow/docs
```

This installs the `tensorflow_docs` package, which includes the code for the API
reference generator.

The
[Python API documentation](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf)
is generated from the main TensorFlow repository using the
`tensorflow/tools/docs/generate2.py` script.

```bash
$ git clone https://github.com/tensorflow/tensorflow tensorflow
$ cd tensorflow/tensorflow/tools/docs
$ pip install tf-nightly-2.0-preview
$ python generate2.py --output_dir=/tmp/out
```

Note: While the script lives in the TensorFlow repository, it generates docs for
the installed TensorFlow to avoid long build times. This script only works for
TensorFlow2, and will fail if you attempt to build TensorFlow1.X docs with it.

#### C++

The C++ API documentation is generated from XML files generated via doxygen;
however, those tools are not available in open-source at this time.

## Narrative documentation

[TensorFlow guides](https://www.tensorflow.org/guide) and
[tutorials](https://www.tensorflow.org/tutorials) are written
[Markdown](https://en.wikipedia.org/wiki/Markdown) files and interactive Python
notebooks (similar to [Jupyter](https://jupyter.org/) notebooks, but we use
[Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb)
to run and publish the notebooks).

### GitHub workflow for Markdown files

Before you can work on TensorFlow documentation, you need to set up a GitHub
account.

The **first time** you start working on the docs:

1.  **Fork the docs repo**. On the
    [TensorFlow Docs repo page](https://github.com/tensorflow/docs), use the
    **Fork** button to create a copy of the repo under your own account. (If you
    work on other documentation projects, you might want to rename your copy of
    the repo to `tf-docs`.)

2.  **Clone down the repo** to your local machine.

    `$ git clone git@github.com:your-user-name/docs` *(or `/tf-docs`)*

Then, everytime you start a new bit of work:

1.  **Create a new branch to work in.**

    `$ git checkout -b new-branch-name`

2.  **Work on the docs in your favorite editor.** Be sure to follow the markdown
    syntax guide and TensorFlow style guide.

3.  **Commit your changes.**

    `$ git add -A` `$ git commit -m "meaningful commit message here"`

4.  **Push your changes to your GitHub copy of the repo.**

    `$ git push origin branch-name`

5.  **Open a pull request.** Go to the
    [TensorFlow docs repo](https://github.com/tensorflow/docs). You'll see a
    message about your recently push branch. Follow the prompts to create a new
    pull request.

6.  Maintainers and other contributors will **review your PR.**. Please
    participate in the discussion and try to make any requested changes.

7.  Once the PR is approved, your edits will be merged.

**Before working on your next contribution**, make sure your local repository is
up to date.

1.  **Set the upstream remote.** (You only have to do this once, not every
    time.)

    `$ git remote add upstream git@github.com:tensorflow/docs`

2.  **Switch to the local master branch.**

    `$ git checkout master`

3.  **Pull down the changes from upstream.**

    `$ git pull upstream master`

4.  **Push the changes to your GitHub account.**

    `$ git push origin master`

5.  **Start a new branch** if you are starting new work.

    `$ git checkout -b branch-name`

Additional git and GitHub resources:

*   [Git documentation](https://git-scm.com/documentation)
*   [Git development workflow](https://docs.scipy.org/doc/numpy/dev/gitwash/development_workflow.html)
*   [Resolving merge conflicts](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).

### GitHub workflow for Python notebooks

It is easier to work on the interactive Python notebooks online, using the
Google Colab service. Before starting, you'll need to
[install the Open in Colab Chrome extension](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo).

Once you have installed the Chrome extension, setup a GitHub account, and forked
the docs repo, you are ready to begin.

1.  Use the GitHub web UI to
    [**create a new branch](https://help.github.com/en/articles/creating-and-deleting-branches-within-your-repository)**.

2.  Navigate to the file you want to work on in.

3.  Click the icon for the Open in Colab extension.

4.  Work on the notebook in Colab.

5.  Commit your changes to your repo with File -> Save Copy to GitHub. The save
    dialog should link to the appropriate repo and branch. Add a meaningful
    commit message.

6.  When you finished working, go to the
    [TensorFlow docs repo](https://github.com/tensorflow/docs). You'll see a
    message about your recent commits. Follow the prompts to create and submit a
    new Pull Request.

7.  Maintainers and other contributors will **review your PR.**. Please
    participate in the discussion and try to make any requested changes.

### Translations

If you are interested in contributing to translations of TensorFlow
documentation, please join our
[documentation mailing list](mailto:docs@tensorflow.org).
