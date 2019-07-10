page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.tpu



<!-- Placeholder for "Used in" -->


## Modules

[`experimental`](../tf/tpu/experimental) module

## Classes

[`class CrossShardOptimizer`](../tf/tpu/CrossShardOptimizer): An optimizer that averages gradients across TPU shards.

## Functions

[`batch_parallel(...)`](../tf/tpu/batch_parallel): Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](../tf/tpu/bfloat16_scope): Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](../tf/tpu/core): Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](../tf/tpu/cross_replica_sum): Sum the input tensor across replicas according to group_assignment.

[`initialize_system(...)`](../tf/tpu/initialize_system): Initializes a distributed TPU system for use with TensorFlow.

[`outside_compilation(...)`](../tf/tpu/outside_compilation): Builds part of a computation outside any current TPU replicate scope.

[`replicate(...)`](../tf/tpu/replicate): Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](../tf/tpu/rewrite): Rewrites `computation` for execution on a TPU system.

[`shard(...)`](../tf/tpu/shard): Shards `computation` for parallel execution.

[`shutdown_system(...)`](../tf/tpu/shutdown_system): Shuts down a running a distributed TPU system.

