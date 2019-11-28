# TensorFlow 1.x guide (archived)

Note: Please use the latest guide at https://www.tensorflow.org/guide

The documents in this unit dive into the details of how TensorFlow 1.x
works. The units are as follows:

## High Level APIs

* [Keras](keras.ipynb), TensorFlow's high-level API for building and
  training deep learning models.
* [Eager Execution](eager.ipynb), an API for writing TensorFlow code
  imperatively, like you would use Numpy.
* [Importing Data](datasets.md), easy input pipelines to bring your data into
  your TensorFlow program.
* [Estimators](estimators.md), a high-level API that provides
  fully-packaged models ready for large-scale training and production.

## Estimators

* [Premade Estimators](premade_estimators.md), the basics of premade
  Estimators.
* [Checkpoints](checkpoints.md), save training progress and resume where you
  left off.
* [Feature Columns](feature_columns.md), handle a variety of input data types
  without changes to the model.
* [Datasets for Estimators](datasets_for_estimators.md), use `tf.data` to
  input data.
* [Creating Custom Estimators](custom_estimators.md), write your own
  Estimator.

## Accelerators

* [Distributed Strategy](distribute_strategy.ipynb)
* [Using GPUs](using_gpu.md) explains how TensorFlow assigns operations to
  devices and how you can change the arrangement manually.
* [Using TPUs](using_tpu.md) explains how to modify `Estimator` programs to
  run on a TPU.

## Low Level APIs

* [Introduction](low_level_intro.md), which introduces the
  basics of how you can use TensorFlow outside of the high Level APIs.
* [Tensors](tensors.md), which explains how to create,
  manipulate, and access Tensors--the fundamental object in TensorFlow.
* [Variables](variables.md), which details how
  to represent shared, persistent state in your program.
* [Graphs and Sessions](graphs.md)
* [Control flow](autograph.ipynb), using AutoGraph and `tf.function`.
* [Save and Restore](saved_model.md), which
  explains how to save and restore variables and models.
* [Ragged Tensors](ragged_tensors.ipynb), which explains how to use
  Ragged Tensors to encode nested variable-length lists.

## ML Concepts

* [Embeddings](embedding.md), which introduces the concept
  of embeddings, provides a simple example of training an embedding in
  TensorFlow, and explains how to view embeddings with the TensorBoard
  Embedding Projector.

## Debugging

* [TensorFlow Debugger](debugger.md), which
  explains how to use the TensorFlow debugger (tfdbg).

## Performance

Performance is an important consideration when training machine learning models.
Performance speeds up and scales research while also providing end users with
near instant predictions.

* [Performance overview](./performance/overview.md) contains a collection of best
  practices for optimizing your TensorFlow code.
* [Data input pipeline](./performance/datasets.md) describes the `tf.data` API
  for building efficient data input pipelines for TensorFlow.
* [Benchmarks](./performance/benchmarks.md) contain a collection of benchmark
  results for a variety of hardware configurations.

Additionally, [TensorFlow Lite](https://www.tensorflow.org/lite) has
[optimization techniques](https://www.tensorflow.org/lite/performance/best_practices)
for mobile and embedded devices.

## Extend

This section explains how developers can add functionality to TensorFlow's
capabilities.

* [TensorFlow architecture](./extend/architecture.md) presents an architectural
  overview.
* [Create an op](./extend/op.md), which explains how to create your own operations.
* [Custom filesystem plugin](./extend/filesystem.md), which explains how to add
  support for your own shared or distributed filesystem.
* [Custom file and record formats](./extend/formats.md), which details how to add
  support for your own file and record formats.
* [Model files](./extend/model_files.md), for creating tools compatible with
  TensorFlow's model format.
* [Language bindings](./extend/bindings.md), Python is currently the only
  language supported by TensorFlow's API stability promises. However, TensorFlow
  also provides functionality to create or develop features in other languages.
* [C++ guide](./extend/cc.md)

[XLA (Accelerated Linear Algebra)](https://www.tensorflow.org/xla) is an
experimental compiler for linear algebra that optimizes TensorFlow computations.

## Misc

* [TensorFlow Version Compatibility](version_compat.md),
  which explains backward compatibility guarantees and non-guarantees.
