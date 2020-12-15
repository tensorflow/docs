description: A distribution strategy for running on a single device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.OneDeviceStrategy" />
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

# tf.distribute.OneDeviceStrategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L40-L237">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A distribution strategy for running on a single device.

Inherits From: [`Strategy`](../../tf/distribute/Strategy.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.OneDeviceStrategy(
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

In general, when using a multi-worker <a href="../../tf/distribute.md"><code>tf.distribute</code></a> strategy such as
<a href="../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> or
<a href="../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy()</code></a>, there is a
<a href="../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> associated with the
strategy used, and such an instance is returned by this property.

Strategies that intend to have an associated
<a href="../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> must set the
relevant attribute, or override this property; otherwise, `None` is returned
by default. Those strategies should also provide information regarding what
is returned by this property.

Single-worker strategies usually do not have a
<a href="../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>, and in those cases this
property will return `None`.

The <a href="../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a> may be useful when the
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
<a href="../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s API docstring.
</td>
</tr><tr>
<td>
`extended`
</td>
<td>
<a href="../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> with additional methods.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L112-L154">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>distribute_datasets_from_function(
    dataset_fn, options=None
)
</code></pre>

Distributes <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

`dataset_fn` will be called once for each worker in the strategy. In this
case, we only have one worker and one device so `dataset_fn` is called
once.

The `dataset_fn` should take an <a href="../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed:

```
def dataset_fn(input_context):
  batch_size = input_context.get_per_replica_batch_size(global_batch_size)
  d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
  return d.shard(
      input_context.num_input_pipelines, input_context.input_pipeline_id)

inputs = strategy.distribute_datasets_from_function(dataset_fn)

for batch in inputs:
  replica_results = strategy.run(replica_fn, args=(batch,))
```

IMPORTANT: The <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size.  This may be computed using
`input_context.get_per_replica_batch_size`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset_fn`
</td>
<td>
A function taking a <a href="../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance and
returning a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.
</td>
</tr><tr>
<td>
`options`
</td>
<td>
<a href="../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
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
A "distributed `Dataset`", which the caller can iterate over like regular
datasets.
</td>
</tr>

</table>



<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L83-L110">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset, options=None
)
</code></pre>

Distributes a tf.data.Dataset instance provided via dataset.

In this case, there is only one device, so this is only a thin wrapper
around the input dataset. It will, however, prefetch the input data to the
specified device. The returned distributed dataset can be iterated over
similar to how regular datasets can.

NOTE: Currently, the user cannot add any more transformations to a
distributed dataset.

#### Example:


```
strategy = tf.distribute.OneDeviceStrategy()
dataset = tf.data.Dataset.range(10).batch(2)
dist_dataset = strategy.experimental_distribute_dataset(dataset)
for x in dist_dataset:
  print(x)  # [0, 1], [2, 3],...
```
Args:
  dataset: <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> to be prefetched to device.
  options: <a href="../../tf/distribute/InputOptions.md"><code>tf.distribute.InputOptions</code></a> used to control options on how this
    dataset is distributed.
Returns:
  A "distributed `Dataset`" that the caller can iterate over.

<h3 id="experimental_distribute_values_from_function"><code>experimental_distribute_values_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1616-L1690">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_values_from_function(
    value_fn
)
</code></pre>

Generates <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> from `value_fn`.

This function is to generate <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> to pass
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
A <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing a value for each replica.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L156-L170">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_local_results(
    value
)
</code></pre>

Returns the list of all local per-replica values contained in `value`.

In `OneDeviceStrategy`, the `value` is always expected to be a single
value, so the result is just the value in a tuple.

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



<h3 id="gather"><code>gather</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L1692-L1796">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>gather(
    value, axis
)
</code></pre>

Gather `value` across replicas along `axis` to the current device.

Given a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> or <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a>-like
object `value`, this API gathers and concatenates `value` across replicas
along the `axis`-th dimension. The result is copied to the "current" device
- which would typically be the CPU of the worker on which the program is
running. For <a href="../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, it is the first TPU host. For
multi-client `MultiWorkerMirroredStrategy`, this is CPU of each worker.

This API can only be called in the cross-replica context. For a counterpart
in the replica context, see <a href="../../tf/distribute/ReplicaContext.md#all_gather"><code>tf.distribute.ReplicaContext.all_gather</code></a>.

Note: For all strategies except <a href="../../tf/distribute/TPUStrategy.md"><code>tf.distribute.TPUStrategy</code></a>, the input
`value` on different replicas must have the same rank, and their shapes must
be the same in all dimensions except the `axis`-th dimension. In other
words, their shapes cannot be different in a dimension `d` where `d` does
not equal to the `axis` argument. For example, given a
<a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> with component tensors of shape
`(1, 2, 3)` and `(1, 3, 3)` on two replicas, you can call
`gather(..., axis=1, ...)` on it, but not `gather(..., axis=0, ...)` or
`gather(..., axis=2, ...)`. However, for <a href="../../tf/distribute/TPUStrategy.md#gather"><code>tf.distribute.TPUStrategy.gather</code></a>,
all tensors must have exactly the same rank and same shape.

Note: Given a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> `value`, its component
tensors must have a non-zero rank. Otherwise, consider using
<a href="../../tf/expand_dims.md"><code>tf.expand_dims</code></a> before gathering them.

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
a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance, e.g. returned by
<a href="../../tf/distribute/MirroredStrategy.md#run"><code>Strategy.run</code></a>, to be combined into a single tensor. It can also be a
regular tensor when used with <a href="../../tf/distribute/OneDeviceStrategy.md"><code>tf.distribute.OneDeviceStrategy</code></a> or the
default strategy. The tensors that constitute the DistributedValues
can only be dense tensors with non-zero rank, NOT a <a href="../../tf/IndexedSlices.md"><code>tf.IndexedSlices</code></a>.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L190-L221">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis
)
</code></pre>

Reduce `value` across replicas.

In `OneDeviceStrategy`, there is only one replica, so if axis=None, value
is simply returned. If axis is specified as something other than None,
such as axis=0, value is reduced along that axis and returned.

#### Example:


```
t = tf.range(10)

result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=None).numpy()
# result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = strategy.reduce(tf.distribute.ReduceOp.SUM, t, axis=0).numpy()
# result: 45
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
A <a href="../../tf/distribute/ReduceOp.md"><code>tf.distribute.ReduceOp</code></a> value specifying how values should
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L172-L188">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Run `fn` on each replica, with the given arguments.

In `OneDeviceStrategy`, `fn` is simply called within a device scope for the
given device, with the provided arguments.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fn`
</td>
<td>
The function to run. The output must be a <a href="../../tf/nest.md"><code>tf.nest</code></a> of `Tensor`s.
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
(Optional) An instance of <a href="../../tf/distribute/RunOptions.md"><code>tf.distribute.RunOptions</code></a> specifying
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/one_device_strategy.py#L223-L237">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scope()
</code></pre>

Returns a context manager selecting this Strategy as current.

Inside a `with strategy.scope():` code block, this thread
will use a variable creator set by `strategy`, and will
enter its "cross-replica context".

In `OneDeviceStrategy`, all variables created inside `strategy.scope()`
will be on `device` specified at strategy construction time.
See example in the docs for this class.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager to use for creating variables with this strategy.
</td>
</tr>

</table>





