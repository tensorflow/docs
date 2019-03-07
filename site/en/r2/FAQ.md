# TensorFlow 2.0: An Overview

Last Updated: _Feb 27, 2019_

A key element of the evolution of TensorFlow is TF 2.0, which is primarily focused on: 

* Cleaning up and standardizing the high-level API surface; 
* Making TensorFlow more intuitive and easier to debug; and 
* Continuing to enable scalable production deployment. 

**TF 2.0 is just in the beginning of this transition.**

You can experiment with the alpha release today - please let us know what you create, and what the experience is like! Over the next few months, we will be focused on making it RC/production ready internally; making it 100% compatible with the rest of TF ecosystem; and sharing that journey with you. We’d love for you to join us and help us!

## Frequently Asked Questions (FAQ)

### :: COMPATIBILITY ::

**Q. Can I still use Keras in TensorFlow 2.0?**

A.  Yes! In fact, Keras (as [`tf.keras`](https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras)) is the preferred higher-level API for TF 2.0. We recommend using tf.keras layers and model.fit() whenever possible; and subclassing when you need more specialized control. For more information, check out this recent [blogpost](https://medium.com/tensorflow/standardizing-on-keras-guidance-on-high-level-apis-in-tensorflow-2-0-bad2b04c819a) on higher-level APIs in TensorFlow 2.0.

**Q. Will TF 1.x scripts continue to work with TF 2.0? How can I upgrade?**

A.  No, TF 1.x scripts **will not** continue to work with TF 2.0. If your models have been written in Keras, however, the upgrade process should be very straightforward. An upgrade utility called `tf_upgrade_v2` is included with every install of TensorFlow 2.0. This tool will allow you to upgrade individual Python files, Jupyter notebooks, and directories of Python files and Jupyter notebooks. For more on the upgrade script, check out this [blogpost](https://medium.com/tensorflow/upgrading-your-code-to-tensorflow-2-0-f72c3a4d83b5). 

**Q. If I use `tf.compat.v1`, will my script still be TF 2.0 compliant?**

A.  Yes, you will still be compliant. You will not be using TF 2.0 style, and you will not be able to use all of its features; but you will be in a safe state, and your code will continue to work through the lifetime of 2.x. For more on upgrading your code to TF 2.0, check [here](https://www.tensorflow.org/alpha/guide/migration_guide).

**Q. Can I still use Estimators in TensorFlow 2.0?**

A.  Yes, absolutely! Estimators will still be available in TF 2.0. Links to the API docs for tf.estimator can be found here; and Toby Boyd has converted the existing ResNet50 Estimator to work on TF 2.0.

**Q. Can I use TensorBoard with TF 2.0? With Keras in TF 2.0?**

A.  Yes! We even have TensorBoard support in Colab and in Jupyter notebooks. Check it out here.

**Q. Is there a 1:1 relationship between stand-alone Keras and tf.keras?**

A. No, there is not. Many of the endpoints in tf.keras are not included in stand-alone Keras, and tf.keras does not support Theano or CNTK as a back-end. If you are interested in the details, please check http://keras.io and the TF 2.0 tf.keras API documentation.

**Q. When will TensorFlow stop supporting Python 2.x?**

A. TensorFlow has signed the Python 3 Statement, and will no longer be supporting Python 2.x as of January 1, 2020.

**Q. What versions of Python does TensorFlow support?**

A. TensorFlow (dependent on version) currently supports Python 2.7, 3.5, 3.6, and 3.7. Support for Python 3.5 and 3.7 will be added for TensorFlow 2.0. You can track this issue to keep updated.

**Q: Is TensorFlow 2.0 compatible with TensorFlow Lite?**

A: TensorFlow 2.0 is compatible with TensorFlow Lite. We will continue to test and expand support as needed. For more information, track this issue.

**Q: Is TensorFlow 2.0 compatible with TensorFlow.js?**

A: TensorFlow 2.0 supports TensorFlow.js v1.0, and most models saved in TF 2.0 will work through the converter process for deployment using TensorFlow.js. Between now and the official release, this support will be expanded. For more information, track this issue.

**Q: Is TensorFlow 2.0 compatible with TensorFlow Extended (TFX)?**

A: Yes, partially! TFX supports distributed training with estimators today, and will support distributed training with Keras shortly. For more information, track this issue.

**Q: Is TensorFlow 2.0 compatible with TensorFlow Hub?**

A: The SavedModel format has been improved to handle TF-Hub use cases. There is a starter list of Hub modules using this format and usable in TF-2.0. . This will be expanded by the RC with support for 1.x TF-Hub module conversion. For more information, track this issue.

**Q: Is TF 2.0 compatible with [insert your favorite TensorFlow organization project here!].**

A. We are working with many TensorFlow related project to make them ready for 2.0. The development work on TensorFlow 2.0 is completely transparent. You can track the engineering team’s status on our GitHub project status tracker here. 

**Q: Does TensorFlow 2.0 have support for TPU?**

A:  TPUs are supported in the alpha release via the TPUStrategy and tf.estimator API. Full support with tf.keras is limited at the moment. You can track this issue on GitHub to keep updated.


**Q: Does TensorFlow 2.0 support Windows?**

A:  We list the status of continuous builds in the README for tensorflow/tensorflow. You can go and take a look at it here. 

### :: FUNCTIONALITY ::

**Q: What is eager execution? Why is it useful?**

A: Eager execution is a flexible machine learning platform for machine learning experimentation, and provides easier debugging, a natural control flow, and a more intuitive interface. Eager execution will be enabled by default in TensorFlow 2.0. You can learn more about eager execution here.

**Q: Can I disable eager execution, if I don’t want to use it?**

A: Yes, use tf.disable_eager_execution() or tf.compat.v1.disable_eager_execution(). Eager execution is also disabled inside functions decorated with @tf.function, as well as in any code inside a `with Graph().as_default():` statement.

**Q. Where can I find a style guide for TensorFlow 2.0?**

A:  There are multiple changes in TensorFlow 2.0 to help support end-user productivity. For a style guide including best practices for API clean-up, @tf.function, and more, check out the Effective TF 2.0 Style Guide and this accompanying blog post.

**Q. Where can I find a mapping of all API symbols in TensorFlow 1.x to their equivalents in TF 2.0, TensorFlow Probability, addons, etc.?**

A:  API symbol 1:1 map (work in progress, not yet including tensorflow/addons!).

**Q: Why should I upgrade to TensorFlow 2.0?**

A: Ease of use, eager execution, accelerating the speed of development, giving your engineers the ability to rapidly prototype, and still offering the performance and production-ready functionality that you’ve come to expect from TensorFlow. An early alpha for TF 2.0 has been released at the TF Dev Summit, if you are interested in kicking the tires and testing. For more information on what to expect in TensorFlow 2.0, check out this blog post.

### :: MIGRATION SUPPORT ::

**Q. How can I upgrade my TensorFlow 1.x models to TensorFlow 2.0?**

An upgrade utility called tf_upgrade_v2 is included with every install of TensorFlow 2.0. This tool will allow you to upgrade individual Python files, Jupyter notebooks, and directories of Python files and Jupyter notebooks. For more on the upgrade script, check out this blog post. 

**Q. How do I convert my code from tf.Session, tf.cond, etc., to @tf.function?**

A: Link to the Effective TF 2.0 Style Guide and Tomer’s upgrade guide. 

**Q. Where can I find a list of all of the changes in TensorFlow 2.0?**

A: <link to the 1:1 symbol map (work in progress, does not yet include tensorflow/addons!), RFCs, and the Effective TF 2.0 Style Guide.>

**Q. How long will TensorFlow 1.x be supported?**

A: We will provide security patches for the latest 1.x release for one year after TensorFlow 2.0.0 is released. We will otherwise concentrate our efforts on 2.x, and we do not expect to add or backport features to TensorFlow 1.x.

**Q. How can I migrate and support functionality in tf.contrib?**

A: We have created a special interest group called TensorFlow Addons that is responsible for migrating functionality from tf.contrib. If you have interest in migrating functionality, please join the SIG.

**Q. TF 2.0 has had a very rapid speed of development. Will there be any more breaking changes in 2.0?**

A: Once the final version of 2.0 is released, semver backwards compatibility guarantees apply <link to version_compat>. All 2.x releases will be backwards compatible with 2.0. We do not make strict compatibility guarantees for 2.0.0-alpha, but we do not expect major breaking API changes. 

**Q. How can I migrate and support functionality in tf.contrib?**

A: We have created a special interest group called TensorFlow Addons that is responsible for migrating functionality from tf.contrib. If you have interest in migrating functionality, please join the SIG.

**Q. My project relies on tf.contrib. How will I be impacted?**

A: tf.contrib will be deprecated, but many of its modules will be moving to new homes as part of the core TensorFlow API itself, or tensorflow/addons. You are encouraged to take a look at the 1:1 symbol map (still very much a work in progress!), and if you feel strongly about one of the modules that has not been migrated, please consider supporting it in tensorflow/addons.

**Q. Where can I find a list of TensorFlow 2.0-related issues?**

A: All of our issues are tagged with 2.0 and viewable on GitHub. Take a look!

### :: GENERAL ::

**Q. Where can I find the TF 2.0 API documentation?**

A. TensorFlow 2.0 API documentation can be found here.

**Q.  Should I start learning TensorFlow 1.x or TF 2.0?**

A: We strongly suggest greenfield projects should begin using TensorFlow 2.0. Here’s how to get started:
- Udacity Course
- DeepLearning.ai Course
- TensorFlow Documentation

**Q. I’ve noticed a problem with TensorFlow 2.0. How can I file an issue?**

A: You can file an issue with TF 2.0 on GitHub. Please make sure to include “TensorFlow 2.0” as your version number, and to review the “What makes a good issue?” page before submitting.

**Q. Can I try TensorFlow 2.0 right now?**

A:  You bet! Just pip install tf-nightly-2.0-preview or pip install tf-nightly-gpu-2.0-preview.

**Q. What is the plan for support of stand-alone Keras (not tf.keras)?**

A: Please refer to Francois Chollet’s post on the keras-users group. Keras is an independent open-source project, and its development work is not dependent on TensorFlow. It will continue to function independently.

**Q. How can I become involved in the planning discussions for TF 2.0?**

A: We would love to hear your thoughts about the direction TF 2.0 is heading! Please take a look at this blog post to find ways to get involved (SIGs, RFCs, etc.).

**Q. How can I learn more, and stay up-to-date on the latest TF 2.0 announcements?**

A: Please review this blogpost detailing how to sign up to join a special interest group, be part of the RFC process, and join and discussion forum.

**Q. Can I use TensorFlow 2.0 in Google Colab?**

A: You bet! TF 2.0 is not the default TensorFlow in Google Colab, but you can certainly pip install it. Here’s how: beginner and advanced. We also have a TensorBoard tutorial!

**Q. How can I contribute to TensorFlow 2.0?**

A: We welcome contributions, and are excited to have you as part of the community! Here is a link to our contribution guide: <to be added once the website goes live>

**Q. Where can I find example code for TensorFlow 2.0?**

A: We’ve prepared many sample tutorials and guides, which you can review on tensorflow/docs.

**Q. My project relies on TensorFlow 2.0. Are there any detailed testing plans or guides available?**

A: We have a weekly testing stand-up (Tuesdays, 2:00pm PT), as well as a weekly migration support hour (Mondays, 10:00am PT). We have been tracking common issues and debugging via the testing@ mailing group, and a list of common troubleshooting questions and answers can be found here.

**Q. How long are estimators going to be around?**

A: Estimators will continue to be supported through at least the lifetime of TensorFlow 2.x.

**Q. What is the official launch date for TensorFlow 2.0?**

A: We will release an alpha at the TensorFlow Dev Summit (March 6th, 2019).

**Q. When will TensorFlow support [my most favorite and beloved language]?**

A: If you would like to have your language of choice supported in TensorFlow, we highly encourage you to create a Special Interest Group and potentially a Keras binding. An example would be the Rust and the R communities. Learn more about SIGs here.

### :: TECHNICAL ::

**Q. What is the performance difference between TF 1.x and TF 2.0?**

A.  For FP32, TF 2.0 (keras-graph mode) is slightly slower than TF 1.0 (legacy-graph mode) in basic tests. In other tests, like densenet training CIFAR-10 (a small, custom model), custom run loops in TF 2.0 are faster than keras-graph in TF 2.0. Coming soon will be an out-of-the-box way to run a wide range of models using fp16 (with a graph rewrite that Nvidia has created). With FP16, there is a 2x performance improvement for free by adding 1+ line of code.

**Q. I use checkpoints. How can I convert them?**
A. The answer right now is, manually, and very carefully (see b/125850323 / #26353). For more information, check out this guide for checkpoint-breakers and checkpoint-breakees: go/tf-2.0-checkpoint-breaking

**Q. How do I know if my migration changes from TensorFlow 1.x to TF 2.0 are checkpoint-breaking?**

A.  See above.

**Q. How can I learn more about subclassing tf.Variable and using tf.Module?**

A.  The original TensorFlow API’s approach to variables had many drawbacks. As detailed by this RFC, we’ve worked to make them a bit more tenable in TF 2.0. < link to Colab notebook that Alex and Artem created; link to the tf.Module guide; link to the RFC about Variables>

**Q. What’s the deal with collections?**

A.  Global collections have been removed in TensorFlow 2.0, in favor of variable garbage collecting. For more on variables in TF 2.0, and how they’ve changed since TF 1.x, please refer to the Effective TF 2.0 Style Guide.

**Q. I use PyTorch, but would like to try TF 2.0. Is there a migration guide?**

A: No, but we are in the process of creating one! Reach out to webpaige@google.com for more details.

**Q. I use scikit-learn, but would like to try TF 2.0. Is there a migration guide?**

A: No, but we are in the process of creating one! Reach out to webpaige@google.com for more details.

**Q. I use estimators, but would like to try tf.keras. Is there a migration guide?**

A: No, but we are in the process of creating one! Reach out to karmel@google.com for more details.

**Q. What models are available for me to use with TF 2.0? Is there a model zoo?**

A: We will have several models ready for the alpha release (some CPU, some single-node GPU, and some available on a cluster of GPUs). You can track the bugs listed below for more information about timelines and implementation details.

- ResNet50 v1.5 and Resnet56 CIFAR-10 (1 GPU and 8 GPU with dist strat and keras-graph also run under TF 1.0 along with an estimator example that has been converted to TF 2.0 tested on TF 1.0.  You can remove this but here is the matrix of tests.  Messy code but it covers everything and is where we will test all new features like multi-node keras. )

- Keras Application Set (CPU)
- NMT Model (example Colab notebook, CPU)
- Pix2Pix [DevRel] (example Colab notebook, CPU and 1 GPU)
- DenseNet [DevRel]  (keras-fit and custom run loop 1 and 2 GPUs tested nightly with Distribution Strategy)
- Dcgan [DevRel] (example Colab notebook, CPU and 1 GPU)
- NCF Model (CPU?)

**Q. Will static graphs still be supported in TensorFlow 2.0?**

A: Yes. For an example, please refer to testing estimator ResNet56 Cifar-10 with compat.v1 calls and graphs.

**Q. Keras is great, but what options will I have for building fully-customizable models?**

A: You can do a lot with Keras, including subclassing layers (see: Symbolic and Imperative APIs in Keras), or writing your own training logic by subclassing Model. If you are a framework developer and you need to be free of the conventions Keras’ classes impose, take a look at tf.Module. (Variables, Custom Layers)

**Q. What options do I have for distributed training with TensorFlow 2.0?**

A: You can train your TensorFlow 2.0 models with multiple GPUs today, using distribution strategies. For more information on distributed training, be sure to check out the TF 2.0 Project Tracker on Github, and search for the keyword “dist-strat”. Also see our tutorials here and here. 

**Q. How can I deploy TF 2.0 models to other platforms (TF.js, TensorFlow Lite, etc.)?**

A: <picture of saved_model wearing a superhero cape>

**Q. Will the frozen graph generated from a TensorFlow 1.x model work in TF 2.0?**

A.  No. 

**Q. What is the preferred format for saving a TF model, going forward? (saved_model or HD5)**

A.  saved_model. For more on exporting, restoring, and running a saved model in TensorFlow 2.0, check here. An added bonus: this format is compatible with TensorFlow.js, TFLite, and more.

**Q. Will the TensorFlow team convert all checkpoints available in the tensorflow/models repo to HD5 or saved_model?**

A.  No.

**Q. How do I choose between tf.data and TF Transform? They seem to do many of the same things.**

A.  TensorFlow Transform and tf.data are complementary.

TensorFlow Transform produces a transform graph that includes full-pass data pre-processing tasks on production data pipelines (tasks that you would wish to automate). If you do not need a full pass over your data, you can always simply express transforms with TensorFlow graphs yourself. 

tf.data allows you to build a variety of complex data input pipelines for your machine learning models and is used to feed TensorFlow graphs (including TFT graphs); but doesn’t necessarily require a full-pass for operations. 

**Q. How do I choose between KubeFlow Pipelines and TFX? They seem very similar.**

A. KubeFlow Pipelines is intended for scaling production machine learning workloads with Kubernetes on Google Cloud. It uses many TFX components for its orchestration, including TensorFlow Transform (TFT), TensorFlow Serving, and TensorFlow Data Validation (TFDV). TFX is open-source, which means you can use it on any infrastructure you wish.

### :: MLIR: Multi-Level Intermediate Representation ::

**Q.  I heard something about an intermediate representation layer?**

Yes, that's true, we are working on it.  Chris Lattner discussed the outline at c4ml.org. 

**Q. What's the three-sentence summary of MLIR?**

MLIR stands for Multi-Level Intermediate Representation. It aims at unifying TensorFlow graph representations and strategies for optimization, exploring new code generation approaches, and simplifying backend compiler integration.  This opens up an easier path to the support of a variety of hardware accelerators. 

**Q. Who is this targeted to?**

We expect this project to be of great interest to compiler developers, system integrators and, in general, anyone who is interested in making TensorFlow work on a new hardware target. 

**Q. If I'm interested in MLIR, what should I do?**

- Check out Chris's slides
- Talk to Chris or Tatiana at the Summit
- Stay tuned to our blog for more

**Q. What about XLA?**

XLA is an important area for investment for us, and continues to be a great place for our partners to contribute to TensorFlow.  These projects are developed by the same team, and are closely aligned in the long term.
