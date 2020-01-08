page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.distribute



Defined in [`tensorflow/contrib/distribute/__init__.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/distribute/__init__.py).

A distributed computation library for TF.

See [tensorflow/contrib/distribute/README.md](
https://www.github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/distribute/README.md)
for overview and examples.

## Classes

[`class AllReduceCrossTowerOps`](../../tf/contrib/distribute/AllReduceCrossTowerOps): Reduction using all reduce.

[`class CollectiveAllReduceStrategy`](../../tf/contrib/distribute/CollectiveAllReduceStrategy): Distribution strategy that uses collective ops for all-reduce.

[`class CrossTowerOps`](../../tf/contrib/distribute/CrossTowerOps): Base class for cross-tower reduction and broadcasting algorithms.

[`class DistributeConfig`](../../tf/contrib/distribute/DistributeConfig): A config tuple for distribution strategies.

[`class DistributionStrategy`](../../tf/contrib/distribute/DistributionStrategy): A list of devices with a state & compute distribution policy.

[`class MirroredStrategy`](../../tf/contrib/distribute/MirroredStrategy): Mirrors vars to distribute across multiple devices and machines.

[`class Monitor`](../../tf/contrib/distribute/Monitor): Executes training steps, recovers and checkpoints.

[`class OneDeviceStrategy`](../../tf/contrib/distribute/OneDeviceStrategy): A distribution strategy for running on a single device.

[`class ParameterServerStrategy`](../../tf/contrib/distribute/ParameterServerStrategy): A parameter server DistributionStrategy.

[`class ReductionToOneDeviceCrossTowerOps`](../../tf/contrib/distribute/ReductionToOneDeviceCrossTowerOps): Always do reduction to one device first and then do broadcasting.

[`class StandardInputStep`](../../tf/contrib/distribute/StandardInputStep): Step with a standard implementation of input handling.

[`class StandardSingleLossStep`](../../tf/contrib/distribute/StandardSingleLossStep): A step function that implements a training step for a feed forward network.

[`class Step`](../../tf/contrib/distribute/Step): Interface for performing each step of a training algorithm.

[`class TPUStrategy`](../../tf/contrib/distribute/TPUStrategy): Experimental TPU distribution strategy implementation.

[`class TowerContext`](../../tf/contrib/distribute/TowerContext): DistributionStrategy API inside a `call_for_each_tower()` call.

[`class UpdateContext`](../../tf/contrib/distribute/UpdateContext): Context manager when you are in `update()` or `update_non_slot()`.

## Functions

[`get_cross_tower_context(...)`](../../tf/contrib/distribute/get_cross_tower_context): Returns the current DistributionStrategy if in a cross-tower context.

[`get_distribution_strategy(...)`](../../tf/contrib/distribute/get_distribution_strategy): Returns the current `DistributionStrategy` object.

[`get_loss_reduction(...)`](../../tf/contrib/distribute/get_loss_reduction): Reduce `aggregation` corresponding to the last loss reduction.

[`get_tower_context(...)`](../../tf/contrib/distribute/get_tower_context): Returns the current TowerContext or None if in a cross-tower context.

[`has_distribution_strategy(...)`](../../tf/contrib/distribute/has_distribution_strategy): Return if there is a current non-default `DistributionStrategy`.

[`require_tower_context(...)`](../../tf/contrib/distribute/require_tower_context): Verify in `tower_ctx` tower context.

[`run_standard_tensorflow_server(...)`](../../tf/contrib/distribute/run_standard_tensorflow_server): Starts a standard TensorFlow server.

