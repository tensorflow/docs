page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.distribute





Library for running a computation across multiple devices.

## Classes

[`class InputContext`](../tf/distribute/InputContext): A class wrapping information needed by an input function.

[`class InputReplicationMode`](../tf/distribute/InputReplicationMode): Replication mode for input function.

[`class MirroredStrategy`](../tf/distribute/MirroredStrategy): Mirrors vars to distribute across multiple devices and machines.

[`class ReduceOp`](../tf/distribute/ReduceOp): Indicates how a set of values should be reduced.

[`class ReplicaContext`](../tf/distribute/ReplicaContext): <a href="../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> API when in a replica context.

[`class Server`](../tf/distribute/Server): An in-process TensorFlow server, for use in distributed training.

[`class Strategy`](../tf/distribute/Strategy): A list of devices with a state & compute distribution policy.

[`class StrategyExtended`](../tf/distribute/StrategyExtended): Additional APIs for algorithms that need to be distribution-aware.

## Functions

[`get_loss_reduction(...)`](../tf/distribute/get_loss_reduction): <a href="../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

[`get_replica_context(...)`](../tf/distribute/get_replica_context): Returns the current <a href="../tf/distribute/ReplicaContext"><code>tf.distribute.ReplicaContext</code></a> or `None`.

[`get_strategy(...)`](../tf/distribute/get_strategy): Returns the current <a href="../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> object.

[`has_strategy(...)`](../tf/distribute/has_strategy): Return if there is a current non-default <a href="../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a>.

[`in_cross_replica_context(...)`](../tf/distribute/in_cross_replica_context): Returns True if in a cross-replica context.

