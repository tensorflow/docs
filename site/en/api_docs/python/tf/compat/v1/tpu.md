description: Ops related to Tensor Processing Units.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.tpu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Ops related to Tensor Processing Units.



## Modules

[`experimental`](../../../tf/compat/v1/tpu/experimental.md) module: Public API for tf.tpu.experimental namespace.

## Classes

[`class CrossShardOptimizer`](../../../tf/compat/v1/tpu/CrossShardOptimizer.md): An optimizer that averages gradients across TPU shards.

[`class PaddingSpec`](../../../tf/compat/v1/tpu/PaddingSpec.md): Represents the type of padding policies for tpu.replicate.

## Functions

[`batch_parallel(...)`](../../../tf/compat/v1/tpu/batch_parallel.md): Shards `computation` along the batch dimension for parallel execution.

[`bfloat16_scope(...)`](../../../tf/compat/v1/tpu/bfloat16_scope.md): Scope class for bfloat16 variables so that the model uses custom getter.

[`core(...)`](../../../tf/compat/v1/tpu/core.md): Returns the device name for a core in a replicated TPU computation.

[`cross_replica_sum(...)`](../../../tf/compat/v1/tpu/cross_replica_sum.md): Sum the input tensor across replicas according to group_assignment.

[`initialize_system(...)`](../../../tf/compat/v1/tpu/initialize_system.md): Initializes a distributed TPU system for use with TensorFlow.

[`outside_compilation(...)`](../../../tf/compat/v1/tpu/outside_compilation.md): Builds part of a computation outside any current TPU replicate scope.

[`replicate(...)`](../../../tf/compat/v1/tpu/replicate.md): Builds a graph operator that runs a replicated TPU computation.

[`rewrite(...)`](../../../tf/compat/v1/tpu/rewrite.md): Rewrites `computation` for execution on a TPU system.

[`shard(...)`](../../../tf/compat/v1/tpu/shard.md): Shards `computation` for parallel execution.

[`shutdown_system(...)`](../../../tf/compat/v1/tpu/shutdown_system.md): Shuts down a running a distributed TPU system.

