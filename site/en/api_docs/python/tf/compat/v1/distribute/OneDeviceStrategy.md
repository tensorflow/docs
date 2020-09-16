description: A distribution strategy for running on a single device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute.OneDeviceStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="experimental_distribute_dataset"/>
<meta itemprop="property" content="experimental_distribute_datasets_from_function"/>
<meta itemprop="property" content="experimental_local_results"/>
<meta itemprop="property" content="experimental_make_numpy_dataset"/>
<meta itemprop="property" content="experimental_run"/>
<meta itemprop="property" content="make_dataset_iterator"/>
<meta itemprop="property" content="make_input_fn_iterator"/>
<meta itemprop="property" content="reduce"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="scope"/>
<meta itemprop="property" content="update_config_proto"/>
</div>

# tf.compat.v1.distribute.OneDeviceStrategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/one_device_strategy.py#L235-L243">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A distribution strategy for running on a single device.

Inherits From: [`Strategy`](../../../../tf/compat/v1/distribute/Strategy.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.distribute.OneDeviceStrategy(
    device
)
</code></pre>



<!-- Placeholder for "Used in" -->

Using this strategy will place any variables created in its scope on the
specified device. Input distributed through this strategy will be
prefetched to the specified device. Moreover, any functions called via
`strategy.run` will also be placed on the specified device
as well.

Typical usage of this strategy could be testing your code with the
tf.distribute.Strategy API before switching to other strategies which
actually distribute to multiple devices/machines.

#### For example:


```
tf.enable_eager_execution()
strategy = tf.distribute.OneDeviceStrategy(device="/gpu:0")

with strategy.scope():
  v = tf.Variable(1.0)
  print(v.device)  # /job:localhost/replica:0/task:0/device:GPU:0

def step_fn(x):
  return x * 2

result = 0
for i in range(10):
  result += strategy.run(step_fn, args=(i,))
print(result)  # 90
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`device`
</td>
<td>
Device string identifier for the device on which the variables
should be placed. See class docs for more details on how the device is
used. Examples: "/cpu:0", "/gpu:0", "/device:CPU:0", "/device:GPU:0"
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`extended`
</td>
<td>
<a href="../../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> with additional methods.
</td>
</tr><tr>
<td>
`num_replicas_in_sync`
</td>
<td>
Returns number of replicas over which gradients are aggregated.
</td>
</tr>
</table>



## Methods

<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L715-L805">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset
)
</code></pre>

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
  strategy.run(train_step, args=(x,))
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
if this method of sharding is selected.

You can disable dataset sharding across workers using the
`auto_shard_policy` option in <a href="../../../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a>.

Within each worker, we will also split the data among all the worker
devices (if more than one a present), and this will happen even if
multi-worker sharding is disabled using the method above.

If the above batch splitting and dataset sharding logic is undesirable,
please use `experimental_distribute_datasets_from_function` instead, which
does not do any automatic splitting or sharding.

You can also use the `element_spec` property of the distributed dataset
returned by this API to query the <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned
by the iterator. This can be used to set the `input_signature` property
of a <a href="../../../../tf/function.md"><code>tf.function</code></a>.

```python
strategy = tf.distribute.MirroredStrategy()

# Create a dataset
dataset = dataset_ops.Dataset.TFRecordDataset([
  "/a/1.tfr", "/a/2.tfr", "/a/3.tfr", "/a/4.tfr"])

# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(dataset)

@tf.function(input_signature=[dist_dataset.element_spec])
def train_step(inputs):
  # train model with inputs
  return

# Iterate over the distributed dataset
for x in dist_dataset:
  # process dataset elements
  strategy.run(train_step, args=(x,))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
<a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> that will be sharded across all replicas using
the rules stated above.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A "distributed `Dataset`", which acts like a <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> except
it produces "per-replica" values.
</td>
</tr>

</table>



<h3 id="experimental_distribute_datasets_from_function"><code>experimental_distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L807-L875">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_datasets_from_function(
    dataset_fn
)
</code></pre>

Distributes <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

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

The `dataset_fn` should take an <a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed:

```
def dataset_fn(input_context):
  batch_size = input_context.get_per_replica_batch_size(global_batch_size)
  d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
  return d.shard(
      input_context.num_input_pipelines, input_context.input_pipeline_id)

inputs = strategy.experimental_distribute_datasets_from_function(dataset_fn)

for batch in inputs:
  replica_results = strategy.run(replica_fn, args=(batch,))
```

IMPORTANT: The <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size.  This may be computed using
`input_context.get_per_replica_batch_size`.

To query the <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements in the distributed dataset
returned by this API, you need to use the `element_spec` property of the
distributed iterator. This <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> can be used to set the
`input_signature` property of a <a href="../../../../tf/function.md"><code>tf.function</code></a>.

```python
# If you want to specify `input_signature` for a `tf.function` you must
# first create the iterator.
iterator = iter(inputs)

@tf.function(input_signature=[iterator.element_spec])
def replica_fn_with_signature(inputs):
  # train the model with inputs
  return

for _ in range(steps):
  strategy.run(replica_fn_with_signature,
      args=(next(iterator),))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset_fn`
</td>
<td>
A function taking a <a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance and
returning a <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A "distributed `Dataset`", which acts like a <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> except
it produces "per-replica" values.
</td>
</tr>

</table>



<h3 id="experimental_local_results"><code>experimental_local_results</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1080-L1097">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_local_results(
    value
)
</code></pre>

Returns the list of all local per-replica values contained in `value`.

Note: This only returns values on the worker initiated by this client.
When using a <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> like
<a href="../../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>, each worker
will be its own client, and this function will only return values
computed on that worker.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value returned by `experimental_run()`, `run()`,
`extended.call_for_each_replica()`, or a variable created in `scope`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tuple of values contained in `value`. If `value` represents a single
value, this returns `(value,).`
</td>
</tr>

</table>



<h3 id="experimental_make_numpy_dataset"><code>experimental_make_numpy_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1473-L1502">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_make_numpy_dataset(
    numpy_input, session=None
)
</code></pre>

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`numpy_input`
</td>
<td>
A nest of NumPy input arrays that will be converted into a
dataset. Note that lists of Numpy arrays are stacked, as that is normal
<a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> behavior.
</td>
</tr><tr>
<td>
`session`
</td>
<td>
(TensorFlow v1.x graph execution only) A session used for
initialization.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> representing `numpy_input`.
</td>
</tr>

</table>



<h3 id="experimental_run"><code>experimental_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1504-L1537">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_run(
    fn, input_iterator=None
)
</code></pre>

Runs ops in `fn` on each replica, with inputs from `input_iterator`.

DEPRECATED: This method is not available in TF 2.x. Please switch
to using `run` instead.

When eager execution is enabled, executes ops specified by `fn` on each
replica. Otherwise, builds a graph to execute the ops on each replica.

Each replica will take a single, different input from the inputs provided by
one `get_next` call on the input iterator.

`fn` may call <a href="../../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context()</code></a> to access members such
as `replica_id_in_sync_group`.

IMPORTANT: Depending on the <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> implementation being
used, and whether eager execution is enabled, `fn` may be called one or more
times (once for each replica).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
The function to run. The inputs to the function must match the outputs
of `input_iterator.get_next()`. The output must be a <a href="../../../../tf/nest.md"><code>tf.nest</code></a> of
`Tensor`s.
</td>
</tr><tr>
<td>
`input_iterator`
</td>
<td>
(Optional) input iterator from which the inputs are taken.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be `PerReplica` (if the values are unsynchronized),
`Mirrored` (if the values are kept in sync), or `Tensor` (if running on a
single replica).
</td>
</tr>

</table>



<h3 id="make_dataset_iterator"><code>make_dataset_iterator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1405-L1429">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_dataset_iterator(
    dataset
)
</code></pre>

Makes an iterator for input provided via `dataset`.

DEPRECATED: This method is not available in TF 2.x.

Data from the given dataset will be distributed evenly across all the
compute replicas. We will assume that the input dataset is batched by the
global batch size. With this assumption, we will make a best effort to
divide each batch across all the replicas (one or more workers).
If this effort fails, an error will be thrown, and the user should instead
use `make_input_fn_iterator` which provides more control to the user, and
does not try to divide a batch across replicas.

The user could also use `make_input_fn_iterator` if they want to
customize which input is fed to which replica/worker etc.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
<a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> that will be distributed evenly across all
replicas.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `tf.distribute.InputIterator` which returns inputs for each step of the
computation.  User should call `initialize` on the returned iterator.
</td>
</tr>

</table>



<h3 id="make_input_fn_iterator"><code>make_input_fn_iterator</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1431-L1471">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_input_fn_iterator(
    input_fn, replication_mode=tf.distribute.InputReplicationMode.PER_WORKER
)
</code></pre>

Returns an iterator split across replicas created from an input function.

DEPRECATED: This method is not available in TF 2.x.

The `input_fn` should take an <a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> object where
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

The <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `input_fn` should have a per-replica
batch size, which may be computed using
`input_context.get_per_replica_batch_size`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`input_fn`
</td>
<td>
A function taking a <a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> object and
returning a <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr><tr>
<td>
`replication_mode`
</td>
<td>
an enum value of <a href="../../../../tf/distribute/InputReplicationMode.md"><code>tf.distribute.InputReplicationMode</code></a>.
Only `PER_WORKER` is supported currently, which means there will be
a single call to `input_fn` per worker. Replicas will dequeue from the
local <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> on their worker.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An iterator object that should first be `.initialize()`-ed. It may then
either be passed to `strategy.experimental_run()` or you can
`iterator.get_next()` to get the next value to pass to
`strategy.extended.call_for_each_replica()`.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1539-L1540">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis=None
)
</code></pre>

Reduce `value` across replicas.

Given a per-replica value returned by `run`, say a
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
<a href="../../../../tf/distribute/ReduceOp.md#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>, using `axis=0` will use the correct
denominator of 6. Contrast this with computing `reduce_mean` to get a
scalar value on each replica and this function to average those means,
which will weigh some values `1/8` and others `1/4`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
A <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
be combined.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
A "per replica" value, e.g. returned by `run` to
be combined into a single tensor.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Specifies the dimension to reduce along within each
replica's tensor. Should typically be set to the batch dimension, or
`None` to only reduce across replicas (e.g. if the tensor has no batch
dimension).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`.
</td>
</tr>

</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L877-L951">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Run `fn` on each replica, with the given arguments.

Executes ops specified by `fn` on each replica. If `args` or `kwargs` have
<a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, such as those produced by a
"distributed `Dataset`" or `experimental_distribute_values_from_function`
when `fn` is executed on a particular replica, it will be executed with the
component of <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> that correspond to that
replica.

`fn` may call <a href="../../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context()</code></a> to access members such
as `all_reduce`.

All arguments in `args` or `kwargs` should either be nest of tensors or
<a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing tensors or composite tensors.

IMPORTANT: Depending on the implementation of <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> and
whether eager execution is enabled, `fn` may be called one or more times (
once for each replica).

#### Example usage:



1. Constant tensor input.

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> tensor_input = tf.constant(3.0)
>>> @tf.function
... def replica_fn(input):
...   return input*2.0
>>> result = strategy.run(replica_fn, args=(tensor_input,))
>>> result
<tf.Tensor: shape=(), dtype=float32, numpy=6.0>
```

2. DistributedValues input.

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> @tf.function
... def run():
...   def value_fn(value_context):
...     return value_context.num_replicas_in_sync
...   distributed_values = (
...     strategy.experimental_distribute_values_from_function(
...       value_fn))
...   def replica_fn2(input):
...     return input*2
...   return strategy.run(replica_fn2, args=(distributed_values,))
>>> result = run()
>>> result
<tf.Tensor: shape=(), dtype=int32, numpy=2>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
The function to run. The output must be a <a href="../../../../tf/nest.md"><code>tf.nest</code></a> of `Tensor`s.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
(Optional) Positional arguments to `fn`.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
(Optional) Keyword arguments to `fn`.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
(Optional) An instance of <a href="../../../../tf/distribute/RunOptions.md"><code>tf.distribute.RunOptions</code></a> specifying
the options to run `fn`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, `Tensor`
objects, or `Tensor`s (for example, if running on a single replica).
</td>
</tr>

</table>



<h3 id="scope"><code>scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L646-L656">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scope()
</code></pre>

Returns a context manager selecting this Strategy as current.

Inside a `with strategy.scope():` code block, this thread
will use a variable creator set by `strategy`, and will
enter its "cross-replica context".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager.
</td>
</tr>

</table>



<h3 id="update_config_proto"><code>update_config_proto</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/distribute_lib.py#L1544-L1559">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>update_config_proto(
    config_proto
)
</code></pre>

Returns a copy of `config_proto` modified for use with this strategy.

DEPRECATED: This method is not available in TF 2.x.

The updated config has something needed to run a strategy, e.g.
configuration to run collective ops, or device filters to improve
distributed training performance.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config_proto`
</td>
<td>
a `tf.ConfigProto` object.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The updated copy of the `config_proto`.
</td>
</tr>

</table>





