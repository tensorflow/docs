page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.MirroredStrategy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/mirrored_strategy.py#L31-L124">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MirroredStrategy`

Mirrors vars to distribute across multiple devices and machines.

Inherits From: [`Strategy`](../../../tf/distribute/Strategy)

<!-- Placeholder for "Used in" -->

*** contrib version ***

This strategy uses one replica per device and sync replication for its
multi-GPU version.

When `cluster_spec` is given by the `configure` method., it turns into the
mulit-worker version that works on multiple workers with in-graph replication.
Note: `configure` will be called by higher-level APIs if running in
distributed environment.

There are several important concepts for distributed TensorFlow, e.g.
`client`, `job`, `task`, `cluster`, `in-graph replication` and
`synchronous training` and they have already been defined in the
[TensorFlow's documentation](https://www.tensorflow.org/deploy/distributed).
The distribution strategy inherits these concepts as well and in addition to
that we also clarify several more concepts:

* **In-graph replication**: the `client` creates a single <a href="../../../tf/Graph"><code>tf.Graph</code></a> that
  specifies tasks for devices on all workers. The `client` then creates a
  client session which will talk to the `master` service of a `worker`. Then
  the `master` will partition the graph and distribute the work to all
  participating workers.
* **Worker**: A `worker` is a TensorFlow `task` that usually maps to one
  physical machine. We will have multiple `worker`s with different `task`
  index. They all do similar things except for one worker checkpointing model
  variables, writing summaries, etc. in addition to its ordinary work.

The multi-worker version of this class maps one replica to one device on a
worker. It mirrors all model variables on all replicas. For example, if you
have two `worker`s and each `worker` has 4 GPUs, it will create 8 copies of
the model variables on these 8 GPUs. Then like in MirroredStrategy, each
replica performs their computation with their own copy of variables unless in
cross-replica model where variable or tensor reduction happens.

#### Args:


* <b>`devices`</b>: a list of device strings.
* <b>`num_gpus`</b>: number of GPUs. For local training, either specify `devices` or
  `num_gpus`. In distributed training, this must be specified as number of
  GPUs on each worker.
* <b>`num_gpus_per_worker`</b>: number of GPUs per worker. This is the same as
  `num_gpus` and only one of `num_gpus` and `num_gpus_per_worker` can be
  specified.
* <b>`cross_device_ops`</b>: optional, a descedant of `CrossDeviceOps`. If this is not
  set, the `configure` method will try to find the best one.
* <b>`auto_shard_dataset`</b>: whether to auto-shard the dataset when there are
  multiple workers.
* <b>`cross_tower_ops`</b>: Deprecated alias for `cross_device_ops`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/mirrored_strategy.py#L83-L99">View source</a>

``` python
__init__(
    devices=None,
    num_gpus=None,
    num_gpus_per_worker=None,
    cross_device_ops=None,
    auto_shard_dataset=False,
    cross_tower_ops=None
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="extended"><code>extended</code></h3>

<a href="../../../tf/distribute/StrategyExtended"><code>tf.distribute.StrategyExtended</code></a> with additional methods.


<h3 id="num_replicas_in_sync"><code>num_replicas_in_sync</code></h3>

Returns number of replicas over which gradients are aggregated.




## Methods

<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L614-L678">View source</a>

``` python
experimental_distribute_dataset(dataset)
```

Distributes a tf.data.Dataset instance provided via `dataset`.

The returned distributed dataset can be iterated over similar to how
regular datasets can.
NOTE: Currently, the user cannot add any more transformations to a
distributed dataset.

The following is an example:

```python
strategy = tf.distribute.MirroredStrategy()

# Create a dataset
dataset = dataset_ops.Dataset.TFRecordDataset([
  "/a/1.tfr", "/a/2.tfr", "/a/3.tfr", "/a/4.tfr"])

# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(dataset)
# Iterate over the distributed dataset
for x in dist_dataset:
  # process dataset elements
  strategy.experimental_run_v2(train_step, args=(x,))
```

We will assume that the input dataset is batched by the
global batch size. With this assumption, we will make a best effort to
divide each batch across all the replicas (one or more workers).

In a multi-worker setting, we will first attempt to distribute the dataset
by attempting to detect whether the dataset is being created out of
ReaderDatasets (e.g. TFRecordDataset, TextLineDataset, etc.) and if so,
attempting to shard the input files. Note that there has to be at least one
input file per worker. If you have less than one input file per worker, we
suggest that you should disable distributing your dataset using the method
below.

If that attempt is unsuccessful (e.g. the dataset is created from a
Dataset.range), we will shard the dataset evenly at the end by appending a
`.shard` operation to the end of the processing pipeline. This will cause
the entire preprocessing pipeline for all the data to be run on every
worker, and each worker will do redundant work. We will print a warning
if this method of sharding is selected. In this case, consider using
`experimental_distribute_datasets_from_function` instead.

You can disable dataset sharding across workers using the `auto_shard`
option in <a href="../../../tf/data/experimental/DistributeOptions"><code>tf.data.experimental.DistributeOptions</code></a>.

Within each worker, we will also split the data among all the worker
devices (if more than one a present), and this will happen even if
multi-worker sharding is disabled using the method above.

If the above batch splitting and dataset sharding logic is undesirable,
please use `experimental_distribute_datasets_from_function` instead, which
does not do any automatic splitting or sharding.

#### Args:


* <b>`dataset`</b>: <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> that will be sharded across all replicas using
  the rules stated above.


#### Returns:

A "distributed `Dataset`", which acts like a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> except
it produces "per-replica" values.


<h3 id="experimental_distribute_datasets_from_function"><code>experimental_distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L680-L728">View source</a>

``` python
experimental_distribute_datasets_from_function(dataset_fn)
```

Distributes <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

`dataset_fn` will be called once for each worker in the strategy. Each
replica on that worker will dequeue one batch of inputs from the local
`Dataset` (i.e. if a worker has two replicas, two batches will be dequeued
from the `Dataset` every step).

This method can be used for several purposes. For example, where
`experimental_distribute_dataset` is unable to shard the input files, this
method might be used to manually shard the dataset (avoiding the slow
fallback behavior in `experimental_distribute_dataset`). In cases where the
dataset is infinite, this sharding can be done by creating dataset replicas
that differ only in their random seed.
`experimental_distribute_dataset` may also sometimes fail to split the
batch across replicas on a worker. In that case, this method can be used
where that limitation does not exist.

The `dataset_fn` should take an <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed:

```
def dataset_fn(input_context):
  batch_size = input_context.get_per_replica_batch_size(global_batch_size)
  d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
  return d.shard(
      input_context.num_input_pipelines, input_context.input_pipeline_id)

inputs = strategy.experimental_distribute_datasets_from_function(dataset_fn)

for batch in inputs:
  replica_results = strategy.experimental_run_v2(replica_fn, args=(batch,))
```

IMPORTANT: The <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size.  This may be computed using
`input_context.get_per_replica_batch_size`.

#### Args:


* <b>`dataset_fn`</b>: A function taking a <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> instance and
  returning a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.


#### Returns:

A "distributed `Dataset`", which acts like a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> except
it produces "per-replica" values.


<h3 id="experimental_local_results"><code>experimental_local_results</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L887-L904">View source</a>

``` python
experimental_local_results(value)
```

Returns the list of all local per-replica values contained in `value`.

Note: This only returns values on the worker initiated by this client.
When using a <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> like
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>, each worker
will be its own client, and this function will only return values
computed on that worker.

#### Args:


* <b>`value`</b>: A value returned by `experimental_run()`, `experimental_run_v2()`,
  `extended.call_for_each_replica()`, or a variable created in `scope`.


#### Returns:

A tuple of values contained in `value`. If `value` represents a single
value, this returns `(value,).`


<h3 id="experimental_make_numpy_dataset"><code>experimental_make_numpy_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L1052-L1081">View source</a>

``` python
experimental_make_numpy_dataset(
    numpy_input,
    session=None
)
```

Makes a tf.data.Dataset for input provided via a numpy array.

This avoids adding `numpy_input` as a large constant in the graph,
and copies the data to the machine or machines that will be processing
the input.

Note that you will likely need to use
tf.distribute.Strategy.experimental_distribute_dataset
with the returned dataset to further distribute it with the strategy.

#### Example:


```
numpy_input = np.ones([10], dtype=np.float32)
dataset = strategy.experimental_make_numpy_dataset(numpy_input)
dist_dataset = strategy.experimental_distribute_dataset(dataset)
```

#### Args:


* <b>`numpy_input`</b>: A nest of NumPy input arrays that will be converted into a
dataset. Note that lists of Numpy arrays are stacked, as that is normal
<a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> behavior.
* <b>`session`</b>: (TensorFlow v1.x graph execution only) A session used for
  initialization.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> representing `numpy_input`.


<h3 id="experimental_run"><code>experimental_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L1083-L1116">View source</a>

``` python
experimental_run(
    fn,
    input_iterator=None
)
```

Runs ops in `fn` on each replica, with inputs from `input_iterator`.

DEPRECATED: This method is not available in TF 2.x. Please switch
to using `experimental_run_v2` instead.

When eager execution is enabled, executes ops specified by `fn` on each
replica. Otherwise, builds a graph to execute the ops on each replica.

Each replica will take a single, different input from the inputs provided by
one `get_next` call on the input iterator.

`fn` may call <a href="../../../tf/distribute/get_replica_context"><code>tf.distribute.get_replica_context()</code></a> to access members such
as `replica_id_in_sync_group`.

IMPORTANT: Depending on the <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> implementation being
used, and whether eager execution is enabled, `fn` may be called one or more
times (once for each replica).

#### Args:


* <b>`fn`</b>: The function to run. The inputs to the function must match the outputs
  of `input_iterator.get_next()`. The output must be a <a href="../../../tf/nest"><code>tf.nest</code></a> of
  `Tensor`s.
* <b>`input_iterator`</b>: (Optional) input iterator from which the inputs are taken.


#### Returns:

Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be `PerReplica` (if the values are unsynchronized),
`Mirrored` (if the values are kept in sync), or `Tensor` (if running on a
single replica).


<h3 id="experimental_run_v2"><code>experimental_run_v2</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L730-L764">View source</a>

``` python
experimental_run_v2(
    fn,
    args=(),
    kwargs=None
)
```

Run `fn` on each replica, with the given arguments.

Executes ops specified by `fn` on each replica. If `args` or `kwargs` have
"per-replica" values, such as those produced by a "distributed `Dataset`",
when `fn` is executed on a particular replica, it will be executed with the
component of those "per-replica" values that correspond to that replica.

`fn` may call <a href="../../../tf/distribute/get_replica_context"><code>tf.distribute.get_replica_context()</code></a> to access members such
as `all_reduce`.

All arguments in `args` or `kwargs` should either be nest of tensors or
per-replica objects containing tensors or composite tensors.

IMPORTANT: Depending on the implementation of <a href="../../../tf/distribute/Strategy"><code>tf.distribute.Strategy</code></a> and
whether eager execution is enabled, `fn` may be called one or more times (
once for each replica).

#### Args:


* <b>`fn`</b>: The function to run. The output must be a <a href="../../../tf/nest"><code>tf.nest</code></a> of `Tensor`s.
* <b>`args`</b>: (Optional) Positional arguments to `fn`.
* <b>`kwargs`</b>: (Optional) Keyword arguments to `fn`.


#### Returns:

Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be "per-replica" `Tensor` objects or `Tensor`s
(for example, if running on a single replica).


<h3 id="make_dataset_iterator"><code>make_dataset_iterator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/mirrored_strategy.py#L103-L124">View source</a>

``` python
make_dataset_iterator(dataset)
```

Makes an iterator for input provided via `dataset`.

NOTE: The batch size of the `dataset` argument is treated differently for
this contrib version of `MirroredStrategy`.

Data from the given dataset will be distributed evenly across all the
compute replicas. We will assume that the input dataset is batched by the
per-replica batch size.

The user could also use `make_input_fn_iterator` if they want to
customize which input is fed to which replica/worker etc.

#### Args:


* <b>`dataset`</b>: <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> that will be distributed evenly across all
  replicas.


#### Returns:

An `tf.distribute.InputIterator` which returns inputs for each step of the
computation.  User should call `initialize` on the returned iterator.


<h3 id="make_input_fn_iterator"><code>make_input_fn_iterator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L1010-L1050">View source</a>

``` python
make_input_fn_iterator(
    input_fn,
    replication_mode=tf.distribute.InputReplicationMode.PER_WORKER
)
```

Returns an iterator split across replicas created from an input function.

DEPRECATED: This method is not available in TF 2.x.

The `input_fn` should take an <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> object where
information about batching and input sharding can be accessed:

```
def input_fn(input_context):
  batch_size = input_context.get_per_replica_batch_size(global_batch_size)
  d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
  return d.shard(input_context.num_input_pipelines,
                 input_context.input_pipeline_id)
with strategy.scope():
  iterator = strategy.make_input_fn_iterator(input_fn)
  replica_results = strategy.experimental_run(replica_fn, iterator)
```

The <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returned by `input_fn` should have a per-replica
batch size, which may be computed using
`input_context.get_per_replica_batch_size`.

#### Args:


* <b>`input_fn`</b>: A function taking a <a href="../../../tf/distribute/InputContext"><code>tf.distribute.InputContext</code></a> object and
  returning a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.
* <b>`replication_mode`</b>: an enum value of <a href="../../../tf/distribute/InputReplicationMode"><code>tf.distribute.InputReplicationMode</code></a>.
  Only `PER_WORKER` is supported currently, which means there will be
  a single call to `input_fn` per worker. Replicas will dequeue from the
  local <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> on their worker.


#### Returns:

An iterator object that should first be `.initialize()`-ed. It may then
either be passed to `strategy.experimental_run()` or you can
`iterator.get_next()` to get the next value to pass to
`strategy.extended.call_for_each_replica()`.


<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L1118-L1119">View source</a>

``` python
reduce(
    reduce_op,
    value,
    axis=None
)
```

Reduce `value` across replicas.

Given a per-replica value returned by `experimental_run_v2`, say a
per-example loss, the batch will be divided across all the replicas.  This
function allows you to aggregate across replicas and optionally also across
batch elements.  For example, if you have a global batch size of 8 and 2
replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
`[4, 5, 6, 7]` will be on replica 1. By default, `reduce` will just
aggregate across replicas, returning `[0+4, 1+5, 2+6, 3+7]`. This is useful
when each replica is computing a scalar or some other value that doesn't
have a "batch" dimension (like a gradient). More often you will want to
aggregate across the global batch, which you can get by specifying the batch
dimension as the `axis`, typically `axis=0`. In this case it would return a
scalar `0+1+2+3+4+5+6+7`.

If there is a last partial batch, you will need to specify an axis so
that the resulting shape is consistent across replicas. So if the last
batch has size 6 and it is divided into [0, 1, 2, 3] and [4, 5], you
would get a shape mismatch unless you specify `axis=0`. If you specify
<a href="../../../tf/distribute/ReduceOp#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>, using `axis=0` will use the correct
denominator of 6. Contrast this with computing `reduce_mean` to get a
scalar value on each replica and this function to average those means,
which will weigh some values `1/8` and others `1/4`.

#### Args:


* <b>`reduce_op`</b>: A <a href="../../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
  be combined.
* <b>`value`</b>: A "per replica" value, e.g. returned by `experimental_run_v2` to
  be combined into a single tensor.
* <b>`axis`</b>: Specifies the dimension to reduce along within each
  replica's tensor. Should typically be set to the batch dimension, or
  `None` to only reduce across replicas (e.g. if the tensor has no batch
  dimension).


#### Returns:

A `Tensor`.


<h3 id="scope"><code>scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L545-L555">View source</a>

``` python
scope()
```

Returns a context manager selecting this Strategy as current.

Inside a `with strategy.scope():` code block, this thread
will use a variable creator set by `strategy`, and will
enter its "cross-replica context".

#### Returns:

A context manager.


<h3 id="update_config_proto"><code>update_config_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L1123-L1138">View source</a>

``` python
update_config_proto(config_proto)
```

Returns a copy of `config_proto` modified for use with this strategy.

DEPRECATED: This method is not available in TF 2.x.

The updated config has something needed to run a strategy, e.g.
configuration to run collective ops, or device filters to improve
distributed training performance.

#### Args:


* <b>`config_proto`</b>: a <a href="../../../tf/ConfigProto"><code>tf.ConfigProto</code></a> object.


#### Returns:

The updated copy of the `config_proto`.
