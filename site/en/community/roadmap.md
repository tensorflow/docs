# Roadmap
**Last updated: Sep 4, 2018**

TensorFlow is a rapidly moving, community supported project. This document is intended
to provide guidance about priorities and focus areas of the core set of TensorFlow
developers and expected functionality in the upcoming releases of TensorFlow. Many of
these areas are driven by community use cases, and we welcome further
[contributions](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)
to TensorFlow.


## TensorFlow 2.0 is coming

[As announced recently](https://groups.google.com/a/tensorflow.org/forum/#!topic/discuss/bgug1G6a89A), we have started work on the next major version of TensorFlow. TensorFlow 2.0 will be a significant milestone, with a focus on ease of use. Here are some highlights of what users can expect with TensorFlow 2.0:

* Eager execution is a central feature of 2.0. It aligns users’ expectations about the programming model better with TensorFlow practice and should make TensorFlow easier to learn and apply.
* Support for more platforms and languages, and improved compatibility and parity between these components via standardization on exchange formats and alignment of APIs.
* We will remove deprecated APIs and reduce the amount of duplication, which has confused for users.

For more details on 2.0 and associated public design consultations, please see the [full announcement](https://groups.google.com/a/tensorflow.org/forum/#!topic/discuss/bgug1G6a89A).


## Roadmap

The features below do not have concrete release dates. However, the majority are
expected in the next one to two releases.

### APIs

#### High-level APIs

* Stronger integration of Keras, Eager, and Estimators to use same data pipelines, APIs, and serialization formats (Saved Model).
* Canned Estimators for commonly used ML models (such as TimeSeries, RNNs, TensorForest, additional boosted trees features) and related functionality (like sequence feature columns) in TensorFlow Core (migrated from contrib if they exist).

#### Eager execution

* Use DistributionStrategy to utilize multiple GPUs and multiple TPU cores.
* Distributed training support (multi-machine).
* Performance improvements.
* Simpler export to a GraphDef/SavedModel.

#### Reference models

* Building out a set of [models](https://github.com/tensorflow/models/tree/master/official)
  across image recognition, object detection, speech, translation, recommendation,
  and reinforcement learning that demonstrate best practices and serve as a starting point for
  high-performance model development.
* A growing set of high-performance [Cloud TPU reference models](https://github.com/tensorflow/tpu).

#### Contrib

* Deprecate parts of `tf.contrib` where preferred implementations exist outside of `tf.contrib`.
* As much as possible, move large projects inside `tf.contrib` to separate repositories.
* The `tf.contrib` module will be discontinued in its current form with TensorFlow 2.0. Experimental
  development will happen in other repositories in the future.

### Platforms

#### TensorFlow Lite

* Increase coverage of supported ops in TensorFlow Lite.
* Easier conversion of a trained TensorFlow graph for use on TensorFlow Lite.
* Tools for mobile model optimization.
* Extend support for Edge TPUs, TPU AIY boards.
* Better documentation and tutorials.

#### TensorFlow.js

* Improve performance of TensorFlow.js in the browser; Implement prototype using compute shaders or WebGPU,
  when available; Improve CPU performance, implement SIMD+ Web Assembly support when available.
* Expand support for importing TensorFlow SavedModels and Keras models, with focus on audio and text-based models.
* Release a new tfjs-data API for efficient data input pipelines, and a new tfjs-vis library for interactive model visualizations during browser training.
* For server-side TensorFlow.js using Node - improve parity with native TensorFlow ops and model formats by
  exposing all TensorFlow ops; Add async mode support using libuv.

#### TensorFlow with Swift

* Continue to refine the design and implementation through 2018.
* Core components (Graph Program Extraction, Basic AutoDiff, Send/Receives) reliable enough for general use by the
  end of 2018.
* Explore the use of Swift for TensorFlow for building dynamic models through 2018.
* Basic tutorials for getting started on Swift for TensorFlow in Colab in early 2019.

### Performance

#### Distributed TensorFlow

* Expand new distribution strategy API to support Keras on TPUs and multi-node GPU.
* Demonstrate great out-of-the-box performance and easy deployment.

#### GPU optimizations

* Simplify mixed precision API with public design review.
* Finalize TensorRT API and move to core.
* TensorRT support for SavedModel and TF Serving.
* CUDA 10 integration (plan to skip CUDA 9.2 as it has minimal advantages to CUDA 9.0 when using the same version of cuDNN).
* Optimizations for DGX-2.

#### Cloud TPUs and Cloud TPU Pods

* Expand support for Keras on Cloud TPUs and further optimize performance.
* Extend support for image segmentation - add Mask R-CNN to current
  [RetinaNet](https://github.com/tensorflow/tpu/tree/master/models/official/retinanet) and
  [DeepLab](https://github.com/tensorflow/tpu/tree/master/models/experimental/deeplab) semantic
  segmentation reference models.
* Optimize new Cloud TPU integrations: GKE, CMLE, Cloud Bigtable, gRPC data input.
* Enable large-scale model parallelism on Cloud TPU Pods.
* Optimize reference model performance on Cloud TPU v3.

#### CPU optimizations

* Int8 support for SkyLake via MKL.
* Faster 3D ops via MKL.
* Dynamic loading of SIMD-optimized kernels.
* MKL for Linux and Windows.

### Other packages

#### TensorFlow Probability

* Additional implementations of Gaussian processes, including applications to hyperparameter optimization.
* Bayesian Structural Time Series models.
* Enhancements to sampling and optimization methods.
* Rich set of Colab tutorials for using TFP.

#### Tensor2Tensor library

* New datasets and models for video, speech, and music with support for autoencoders, GANs, and RL.
* Improve support for all platforms and simplify internals using TensorFlow 2.0 best practices.
* Train huge models with model-parallelism with Mesh TensorFlow.

### End-to-end ML systems

#### TensorFlow Hub

* Expand support for TF-Hub modules with TF Eager integration, Keras layers integration,
  and TensorFlow.js integration, and support for TF-Transform and TF-Data workflows.

#### TensorFlow Extended

* Open source more of the TensorFlow Extended platform to facilitate the adoption of TensorFlow in production settings.
* Package TF Model Analysis for model evaluation and validation.
* Release TFX libraries for Data Validation.
* Publish end-to-end ML pipeline workflow examples.

### Community and partner engagement

#### Special Interest Groups (SIGs)

* Mobilize the community to work together in focused domains.
* [Evaluate and form new SIGs](https://github.com/tensorflow/community/blob/master/governance/SIGS.md) as
  needed to support ecosystem.

#### Community

* Continue public feedback on significant design decisions through the
  [Request-for-Comment (RFC) process](https://github.com/tensorflow/community/blob/master/governance/TF-RFCs.md).
* Create a contributors’ guide to augment our
  [published governance and process](https://github.com/tensorflow/community/tree/master/governance).
* Grow global TensorFlow communities and user groups.
* Collaborate with partners to co-develop and publish research papers.
* Continue to publish blog posts and YouTube videos showcasing applications of TensorFlow and build user
  case studies for high impact applications.
