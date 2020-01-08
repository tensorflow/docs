

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.tpu



Defined in [`tensorflow/contrib/tpu/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/tpu/__init__.py).

Ops related to Tensor Processing Units.









## Modules

[`profiler`](../../tf/contrib/tpu/profiler) module: Classes for TPU trace events.

## Classes

[`class CrossShardOptimizer`](../../tf/contrib/tpu/CrossShardOptimizer): An optimizer that averages gradients across TPU shards.

[`class DeviceAssignment`](../../tf/contrib/tpu/DeviceAssignment): Mapping from logical cores in a computation to the physical TPU topology.

[`class InfeedQueue`](../../tf/contrib/tpu/InfeedQueue): A helper object to build a device infeed queue.

[`class InputPipelineConfig`](../../tf/contrib/tpu/InputPipelineConfig): Please see the definition of these values in TPUConfig.

[`class RunConfig`](../../tf/contrib/tpu/RunConfig): RunConfig with TPU support.

[`class TPUConfig`](../../tf/contrib/tpu/TPUConfig): TPU related configuration required by `TPUEstimator`.

[`class TPUEstimator`](../../tf/contrib/tpu/TPUEstimator): Estimator with TPU support.

[`class TPUEstimatorSpec`](../../tf/contrib/tpu/TPUEstimatorSpec): Ops and objects returned from a `model_fn` and passed to `TPUEstimator`.

[`class Topology`](../../tf/contrib/tpu/Topology): Describes a set of TPU devices.

## Functions

[`batch_parallel(...)`](../../tf/contrib/tpu/batch_parallel): Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](../../tf/contrib/tpu/bfloat16_scope): Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](../../tf/contrib/tpu/core): Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](../../tf/contrib/tpu/cross_replica_sum): An Op to sum inputs across replicated TPU instances. Each

[`device_assignment(...)`](../../tf/contrib/tpu/device_assignment): Computes a device_assignment of a computation across a TPU topology.

[`infeed_dequeue(...)`](../../tf/contrib/tpu/infeed_dequeue): A placeholder op for a value that will be fed into the computation.

[`infeed_dequeue_tuple(...)`](../../tf/contrib/tpu/infeed_dequeue_tuple): A placeholder op for values fed into the TPU simultaneously as a tuple.

[`initialize_system(...)`](../../tf/contrib/tpu/initialize_system): Initializes a distributed TPU system for use with TensorFlow.

[`outfeed_enqueue(...)`](../../tf/contrib/tpu/outfeed_enqueue): An op which emits a single Tensor value from an XLA computation.

[`outfeed_enqueue_tuple(...)`](../../tf/contrib/tpu/outfeed_enqueue_tuple): An op which emits multiple Tensor values from an XLA computation.

[`repeat(...)`](../../tf/contrib/tpu/repeat): Builds a training loop that executes a fixed number of iterations.

[`replicate(...)`](../../tf/contrib/tpu/replicate): Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](../../tf/contrib/tpu/rewrite): Rewrites `computation` for execution on a TPU system.

[`shard(...)`](../../tf/contrib/tpu/shard): Shards `computation` for parallel execution.

[`shutdown_system(...)`](../../tf/contrib/tpu/shutdown_system): Shuts down a running a distributed TPU system.

[`while_loop(...)`](../../tf/contrib/tpu/while_loop): Builds a training loop for TPUs.

