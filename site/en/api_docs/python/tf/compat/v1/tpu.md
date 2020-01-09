page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v1.tpu


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Ops related to Tensor Processing Units.

<!-- Placeholder for "Used in" -->


## Modules

[`experimental`](../../../tf/compat/v1/tpu/experimental) module: Public API for tf.tpu.experimental namespace.

## Classes

[`class CrossShardOptimizer`](../../../tf/compat/v1/tpu/CrossShardOptimizer): An optimizer that averages gradients across TPU shards.

## Functions

[`batch_parallel(...)`](../../../tf/compat/v1/tpu/batch_parallel): Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](../../../tf/compat/v1/tpu/bfloat16_scope): Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](../../../tf/compat/v1/tpu/core): Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](../../../tf/compat/v1/tpu/cross_replica_sum): Sum the input tensor across replicas according to group_assignment.

[`initialize_system(...)`](../../../tf/compat/v1/tpu/initialize_system): Initializes a distributed TPU system for use with TensorFlow.

[`outside_compilation(...)`](../../../tf/compat/v1/tpu/outside_compilation): Builds part of a computation outside any current TPU replicate scope.

[`replicate(...)`](../../../tf/compat/v1/tpu/replicate): Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](../../../tf/compat/v1/tpu/rewrite): Rewrites `computation` for execution on a TPU system.

[`shard(...)`](../../../tf/compat/v1/tpu/shard): Shards `computation` for parallel execution.

[`shutdown_system(...)`](../../../tf/compat/v1/tpu/shutdown_system): Shuts down a running a distributed TPU system.
