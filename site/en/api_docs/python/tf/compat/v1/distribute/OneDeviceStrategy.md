description: A distribution strategy for running on a single device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.distribute.OneDeviceStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="distribute_datasets_from_function"/>
<meta itemprop="property" content="experimental_distribute_dataset"/>
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
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L241-L251">
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
`cluster_resolver`
</td>
<td>
Returns the cluster resolver associated with this strategy.

In general, when using a multi-worker <a href="../../../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as
<a href="../../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> or
<a href="../../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy()</code></a>, there is a
<a href="../../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> associated with the
strategy used, and such an instance is returned by this property.

Strategies that intend to have an associated
<a href="../../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> must set the
relevant attribute, or override this property; otherwise, `None` is returned
by default. Those strategies should also provide information regarding what
is returned by this property.

Single-worker strategies usually do not have a
<a href="../../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>, and in those cases this
property will return `None`.

The <a href="../../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> may be useful when the
user needs to access information such as the cluster spec, task type or task
id. For example,

```python

os.environ['TF_CONFIG'] = json.dumps({
'cluster': {
'worker': ["localhost:12345", "localhost:23456"],
'ps': ["localhost:34567"]
},
'task': {'type': 'worker', 'index': 0}
})

# This implicitly uses TF_CONFIG for the cluster and current task info.
strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()

...

if strategy.cluster_resolver.task_type == 'worker':
# Perform something that's only applicable on workers. Since we set this
# as a worker above, this block will run on this particular instance.
elif strategy.cluster_resolver.task_type == 'ps':
# Perform something that's only applicable on parameter servers. Since we
# set this as a worker above, this block will not run on this particular
# instance.
```

For more information, please see
<a href="../../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s API docstring.
</td>
</tr><tr>
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

<h3 id="distribute_datasets_from_function"><code>distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1061-L1135">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>distribute_datasets_from_function(
    dataset_fn, options=None
)
</code></pre>

Distributes <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

The argument `dataset_fn` that users pass in is an input function that has a
<a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> argument and returns a <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>
instance. It is expected that the returned dataset from `dataset_fn` is
already batched by per-replica batch size (i.e. global batch size divided by
the number of replicas in sync) and sharded.
<a href="../../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> does
not batch or shard the <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance
returned from the input function. `dataset_fn` will be called on the CPU
device of each of the workers and each generates a dataset where every
replica on that worker will dequeue one batch of inputs (i.e. if a worker
has two replicas, two batches will be dequeued from the `Dataset` every
step).

This method can be used for several purposes. First, it allows you to
specify your own batching and sharding logic. (In contrast,
`tf.distribute.experimental_distribute_dataset` does batching and sharding
for you.) For example, where
`experimental_distribute_dataset` is unable to shard the input files, this
method might be used to manually shard the dataset (avoiding the slow
fallback behavior in `experimental_distribute_dataset`). In cases where the
dataset is infinite, this sharding can be done by creating dataset replicas
that differ only in their random seed.

The `dataset_fn` should take an <a href="../../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed.

You can use `element_spec` property of the
<a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> returned by this API to query the
<a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned by the iterator. This can be used to
set the `input_signature` property of a <a href="../../../../tf/function.md"><code>tf.function</code></a>. Follow
<a href="../../../../tf/distribute/DistributedDataset.md#element_spec"><code>tf.distribute.DistributedDataset.element_spec</code></a> to see an example.

IMPORTANT: The <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size. This may be computed using
`input_context.get_per_replica_batch_size`.

Note: If you are using TPUStrategy, the order in which the data is processed
by the workers when using
<a href="../../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

Note: Stateful dataset transformations are currently not supported with
`tf.distribute.experimental_distribute_dataset` or
`tf.distribute.distribute_datasets_from_function`. Any stateful
ops that the dataset may have are currently ignored. For example, if your
dataset has a `map_fn` that uses <a href="../../../../tf/random/uniform.md"><code>tf.random.uniform</code></a> to rotate an image,
then you have a dataset graph that depends on state (i.e the random seed) on
the local machine where the python process is being executed.

For a tutorial on more usage and properties of this method, refer to the
[tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_datasets_from_function)).
If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

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
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
dataset is distributed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L942-L1059">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset, options=None
)
</code></pre>

Creates <a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

The returned <a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> can be iterated over
similar to regular datasets.
NOTE: The user cannot add any more transformations to a
<a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>. You can only create an iterator or
examine the <a href="../../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the data generated by it. See API docs of
<a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> to learn more.

The following is an example:

```
>>> global_batch_size = 2
>>> # Passing the devices is optional.
... strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
>>> # Create a dataset
... dataset = tf.data.Dataset.range(4).batch(global_batch_size)
>>> # Distribute that dataset
... dist_dataset = strategy.experimental_distribute_dataset(dataset)
>>> @tf.function
... def replica_fn(input):
...   return input*2
>>> result = []
>>> # Iterate over the `tf.distribute.DistributedDataset`
... for x in dist_dataset:
...   # process dataset elements
...   result.append(strategy.run(replica_fn, args=(x,)))
>>> print(result)
[PerReplica:{
  0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([0])>,
  1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([2])>
}, PerReplica:{
  0: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([4])>,
  1: <tf.Tensor: shape=(1,), dtype=int64, numpy=array([6])>
}]
```


Three key actions happending under the hood of this method are batching,
sharding, and prefetching.

In the code snippet above, `dataset` is batched by `global_batch_size`, and
calling `experimental_distribute_dataset` on it rebatches `dataset` to a
new batch size that is equal to the global batch size divided by the number
of replicas in sync. We iterate through it using a Pythonic for loop.
`x` is a <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing data for all replicas,
and each replica gets data of the new batch size.
<a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> will take care of feeding the right per-replica
data in `x` to the right `replica_fn` executed on each replica.

Sharding contains autosharding across multiple workers and within every
worker. First, in multi-worker distributed training (i.e. when you use
<a href="../../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>
or <a href="../../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>), autosharding a dataset over a set of
workers means that each worker is assigned a subset of the entire dataset
(if the right <a href="../../../../tf/data/experimental/AutoShardPolicy.md"><code>tf.data.experimental.AutoShardPolicy</code></a> is set). This is to
ensure that at each step, a global batch size of non-overlapping dataset
elements will be processed by each worker. Autosharding has a couple of
different options that can be specified using
<a href="../../../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a>. Then, sharding within each worker
means the method will split the data among all the worker devices (if more
than one a present). This will happen regardless of multi-worker
autosharding.

Note: for autosharding across multiple workers, the default mode is
<a href="../../../../tf/data/experimental/AutoShardPolicy.md#AUTO"><code>tf.data.experimental.AutoShardPolicy.AUTO</code></a>. This mode
will attempt to shard the input dataset by files if the dataset is
being created out of reader datasets (e.g. <a href="../../../../tf/data/TFRecordDataset.md"><code>tf.data.TFRecordDataset</code></a>,
<a href="../../../../tf/data/TextLineDataset.md"><code>tf.data.TextLineDataset</code></a>, etc.) or otherwise shard the dataset by data,
where each of the workers will read the entire dataset and only process the
shard assigned to it. However, if you have less than one input file per
worker, we suggest that you disable dataset autosharding across workers by
setting the <a href="../../../../tf/data/experimental/DistributeOptions.md#auto_shard_policy"><code>tf.data.experimental.DistributeOptions.auto_shard_policy</code></a> to be
<a href="../../../../tf/data/experimental/AutoShardPolicy.md#OFF"><code>tf.data.experimental.AutoShardPolicy.OFF</code></a>.

By default, this method adds a prefetch transformation at the end of the
user provided <a href="../../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance. The argument to the prefetch
transformation which is `buffer_size` is equal to the number of replicas in
sync.

If the above batch splitting and dataset sharding logic is undesirable,
please use
<a href="../../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a>
instead, which does not do any automatic batching or sharding for you.

Note: If you are using TPUStrategy, the order in which the data is processed
by the workers when using
<a href="../../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

Note: Stateful dataset transformations are currently not supported with
`tf.distribute.experimental_distribute_dataset` or
`tf.distribute.distribute_datasets_from_function`. Any stateful
ops that the dataset may have are currently ignored. For example, if your
dataset has a `map_fn` that uses <a href="../../../../tf/random/uniform.md"><code>tf.random.uniform</code></a> to rotate an image,
then you have a dataset graph that depends on state (i.e the random seed) on
the local machine where the python process is being executed.

For a tutorial on more usage and properties of this method, refer to the
[tutorial on distributed input](https://www.tensorflow.org/tutorials/distribute/input#tfdistributestrategyexperimental_distribute_dataset).
If you are interested in last partial batch handling, read [this section](https://www.tensorflow.org/tutorials/distribute/input#partial_batches).

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
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
dataset is distributed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_local_results"><code>experimental_local_results</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1482-L1499">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1880-L1909">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1911-L1944">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1812-L1836">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1838-L1878">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1946-L1947">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis=None
)
</code></pre>

Reduce `value` across replicas and return result on current device.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def step_fn():
...   i = tf.distribute.get_replica_context().replica_id_in_sync_group
...   return tf.identity(i)
>>>
>>> per_replica_result = strategy.run(step_fn)
>>> total = strategy.reduce("SUM", per_replica_result, axis=None)
>>> total
<tf.Tensor: shape=(), dtype=int32, numpy=1>
```

To see how this would look with multiple replicas, consider the same
example with MirroredStrategy with 2 GPUs:

```python
strategy = tf.distribute.MirroredStrategy(devices=["GPU:0", "GPU:1"])
def step_fn():
  i = tf.distribute.get_replica_context().replica_id_in_sync_group
  return tf.identity(i)

per_replica_result = strategy.run(step_fn)
# Check devices on which per replica result is:
strategy.experimental_local_results(per_replica_result)[0].device
# /job:localhost/replica:0/task:0/device:GPU:0
strategy.experimental_local_results(per_replica_result)[1].device
# /job:localhost/replica:0/task:0/device:GPU:1

total = strategy.reduce("SUM", per_replica_result, axis=None)
# Check device on which reduced result is:
total.device
# /job:localhost/replica:0/task:0/device:CPU:0

```

This API is typically used for aggregating the results returned from
different replicas, for reporting etc. For example, loss computed from
different replicas can be averaged using this API before printing.

Note: The result is copied to the "current" device - which would typically
be the CPU of the worker on which the program is running. For `TPUStrategy`,
it is the first TPU host. For multi client `MultiWorkerMirroredStrategy`,
this is CPU of each worker.

There are a number of different tf.distribute APIs for reducing values
across replicas:
* <a href="../../../../tf/distribute/ReplicaContext.md#all_reduce"><code>tf.distribute.ReplicaContext.all_reduce</code></a>: This differs from
`Strategy.reduce` in that it is for replica context and does
not copy the results to the host device. `all_reduce` should be typically
used for reductions inside the training step such as gradients.
* <a href="../../../../tf/distribute/StrategyExtended.md#reduce_to"><code>tf.distribute.StrategyExtended.reduce_to</code></a> and
<a href="../../../../tf/distribute/StrategyExtended.md#batch_reduce_to"><code>tf.distribute.StrategyExtended.batch_reduce_to</code></a>: These APIs are more
advanced versions of `Strategy.reduce` as they allow customizing the
destination of the result. They are also called in cross replica context.

_What should axis be?_

Given a per-replica value returned by `run`, say a
per-example loss, the batch will be divided across all the replicas.  This
function allows you to aggregate across replicas and optionally also across
batch elements by specifying the axis parameter accordingly.

For example, if you have a global batch size of 8 and 2
replicas, values for examples `[0, 1, 2, 3]` will be on replica 0 and
`[4, 5, 6, 7]` will be on replica 1. With `axis=None`, `reduce` will
aggregate only across replicas, returning `[0+4, 1+5, 2+6, 3+7]`.
This is useful when each replica is computing a scalar or some other value
that doesn't have a "batch" dimension (like a gradient or loss).
```
strategy.reduce("sum", per_replica_result, axis=None)
```

Sometimes, you will want to aggregate across both the global batch _and_
all replicas. You can get this behavior by specifying the batch
dimension as the `axis`, typically `axis=0`. In this case it would return a
scalar `0+1+2+3+4+5+6+7`.
```
strategy.reduce("sum", per_replica_result, axis=0)
```

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
a <a href="../../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
be combined. Allows using string representation of the enum such as
"SUM", "MEAN".
</td>
</tr><tr>
<td>
`value`
</td>
<td>
a <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance, e.g. returned by
`Strategy.run`, to be combined into a single tensor. It can also be a
regular tensor when used with `OneDeviceStrategy` or default strategy.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
specifies the dimension to reduce along within each
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1145-L1259">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Invokes `fn` on each replica, with the given arguments.

This method is the primary way to distribute your computation with a
tf.distribute object. It invokes `fn` on each replica. If `args` or `kwargs`
have <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, such as those produced by a
<a href="../../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from
<a href="../../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a>,
when `fn` is executed on a particular replica, it will be executed with the
component of <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> that correspond to that
replica.

`fn` is invoked under a replica context. `fn` may call
<a href="../../../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context()</code></a> to access members such as
`all_reduce`. Please see the module-level docstring of tf.distribute for the
concept of replica context.

All arguments in `args` or `kwargs` should either be Python values of a
nested structure of tensors, e.g. a list of tensors, in which case `args`
and `kwargs` will be passed to the `fn` invoked on each replica. Or `args`
or `kwargs` can be <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing tensors or
composite tensors, i.e. <a href="../../../../tf/compat/v1/TensorInfo/CompositeTensor.md"><code>tf.compat.v1.TensorInfo.CompositeTensor</code></a>, in which
case each `fn` call will get the component of a
<a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> corresponding to its replica.

IMPORTANT: Depending on the implementation of <a href="../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> and
whether eager execution is enabled, `fn` may be called one or more times. If
`fn` is annotated with <a href="../../../../tf/function.md"><code>tf.function</code></a> or <a href="../../../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> is
called inside a <a href="../../../../tf/function.md"><code>tf.function</code></a> (eager execution is disabled inside a
<a href="../../../../tf/function.md"><code>tf.function</code></a> by default), `fn` is called once per replica to generate a
Tensorflow graph, which will then be reused for execution with new inputs.
Otherwise, if eager execution is enabled, `fn` will be called once per
replica every step just like regular python code.

#### Example usage:



1. Constant tensor input.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> tensor_input = tf.constant(3.0)
>>> @tf.function
... def replica_fn(input):
...   return input*2.0
>>> result = strategy.run(replica_fn, args=(tensor_input,))
>>> result
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>,
  1: <tf.Tensor: shape=(), dtype=float32, numpy=6.0>
}
```

2. DistributedValues input.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
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
<tf.Tensor: shape=(), dtype=int32, numpy=4>
```

3. Use <a href="../../../../tf/distribute/ReplicaContext.md"><code>tf.distribute.ReplicaContext</code></a> to allreduce values.

```
>>> strategy = tf.distribute.MirroredStrategy(["gpu:0", "gpu:1"])
>>> @tf.function
... def run():
...    def value_fn(value_context):
...      return tf.constant(value_context.replica_id_in_sync_group)
...    distributed_values = (
...        strategy.experimental_distribute_values_from_function(
...            value_fn))
...    def replica_fn(input):
...      return tf.distribute.get_replica_context().all_reduce("sum", input)
...    return strategy.run(replica_fn, args=(distributed_values,))
>>> result = run()
>>> result
PerReplica:{
  0: <tf.Tensor: shape=(), dtype=int32, numpy=1>,
  1: <tf.Tensor: shape=(), dtype=int32, numpy=1>
}
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
The function to run on each replica.
</td>
</tr><tr>
<td>
`args`
</td>
<td>
Optional positional arguments to `fn`. Its element can be a Python
value, a tensor or a <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr><tr>
<td>
`kwargs`
</td>
<td>
Optional keyword arguments to `fn`. Its element can be a Python
value, a tensor or a <a href="../../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
An optional instance of <a href="../../../../tf/distribute/RunOptions.md"><code>tf.distribute.RunOptions</code></a> specifying
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L822-L910">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scope()
</code></pre>

Context manager to make the strategy current and distribute variables.

This method returns a context manager, and is used as follows:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> # Variable created inside scope:
>>> with strategy.scope():
...   mirrored_variable = tf.Variable(1.)
>>> mirrored_variable
MirroredVariable:{
  0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>,
  1: <tf.Variable 'Variable/replica_1:0' shape=() dtype=float32, numpy=1.0>
}
>>> # Variable created outside scope:
>>> regular_variable = tf.Variable(1.)
>>> regular_variable
<tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
```

_What happens when Strategy.scope is entered?_

* `strategy` is installed in the global context as the "current" strategy.
  Inside this scope, <a href="../../../../tf/distribute/get_strategy.md"><code>tf.distribute.get_strategy()</code></a> will now return this
  strategy. Outside this scope, it returns the default no-op strategy.
* Entering the scope also enters the "cross-replica context". See
  <a href="../../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> for an explanation on cross-replica and
  replica contexts.
* Variable creation inside `scope` is intercepted by the strategy. Each
  strategy defines how it wants to affect the variable creation. Sync
  strategies like `MirroredStrategy`, `TPUStrategy` and
  `MultiWorkerMiroredStrategy` create variables replicated on each replica,
  whereas `ParameterServerStrategy` creates variables on the parameter
  servers. This is done using a custom <a href="../../../../tf/variable_creator_scope.md"><code>tf.variable_creator_scope</code></a>.
* In some strategies, a default device scope may also be entered: in
  `MultiWorkerMiroredStrategy`, a default device scope of "/CPU:0" is
  entered on each worker.

Note: Entering a scope does not automatically distribute a computation, except
  in the case of high level training framework like keras `model.fit`. If
  you're not using `model.fit`, you
  need to use `strategy.run` API to explicitly distribute that computation.
  See an example in the [custom training loop tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training).


_What should be in scope and what should be outside?_

There are a number of requirements on what needs to happen inside the scope.
However, in places where we have information about which strategy is in use,
we often enter the scope for the user, so they don't have to do it
explicitly (i.e. calling those either inside or outside the scope is OK).

* Anything that creates variables that should be distributed variables
  must be in `strategy.scope`. This can be either by directly putting it in
  scope, or relying on another API like `strategy.run` or `model.fit` to
  enter it for you. Any variable that is created outside scope will not be
  distributed and may have performance implications. Common things that
  create variables in TF: models, optimizers, metrics. These should always
  be created inside the scope. Another source of variable creation can be
  a checkpoint restore - when variables are created lazily. Note that any
  variable created inside a strategy captures the strategy information. So
  reading and writing to these variables outside the `strategy.scope` can
  also work seamlessly, without the user having to enter the scope.
* Some strategy APIs (such as `strategy.run` and `strategy.reduce`) which
  require to be in a strategy's scope, enter the scope for you
  automatically, which means when using those APIs you don't need to
  enter the scope yourself.
* When a <a href="../../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is created inside a `strategy.scope`, we capture
  this information. When high level training frameworks methods such as
  `model.compile`, `model.fit` etc are then called
  on this model, we automatically enter the scope, as well as use this
  strategy to distribute the training etc. See
  detailed example in [distributed keras tutorial](https://www.tensorflow.org/tutorials/distribute/keras).
  Note that simply calling the `model(..)` is not impacted - only high
  level training framework APIs are. `model.compile`, `model.fit`,
  `model.evaluate`, `model.predict` and `model.save` can all be called
  inside or outside the scope.
* The following can be either inside or outside the scope:
    * Creating the input datasets
    * Defining <a href="../../../../tf/function.md"><code>tf.function</code></a>s that represent your training step
    * Saving APIs such as <a href="../../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a>. Loading creates variables,
      so that should go inside the scope if you want to train the model in a
      distributed way.
    * Checkpoint saving. As mentioned above - `checkpoint.restore` may
      sometimes need to be inside scope if it creates variables.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1951-L1966">View source</a>

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





