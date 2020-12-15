description: Library for running a computation across multiple devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.distribute

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Library for running a computation across multiple devices.


The intent of this library is that you can write an algorithm in a stylized way
and it will be usable with a variety of different <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>
implementations. Each descendant will implement a different strategy for
distributing the algorithm across multiple devices/machines.  Furthermore, these
changes can be hidden inside the specific layers and other library classes that
need special treatment to run in a distributed setting, so that most users'
model definition code can run unchanged. The <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> API works
the same way with eager and graph execution.

*Guides*

* [TensorFlow v2.x](https://www.tensorflow.org/guide/distributed_training)
* [TensorFlow v1.x](https://github.com/tensorflow/docs/blob/master/site/en/r1/guide/distribute_strategy.ipynb)

*Tutorials*

* [Distributed Training Tutorials](https://www.tensorflow.org/tutorials/distribute/)

  The tutorials cover how to use <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> to do distributed
  training with native Keras APIs, custom training loops,
  and Esitmator APIs. They also cover how to save/load model when using
  <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

*Glossary*

* _Data parallelism_ is where we run multiple copies of the model
  on different slices of the input data. This is in contrast to
  _model parallelism_ where we divide up a single copy of a model
  across multiple devices.
  Note: we only support data parallelism for now, but
  hope to add support for model parallelism in the future.
* A _device_ is a CPU or accelerator (e.g. GPUs, TPUs) on some machine that
  TensorFlow can run operations on (see e.g. <a href="../tf/device.md"><code>tf.device</code></a>). You may have multiple
  devices on a single machine, or be connected to devices on multiple
  machines. Devices used to run computations are called _worker devices_.
  Devices used to store variables are _parameter devices_. For some strategies,
  such as <a href="../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a>, the worker and parameter devices
  will be the same (see mirrored variables below). For others they will be
  different. For example, <a href="../tf/distribute/experimental/CentralStorageStrategy.md"><code>tf.distribute.experimental.CentralStorageStrategy</code></a>
  puts the variables on a single device (which may be a worker device or may be
  the CPU), and <a href="../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a> puts the
  variables on separate machines called _parameter servers_ (see below).
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
  <a href="../tf/distribute/experimental/ParameterServerStrategy.md"><code>tf.distribute.experimental.ParameterServerStrategy</code></a>). All replicas that want
  to operate on a variable retrieve it at the beginning of a step and send an
  update to be applied at the end of the step. These can in priniciple support
  either sync or async training, but right now we only have support for async
  training with parameter servers. Compare to
  <a href="../tf/distribute/experimental/CentralStorageStrategy.md"><code>tf.distribute.experimental.CentralStorageStrategy</code></a>, which puts all variables
  on a single device on the same machine (and does sync training), and
  <a href="../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a>, which mirrors variables to multiple devices
  (see below).

* _Replica context_ vs. _Cross-replica context_ vs _Update context_

  A _replica context_ applies
  when you execute the computation function that was called with `strategy.run`.
  Conceptually, you're in replica context when executing the computation
  function that is being replicated.

  An _update context_ is entered in a <a href="../tf/distribute/StrategyExtended.md#update"><code>tf.distribute.StrategyExtended.update</code></a>
  call.

  An _cross-replica context_ is entered when you enter a `strategy.scope`. This
  is useful for calling <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> methods which operate across
  the replicas (like `reduce_to()`). By default you start in a _replica context_
  (the "default single _replica context_") and then some methods can switch you
  back and forth.

* _Distributed value_: Distributed value is represented by the base class
  <a href="../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>. <a href="../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> is useful
  to represent values on multiple devices, and it contains a map from replica id
  to values. Two representative kinds of <a href="../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> are
  "PerReplica" and "Mirrored" values.

  "PerReplica" values exist on the worker
  devices, with a different value for each replica. They are produced by
  iterating through a distributed dataset returned by
  <a href="../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> and
  <a href="../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a>. They
  are also the typical result returned by
  <a href="../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a>.

  "Mirrored" values are like "PerReplica" values, except we know that the value
  on all replicas are the same. We can safely read a "Mirrored" value in a
  cross-replica context by using the value on any replica.

* _Unwrapping_ and _merging_: Consider calling a function `fn` on multiple
  replicas, like `strategy.run(fn, args=[w])` with an
  argument `w` that is a <a href="../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>. This means `w` will
  have a map taking replica id `0` to `w0`, replica id `1` to `w1`, etc.
  `strategy.run()` unwraps `w` before calling `fn`, so it calls `fn(w0)` on
  device `d0`, `fn(w1)` on device `d1`, etc.  It then merges the return
  values from `fn()`, which leads to one common object if the returned values
  are the same object from every replica, or a `DistributedValues` object
  otherwise.

* _Reductions_ and _all-reduce_: A _reduction_ is a method of aggregating
  multiple values into one value, like "sum" or "mean". If a strategy is doing
  sync training, we will perform a reduction on the gradients to a parameter
  from all replicas before applying the update. _All-reduce_ is an algorithm for
  performing a reduction on values from multiple devices and making the result
  available on all of those devices.

* _Mirrored variables_: These are variables that are created on multiple
  devices, where we keep the variables in sync by applying the same
  updates to every copy. Mirrored variables are created with
  <a href="../tf/Variable.md"><code>tf.Variable(...synchronization=tf.VariableSynchronization.ON_WRITE...)</code></a>.
  Normally they are only used in synchronous training.

* _SyncOnRead variables_

  _SyncOnRead variables_ are created by
  <a href="../tf/Variable.md"><code>tf.Variable(...synchronization=tf.VariableSynchronization.ON_READ...)</code></a>, and
  they are created on multiple devices. In replica context, each
  component variable on the local replica can perform reads and writes without
  synchronization with each other. When the
  _SyncOnRead variable_ is read in cross-replica context, the values from
  component variables are aggregated and returned.

  _SyncOnRead variables_ bring a lot of custom configuration difficulty to the
  underlying logic, so we do not encourage users to instantiate and use
  _SyncOnRead variable_ on their own. We have mainly used _SyncOnRead
  variables_ for use cases such as batch norm and metrics. For performance
  reasons, we often don't need to keep these statistics in sync every step and
  they can be accumulated on each replica independently. The only time we want
  to sync them is reporting or checkpointing, which typically happens in
  cross-replica context. _SyncOnRead variables_ are also often used by advanced
  users who want to control when variable values are aggregated. For example,
  users sometimes want to maintain gradients independently on each replica for a
  couple of steps without aggregation.

* _Distribute-aware layers_

  Layers are generally called in a replica context, except when defining a
  Keras functional model. <a href="../tf/distribute/in_cross_replica_context.md"><code>tf.distribute.in_cross_replica_context</code></a> will let you
  determine which case you are in. If in a replica context,
  the <a href="../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context</code></a> function will return the default
  replica context outside a strategy scope, `None` within a strategy scope, and
  a <a href="../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> object inside a strategy scope and within a
  <a href="../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> function. The `ReplicaContext` object has an
  `all_reduce` method for aggregating across all replicas.


Note that we provide a default version of <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> that is
used when no other strategy is in scope, that provides the same API with
reasonable default behavior.

## Modules

[`cluster_resolver`](../tf/distribute/cluster_resolver.md) module: Library imports for ClusterResolvers.

[`experimental`](../tf/distribute/experimental.md) module: Public API for tf.distribute.experimental namespace.

## Classes

[`class CrossDeviceOps`](../tf/distribute/CrossDeviceOps.md): Base class for cross-device reduction and broadcasting algorithms.

[`class DistributedDataset`](../tf/distribute/DistributedDataset.md): Represents a dataset distributed among devices and machines.

[`class DistributedIterator`](../tf/distribute/DistributedIterator.md): An iterator over <a href="../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

[`class DistributedValues`](../tf/distribute/DistributedValues.md): Base class for representing distributed values.

[`class HierarchicalCopyAllReduce`](../tf/distribute/HierarchicalCopyAllReduce.md): Hierarchical copy all-reduce implementation of CrossDeviceOps.

[`class InputContext`](../tf/distribute/InputContext.md): A class wrapping information needed by an input function.

[`class InputOptions`](../tf/distribute/InputOptions.md): Run options for `experimental_distribute_dataset(s_from_function)`.

[`class InputReplicationMode`](../tf/distribute/InputReplicationMode.md): Replication mode for input function.

[`class MirroredStrategy`](../tf/distribute/MirroredStrategy.md): Synchronous training across multiple replicas on one machine.

[`class MultiWorkerMirroredStrategy`](../tf/distribute/MultiWorkerMirroredStrategy.md): A distribution strategy for synchronous training on multiple workers.

[`class NcclAllReduce`](../tf/distribute/NcclAllReduce.md): NCCL all-reduce implementation of CrossDeviceOps.

[`class OneDeviceStrategy`](../tf/distribute/OneDeviceStrategy.md): A distribution strategy for running on a single device.

[`class ReduceOp`](../tf/distribute/ReduceOp.md): Indicates how a set of values should be reduced.

[`class ReductionToOneDevice`](../tf/distribute/ReductionToOneDevice.md): A CrossDeviceOps implementation that copies values to one device to reduce.

[`class ReplicaContext`](../tf/distribute/ReplicaContext.md): A class with a collection of APIs that can be called in a replica context.

[`class RunOptions`](../tf/distribute/RunOptions.md): Run options for `strategy.run`.

[`class Server`](../tf/distribute/Server.md): An in-process TensorFlow server, for use in distributed training.

[`class Strategy`](../tf/distribute/Strategy.md): A state & compute distribution policy on a list of devices.

[`class StrategyExtended`](../tf/distribute/StrategyExtended.md): Additional APIs for algorithms that need to be distribution-aware.

[`class TPUStrategy`](../tf/distribute/TPUStrategy.md): Synchronous training on TPUs and TPU Pods.

## Functions

[`experimental_set_strategy(...)`](../tf/distribute/experimental_set_strategy.md): Set a <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> as current without `with strategy.scope()`.

[`get_replica_context(...)`](../tf/distribute/get_replica_context.md): Returns the current <a href="../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> or `None`.

[`get_strategy(...)`](../tf/distribute/get_strategy.md): Returns the current <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> object.

[`has_strategy(...)`](../tf/distribute/has_strategy.md): Return if there is a current non-default <a href="../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>.

[`in_cross_replica_context(...)`](../tf/distribute/in_cross_replica_context.md): Returns `True` if in a cross-replica context.

