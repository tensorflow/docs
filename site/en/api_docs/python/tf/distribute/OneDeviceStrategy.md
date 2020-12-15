description: A distribution strategy for running on a single device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.OneDeviceStrategy" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="experimental_assign_to_logical_device"/>
<meta itemprop="property" content="experimental_distribute_dataset"/>
<meta itemprop="property" content="experimental_distribute_datasets_from_function"/>
<meta itemprop="property" content="experimental_distribute_values_from_function"/>
<meta itemprop="property" content="experimental_local_results"/>
<meta itemprop="property" content="experimental_make_numpy_dataset"/>
<meta itemprop="property" content="experimental_replicate_to_logical_devices"/>
<meta itemprop="property" content="experimental_split_to_logical_devices"/>
<meta itemprop="property" content="reduce"/>
<meta itemprop="property" content="run"/>
<meta itemprop="property" content="scope"/>
</div>

# tf.distribute.OneDeviceStrategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L41-L233">
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
<a href="../../tf/distribute/experimental/TPUStrategy.md"><code>tf.distribute.experimental.TPUStrategy()</code></a>, there is a
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

<h3 id="experimental_assign_to_logical_device"><code>experimental_assign_to_logical_device</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1507-L1554">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_assign_to_logical_device(
    tensor, logical_device_id
)
</code></pre>

Adds annotation that `tensor` will be assigned to a logical device.

NOTE: This API is only supported in TPUStrategy for now.
This adds an annotation to `tensor` specifying that operations on
`tensor` will be invoked on logical core device id `logical_device_id`.
When model parallelism is used, the default behavior is that all ops
are placed on zero-th logical device.

```python

# Initializing TPU system with 2 logical devices and 4 replicas.
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
topology = tf.tpu.experimental.initialize_tpu_system(resolver)
device_assignment = tf.tpu.experimental.DeviceAssignment.build(
    topology,
    computation_shape=[1, 1, 1, 2],
    num_replicas=4)
strategy = tf.distribute.TPUStrategy(
    resolver, experimental_device_assignment=device_assignment)
iterator = iter(inputs)

@tf.function()
def step_fn(inputs):
  output = tf.add(inputs, inputs)

  # Add operation will be executed on logical device 0.
  output = strategy.experimental_assign_to_logical_device(output, 0)
  return output

strategy.run(step_fn, args=(next(iterator),))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
Input tensor to annotate.
</td>
</tr><tr>
<td>
`logical_device_id`
</td>
<td>
Id of the logical core to which the tensor will be
assigned.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
The logical device id presented is not consistent with total
number of partitions specified by the device assignment.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Annotated tensor with idential value as `tensor`.
</td>
</tr>

</table>



<h3 id="experimental_distribute_dataset"><code>experimental_distribute_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L84-L110">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset
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



<h3 id="experimental_distribute_datasets_from_function"><code>experimental_distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L112-L150">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_datasets_from_function(
    dataset_fn
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

inputs = strategy.experimental_distribute_datasets_from_function(dataset_fn)

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



<h3 id="experimental_distribute_values_from_function"><code>experimental_distribute_values_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1668-L1741">View source</a>

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
>>> strategy = tf.distribute.MirroredStrategy()
>>> def value_fn(ctx):
...   return tf.constant(1.)
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(<tf.Tensor: shape=(), dtype=float32, numpy=1.0>,)
```

2. Distribute values in array based on replica_id:

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> array_value = np.array([3., 2., 1.])
>>> def value_fn(ctx):
...   return array_value[ctx.replica_id_in_sync_group]
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(3.0,)
```

3. Specify values using num_replicas_in_sync:

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> def value_fn(ctx):
...   return ctx.num_replicas_in_sync
>>> distributed_values = (
...      strategy.experimental_distribute_values_from_function(
...        value_fn))
>>> local_result = strategy.experimental_local_results(distributed_values)
>>> local_result
(1,)
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L152-L166">View source</a>

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



<h3 id="experimental_make_numpy_dataset"><code>experimental_make_numpy_dataset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L903-L934">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_make_numpy_dataset(
    numpy_input
)
</code></pre>

Makes a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> from a numpy array. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2020-09-30.
Instructions for updating:
Please use tf.data.Dataset.from_tensor_slices instead

This avoids adding `numpy_input` as a large constant in the graph,
and copies the data to the machine or machines that will be processing
the input.

Note that you will likely need to use `experimental_distribute_dataset`
with the returned dataset to further distribute it with the strategy.

#### Example:



```
>>> strategy = tf.distribute.MirroredStrategy()
>>> numpy_input = np.ones([10], dtype=np.float32)
>>> dataset = strategy.experimental_make_numpy_dataset(numpy_input)
>>> dataset
<TensorSliceDataset shapes: (), types: tf.float32>
>>> dataset = dataset.batch(2)
>>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
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
a nest of NumPy input arrays that will be converted into a
dataset. Note that the NumPy arrays are stacked, as that is normal
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> behavior.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> representing `numpy_input`.
</td>
</tr>

</table>



<h3 id="experimental_replicate_to_logical_devices"><code>experimental_replicate_to_logical_devices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1619-L1666">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_replicate_to_logical_devices(
    tensor
)
</code></pre>

Adds annotation that `tensor` will be replicated to all logical devices.

NOTE: This API is only supported in TPUStrategy for now.
This adds an annotation to tensor `tensor` specifying that operations on
`tensor` will be invoked on all logical devices.

```python
# Initializing TPU system with 2 logical devices and 4 replicas.
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
topology = tf.tpu.experimental.initialize_tpu_system(resolver)
device_assignment = tf.tpu.experimental.DeviceAssignment.build(
    topology,
    computation_shape=[1, 1, 1, 2],
    num_replicas=4)
strategy = tf.distribute.TPUStrategy(
    resolver, experimental_device_assignment=device_assignment)

iterator = iter(inputs)

@tf.function()
def step_fn(inputs):
  images, labels = inputs
  images = strategy.experimental_split_to_logical_devices(
    inputs, [1, 2, 4, 1])

  # model() function will be executed on 8 logical devices with `inputs`
  # split 2 * 4  ways.
  output = model(inputs)

  # For loss calculation, all logical devices share the same logits
  # and labels.
  labels = strategy.experimental_replicate_to_logical_devices(labels)
  output = strategy.experimental_replicate_to_logical_devices(output)
  loss = loss_fn(labels, output)

  return loss

strategy.run(step_fn, args=(next(iterator),))
```
Args:
  tensor: Input tensor to annotate.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Annotated tensor with idential value as `tensor`.
</td>
</tr>

</table>



<h3 id="experimental_split_to_logical_devices"><code>experimental_split_to_logical_devices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1556-L1617">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_split_to_logical_devices(
    tensor, partition_dimensions
)
</code></pre>

Adds annotation that `tensor` will be split across logical devices.

NOTE: This API is only supported in TPUStrategy for now.
This adds an annotation to tensor `tensor` specifying that operations on
`tensor` will be be split among multiple logical devices. Tensor `tensor`
will be split across dimensions specified by `partition_dimensions`.
The dimensions of `tensor` must be divisible by corresponding value in
`partition_dimensions`.

For example, for system with 8 logical devices, if `tensor` is an image
tensor with shape (batch_size, width, height, channel) and
`partition_dimensions` is [1, 2, 4, 1], then `tensor` will be split
2 in width dimension and 4 way in height dimension and the split
tensor values will be fed into 8 logical devices.

```python
# Initializing TPU system with 8 logical devices and 1 replica.
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
topology = tf.tpu.experimental.initialize_tpu_system(resolver)
device_assignment = tf.tpu.experimental.DeviceAssignment.build(
    topology,
    computation_shape=[1, 2, 2, 2],
    num_replicas=1)
strategy = tf.distribute.TPUStrategy(
    resolver, experimental_device_assignment=device_assignment)

iterator = iter(inputs)

@tf.function()
def step_fn(inputs):
  inputs = strategy.experimental_split_to_logical_devices(
    inputs, [1, 2, 4, 1])

  # model() function will be executed on 8 logical devices with `inputs`
  # split 2 * 4  ways.
  output = model(inputs)
  return output

strategy.run(step_fn, args=(next(iterator),))
```
Args:
  tensor: Input tensor to annotate.
  partition_dimensions: An unnested list of integers with the size equal to
    rank of `tensor` specifying how `tensor` will be partitioned. The
    product of all elements in `partition_dimensions` must be equal to the
    total number of logical devices per replica.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
1) If the size of partition_dimensions does not equal to rank
of `tensor` or 2) if product of elements of `partition_dimensions` does
not match the number of logical devices per replica defined by the
implementing DistributionStrategy's device specification or
3) if a known size of `tensor` is not divisible by corresponding
value in `partition_dimensions`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Annotated tensor with idential value as `tensor`.
</td>
</tr>

</table>



<h3 id="reduce"><code>reduce</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L186-L217">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L168-L184">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/one_device_strategy.py#L219-L233">View source</a>

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





