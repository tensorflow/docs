'# TensorFlow 2.0: An Overview

Last Updated: _Mar 6, 2019_

A key element of the evolution of TensorFlow (TF) is TF 2.0, which is primarily focused on:

* Cleaning up and standardizing the high-level API surface;
* Making TensorFlow more intuitive and easier to debug; and
* Continuing to enable scalable production deployment.

**TF 2.0 is just in the beginning of this transition.**

You can experiment with the alpha release today - please let us know what you create, and your overall experience with it. Over the course of the next few months, we will be focused on making TF 2.0:

 * RC/Production ready
 * Making it 100% compatible with the rest of TF ecosystem
 * Incorporating major feedback from the community

and sharing this process as openly as we can.

## Frequently Asked Questions (FAQ)

1. [Compatibility](#compatibility)
2. [Functionality](#functionality)
3. [Migration Support](#migration)
4. [General](#general)
5. [Technical](#technical)
6. [Multi-Level Intermediate Representation (MLIR)](#mlir)

<a name="compatibility"></a>
### Compatibility

**Can I still use Keras in TensorFlow 2.0?**

Yes. In fact, Keras (as [`tf.keras`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras)) is the preferred higher-level API for TF 2.0. We recommend using tf.keras layers and model.fit() whenever possible and subclassing when you need more specialized control. For more information, please visit this recent [blogpost](https://medium.com/tensorflow/standardizing-on-keras-guidance-on-high-level-apis-in-tensorflow-2-0-bad2b04c819a) on higher-level APIs in TensorFlow 2.0.

**Will TF 1.x scripts continue to work with TF 2.0? How can I upgrade?**

No, TF 1.x scripts **will not** continue to work with TF 2.0. If your models have been written in Keras, the upgrade process should be very straightforward. An upgrade utility called `tf_upgrade_v2` is included with every install of TensorFlow 2.0. This tool will allow you to upgrade individual Python files, Jupyter notebooks, and directories of Python files and Jupyter notebooks. For more on the upgrade script, visit this [blogpost](https://medium.com/tensorflow/upgrading-your-code-to-tensorflow-2-0-f72c3a4d83b5).

**If I use `tf.compat.v1`, will my script still be TF 2.0 compliant?**

Yes, you will still be compliant. You will not be using TF 2.0 style, and you will not be able to use all of its features - but you will be in a safe state, and your code will continue to work through the lifetime of 2.x. For more on upgrading your code to TF 2.0, check [here](https://www.tensorflow.org/alpha/guide/migration_guide).

**Can I still use Estimators in TensorFlow 2.0?**

Yes. Estimators will still be available and supported in TF 2.0. Links to the API docs for tf.estimator can be found [here](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/estimator).

**Can I use TensorBoard with TF 2.0? With Keras in TF 2.0?**

Yes. We even have TensorBoard support in Colab and in Jupyter notebooks. Check it out [here](https://www.tensorflow.org/guide/summaries_and_tensorboard).

**Is there a 1:1 relationship between stand-alone Keras and tf.keras?**

No, there is not. Many of the endpoints in tf.keras are not included in stand-alone Keras, and tf.keras does not support Theano or CNTK as a back-end. If you are interested in the details, please check http://keras.io and the TF 2.0 tf.keras API documentation [here](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras).

**When will TensorFlow stop supporting Python 2.x?**

TensorFlow has signed the Python 3 Statement, and will no longer be supporting Python 2.x as of January 1, 2020.

**What versions of Python does TensorFlow support?**

TensorFlow (dependent on version) currently supports Python 2.7, 3.5, 3.6, and 3.7. Support for Python 3.5 and 3.7 will be added for TensorFlow 2.0. You can track [this issue](https://github.com/tensorflow/tensorflow/issues/25429) to keep updated.

**Is TensorFlow 2.0 compatible with TensorFlow Lite?**

TensorFlow 2.0 is compatible with TensorFlow Lite. We will continue to test and expand support as needed. For more information, track [this issue](https://github.com/tensorflow/tensorflow/issues/25361).

**Is TensorFlow 2.0 compatible with TensorFlow.js?**

TensorFlow 2.0 supports TensorFlow.js v1.0, and most models saved in TF 2.0 will work through the converter process for deployment using TensorFlow.js. Between now and the official release, this support will be expanded. For more information, track [this issue](https://github.com/tensorflow/tensorflow/issues/25360).

**Is TensorFlow 2.0 compatible with TensorFlow Extended (TFX)?**

Partially. TFX supports distributed training with estimators today, and will support distributed training with Keras shortly. For more information, track [this issue](https://github.com/tensorflow/tensorflow/issues/25369).

**Is TensorFlow 2.0 compatible with TensorFlow Hub?**

The SavedModel format has been improved to handle TF-Hub use cases. There is a starter list of Hub modules using this format and usable in TF-2.0. This will be expanded by the RC with support for 1.x TF-Hub module conversion. For more information, track [this issue](https://github.com/tensorflow/tensorflow/issues/25362).

**Is TF 2.0 compatible with many of the existing TensorFlow projects?.**

We are working with many TensorFlow related project to make them ready for 2.0. The development work on TensorFlow 2.0 is completely transparent. You can track the engineering team’s status on our GitHub project [status tracker](https://github.com/orgs/tensorflow/projects/4).

**Does TensorFlow 2.0 have support for TPU?**

 TPUs are supported in the alpha release via the TPUStrategy and tf.estimator API. Full support with tf.keras is limited at the moment. You can track [this issue](https://github.com/tensorflow/tensorflow/issues/24412) on GitHub to keep updated.

**Does TensorFlow 2.0 support Windows?**

 We list the status of continuous builds in the README for tensorflow/tensorflow. You can go and take a look at it [here](https://github.com/tensorflow/tensorflow#continuous-build-status).

<a name="functionality"></a>
### Functionality

**What is eager execution? Why is it useful?**

Eager execution is a flexible machine learning platform for machine learning experimentation, and provides easier debugging, a natural control flow, and a more intuitive interface. Eager execution will be enabled by default in TensorFlow 2.0. You can learn more about eager execution [here](https://www.tensorflow.org/guide/eager).

**Can I disable eager execution, if I don’t want to use it?**

Yes. Use tf.disable_eager_execution() or tf.compat.v1.disable_eager_execution(). Eager execution is also disabled inside functions decorated with @tf.function, as well as in any code inside a `with Graph().as_default():` statement.

**Where can I find a style guide for TensorFlow 2.0?**

 There are multiple changes in TensorFlow 2.0 to help support end-user productivity. For a style guide including best practices for API clean-up, @tf.function, see [Effective TF 2.0 Style Guide](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/effective_tf2.md) and this accompanying [blog post](https://medium.com/tensorflow/effective-tensorflow-2-0-best-practices-and-whats-changed-a0ca48767aff).

**Where can I find a mapping of all API symbols in TensorFlow 1.x to their equivalents in TF 2.0, TensorFlow Probability, addons, etc.?**

 You can find the API symbol 1:1 map [here](https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0).

**Why should I upgrade to TensorFlow 2.0?**

Ease of use, eager execution, accelerating the speed of development, giving your engineers the ability to rapidly prototype, and still offering the performance and production-ready functionality that you’ve come to expect from TensorFlow. An early alpha for TF 2.0 has been released at the TF Dev Summit for you to experiment with, test and provide feedback. For more information on what to expect in TensorFlow 2.0, see this [blog post](https://medium.com/tensorflow/whats-coming-in-tensorflow-2-0-d3663832e9b8).

<a name="migration"></a>
### Migration Support

**How can I upgrade my TensorFlow 1.x models to TensorFlow 2.0?**

An upgrade utility called tf_upgrade_v2 is included with every install of TensorFlow 2.0. This tool will allow you to upgrade individual Python files, Jupyter notebooks, and directories of Python files and Jupyter notebooks. For more on the upgrade script, check out this [blog post](https://medium.com/tensorflow/upgrading-your-code-to-tensorflow-2-0-f72c3a4d83b5).

**How do I convert my code from tf.Session, tf.cond, etc., to @tf.function?**

See [Effective TF 2.0 Style Guide](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/effective_tf2.md).

**Where can I find a list of all of the changes in TensorFlow 2.0?**

You can find the API symbol 1:1 map [here](https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0), RFCs on Github, and the [Effective TF 2.0 Style Guide](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/effective_tf2.md).

**How long will TensorFlow 1.x be supported?**

We will provide security patches for the latest 1.x release for one year after TensorFlow 2.0.0 is released. We will otherwise concentrate our efforts on 2.x, and we do not expect to add or backport features to TensorFlow 1.x.

**How can I migrate and support functionality in tf.contrib?**

We have created a special interest group called [TensorFlow Addons](http://www.github.com/tensorflow/addons) that is responsible for migrating functionality from tf.contrib. If you have interest in migrating functionality, please join the SIG.

**TF 2.0 has had a very rapid speed of development. Will there be any more breaking changes in 2.0?**

Once the final version of 2.0 is released, semantic versioning backwards compatibility guarantees apply. All 2.x releases will be backwards compatible with 2.0. We do not make strict compatibility guarantees for 2.0.0-alpha, but we do not expect major breaking API changes.

**How can I migrate and support functionality in tf.contrib?**

We have created a special interest group called [TensorFlow Addons](http://www.github.com/tensorflow/addons) that is responsible for migrating functionality from tf.contrib. If you have interest in migrating functionality, please join the SIG.

**My project relies on tf.contrib. How will I be impacted?**

tf.contrib will be [deprecated](https://github.com/tensorflow/community/blob/master/rfcs/20180907-contrib-sunset.md), but many of its modules will be relocated to part of the core TensorFlow API , or as tensorflow/addons. You are encouraged to take a look at the 1:1 symbol map [here](https://docs.google.com/spreadsheets/d/1FLFJLzg7WNP6JHODX5q8BDgptKafq_slHpnHVbJIteQ/edit#gid=0), and if you feel strongly about one of the modules that has not been migrated, please consider supporting it in tensorflow/addons.

**Where can I find a list of TensorFlow 2.0-related issues?**

All of our issues are tagged with 2.0 and viewable on GitHub [here](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf).

<a name="general"></a>
### General

**Where can I find the TF 2.0 API documentation?**

TensorFlow 2.0 API documentation can be found [here](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf).

** Should I start learning TensorFlow 1.x or TF 2.0?**

We recommend that greenfield projects should begin using TensorFlow 2.0. Here’s how to get started:
- [Udacity Course](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187)
- [DeepLearning.ai Course](https://www.deeplearning.ai/tensorflow-specialization/)
- [TensorFlow Documentation](https://www.tensorflow.org/alpha)

**I’ve noticed a problem with TensorFlow 2.0. How can I file an issue?**

You can file an issue with TF 2.0 on GitHub. Please make sure to include “TensorFlow 2.0” as your version number, and to review the [“What makes a good issue?”](https://github.com/tensorflow/community/blob/master/sigs/build/tensorflow-testing.md) page before submitting.

**Can I try TensorFlow 2.0 right now?**

 Yes. Just pip [install](https://www.tensorflow.org/install) tf-nightly-2.0-preview or pip install tf-nightly-gpu-2.0-preview.

**What is the plan for support of stand-alone Keras (not tf.keras)?**

Refer to Francois Chollet’s [post on the keras-users group](https://groups.google.com/forum/#!searchin/keras-users/francois$20support%7Csort:date/keras-users/wALdULsH9Rs/yN4SdkefFQAJ). Keras is an independent open-source project, and its development work is not dependent on TensorFlow. It will continue to function independently.

**How can I become involved in the planning discussions for TF 2.0?**

We are an open and inclusive community and we value your feedback on TensorFlow 2.0. To get involved in these discussions, please take a look at this [blog post](https://medium.com/tensorflow/contributing-to-tensorflow-sigs-rfcs-testing-and-docs-1c0f8240166c) to find ways to get involved (SIGs, RFCs, etc.).

**How can I learn more, and stay up-to-date on the latest TF 2.0 announcements?**

Review [this blogpost](https://medium.com/tensorflow/contributing-to-tensorflow-sigs-rfcs-testing-and-docs-1c0f8240166c) detailing how to sign up to join a special interest group, be part of the RFC process, and join and discussion forum.

**Can I use TensorFlow 2.0 in Google Colab?**

Yes. TF 2.0 is not the default TensorFlow in Google Colab, but you can certainly pip install it. Here’s how: [Beginner](https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/quickstart/beginner.ipynb), [Advanced](https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/quickstart/advanced.ipynb) and [TensorBoard](https://github.com/tensorflow/tensorboard/blob/master/docs/r2/tensorboard_in_notebooks.ipynb) tutorial guides.

**How can I contribute to TensorFlow 2.0?**

We welcome contributions to TensorFlow and welcome you to our open and inclusive community. See our [Contribution Guide](https://www.tensorflow.org/community/contribute).

**Where can I find example code for TensorFlow 2.0?**

There are many sample tutorials and guides which you can review on TensorFlow start [here](https://github.com/tensorflow/docs/tree/master/site/en/r2).

**My project relies on TensorFlow 2.0. Are there any detailed testing plans or guides available?**

There is a [weekly testing stand-up](https://groups.google.com/a/tensorflow.org/forum/#!forum/testing) (Tuesdays, 2:00pm PT), as well as a weekly migration support hour (Mondays, 10:00am PT). We have been tracking common issues and debugging via the testing@ mailing group, and a list of common troubleshooting questions and answers can be found [here](https://docs.google.com/document/d/1i9_Ey9rYtslS6fryZ5Wm0vWWbrpScW3oh9bTRNVQ87Q/edit).

**How long are estimators going to be around?**

Estimators will continue to be supported through at least the lifetime of TensorFlow 2.x.

**What is the official launch date for TensorFlow 2.0?**

We will release an alpha at the TensorFlow Dev Summit (March 6th, 2019). You can install it [here](https://www.tensorflow.org/install).

**When will TensorFlow support my preferred language?**

If you would like to have your language of choice supported in TensorFlow, we highly encourage you to create a Special Interest Group (SIG) and potentially a Keras binding. An example would be the Rust and the R communities. You can learn more about SIGs [here](https://github.com/tensorflow/community/tree/master/sigs).

<a name="technical"></a>
### Technical

**What is the performance difference between TF 1.x and TF 2.0?**

For FP32, TF 2.0 (keras-graph mode) is slightly slower than TF 1.0 (legacy-graph mode) in basic tests. In other tests, like densenet training CIFAR-10 (a small, custom model), custom run loops in TF 2.0 are faster than keras-graph in TF 2.0. Coming soon will be an out-of-the-box way to run a wide range of models using fp16 (with a graph rewrite that Nvidia has created). With FP16, there is a 2x performance improvement for free by adding 1+ line of code.

**I use checkpoints. How can I convert them?**

The answer right now is, manually, and very carefully - track [this issue](https://github.com/tensorflow/tensorflow/issues/26353).

**How do I know if my migration changes from TensorFlow 1.x to TF 2.0 are checkpoint-breaking?**

See above.

**How can I learn more about subclassing tf.Variable and using tf.Module?**

The original TensorFlow API’s approach to variables had many drawbacks. As detailed by [this RFC](https://github.com/tensorflow/community/pull/11), we’ve worked to make them a bit more tenable in TF 2.0.

**What’s the deal with collections?**

Global collections have been removed in TensorFlow 2.0, in favor of variable garbage collecting. For more on variables in TF 2.0, and how they’ve changed since TF 1.x, please refer to the [Effective TF 2.0 Style Guide](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/effective_tf2.md).

**I use PyTorch, but would like to try TF 2.0. Is there a migration guide?**

No, but we are in the process of creating one. Please reach out through the [TensorFlow community forum](https://www.tensorflow.org/community/forums).

**I use scikit-learn, but would like to try TF 2.0. Is there a migration guide?**

No, but we are in the process of creating one. Please reach out through the [TensorFlow community forum](https://www.tensorflow.org/community/forums).

**I use estimators, but would like to try tf.keras. Is there a migration guide?**

No, but we are in the process of creating one. Please reach out through the [TensorFlow community forum](https://www.tensorflow.org/community/forums).

**What models are available for me to use with TF 2.0? Is there a model zoo?**

We will have several models ready for the alpha release (some CPU, some single-node GPU, and some available on a cluster of GPUs). You can track the bugs listed below for more information about timelines and implementation details.

- [ResNet50 v1.5 & Resnet56 CIFAR-10](https://github.com/tensorflow/tensorflow/issues/25340)
- [NMT Model](https://github.com/tensorflow/tensorflow/issues/25343) ([Example Colab](https://colab.sandbox.google.com/github/tensorflow/docs/blob/master/site/en/r2/tutorials/sequences/nmt_with_attention.ipynb))
- [Pix2Pix](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/models/pix2pix) ([Example Colab](https://colab.sandbox.google.com/github/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/pix2pix.ipynb))
- [DenseNet](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/models/densenet)
- [Dcgan](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/models/dcgan) ([Example Colab](https://colab.sandbox.google.com/github/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/dcgan.ipynb))
- [NCF Model](https://github.com/tensorflow/tensorflow/issues/25344)

**Will static graphs still be supported in TensorFlow 2.0?**

Yes. For an example, please refer to testing estimator ResNet56 Cifar-10 with compat.v1 calls and graphs.

**While Keras is exciting, what other options will I have for building fully-customizable models?**

You can do a lot with Keras, including [subclassing layers](https://medium.com/tensorflow/what-are-symbolic-and-imperative-apis-in-tensorflow-2-0-dfccecb01021), or writing your own training logic by subclassing Model. If you are a framework developer and you need to be free of the conventions Keras’ classes impose, take a look at tf.Module. ([Variables](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/variables.md), [Custom Layers](https://critique.corp.google.com/#review/231992098/depot/google3/third_party/py/tensorflow_docs/g3doc/en/tutorials/eager/custom_layers.ipynb))

**What options do I have for distributed training with TensorFlow 2.0?**

You can train your TensorFlow 2.0 models with multiple GPUs today, using distribution strategies. For more information on distributed training, be sure to check out the [TensorFlow 2.0 Project Tracker](https://github.com/orgs/tensorflow/projects/4) on Github, and search for the keyword “dist-strat”.

For further information, see our tutorials [here](https://github.com/tensorflow/docs/tree/master/site/en/r2/tutorials/distribute) and [here](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/models/densenet).

**How can I deploy TF 2.0 models to other platforms (TF.js, TensorFlow Lite, etc.)?**

A SavedModel contains a complete TensorFlow program, including weights and computation. It does not require the original model building code to run, which makes it useful for deploying with TFLite, TensorFlow.js, or TensorFlow Serving and sharing models (with TFHub).

**Will the frozen graph generated from a TensorFlow 1.x model work in TF 2.0?**

No.

**What is the preferred format for saving a TF model, going forward? (saved_model or HD5)**

Saved_model is the preferred format. For more on exporting, restoring, and running a saved model in [TensorFlow 2.0](https://www.tensorflow.org/r2/tutorials/beginner/tf2_overview#export_a_savedmodel). This format is compatible with TensorFlow.js, TFLite, and more.

**Will the TensorFlow team convert all checkpoints available in the tensorflow/models repo to HD5 or saved_model?**

No.

**How do I choose between tf.data and TF Transform? They seem to do many of the same things.**

[TensorFlow Transform](https://github.com/tensorflow/transform) and tf.data are complementary.

TensorFlow Transform produces a transform graph that includes full-pass data pre-processing tasks on production data pipelines (tasks that you would wish to automate). If you do not need a full pass over your data, you can always simply express transforms with TensorFlow graphs yourself.

[tf.data](https://www.tensorflow.org/guide/datasets) allows you to build a variety of complex data input pipelines for your machine learning models and is used to feed TensorFlow graphs (including TFT graphs); but doesn’t necessarily require a full-pass for operations.

**How do I choose between KubeFlow Pipelines and TFX? They seem very similar.**

KubeFlow Pipelines is intended for scaling production machine learning workloads with Kubernetes on Google Cloud. It uses many TFX components for its orchestration, including TensorFlow Transform (TFT), TensorFlow Serving, and TensorFlow Data Validation (TFDV). TFX is open-source, which means you can use it on any infrastructure you wish.

<a name="mlir"></a>
#### Multi-Level Intermediate Representation

**Are you working on a multi-level intermediate representation layer (MLIR)?**

Yes. Chris Lattner discussed the outline at [c4ml.org](https://www.c4ml.org).

**What's the three-sentence summary of MLIR?**

MLIR stands for Multi-Level Intermediate Representation. It aims at unifying TensorFlow graph representations and strategies for optimization, exploring new code generation approaches, and simplifying backend compiler integration.  This opens up an easier path to the support of a variety of hardware accelerators.

**Who is this targeted to?**

We expect this project to be of great interest to compiler developers, system integrators and, in general, anyone who is interested in making TensorFlow work on a new hardware target.

**If I'm interested in MLIR, what should I do?**

We don't have more to announce at this stage. However:

- You can see Chris Lattner slides from [c4ml.org](https://drive.google.com/file/d/1hUeAJXcAXwz82RXA5VtO5ZoH8cVQhrOK/view)
- Stay tuned to the TensorFlow Blog for more information.

**What about XLA?**

XLA is an important area for investment for us, and continues to be a great place for our partners to contribute to TensorFlow.  These projects are developed by the same team, and are closely aligned in the long term.
'
