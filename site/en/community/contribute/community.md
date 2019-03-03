# Contribute to the community

An open source project isn't just about the code, it's also about the community of users, developers, writers, researchers, and other contributors. You can help grow and support this community.

## Submitting a bug report or feature request

If you experience an issue while using TensorFlow, please do not hesitate to submit a support ticket to GitHub. You are also welcome to post feature requests, pull requests, and requests for Ops to be added to TF Lite.

We recommend that you be sure your issue complies with the following guidelines before submitting:

* Verify that your issue is not being addressed by [other issues](https://github.com/tensorflow/tensorflow/issues) or [pull requests](https://github.com/tensorflow/tensorflow/pulls). 
* If you are submitting an algorithm or feature request, please verify that the algorithm has been vetted via [RFC](https://github.com/tensorflow/community/tree/master/rfcs).
* If you are submitting a bug report, we strongly encourage you to follow  the guidelines in How to Make a Good Bug Report.
* If you are submitting a link to a friction log, use the [friction log template](https://docs.google.com/document/d/1_-0Zzn0hqS4ltLwqWAHm41-MgE60_9zlKyPHr5c-HCs/edit?usp=sharing).

To submit a bug or issue for TensorFlow Core, please use the following links to submit tickets, and follow the information listed:

* [Bug / Performance Issues](https://github.com/tensorflow/tensorflow/issues/new?template=00-bug-performance-issue.md)
* [Build / Installation Issues](https://github.com/tensorflow/tensorflow/issues/new?template=10-build-installation-issue.md)
* [Documentation Issue](https://github.com/tensorflow/tensorflow/issues/new?template=20-documentation-issue.md)
* [Feature Requests](https://github.com/tensorflow/tensorflow/issues/new?template=30-feature-request.md)
* [TensorFlow Lite Ops Request](https://github.com/tensorflow/tensorflow/issues/new?template=40-tflite-op-request.md)
* [Other Issues](https://github.com/tensorflow/tensorflow/issues/new?template=50-other-issues.md)


### How to make a good bug report

When you submit an issue to Github, please do your best to follow these guidelines:

* The ideal bug report contains a short, reproducible code snippet. If your snippet is longer than 50 lines, please link to a [gist](https://gist.github.com/) or a Github repo.

* If you cannot include a reproducible code snippet, please be specific about what classes, functions, or ops are involved, and mention the shape and format of your input data. Any visualizations you can add would also be appreciated.

* If an exception is raised, please provide the full traceback. Include any error messages or logs that are produced by your code.

* Please make sure to include your operating system and distribution, the version of TensorFlow that you are using, your Python version, whether TensorFlow was installed from source or binary, your CUDA/cuDNN version, your GPU model and memory, and your Bazel version (if compiling from source). This information can be found by running the [environment capture script](https://github.com/tensorflow/tensorflow/tree/master/tools/tf_env_collect.sh).

* Please ensure all code snippets and error messages are formatted in appropriate code blocks. See Op documentation style guide for more details.

* For documentation issues, please provide TensorFlow version, a URL link to the page or file, and a detailed description of the location of the error. For documentation that is generated from docstrings, provide the line that contains the error.

## Participating in code review

Reviewing code contributed to the project as PRs is a crucial component of TensorFlow development. We encourage anyone to start reviewing code of other developers, especially if the feature is something that you are likely to use.

Some questions to keep in mind during the code review process:

* Do we want this in TensorFlow? Is it likely to be used? Do you, as a TensorFlow user, like the change and intend to use it? Is this change in the scope of TensorFlow? Will the cost of maintaining a new feature be worth its benefits?
Is the code consistent with the TensorFlow API? Are public functions, classes, and parameters well-named and intuitively designed?

* Are all public functions, classes, parameters, return types, and stored attributes named according to TensorFlow conventions and clearly documented?

* Is new functionality described in TensorFlow’s documentation and illustrated with examples, whenever possible?

* Is every public function and class tested? Are a reasonable set of parameters, their values, value types, and combinations tested? Do the tests validate that the code is correct - i.e., doing what the documentation says the code is intended to do?

* If the change is a bug fix, is a non-regression test included?

* Do the tests pass in the continuous integration build?

* Do the tests cover every line of code? If not, are the lines missing coverage good exceptions?

* Is the code human-readable and low on redundancy? Should variable names be improved for clarity or consistency? Should comments be added? Should any comments be removed as unhelpful or extraneous?

* Could the code easily be rewritten to run more efficiently?

* Is the code backwards compatible with previous versions of TensorFlow?

* Will the new code add any dependencies on other libraries?

* Does the documentation render properly?

If the answer is ‘no’ to any of these questions, please consider helping the contributor understand why and resolve the issue with their tests.

### Keeping the bar high

While we encourage and celebrate every contributor, the bar for RFC acceptance should be kept intentionally high. A design may be rejected or need significant revision at any one of these stages:

* Initial design conversations on the relevant mailing list.

* Failure to recruit a sponsor.

* Critical objections during the feedback phase.

* Failure to achieve consensus during the design review.

* Concerns raised during implementation (e.g., inability to achieve backwards compatibility, concerns about maintenance appearing once a partial implementation is available).

If this process is functioning well, RFCs are expected to fail in the earlier, rather than later, stages. An approved RFC is no guarantee of a commitment to implement, and acceptance of a proposed RFC implementation is still subject to the usual code review process.


## Community support

To ask or answer technical questions about TensorFlow, please use [StackOverflow](https://stackoverflow.com/questions/tagged/tensorflow). To report bugs and issues, please use [GitHub](http://www.github.com/tensorflow/tensorflow). These are the best resources for finding common snags during installation, model training, and model deployment.

## Reporting security issues and vulnerabilities

Before using TensorFlow, please take a look at our [security model](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md#tensorflow-models-are-programs), [list of recent security advisories and announcements](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/security/index.md), and [ways that you can report security issues](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md#reporting-vulnerabilities) to the TensorFlow team at the [*Using TensorFlow Securely*](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md) page on GitHub.


## Communication

The TensorFlow community has a number of formal and informal ways of keeping in touch.

### GitHub

The primary communication about work on TensorFlow happens in the [TensorFlow repositories on GitHub](https://github.com/tensorflow). This is the place to discuss bugs, new features, and in-progress work.

### Mailing groups

Mailing groups are reserved for announcements and contrinbutor conversation. They are not intended to provide technical support. For more information about the TensorFlow mailing lists, please refer to [this page](https://www.tensorflow.org/community/lists).


### Blog

We post regularly to the [TensorFlow Blog](http://blog.tensorflow.org/), with content sourced from both TensorFlow developers and the broader community. If you would like to submit an article for review, please contact the TensorFlow Developer Relations team.

### Social media

For news and updates from around the universe of TensorFlow projects, follow [@tensorflow](https://twitter.com/tensorflow) on Twitter. To watch TensorFlow-related content, check out our [YouTube](http://youtube.com/tensorflow/) channel.

### Development roadmap

The [Roadmap](https://www.tensorflow.org/community/roadmap) summarizes plans for upcoming additions to TensorFlow.

### User groups

TensorFlow has many communities all over the world! For a complete listing, please refer to the [Community](https://www.tensorflow.org/community/groups) section on the TensorFlow website.

### Special Interest Groups (SIGs)

To enable focused collaboration on particular areas of TensorFlow, we host Special Interest Groups (SIGs). SIGs do their work in public. If you want to join and contribute, review the work of the group, and get in touch with the relevant SIG leader. Membership policies vary on a per-SIG basis.
