page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.distribute



Defined in [`tensorflow/contrib/distribute/__init__.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/distribute/__init__.py).

A distributed computation library for TF.

See [tensorflow/contrib/distribute/README.md](
https://www.github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/distribute/README.md)
for overview and examples.

## Classes

[`class AllReduceCrossDeviceOps`](../../tf/contrib/distribute/AllReduceCrossDeviceOps): Reduction using all reduce.

[`class CollectiveAllReduceStrategy`](../../tf/contrib/distribute/CollectiveAllReduceStrategy): Distribution strategy that uses collective ops for all-reduce.

[`class CrossDeviceOps`](../../tf/contrib/distribute/CrossDeviceOps): Base class for cross-device reduction and broadcasting algorithms.

[`class DistributeConfig`](../../tf/contrib/distribute/DistributeConfig): A config tuple for distribution strategies.

[`class DistributionStrategy`](../../tf/distribute/Strategy): A list of devices with a state & compute distribution policy.

[`class DistributionStrategyExtended`](../../tf/distribute/StrategyExtended): Additional APIs for algorithms that need to be distribution-aware.

[`class MirroredStrategy`](../../tf/contrib/distribute/MirroredStrategy): Mirrors vars to distribute across multiple devices and machines.

[`class Monitor`](../../tf/contrib/distribute/Monitor): Executes training steps, recovers and checkpoints.

[`class MultiWorkerAllReduce`](../../tf/contrib/distribute/MultiWorkerAllReduce): All-reduce algorithms for distributed TensorFlow.

[`class OneDeviceStrategy`](../../tf/contrib/distribute/OneDeviceStrategy): A distribution strategy for running on a single device.

[`class ParameterServerStrategy`](../../tf/contrib/distribute/ParameterServerStrategy): A parameter server DistributionStrategy.

[`class ReductionToOneDeviceCrossDeviceOps`](../../tf/contrib/distribute/ReductionToOneDeviceCrossDeviceOps): Always do reduction to one device first and then do broadcasting.

[`class ReplicaContext`](../../tf/distribute/ReplicaContext): <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> API when in a replica context.

[`class StandardInputStep`](../../tf/contrib/distribute/StandardInputStep): Step with a standard implementation of input handling.

[`class StandardSingleLossStep`](../../tf/contrib/distribute/StandardSingleLossStep): A step function that implements a training step for a feed forward network.

[`class Step`](../../tf/contrib/distribute/Step): Interface for performing each step of a training algorithm.

[`class TPUStrategy`](../../tf/contrib/distribute/TPUStrategy): TPU distribution strategy implementation.

[`class UpdateContext`](../../tf/contrib/distribute/UpdateContext): Context manager when you are in `update()` or `update_non_slot()`.

## Functions

[`get_cross_replica_context(...)`](../../tf/contrib/distribute/get_cross_replica_context): Returns the current tf.distribute.Strategy if in a cross-replica context.

[`get_distribution_strategy(...)`](../../tf/distribute/get_strategy): Returns the current <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.

[`get_loss_reduction(...)`](../../tf/distribute/get_loss_reduction): <a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

[`get_replica_context(...)`](../../tf/distribute/get_replica_context): Returns the current <a href="../../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> or `None`.

[`has_distribution_strategy(...)`](../../tf/distribute/has_strategy): Return if there is a current non-default <a href="../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

[`in_cross_replica_context(...)`](../../tf/distribute/in_cross_replica_context): Returns True if in a cross-replica context.

[`require_replica_context(...)`](../../tf/contrib/distribute/require_replica_context): Verify in `replica_ctx` replica context.

[`run_standard_tensorflow_server(...)`](../../tf/contrib/distribute/run_standard_tensorflow_server): Starts a standard TensorFlow server.

