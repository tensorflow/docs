description: Library for running a computation across multiple devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.distribute

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Library for running a computation across multiple devices.


See the guide for overview and examples:
[TensorFlow v2.x](https://www.tensorflow.org/guide/distributed_training),
[TensorFlow v1.x](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/distribute_strategy.ipynb).  

The intent of this library is that you can write an algorithm in a stylized way
and it will be usable with a variety of different <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>
implementations. Each descendant will implement a different strategy for
distributing the algorithm across multiple devices/machines.  Furthermore, these
changes can be hidden inside the specific layers and other library classes that
need special treatment to run in a distributed setting, so that most users'
model definition code can run unchanged. The <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> API works
the same way with eager and graph execution.

*Glossary*

* _Data parallelism_ is where we run multiple copies of the model
  on different slices of the input data. This is in contrast to
  _model parallelism_ where we divide up a single copy of a model
  across multiple devices.
  Note: we only support data parallelism for now, but
  hope to add support for model parallelism in the future.
* A _device_ is a CPU or accelerator (e.g. GPUs, TPUs) on some machine that
  TensorFlow can run operations on (see e.g. <a href="../../../tf/device.md"><code>tf.device</code></a>). You may have multiple
  devices on a single machine, or be connected to devices on multiple
  machines. Devices used to run computations are called _worker devices_.
  Devices used to store variables are _parameter devices_. For some strategies,
  such as <a href="../../../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a>, the worker and parameter devices
  will be the same (see mirrored variables below). For others they will be
  different.  For example, <a href="../../../tf/distribute/experimental/CentralStorageStrategy.md"><code>tf.distribute.experimental.CentralStorageStrategy</code></a>
  puts the variables on a single device (which may be a worker device or may be
  the CPU), and <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> puts the
  variables on separate machines called parameter servers (see below).
* A _replica_ is one copy of the model, running on one slice of the
  input data. Right now each replica is executed on its own
  worker device, but once we add support for model parallelism
  a replica may span multiple worker devices.
* A _host_ is the CPU device on a machine with worker devices, typically
  used for running input pipelines.
* A _worker_ is defined to be the physical machine(s) containing the physical
  devices (e.g. GPUs, TPUs) on which the replicated computation is executed. A
  worker may contain one or more replicas, but contains at least one
  replica. Typically one worker will correspond to one machine, but in the case
  of very large models with model parallelism, one worker may span multiple
  machines. We typically run one input pipeline per worker, feeding all the
  replicas on that worker.
* _Synchronous_, or more commonly _sync_, training is where the updates from
  each replica are aggregated together before updating the model variables. This
  is in contrast to _asynchronous_, or _async_ training, where each replica
  updates the model variables independently. You may also have replicas
  partitioned into groups which are in sync within each group but async between
  groups.
* _Parameter servers_: These are machines that hold a single copy of
  parameters/variables, used by some strategies (right now just
  <a href="../../../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>). All replicas that want
  to operate on a variable retrieve it at the beginning of a step and send an
  update to be applied at the end of the step. These can in priniciple support
  either sync or async training, but right now we only have support for async
  training with parameter servers. Compare to
  <a href="../../../tf/distribute/experimental/CentralStorageStrategy.md"><code>tf.distribute.experimental.CentralStorageStrategy</code></a>, which puts all variables
  on a single device on the same machine (and does sync training), and
  <a href="../../../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a>, which mirrors variables to multiple devices
  (see below).
* _Mirrored variables_: These are variables that are copied to multiple
  devices, where we keep the copies in sync by applying the same
  updates to every copy. Normally would only be used with sync training.
* Reductions and all-reduce: A _reduction_ is some method of aggregating
  multiple values into one value, like "sum" or "mean". If a strategy is doing
  sync training, we will perform a reduction on the gradients to a parameter
  from all replicas before applying the update. _All-reduce_ is an algorithm for
  performing a reduction on values from multiple devices and making the result
  available on all of those devices.

Note that we provide a default version of <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> that is
used when no other strategy is in scope, that provides the same API with
reasonable default behavior.

## Modules

[`cluster_resolver`](../../../tf/compat/v1/distribute/cluster_resolver.md) module: Library imports for ClusterResolvers.

[`experimental`](../../../tf/compat/v1/distribute/experimental.md) module: Experimental Distribution Strategy library.

## Classes

[`class CrossDeviceOps`](../../../tf/distribute/CrossDeviceOps.md): Base class for cross-device reduction and broadcasting algorithms.

[`class HierarchicalCopyAllReduce`](../../../tf/distribute/HierarchicalCopyAllReduce.md): Reduction using hierarchical copy all-reduce.

[`class InputContext`](../../../tf/distribute/InputContext.md): A class wrapping information needed by an input function.

[`class InputReplicationMode`](../../../tf/distribute/InputReplicationMode.md): Replication mode for input function.

[`class MirroredStrategy`](../../../tf/compat/v1/distribute/MirroredStrategy.md): Synchronous training across multiple replicas on one machine.

[`class NcclAllReduce`](../../../tf/distribute/NcclAllReduce.md): Reduction using NCCL all-reduce.

[`class OneDeviceStrategy`](../../../tf/compat/v1/distribute/OneDeviceStrategy.md): A distribution strategy for running on a single device.

[`class ReduceOp`](../../../tf/distribute/ReduceOp.md): Indicates how a set of values should be reduced.

[`class ReductionToOneDevice`](../../../tf/distribute/ReductionToOneDevice.md): Always do reduction to one device first and then do broadcasting.

[`class ReplicaContext`](../../../tf/distribute/ReplicaContext.md): <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> API when in a replica context.

[`class RunOptions`](../../../tf/distribute/RunOptions.md): Run options for `strategy.run`.

[`class Server`](../../../tf/distribute/Server.md): An in-process TensorFlow server, for use in distributed training.

[`class Strategy`](../../../tf/compat/v1/distribute/Strategy.md): A list of devices with a state & compute distribution policy.

[`class StrategyExtended`](../../../tf/compat/v1/distribute/StrategyExtended.md): Additional APIs for algorithms that need to be distribution-aware.

## Functions

[`experimental_set_strategy(...)`](../../../tf/distribute/experimental_set_strategy.md): Set a <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> as current without `with strategy.scope()`.

[`get_loss_reduction(...)`](../../../tf/compat/v1/distribute/get_loss_reduction.md): <a href="../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

[`get_replica_context(...)`](../../../tf/distribute/get_replica_context.md): Returns the current <a href="../../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> or `None`.

[`get_strategy(...)`](../../../tf/distribute/get_strategy.md): Returns the current <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object.

[`has_strategy(...)`](../../../tf/distribute/has_strategy.md): Return if there is a current non-default <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

[`in_cross_replica_context(...)`](../../../tf/distribute/in_cross_replica_context.md): Returns `True` if in a cross-replica context.

