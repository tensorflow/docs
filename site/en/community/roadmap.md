# Roadmap

*Last updated: Jun 4, 2019*

TensorFlow is a fast-moving, community supported project. This roadmap provides
guidance about priorities and focus areas of the TensorFlow team and lists the
functionality expected in upcoming releases of TensorFlow. Many of these areas
are driven by community use cases, and we welcome further
[contributions](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)
to TensorFlow.

## TensorFlow 2.0 Beta is available

[As announced previously](https://groups.google.com/a/tensorflow.org/forum/#!topic/discuss/bgug1G6a89A),
we have been working on TensorFlow 2.0, which is a significant milestone and a
major new release, with a focus on ease of use and simplification.

The 2.0 Beta release is available now. Users can use this today and get started
with all that TensorFlow 2.0 has to offer. This is an early version meant to
share with users what the TensorFlow 2.0 API will be like, to gather feedback,
and to identify and fix issues. Below are some of the key enhancements:

*   Eager execution as a central feature of 2.0. It aligns users’ expectations
    about the programming model better with TensorFlow practice and should make
    TensorFlow easier to learn and apply.
*   Keras tightly integrated with the TensorFlow ecosystem, and has support for
    Eager execution, `tf.data` API, `tf.distribute.MirroredStrategy` for
    multi-GPU training, TensorBoard visualization, and TF Lite and TF.js
    conversion.
*   Starter list of TF-Hub models loadable in TF 2.0.
*   Autograph making it easier to write models with custom control flow ops and
    getting graph performance with `tf.function`.
*   Flexible API choices that let users build models quickly using high level
    building blocks, or take full control by writing custom models and custom
    training loops using lower level constructs.
*   Support for TPUs using the TPUStrategy with `tf.estimator`.
*   Support for multi worker synchronous training using `tf.distribute.Strategy`
    with `tf.estimator`.
*   New end-to-end ML framework for building ML pipelines with TFX.
*   Simplified and cleaned-up API by removing deprecated APIs, reducing
    redundancies, renaming symbols to more intuitive names, simplifying how
    variables are treated.
*   Removal of `tf.contrib` - These features have been either moved to
    TensorFlow Core, or to tensorflow/addons, or are no longer part of the
    TensorFlow build but are developed and maintained by their respective
    owners.
*   Updated and revised documentation, examples, and website, including
    migration docs and TF 1.x to 2.0 converter guide.
*   New releases of TensorFlow.js and Swift for TensorFlow packages.
*   Many more add-ons and extensions (eg. TF Datasets, TF Federated, TF Privacy,
    etc).

## Roadmap

After the TensorFlow 2.0 release, we will identify and fix issues, and test the
TensorFlow 2.0 Beta with internal and external partners. The official 2.0
release target is Q2 2019. This is a list of features on the short term roadmap
and beyond:

#### APIs

*   Mixed precision training API in Keras.
*   Premade estimators for boosted trees, random forest, approximate
    nearest-neighbor search, k-means clustering, and more.
*   `tf.distribute.Strategy` support for Keras subclass models, TPUs, and
    multi-node training
*   Improved support for model saving and loading `SavedModel`, and conversion
    of existing 1.x TF-Hub modules

#### Reference models

*   Updated model repository with TF 2.0 best-practice reference models and
    research model implementations. These will include ResNet, MobileNet,
    DenseNet, Mask-RCNN, NMT, NCF, Transformer, and many other models
*   Collection of [TF Hub modules](https://tfhub.dev/s?q=tf2-preview), loadable
    in TensorFlow 2.0.
*   More performance optimizations.

#### TensorBoard

*   General bug fixes and enhancements to make TensorBoard great with TensorFlow
    2.0.
*   Improvements to hyperparameter tuning capabilities and workflow.
*   Enable hosted TensorBoard to make sharing dashboards easy and search/compare
    experiments.
*   Create a better plugin process for testing and adding TensorBoard plugins.
*   Enable plugins to use different frontend technologies (like React).

#### TensorFlow Lite

*   Increase coverage of supported ops in TensorFlow Lite.
*   Easier conversion of TensorFlow 2.0 models to use in TensorFlow Lite.
*   Extended support for Edge TPUs, TPU AIY boards.
*   More documentation and tutorials.

#### TensorFlow.js

*   Continued browser performance improvements.
*   Implement prototype using compute shaders or WebGPU.
*   Improve CPU performance, implement SIMD+ Web Assembly support (when
    available).
*   More off-the-shelf models for image, audio, text models, and more.
*   Improve parity in features and performance on Node with core TensorFlow.
*   Support for TensorBoard visualization in Node training with TensorFlow.js.
*   Integration with more JavaScript platforms.
*   More documentation and getting started content.

#### TensorFlow with Swift

*   Focus on researchers for the first half of 2019.
*   Significant new feature development, such as support for transfer learning.
*   Polish existing features, such as control flow support by the AutoDiff
    system.
*   Deeper integrations with the TensorFlow ecosystem, such as TensorBoard.
*   End-to-end tutorials for getting started on Swift for TensorFlow in Colab
    and additional technical documentation.
*   Collaboration with fast.ai

#### TensorFlow Extended (TFX)

*   Integration of all TFX components with TensorFlow 2.0.
*   Fully orchestrated end-to-end workflows with common configuration and
    metadata tracking.
*   Advanced training features, such as warm-starting.
*   Notebook embedded visualizations and experiment tracking,

#### Extensions and add-ons

*   Migration and TensorFlow 2.0 support for all major extensions to TensorFlow,
    including Probability, Agents, Tensor2Tensor, TensorRT, and more.
*   More data sets in TensorFlow Datasets.
*   Documentation and resources for extension libraries.

#### Community and engagement

*   New resources for community discussion and feedback.
*   Launch new SIGs aligned with TensorFlow roadmap.
*   Gather and highlight novel TensorFlow use cases and applications.

Track the progress of these features and TensorFlow 2.0 development in the
[GitHub project tracker](https://github.com/orgs/tensorflow/projects/4).
