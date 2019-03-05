# Contribute to the TensorFlow community

An open source project isn't just about the code, it's also about the community of users, developers, writers, researchers, and other contributors. You can help grow and support this community.

## Submit a bug report or feature request

If you experience an issue while using TensorFlow, please do not hesitate to submit a support ticket to GitHub. You are also welcome to post feature requests, pull requests, and requests for operations to be added to TensorFlow Lite.

Before you submit an issue, check the following guidelines:

* Verify the issue is not addressed by [other issues](https://github.com/tensorflow/tensorflow/issues) or [pull requests](https://github.com/tensorflow/tensorflow/pulls). 
* If you submit an algorithm or feature request, verify the algorithm has been vetted by an [RFC](https://github.com/tensorflow/community/tree/master/rfcs).
* If you submit a bug report, we strongly encourage you to follow the guidelines listed below in *How to make a good bug report*.
* If you submit a link to a friction log, use the [friction log template](https://docs.google.com/document/d/1_-0Zzn0hqS4ltLwqWAHm41-MgE60_9zlKyPHr5c-HCs/edit?usp=sharing).

To submit a bug or issue for TensorFlow core, use the following links to submit tickets:

* [Bug / performance](https://github.com/tensorflow/tensorflow/issues/new?template=00-bug-performance-issue.md)
* [Build or install](https://github.com/tensorflow/tensorflow/issues/new?template=10-build-installation-issue.md)
* [Documentation](https://github.com/tensorflow/tensorflow/issues/new?template=20-documentation-issue.md)
* [Feature requests](https://github.com/tensorflow/tensorflow/issues/new?template=30-feature-request.md)
* [TensorFlow Lite ops request](https://github.com/tensorflow/tensorflow/issues/new?template=40-tflite-op-request.md)
* [Other issues](https://github.com/tensorflow/tensorflow/issues/new?template=50-other-issues.md)


### How to make a good bug report

When you submit an issue to Github, do your best to follow these guidelines:

* The ideal bug report contains a short, reproducible code snippet. If your snippet is longer than 50 lines, please link to a [gist](https://gist.github.com/) or a Github repo.
* If you cannot include a reproducible code snippet, be specific about what classes, functions, or ops are involved. Mention the shape and format of your input data, and any visualizations you can add are also appreciated.
* If an exception is raised, provide the full traceback. Include any error messages or logs that are produced by your code.
* Please make sure to include your operating system and distribution, your version of TensorFlow, Python version, whether TensorFlow was installed from source or binary, CUDA/cuDNN version, GPU model and memory, and Bazel version (if compiling from source). This information can be found by running the [environment capture script](https://github.com/tensorflow/tensorflow/tree/master/tools/tf_env_collect.sh).
* Ensure all code snippets and error messages are formatted in appropriate code blocks.
* For documentation issues, please provide TensorFlow version, a URL link to the page or file, and a detailed description of the location of the error. For documentation that is generated from docstrings, provide the line that contains the error.

## Participate in the code review

Reviewing code contributed to the project as pull requests is a crucial component of TensorFlow development. We encourage anyone to start reviewing code of other developers, especially if the feature is something that you are likely to use.

Some questions to keep in mind during the code review process:

* Do we want this in TensorFlow? Is it likely to be used? Do you, as a TensorFlow user, like the change and intend to use it? Is this change in the scope of TensorFlow? Will the cost of maintaining a new feature be worth its benefits?
Is the code consistent with the TensorFlow API? Are public functions, classes, and parameters well-named and intuitively designed?
* Are all public functions, classes, parameters, return types, and stored attributes named according to TensorFlow conventions and clearly documented?
* Is new functionality described in TensorFlow’s documentation and illustrated with examples, whenever possible?
* Is every public function and class tested? Are a reasonable set of parameters, their values, value types, and combinations tested? Do the tests validate that the code is correct—is it doing what the documentation says the code is intended to do?
* If the change is a bug fix, is a non-regression test included?
* Do the tests pass in the continuous integration build?
* Do the tests cover every line of code? If not, are the lines missing coverage good exceptions?
* Is the code human-readable and low on redundancy? Should variable names be improved for clarity or consistency? Should comments be added? Should any comments be removed as unhelpful or extraneous?
* Could the code easily be rewritten to run more efficiently?
* Is the code backwards compatible with previous versions of TensorFlow?
* Will the new code add any dependencies on other libraries?
* Does the documentation render properly?

If the answer is ‘no’ to any of these questions, please consider helping the contributor understand why and resolve the issue with their tests.

### Keep the bar high

While we encourage and celebrate every contributor, the bar for RFC acceptance should be kept intentionally high. A design may be rejected or need significant revision at any one of these stages:

* Initial design conversations on the relevant mailing list.
* Failure to recruit a sponsor.
* Critical objections during the feedback phase.
* Failure to achieve consensus during the design review.
* Concerns raised during implementation (for example, the inability to achieve backwards compatibility, concerns about maintenance appearing once a partial implementation is available).

If this process is functioning well, RFCs are expected to fail in the earlier stages—rather than later stages. An approved RFC is no guarantee of a commitment to implement, and acceptance of a proposed RFC implementation is still subject to the usual code review process.

## Community support

To ask or answer technical questions about TensorFlow, please use [StackOverflow](https://stackoverflow.com/questions/tagged/tensorflow). To report bugs and issues, please use [GitHub](http://www.github.com/tensorflow/tensorflow). These are the best resources for finding common problems during installation, model training, and model deployment.

## Reporting security issues and vulnerabilities

Before using TensorFlow, please take a look at our [security model](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md#tensorflow-models-are-programs), [list of recent security advisories and announcements](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/security/index.md), and [ways that you can report security issues](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md#reporting-vulnerabilities) to the TensorFlow team at the [*Using TensorFlow Securely*](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md) page on GitHub.

## Communication

The TensorFlow community has a number of formal and informal ways to keep in touch.

### GitHub

The primary communication about work on TensorFlow happens in the [TensorFlow repositories on GitHub](https://github.com/tensorflow). This is the place to discuss bugs, new features, and in-progress work.

### Forums

TensorFlow [forums and mailing groups](../forums.md) are reserved for announcements and contrinbutor conversation. They are not intended to provide technical support.

### Blog

We post regularly to the [TensorFlow Blog](http://blog.tensorflow.org/), with content sourced from both TensorFlow developers and the broader community.

### Social media

For news and updates from around the universe of TensorFlow projects, follow [@tensorflow](https://twitter.com/tensorflow) on Twitter. To watch TensorFlow-related content, view our [YouTube channel](http://youtube.com/tensorflow/).

### Development roadmap

The [TensorFlow roadmap](../roadmap.md) shows upcoming TensorFlow plans and features.

### Forums and user groups

TensorFlow has many communities all over the world! For a complete list, see the [TensorFlow user groups](../groups.md).

### Special Interest Groups (SIGs)

To enable focused collaboration on particular areas of TensorFlow, we host Special Interest Groups (SIGs). [TensorFlow SIGs](../sig_playbook.md) do their work in public. If you want to join and contribute, review the work of the group, and get in touch with the relevant SIG leader. Membership policies vary on a per-SIG basis.
