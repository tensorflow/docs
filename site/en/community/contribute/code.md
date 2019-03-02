# Contributing to Code

## Before you get started

Before contributing source code to a TensorFlow project, please review the `CONTRIBUTING.md` file in the GitHub repo of the project. (For example, see the [CONTRIBUTING.md file for the core TensorFlow repo](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md).) Also, see the [TensorFlow Code Style Guide](#tensorflow-code-style-guide).

### Contributor License Agreement (CLA)

All code contributors are required to [sign a Contributor License Agreement](https://cla.developers.google.com/clas).


## Reporting and Fixing Bugs

If you experience a bug while using TensorFlow, please do not hesitate to open an issue in GitHub.

### How to make a good bug report {#how-to-make-a-good-bug-report}

When you submit an issue to GitHub, please do your best to follow these guidelines:

*   Make sure you are **actually reporting a bug**, not requesting a new feature. If you want to suggest a new feature, please see the section on [requesting and implementing new features](#new-features).

*   Verify that your **issue is not being addressed** by [other issues](https://github.com/tensorflow/tensorflow/issues) or [pull requests](https://github.com/tensorflow/tensorflow/pulls). 

*   The ideal bug report contains a **short, reproducible code snippet**. If your snippet is longer than 50 lines, please link to a [gist](https://gist.github.com/) or a GitHub repo.

*   If you cannot include a reproducible code snippet, please **be specific** about what **classes, functions, or ops** are involved, and mention the **shape and format** of your input data. Any visualizations you can add would also be appreciated.

*   If an exception is raised, please **provide the full traceback**. Include any error messages or logs that are produced by your code.

*   Please make sure to include your **operating system and distribution**, the **version of TensorFlow** that you are using, your **Python version**, whether TensorFlow was installed from **source or binary**, your **CUDA/cuDNN version**, your **GPU model and memory**, and your **Bazel version** (if compiling from source).

*   If you are submitting a link to a friction log, use the [friction log template](https://docs.google.com/document/d/1_-0Zzn0hqS4ltLwqWAHm41-MgE60_9zlKyPHr5c-HCs/edit?usp=sharing).

*   Please ensure all **code snippets and error messages are formatted in appropriate code blocks**. See [Op documentation style guide](#style-and-voice-quick-start) for more details.

*   For documentation issues, please provide **TensorFlow version**, a **URL link to the page or file**, and a detailed description of the location of the error. For documentation that is generated from docstrings, provide the line that contains the error.

You can use one of the following issue templates to structure your bug report:

*   [Bug / Performance Issues](https://github.com/tensorflow/tensorflow/issues/new?template=00-bug-performance-issue.md)
*   [Build / Installation Issues](https://github.com/tensorflow/tensorflow/issues/new?template=10-build-installation-issue.md)
*   [Documentation Issue](https://github.com/tensorflow/tensorflow/issues/new?template=20-documentation-issue.md)
*   [Other Issues](https://github.com/tensorflow/tensorflow/issues/new?template=50-other-issues.md)


### Contributing bug fixes

Generally, the process for fixing bugs is:

1. Fork the repo on GitHub from the TensorFlow organiztion to your personal account.
2. Clone the repo down to your development machine.
3. Create a new branch for working on the bug fix.
4. Complete the work.
5. Push the branch back to your GitHub copy of the repo.
6. Open a Pull Request against the relevant branch (usually `master`) on the main repo.
7. Once the code has been reviewed and approved, it will be merged by the maintainers.

Some of the projects use a slightly modified version of this workflow, so be sure to read the `CONTRIBUTING.md` file for the repo you are working on, and ask questions if you are unsure.


#### Before beginning

*   Do not submit PRs to fix bugs that have not been reported as issues. If you discover a bug, and know how to fix it, submit the issue first before beginning work on the fix.
*   Read the original issue and the entire conversation that follows. Ask questions to make sure you understand the bug. Discuss your planned approach to fixing it, and your testing strategy.
*   Make sure no one else is already working on fixing the bug.
*   Once you are ready to begin work, make a note of this in the issue thread and have the bug assigned to you.

#### Working on the bug

*   Bug fixes should include new unit tests that verify the fix and guard against regressions. It's a good idea to write these tests before writing the code.
*   Follow the [TensorFlow Code Style Guide](#tensorflow-code-style-guide)
*   Add or update relevant API documentation if needed.
*   Run Unit Tests.
*   Follow any other guidelines laid out in the `CONTRIBUTING.md` file in the project repo you're contributing to.

#### Getting your fix merged

Once you have completed the work, open a PR against the main repo. Be sure to reference the original issue in your PR summary.

*   Be prepared for a thorough review of your code from the maintainers and other community members.
*   Update your PR if the maintainers ask for changes.


## Requesting and Implementing New Features

We are selective about adding new features to TensorFlow, and we do not accept unsolicited PRs unrelated to existing issues or feature requests. If you are interested in writing code for TensorFlow, the best place to start is by fixing known bugs. (See [Issues for new contributors](#issues-for-new-contributors) if you're looking for ideas of what to work on.)

### Feature requests

If you have a feature request, you can [submit your feature request as a GitHub issue](https://github.com/tensorflow/tensorflow/issues/new?template=30-feature-request.md).

You can also submit [TensorFlow Lite Ops Requests](https://github.com/tensorflow/tensorflow/issues/new?template=40-tflite-op-request.md) as GitHub issues.

To help move a feature request from an idea to an implemented feature, you can get involved with the Request for Comment (RFC) process.



## Code Review

New features, bug fixes, and any other changes to the code base are subject to code review.

Reviewing code contributed to the project as PRs is a crucial component of TensorFlow development. We encourage anyone to start reviewing code submitted by other developers, especially if the feature is something that you are likely to use.

Here are some questions to keep in mind during the code review process:

*   **Do we want this in TensorFlow?** Is it likely to be used? Do you, as a TensorFlow user, like the change and intend to use it? Is this change in the scope of TensorFlow? Will the cost of maintaining a new feature be worth its benefits?
*   **Is the code consistent with the TensorFlow API?** Are public functions, classes, and parameters well-named and intuitively designed?
*   **Does it include documentation?** Are all public functions, classes, parameters, return types, and stored attributes named according to TensorFlow conventions and clearly documented? Is new functionality described in TensorFlow's documentation and illustrated with examples, whenever possible? Does the documentation render properly?

*   **Is the code human-readable?** Is it low on redundancy? Should variable names be improved for clarity or consistency? Should comments be added? Should any comments be removed as unhelpful or extraneous?
*   **Is the code efficient?** Could it be rewritten easily to run more efficiently?
*   Is the code **backwards compatible** with previous versions of TensorFlow?
*   Will the new code add **new dependencies** on other libraries?

Of particular concerns in **adequate testing.**   

*   Is **every public function and class** tested? 
*   Are a **reasonable set of parameters**, their values, value types, and combinations tested? 
*   Do the tests validate that the **code is correct**, and that it is **doing what the documentation says** the code is intended to do?
*   If the change is a bug fix, is a **non-regression test** included?
*   Do the tests **pass the continuous integration** build?
*   Do the tests **cover every line of code?** If not, are the exceptions reasonable and explicit?


If you find any problems, please consider helping the contributor understand those problems and resolve them. 


## Testing

Thorough testing is a important to the health and longevity of TensorFlow, and you can help.

For the specific details of testing procedures in each TensorFlow project, see the `README.md` and `CONTRIBUTING.md` files in the project repo on GitHub.

### Improving Test Coverage

All new features and bug fixes must include adequate test coverage. We also welcome contributions of new test cases or improvements to existing tests. If you discover that our existing tests are not complete — even if that is not currently causing a bug — please file an issue and, if possible, a pull request.

### User Testing

The best way to uncover software bugs is for a lot of people to use the software. Each time you use TensorFlow, be on the lookout for odd or unexpected behavior. If you discover a bug, please report it.

If you are able, we encourage you to try out nightly builds, alphas, and release candidates. These give you access to recent bug fixes and upcoming feature, and the project benefits because bugs and rough edges are discovered early.

To access nightly builds:

*   `pip install tf-nightly`
*   `pip install tf-nightly-gpu`

For alphas, release candidates, and other version releases, see:

*   [TensorFlow Installation Guide](https://www.tensorflow.org/install)
*   [TensorFlow Docker Guide](https://www.tensorflow.org/install/docker)



## Contribution workflow

Code contributions — bug fixes, new development, test improvement — all follow a GitHub-centered workflow. To participate in TensorFlow development, set up a GitHub account if you don't have one already. Then:

1.  **Fork the repo you plan to work on.** Go to the project repo page and use the **Fork** button. This will create a copy of the repo, under your username. (For more details on how to fork a repository see [this guide](https://help.github.com/articles/fork-a-repo/).)

2.  **Clone down the repo to your local system.** 

    `$ git clone git@github.com:your-user-name/project-name.git`

3.  **Create a new branch to hold your work.**

    `$ git checkout -b new-branch-name`

4.  **Work on your new code.** Write and run tests.

5.  **Commit your changes.**

    `$ git add -a`
    `$ git commit -m "commit message here"`

6.  **Push your changes to your GitHub repo.**

    `$ git push origin branch-name`

7.  **Open a Pull Request.** Go to the original project repo on GitHub. There will be a message about your recently pushed branch, asking if you would like to open a pull request. Follow the prompts, *compare accross repositories**, and submit the PR. This will send an email to the committers. You may want to consider sending an email to the mailing list for more visibility.

    (For more detals, see [this GitHub guide on PRs](https://help.github.com/articles/creating-a-pull-request-from-a-fork)). 

8.  Maintainers and other contributors will **review your PR**. Please participate in the conversation, and try to **make any requested changes**. Once the PR is approved, the code will be merged.

**Before working on your next contribution**, make sure your local repository is up to date.

1. **Set the upstream remote.** (You only have to do this once per project, not every time.)

    `$ git remote add upstream git@github.com:tensorflow/project-repo-name`

2. **Switch to the local master branch.**

    `$ git checkout master`

3. **Pull down the changes from upstream.**

    `$ git pull upstream master`

4. **Push the changes to your GitHub account.** (Optional, but a good practice.)

    `$ git push origin master`

5. **Start a new branch** if you are starting new work.

    `$ git checkout -b branch-name`

Additional git and GitHub resources:

*   [Git documentation](https://git-scm.com/documentation)
*   [Git development workflow](https://docs.scipy.org/doc/numpy/dev/gitwash/development_workflow.html)
*   [Resolving merge conflicts](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/).




## Contributor checklist

*   Read contributing guidelines.
*   Read the Code of Conduct.
*   Ensure you have signed the Contributor License Agreement (CLA).
*   Check if your changes are consistent with the guidelines.
*   Check if your changes are consistent with the TensorFlow coding style.
*   Run unit tests.

