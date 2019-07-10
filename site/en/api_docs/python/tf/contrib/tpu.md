page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.tpu

Ops related to Tensor Processing Units.



Defined in [`contrib/tpu/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/tpu/__init__.py).

<!-- Placeholder for "Used in" -->










## Modules

[`profiler`](../../tf/contrib/tpu/profiler) module: Stub file to maintain backwards compatibility.

## Classes

[`class AsyncCheckpointSaverHook`](../../tf/contrib/tpu/AsyncCheckpointSaverHook): Saves checkpoints every N steps or seconds.

[`class CrossShardOptimizer`](../../tf/tpu/CrossShardOptimizer): An optimizer that averages gradients across TPU shards.

[`class DeviceAssignment`](../../tf/tpu/experimental/DeviceAssignment): Mapping from logical cores in a computation to the physical TPU topology.

[`class InfeedQueue`](../../tf/contrib/tpu/InfeedQueue): A helper object to build a device infeed queue.

[`class InputPipelineConfig`](../../tf/estimator/tpu/InputPipelineConfig): Please see the definition of these values in TPUConfig.

[`class RunConfig`](../../tf/estimator/tpu/RunConfig): RunConfig with TPU support.

[`class TPUConfig`](../../tf/estimator/tpu/TPUConfig): TPU related configuration required by `TPUEstimator`.

[`class TPUDistributionStrategy`](../../tf/contrib/tpu/TPUDistributionStrategy): The strategy to run Keras model on TPU.

[`class TPUEstimator`](../../tf/estimator/tpu/TPUEstimator): Estimator with TPU support.

[`class TPUEstimatorSpec`](../../tf/estimator/tpu/TPUEstimatorSpec): Ops and objects returned from a `model_fn` and passed to `TPUEstimator`.

[`class Topology`](../../tf/contrib/tpu/Topology): Describes a set of TPU devices.

## Functions

[`batch_parallel(...)`](../../tf/tpu/batch_parallel): Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](../../tf/tpu/bfloat16_scope): Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](../../tf/tpu/core): Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](../../tf/tpu/cross_replica_sum): Sum the input tensor across replicas according to group_assignment.

[`device_assignment(...)`](../../tf/contrib/tpu/device_assignment): Computes a device_assignment of a computation across a TPU topology.

[`export_estimator_savedmodel(...)`](../../tf/contrib/tpu/export_estimator_savedmodel): Export `Estimator` trained model for TPU inference.

[`infeed_dequeue(...)`](../../tf/contrib/tpu/infeed_dequeue): A placeholder op for a value that will be fed into the computation.

[`infeed_dequeue_tuple(...)`](../../tf/contrib/tpu/infeed_dequeue_tuple): A placeholder op for values fed into the TPU simultaneously as a tuple.

[`infeed_enqueue(...)`](../../tf/contrib/tpu/infeed_enqueue): An op which feeds a single Tensor value into the computation.

[`infeed_enqueue_tuple(...)`](../../tf/contrib/tpu/infeed_enqueue_tuple): Feeds multiple Tensor values into the computation as an XLA tuple.

[`initialize_system(...)`](../../tf/tpu/initialize_system): Initializes a distributed TPU system for use with TensorFlow.

[`keras_to_tpu_model(...)`](../../tf/contrib/tpu/keras_to_tpu_model): Copy `model` along with weights to the TPU. (deprecated)

[`outfeed_dequeue(...)`](../../tf/contrib/tpu/outfeed_dequeue): Retrieves a single tensor from the computation outfeed.

[`outfeed_dequeue_tuple(...)`](../../tf/contrib/tpu/outfeed_dequeue_tuple): Retrieve multiple values from the computation outfeed.

[`outfeed_enqueue(...)`](../../tf/contrib/tpu/outfeed_enqueue): Enqueue a Tensor on the computation outfeed.

[`outfeed_enqueue_tuple(...)`](../../tf/contrib/tpu/outfeed_enqueue_tuple): Enqueue multiple Tensor values on the computation outfeed.

[`outside_compilation(...)`](../../tf/tpu/outside_compilation): Builds part of a computation outside any current TPU replicate scope.

[`repeat(...)`](../../tf/contrib/tpu/repeat): Builds a training loop that executes a fixed number of iterations.

[`replicate(...)`](../../tf/tpu/replicate): Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](../../tf/tpu/rewrite): Rewrites `computation` for execution on a TPU system.

[`shard(...)`](../../tf/tpu/shard): Shards `computation` for parallel execution.

[`shutdown_system(...)`](../../tf/tpu/shutdown_system): Shuts down a running a distributed TPU system.

[`while_loop(...)`](../../tf/contrib/tpu/while_loop): Builds a training loop for TPUs.

