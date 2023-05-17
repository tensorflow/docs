# TensorFlow Core APIs overview

The TensorFlow Core APIs provide a set of comprehensive, composable, and
extensible low-level APIs for high-performance (distributed and accelerated)
computation, primarily aimed at building machine learning (ML) models as well as
authoring ML workflow tools and frameworks within the TensorFlow platform. These
APIs provide a foundation for creating highly configurable models with
fine-grained control and new frameworks from the ground up.

The Core APIs can be used as an alternative to high-level machine learning APIs
like Keras. These high-level APIs are best suited for general machine learning
needs. They offer a variety of modules that abstract away the complexities of ML
while also offering functionalities for customization through subclassing. If
you are looking for an overview of TensorFlow using Keras, see the Quickstarts
and Keras sections in the [tutorials](https://www.tensorflow.org/tutorials).

## Who should use the Core APIs

The TensorFlow Core low-level APIs are designed with the following ML developers
in mind:

*   Researchers building complex models with high levels of configurability
*   Developers interested in using TensorFlow as a high-performance scientific
    computing platform
*   Framework authors building tools on top of the TensorFlow platform
*   High-level API users interested in:
    *   Adding additional functionalities to their machine learning workflows
        such as custom layers, losses, models, and optimizers
    *   Learning more about the inner workings of their models

## Core API applications

The TensorFlow Core APIs provide access to low level functionality within the
TensorFlow ecosystem. This API provides more flexibility and control for
building ML models, applications, and tools, compared to high-level APIs, such
as Keras.

### Build models and workflows

The Core APIs are most commonly used to build highly customizable and optimized
machine learning models and workflows. Here are some of the ways that the
TensorFlow Core APIs can improve your machine learning models and workflow
development:

<img src="https://www.tensorflow.org/site-assets/images/marketing/learn/tfx-
transform.svg" alt="TensorFlow" align="right"/>

*   Building non-traditional models or layers that do not fully fit the
    structures supported by high-level APIs
*   Building custom layers, losses, models, and optimizers within Keras
*   Implementing new optimization techniques to expedite convergence during
    training
*   Creating custom metrics for performance evaluation
*   Designing highly-configurable training loops with support for features like
    batching, cross-validation, and distribution strategies

### Build frameworks and tools

The TensorFlow Core APIs can also serve as the building blocks for new
high-level frameworks. Here are some examples of tools and frameworks that are
created with the low-level APIs:
<img src="https://www.tensorflow.org/static/site-assets/images/marketing/icon/learn-ml/human-ai.png" alt="TensorFlow" width=150 align="right"/>

*   [Keras](https://keras.io): deep learning for humans
*   [TensorFlow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization):
    a suite of tools to optimize ML models for deployment and execution
*   [TensorFlow Graphics](https://www.tensorflow.org/graphics): a library for
    making useful graphics functions widely accessible

### Build for scientific computing

The TensorFlow Core APIs can also be applied outside the realm of machine
learning. Here are a few general-purpose use cases of TensorFlow for scientific
computing:
<img src="https://www.tensorflow.org/static/site-assets/images/marketing/icon/learn-ml/math-concepts.png" alt="TensorFlow" width=100 align="right"/>

*   Physics simulations for solid mechanics and
    [fluid dynamics](https://arxiv.org/abs/2108.11076) problems
*   Graphics rendering applications like
    [ray tracing](https://github.com/BachiLi/redner)
*   Solving
    [constrained optimization problems](https://github.com/google-research/tensorflow_constrained_optimization/blob/master/README.md)

## Core API components

Here are some of the fundamental components that comprise TensorFlow Core’s low-
level APIs. Note that this is not an all-encompassing list:

<img src="https://www.tensorflow.org/static/site-assets/images/marketing/resources/edu-hero.svg" alt="TensorFlow" width=300
align="right"/>

*   Data structures : `tf.Tensor`, `tf.Variable`, `tf.TensorArray`
*   Primitive APIs: `tf.shape`,
    [slicing](https://www.tensorflow.org/guide/tensor_slicing), `tf.concat`,
    `tf.bitwise`
*   Numerical: `tf.math`, `tf.linalg`, `tf.random`
*   Functional components: `tf.function`, `tf.GradientTape`
*   Distribution: [DTensor](https://www.tensorflow.org/guide/dtensor_overview)
*   Export: `tf.saved_model`

## Next steps

The *Build with Core* documentation provides tutorials of basic machine learning
concepts from scratch. The tutorials in this section help you get comfortable
with writing low-level code with Core APIs that you can then apply to more
complex use cases of your own.

Note: You should not use the Core APIs to simply re-implement high-level APIs,
and it is possible to use high-level APIs, such as Keras, with the Core APIs.

To get started using and learning more about the Core APIs, check out the
[Quickstart for TensorFlow Core](https://www.tensorflow.org/guide/core/quickstart_core).
