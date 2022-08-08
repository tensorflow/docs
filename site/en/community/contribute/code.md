# Contribute to the TensorFlow code

Whether you are adding a loss function, improving test coverage, or writing an
RFC for a major design change, this portion of the contributor guide will help
you get started. Thank you for work and interest in improving TensorFlow.

## Before you get started

Before you contribute source code to a TensorFlow project, please review the
`CONTRIBUTING.md` file in the GitHub repo of the project. For example, see the
[CONTRIBUTING.md](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)
file in the core TensorFlow repo. All code contributors are required to sign a
[Contributor License Agreement](https://cla.developers.google.com/clas) (CLA).

To avoid duplicating work, please review
[current](https://github.com/tensorflow/community/tree/master/rfcs) or
[proposed](https://github.com/tensorflow/community/labels/RFC%3A%20Proposed)
RFCs and contact the developers on the TensorFlow forums
([developers@tensorflow.org](https://groups.google.com/u/1/a/tensorflow.org/g/developers))
before you start work on a non-trivial feature. We are somewhat selective when
deciding to add new functionality, and the best way to contribute and help the
project is to work on known issues.

## Issues for new contributors

New contributors should look for the following tags when searching for a first
contribution to the TensorFlow code base. We strongly recommend that new
contributors tackle “good first issue” and "contributions welcome" projects
first; this helps the contributor become familiar with the contribution
workflow, and for the core devs to become acquainted with the contributor.

-   [good first issue](https://github.com/tensorflow/tensorflow/labels/good%20first%20issue)
-   [contributions welcome](https://github.com/tensorflow/tensorflow/labels/stat%3Acontributions%20welcome)

If you are interested in recruiting a team to help tackle a large-scale problem
or a new feature, please email the
[developers@ group](https://groups.google.com/a/tensorflow.org/forum/#!forum/developers)
and review our current list of RFCs.

## Code review

New features, bug fixes, and any other changes to the code base are subject to
code review.

Reviewing code contributed to the project as pull requests is a crucial
component of TensorFlow development. We encourage anyone to start reviewing code
submitted by other developers, especially if the feature is something that you
are likely to use.

Here are some questions to keep in mind during the code review process:

*   *Do we want this in TensorFlow?* Is it likely to be used? Do you, as a TensorFlow user, like the change and intend to use it? Is this change in the scope of TensorFlow? Will the cost of maintaining a new feature be worth its benefits?
*   *Is the code consistent with the TensorFlow API?* Are public functions, classes, and parameters well-named and intuitively designed?
*   *Does it include documentation?* Are all public functions, classes, parameters, return types, and stored attributes named according to TensorFlow conventions and clearly documented? Is new functionality described in TensorFlow's documentation and illustrated with examples, whenever possible? Does the documentation render properly?

*   *Is the code human-readable?* Is it low on redundancy? Should variable names be improved for clarity or consistency? Should comments be added? Should any comments be removed as unhelpful or extraneous?
*   *Is the code efficient?* Could it be rewritten easily to run more efficiently?
*   Is the code *backwards compatible* with previous versions of TensorFlow?
*   Will the new code add *new dependencies* on other libraries?

## Test and improve test coverage

High-quality unit testing is a corner-stone of the TensorFlow development
process. For this purpose, we use Docker images. The test functions are
appropriately named, and are responsible for checking the validity of algorithms
as well as different options of the code.

All new features and bug fixes *must* include adequate test coverage. We also
welcome contributions of new test cases or improvements to existing tests. If
you discover that our existing tests are not complete — even if that is not
currently causing a bug — please file an issue and, if possible, a pull request.

For the specific details of testing procedures in each TensorFlow project, see
the `README.md` and `CONTRIBUTING.md` files in the project repo on GitHub.

Of particular concerns in *adequate testing*:

*   Is *every public function and class* tested?
*   Are a *reasonable set of parameters*, their values, value types, and
    combinations tested?
*   Do the tests validate that the *code is correct*, and that it is *doing what
    the documentation says* the code is intended to do?
*   If the change is a bug fix, is a *non-regression test* included?
*   Do the tests *pass the continuous integration* build?
*   Do the tests *cover every line of code?* If not, are the exceptions
    reasonable and explicit?

If you find any problems, please consider helping the contributor understand
those problems and resolve them.

## Improve error messages or logs

We welcome contributions that improve error messages and logging.

## Contribution workflow

Code contributions—bug fixes, new development, test improvement—all follow a
GitHub-centered workflow. To participate in TensorFlow development, set up a
GitHub account. Then:

1.  Fork the repo you plan to work on. Go to the project repo page and use the
    *Fork* button. This will create a copy of the repo, under your username.
    (For more details on how to fork a repository see
    [this guide](https://help.github.com/articles/fork-a-repo/).)

2.  Clone down the repo to your local system.

    `$ git clone git@github.com:your-user-name/project-name.git`

3.  Create a new branch to hold your work.

    `$ git checkout -b new-branch-name`

4.  Work on your new code. Write and run tests.

5.  Commit your changes.

    `$ git add -A`

    `$ git commit -m "commit message here"`

6.  Push your changes to your GitHub repo.

    `$ git push origin branch-name`

7.  Open a *Pull Request* (PR). Go to the original project repo on GitHub. There
    will be a message about your recently pushed branch, asking if you would
    like to open a pull request. Follow the prompts, *compare across
    repositories*, and submit the PR. This will send an email to the committers.
    You may want to consider sending an email to the mailing list for more
    visibility. (For more details, see the
    [GitHub guide on PRs](https://help.github.com/articles/creating-a-pull-request-from-a-fork).

8.  Maintainers and other contributors will *review your PR*. Please participate
    in the conversation, and try to *make any requested changes*. Once the PR is
    approved, the code will be merged.

*Before working on your next contribution*, make sure your local repository is
up to date.

1.  Set the upstream remote. (You only have to do this once per project, not
    every time.)

    `$ git remote add upstream git@github.com:tensorflow/project-repo-name`

2.  Switch to the local master branch.

    `$ git checkout master`

3.  Pull down the changes from upstream.

    `$ git pull upstream master`

4.  Push the changes to your GitHub account. (Optional, but a good practice.)

    `$ git push origin master`

5.  Create a new branch if you are starting new work.

    `$ git checkout -b branch-name`

Additional `git` and GitHub resources:

*   [Git documentation](https://git-scm.com/documentation)
*   [Git development workflow](https://docs.scipy.org/doc/numpy/dev/development_workflow.html)
*   [Resolving merge conflicts](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).


## Contributor checklist

*   Read the [contributing guidelines](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md).
*   Read the [Code of Conduct](https://github.com/tensorflow/tensorflow/blob/master/CODE_OF_CONDUCT.md).
*   Ensure you have signed the [Contributor License Agreement (CLA)](https://cla.developers.google.com/).
*   Check if your changes are consistent with the [guidelines](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md#general-guidelines-and-philosophy-for-contribution).
*   Check if your changes are consistent with the [TensorFlow coding style](https://www.tensorflow.org/community/contribute/code_style).
*   [Run the unit tests](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md#running-unit-tests).
