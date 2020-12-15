description: A one-machine strategy that puts all variables on a single device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.CentralStorageStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="distribute_datasets_from_function"/>
<meta itemprop="property" content="experimental_distribute_dataset"/>
<meta itemprop="property" content="experimental_distribute_values_from_function"/>
<meta itemprop="property" content="experimental_local_results"/>
<meta itemprop="property" content="gather"/>
<meta itemprop="property" content="reduce"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="scope"/>
</div>

# tf.distribute.experimental.CentralStorageStrategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/central_storage_strategy.py#L28-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A one-machine strategy that puts all variables on a single device.

Inherits From: [`Strategy`](../../../tf/distribute/Strategy.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.CentralStorageStrategy(
    compute_devices=None, parameter_device=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Variables are assigned to local CPU or the only GPU. If there is more
than one GPU, compute operations (other than variable update operations)
will be replicated across all GPUs.

#### For Example:


```
strategy = tf.distribute.experimental.CentralStorageStrategy()
# Create a dataset
ds = tf.data.Dataset.range(5).batch(2)
# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(ds)

with strategy.scope():
  @tf.function
  def train_step(val):
    return val + 1

  # Iterate over the distributed dataset
  for x in dist_dataset:
    # process dataset elements
    strategy.run(train_step, args=(x,))
```



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

In general, when using a multi-worker <a href="../../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> or
<a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy()</code></a>, there is a
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> associated with the
strategy used, and such an instance is returned by this property.

Strategies that intend to have an associated
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> must set the
relevant attribute, or override this property; otherwise, `None` is returned
by default. Those strategies should also provide information regarding what
is returned by this property.

Single-worker strategies usually do not have a
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>, and in those cases this
property will return `None`.

The <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> may be useful when the
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
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s API docstring.
</td>
</tr><tr>
<td>
`extended`
</td>
<td>
<a href="../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> with additional methods.
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

Distributes <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

The argument `dataset_fn` that users pass in is an input function that has a
<a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> argument and returns a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>
instance. It is expected that the returned dataset from `dataset_fn` is
already batched by per-replica batch size (i.e. global batch size divided by
the number of replicas in sync) and sharded.
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> does
not batch or shard the <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance
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

The `dataset_fn` should take an <a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed.

You can use `element_spec` property of the
<a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> returned by this API to query the
<a href="../../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned by the iterator. This can be used to
set the `input_signature` property of a <a href="../../../tf/function.md"><code>tf.function</code></a>. Follow
<a href="../../../tf/distribute/DistributedDataset.md#element_spec"><code>tf.distribute.DistributedDataset.element_spec</code></a> to see an example.

IMPORTANT: The <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size. This may be computed using
`input_context.get_per_replica_batch_size`.

Note: If you are using TPUStrategy, the order in which the data is processed
by the workers when using
<a href="../../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

Note: Stateful dataset transformations are currently not supported with
`tf.distribute.experimental_distribute_dataset` or
`tf.distribute.distribute_datasets_from_function`. Any stateful
ops that the dataset may have are currently ignored. For example, if your
dataset has a `map_fn` that uses <a href="../../../tf/random/uniform.md"><code>tf.random.uniform</code></a> to rotate an image,
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
A function taking a <a href="../../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance and
returning a <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
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
A <a href="../../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/central_storage_strategy.py#L77-L113">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset, options=None
)
</code></pre>

Distributes a tf.data.Dataset instance provided via dataset.

The returned dataset is a wrapped strategy dataset which creates a
multidevice iterator under the hood. It prefetches the input data to the
specified devices on the worker. The returned distributed dataset can be
iterated over similar to how regular datasets can.

NOTE: Currently, the user cannot add any more transformations to a
distributed dataset.

#### For Example:


```
strategy = tf.distribute.CentralStorageStrategy()  # with 1 CPU and 1 GPU
dataset = tf.data.Dataset.range(10).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(dataset)
for x in dist_dataset:
  print(x)  # Prints PerReplica values [0, 1], [2, 3],...

```
Args:
  dataset: <a href="../../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> to be prefetched to device.
  options: <a href="../../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
    dataset is distributed.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A "distributed `Dataset`" that the caller can iterate over.
</td>
</tr>

</table>



<h3 id="experimental_distribute_values_from_function"><code>experimental_distribute_values_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1616-L1690">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_values_from_function(
    value_fn
)
</code></pre>

Generates <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> from `value_fn`.

This function is to generate <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> to pass
into `run`, `reduce`, or other methods that take
distributed values when not using datasets.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value_fn`
</td>
<td>
The function to run to generate values. It is called for
each replica with `tf.distribute.ValueContext` as the sole argument. It
must return a Tensor or a type that can be converted to a Tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing a value for each replica.
</td>
</tr>

</table>



#### Example usage:



1. Return constant value per replica:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def value_fn(ctx):
...   return tf.constant(1.)
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(<tf.Tensor: shape=(), dtype=float32, numpy=1.0>,
 <tf.Tensor: shape=(), dtype=float32, numpy=1.0>)
```

2. Distribute values in array based on replica_id:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> array_value = np.array([3., 2., 1.])
>>> def value_fn(ctx):
...   return array_value[ctx.replica_id_in_sync_group]
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(3.0, 2.0)
```

3. Specify values using num_replicas_in_sync:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> def value_fn(ctx):
...   return ctx.num_replicas_in_sync
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(2, 2)
```

4. Place values on devices and distribute:

```
strategy = tf.distribute.TPUStrategy()
worker_devices = strategy.extended.worker_devices
multiple_values = []
for i in range(strategy.num_replicas_in_sync):
  with tf.device(worker_devices[i]):
    multiple_values.append(tf.constant(1.0))

def value_fn(ctx):
  return multiple_values[ctx.replica_id_in_sync_group]

distributed_values = strategy.
  experimental_distribute_values_from_function(
  value_fn)
```

<h3 id="experimental_local_results"><code>experimental_local_results</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/central_storage_strategy.py#L115-L129">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_local_results(
    value
)
</code></pre>

Returns the list of all local per-replica values contained in `value`.

In `CentralStorageStrategy` there is a single worker so the value returned
will be all the values on that worker.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
A value returned by `run()`, `extended.call_for_each_replica()`,
or a variable created in `scope`.
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



<h3 id="gather"><code>gather</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1692-L1796">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>gather(
    value, axis
)
</code></pre>

Gather `value` across replicas along `axis` to the current device.

Given a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> or <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>-like
object `value`, this API gathers and concatenates `value` across replicas
along the `axis`-th dimension. The result is copied to the "current" device
- which would typically be the CPU of the worker on which the program is
running. For <a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, it is the first TPU host. For
multi-client `MultiWorkerMirroredStrategy`, this is CPU of each worker.

This API can only be called in the cross-replica context. For a counterpart
in the replica context, see <a href="../../../tf/distribute/ReplicaContext.md#all_gather"><code>tf.distribute.ReplicaContext.all_gather</code></a>.

Note: For all strategies except <a href="../../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, the input
`value` on different replicas must have the same rank, and their shapes must
be the same in all dimensions except the `axis`-th dimension. In other
words, their shapes cannot be different in a dimension `d` where `d` does
not equal to the `axis` argument. For example, given a
<a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> with component tensors of shape
`(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
`gather(..., axis=1, ...)` on it, but not `gather(..., axis=0, ...)` or
`gather(..., axis=2, ...)`. However, for <a href="../../../tf/distribute/TPUStrategy.md#gather"><code>tf.distribute.TPUStrategy.gather</code></a>,
all tensors must have exactly the same rank and same shape.

Note: Given a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> `value`, its component
tensors must have a non-zero rank. Otherwise, consider using
<a href="../../../tf/expand_dims.md"><code>tf.expand_dims</code></a> before gathering them.

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> # A DistributedValues with component tensor of shape (2, 1) on each replica
... distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(tf.constant([[1], [2]])))
>>> @tf.function
... def run():
...   return strategy.gather(distributed_values, axis=0)
>>> run()
<tf.Tensor: shape=(4, 1), dtype=int32, numpy=
array([[1],
       [2],
       [1],
       [2]], dtype=int32)>
```


Consider the following example for more combinations:

```
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2", "GPU:3"])
>>> single_tensor = tf.reshape(tf.range(6), shape=(1,2,3))
>>> distributed_values = strategy.experimental_distribute_values_from_function(lambda _: tf.identity(single_tensor))
>>> @tf.function
... def run(axis):
...   return strategy.gather(distributed_values, axis=axis)
>>> axis=0
>>> run(axis)
<tf.Tensor: shape=(4, 2, 3), dtype=int32, numpy=
array([[[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]],
       [[0, 1, 2],
        [3, 4, 5]]], dtype=int32)>
>>> axis=1
>>> run(axis)
<tf.Tensor: shape=(1, 8, 3), dtype=int32, numpy=
array([[[0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5],
        [0, 1, 2],
        [3, 4, 5]]], dtype=int32)>
>>> axis=2
>>> run(axis)
<tf.Tensor: shape=(1, 2, 12), dtype=int32, numpy=
array([[[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
        [3, 4, 5, 3, 4, 5, 3, 4, 5, 3, 4, 5]]], dtype=int32)>
```


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`value`
</td>
<td>
a <a href="../../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance, e.g. returned by
<a href="../../../tf/distribute/MirroredStrategy.md#run"><code>Strategy.run</code></a>, to be combined into a single tensor. It can also be a
regular tensor when used with <a href="../../../tf/distribute/OneDeviceStrategy.md"><code>tf.distribute.OneDeviceStrategy</code></a> or the
default strategy. The tensors that constitute the DistributedValues
can only be dense tensors with non-zero rank, NOT a <a href="../../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
0-D int32 Tensor. Dimension along which to gather. Must be in the
range [0, rank(value)).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` that's the concatenation of `value` across replicas along
`axis` dimension.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/central_storage_strategy.py#L149-L213">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis
)
</code></pre>

Reduce `value` across replicas.

Given a per-replica value returned by `run`, say a
per-example loss, the batch will be divided across all the replicas. This
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
<a href="../../../tf/distribute/ReduceOp.md#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>, using `axis=0` will use the correct
denominator of 6. Contrast this with computing `reduce_mean` to get a
scalar value on each replica and this function to average those means,
which will weigh some values `1/8` and others `1/4`.

#### For Example:


```
strategy = tf.distribute.experimental.CentralStorageStrategy(
    compute_devices=['CPU:0', 'GPU:0'], parameter_device='CPU:0')
ds = tf.data.Dataset.range(10)
# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(ds)

with strategy.scope():
  @tf.function
  def train_step(val):
    # pass through
    return val

  # Iterate over the distributed dataset
  for x in dist_dataset:
    result = strategy.run(train_step, args=(x,))

result = strategy.reduce(tf.distribute.ReduceOp.SUM, result,
                         axis=None).numpy()
# result: array([ 4,  6,  8, 10])

result = strategy.reduce(tf.distribute.ReduceOp.SUM, result, axis=0).numpy()
# result: 28
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`reduce_op`
</td>
<td>
A <a href="../../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/central_storage_strategy.py#L131-L147">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Run `fn` on each replica, with the given arguments.

In `CentralStorageStrategy`, `fn` is  called on each of the compute
replicas, with the provided "per replica" arguments specific to that device.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
The function to run. The output must be a <a href="../../../tf/nest.md"><code>tf.nest</code></a> of `Tensor`s.
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
(Optional) An instance of <a href="../../../tf/distribute/RunOptions.md"><code>tf.distribute.RunOptions</code></a> specifying
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
Return value from running `fn`.
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
  Inside this scope, <a href="../../../tf/distribute/get_strategy.md"><code>tf.distribute.get_strategy()</code></a> will now return this
  strategy. Outside this scope, it returns the default no-op strategy.
* Entering the scope also enters the "cross-replica context". See
  <a href="../../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> for an explanation on cross-replica and
  replica contexts.
* Variable creation inside `scope` is intercepted by the strategy. Each
  strategy defines how it wants to affect the variable creation. Sync
  strategies like `MirroredStrategy`, `TPUStrategy` and
  `MultiWorkerMiroredStrategy` create variables replicated on each replica,
  whereas `ParameterServerStrategy` creates variables on the parameter
  servers. This is done using a custom <a href="../../../tf/variable_creator_scope.md"><code>tf.variable_creator_scope</code></a>.
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
* When a <a href="../../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is created inside a `strategy.scope`, we capture
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
    * Defining <a href="../../../tf/function.md"><code>tf.function</code></a>s that represent your training step
    * Saving APIs such as <a href="../../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a>. Loading creates variables,
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





