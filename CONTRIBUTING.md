# Contributing

You don't need to be a developer or a technical writer to make a significant
impact on the TensorFlow documentation—just a [GitHub account](https://github.com/).
This guide shows how to make contributions to [tensorflow.org](https://www.tensorflow.org).

For documentation questions or guidance, see the
[docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)
mailing list. Questions about TensorFlow usage are better addressed on
[StackOverflow](https://stackoverflow.com/questions/tagged/tensorflow) or the
[discuss@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss)
mailing list.

To contribute to the TensorFlow code repositories, see the
[Contributing to TensorFlow](https://www.tensorflow.org/community/contributing) guide
and the
[TensorFlow contribution guidelines](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md).

## Contributor License Agreements

We love patches! To publish your changes, you must sign either the individual or
corporate Contributor License Agreement (CLA):

* If you are an individual writing original documentation or source code and
  you're sure you own the intellectual property, sign an
  [individual CLA](http://code.google.com/legal/individual-cla-v1.0.html).
* If you work for a company that wants to allow you to contribute your work, sign
  a [corporate CLA](http://code.google.com/legal/corporate-cla-v1.0.html).

We can accept your pull requests after you sign the CLA. We can only receive
original documentation and source code from you and other people that have
signed the CLA.


# About our docs

The TensorFlow documentation is written in [Markdown](https://commonmark.org/help/)
and [Jupter/Colab notebooks](https://colab.research.google.com/notebooks/welcome.ipynb).

The root of [tensorflow.org/](https://www.tensorflow.org/) is found in the
`site/en` directory.

Not all technical content on tensorflow.org is located in `site/en`. Some
projects have their repositories under
[github.com/tensorflow](https://github.com/tensorflow) and they contain
project-specific documentation. These projects are navigable from the
tensorflow/docs `site/en` directory and include a redirect link to where the
docs can be updated.

The API reference is generated from the source code located in the core
[tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) repository
and other projects.

Additionally, some non-technical content, images, and design elements are not
located in the tensorflow/docs repository.

## Translations

We are *experimenting* with community-provided translations located in the
`site/{lang}` directories. To contribute, add a translated file to the language
directory and mirror the `en/` file structure. Finding reviewers for this content
is challenging and may take a while.

Note: Official Chinese translations are provided by an internal Google system and
are accessible from [tensorflow.google.cn](http://tensorflow.google.cn/?hl=zh-cn);
these files are not available in GitHub.


# Pull requests

To contribute documentation, please send us a pull request. If you are new to
pull requests, read GitHub's
[Creating a pull request from a fork](https://help.github.com/articles/creating-a-pull-request-from-a-fork/)
guide.

See [Writing TensorFlow documentation](https://www.tensorflow.org/community/documentation)
for a style guide and how to build the reference docs.

Notebooks can be viewed, edited, and run in
[Colab](https://colab.research.google.com/notebooks/welcome.ipynb) by passing
the GitHub path as a URL parameter. For example, open the notebook at
https://github.com/tensorflow/docs/blob/r1.11/site/en/tutorials/keras/basic_classification.ipynb
in Colab here:
https://colab.research.google.com/github/tensorflow/docs/blob/r1.11/site/en/tutorials/keras/basic_classification.ipynb

The [Open in Colab](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo)
Chrome extension will automatically perform the URL substitution.

A TensorFlow notebook style guide is forthcoming.
