description: A state & compute distribution policy on a list of devices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.Strategy" />
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

# tf.distribute.Strategy

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1503-L1741">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A state & compute distribution policy on a list of devices.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.Strategy(
    extended
)
</code></pre>



<!-- Placeholder for "Used in" -->

See [the guide](https://www.tensorflow.org/guide/distributed_training)
for overview and examples. See <a href="../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> and
[`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
for a glossory of concepts mentioned on this page such as "per-replica",
_replica_, and _reduce_.

#### In short:



* To use it with Keras `compile`/`fit`,
  [please
  read](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_keras).
* You may pass descendant of <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> to
  <a href="../../tf/estimator/RunConfig.md"><code>tf.estimator.RunConfig</code></a> to specify how a <a href="../../tf/estimator/Estimator.md"><code>tf.estimator.Estimator</code></a>
  should distribute its computation. See
  [guide](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_estimator_limited_support).
* Otherwise, use <a href="../../tf/distribute/Strategy.md#scope"><code>tf.distribute.Strategy.scope</code></a> to specify that a
  strategy should be used when building an executing your model.
  (This puts you in the "cross-replica context" for this strategy, which
  means the strategy is put in control of things like variable placement.)
* If you are writing a custom training loop, you will need to call a few more
  methods,
  [see the
  guide](https://www.tensorflow.org/guide/distributed_training#using_tfdistributestrategy_with_custom_training_loops):

    * Start by either creating a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> normally or using
      `tf.distribute.experimental_make_numpy_dataset` to make a dataset out of
      a `numpy` array.
    * Use <a href="../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> to convert
      a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> to something that produces "per-replica" values.
      If you want to manually specify how the dataset should be partitioned
      across replicas, use
      <a href="../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a>
      instead.
    * Use <a href="../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> to run a function
      once per replica, taking values that may be "per-replica" (e.g.
      from a <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> object) and returning
      "per-replica" values.
      This function is executed in "replica context", which means each
      operation is performed separately on each replica.
    * Finally use a method (such as <a href="../../tf/distribute/Strategy.md#reduce"><code>tf.distribute.Strategy.reduce</code></a>) to
      convert the resulting "per-replica" values into ordinary `Tensor`s.

A custom training loop can be as simple as:

```
with my_strategy.scope():
  @tf.function
  def distribute_train_epoch(dataset):
    def replica_fn(input):
      # process input and return result
      return result

    total_result = 0
    for x in dataset:
      per_replica_result = my_strategy.run(replica_fn, args=(x,))
      total_result += my_strategy.reduce(tf.distribute.ReduceOp.SUM,
                                         per_replica_result, axis=None)
    return total_result

  dist_dataset = my_strategy.experimental_distribute_dataset(dataset)
  for _ in range(EPOCHS):
    train_result = distribute_train_epoch(dist_dataset)
```

This takes an ordinary `dataset` and `replica_fn` and runs it
distributed using a particular <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> named
`my_strategy` above. Any variables created in `replica_fn` are created
using `my_strategy`'s policy, and library functions called by
`replica_fn` can use the `get_replica_context()` API to implement
distributed-specific behavior.

You can use the `reduce` API to aggregate results across replicas and use
this as a return value from one iteration over a
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>. Or
you can use <a href="../../tf/keras/metrics.md"><code>tf.keras.metrics</code></a> (such as loss, accuracy, etc.) to
accumulate metrics across steps in a given epoch.

See the
[custom training loop
tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training)
for a more detailed example.

Note: <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> currently does not support TensorFlow's
partitioned variables (where a single variable is split across multiple
devices) at this time.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L943-L1052">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_dataset(
    dataset, options=None
)
</code></pre>

Creates <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>.

The returned <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> can be iterated over
similar to how regular datasets can.
NOTE: The user cannot add any more transformations to a
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

The following is an example:

```python
strategy = tf.distribute.MirroredStrategy()

# Create a dataset
dataset = dataset_ops.Dataset.TFRecordDataset([
  "/a/1.tfr", "/a/2.tfr", "/a/3.tfr", "/a/4.tfr"])

# Distribute that dataset
dist_dataset = strategy.experimental_distribute_dataset(dataset)

# Iterate over the `tf.distribute.DistributedDataset`
for x in dist_dataset:
  # process dataset elements
  strategy.run(replica_fn, args=(x,))
```

In the code snippet above, the <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>
`dist_dataset` is batched by `GLOBAL_BATCH_SIZE`, and we iterate through it
using `for x in dist_dataset`. `x` a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>
containing data for all replicas, which aggregates to a batch of
`GLOBAL_BATCH_SIZE`. <a href="../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> will take care of feeding
the right per-replica data in `x` to the right `replica_fn` executed on each
replica.

What's under the hood of this method, when we say the <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>
instance - `dataset` - gets distributed? It depends on how you set the
<a href="../../tf/data/experimental/AutoShardPolicy.md"><code>tf.data.experimental.AutoShardPolicy</code></a> through
<a href="../../tf/data/experimental/DistributeOptions.md"><code>tf.data.experimental.DistributeOptions</code></a>. By default, it is set to
<a href="../../tf/data/experimental/AutoShardPolicy.md#AUTO"><code>tf.data.experimental.AutoShardPolicy.AUTO</code></a>. In a multi-worker setting, we
will first attempt to distribute `dataset` by detecting whether `dataset` is
being created out of reader datasets (e.g. <a href="../../tf/data/TFRecordDataset.md"><code>tf.data.TFRecordDataset</code></a>,
<a href="../../tf/data/TextLineDataset.md"><code>tf.data.TextLineDataset</code></a>, etc.) and if so, try to shard the input files.
Note that there has to be at least one input file per worker. If you have
less than one input file per worker, we suggest that you disable dataset
sharding across workers, by setting the
<a href="../../tf/data/experimental/DistributeOptions.md#auto_shard_policy"><code>tf.data.experimental.DistributeOptions.auto_shard_policy</code></a> to be
<a href="../../tf/data/experimental/AutoShardPolicy.md#OFF"><code>tf.data.experimental.AutoShardPolicy.OFF</code></a>.

If the attempt to shard by file is unsuccessful (i.e. the dataset is not
read from files), we will shard the dataset evenly at the end by
appending a `.shard` operation to the end of the processing pipeline. This
will cause the entire preprocessing pipeline for all the data to be run on
every worker, and each worker will do redundant work. We will print a
warning if this route is selected.

As mentioned before, within each worker, we will also split the data among
all the worker devices (if more than one a present). This will happen
even if multi-worker sharding is disabled.

If the above batch splitting and dataset sharding logic is undesirable,
please use
<a href="../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a>
instead, which does not do any automatic splitting or sharding.

You can also use the `element_spec` property of the
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> instance returned by this API to query
the <a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned
by the iterator. This can be used to set the `input_signature` property
of a <a href="../../tf/function.md"><code>tf.function</code></a>.

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

# Iterate over the `tf.distribute.DistributedDataset`
for x in dist_dataset:
  # process dataset elements
  strategy.run(train_step, args=(x,))
```

Note: The order in which the data is processed by the workers when using
<a href="../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> that will be sharded across all replicas using
the rules stated above.
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
A <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
</td>
</tr>

</table>



<h3 id="experimental_distribute_datasets_from_function"><code>experimental_distribute_datasets_from_function</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1054-L1128">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_distribute_datasets_from_function(
    dataset_fn, options=None
)
</code></pre>

Distributes <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instances created by calls to `dataset_fn`.

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

The `dataset_fn` should take an <a href="../../tf/distribute/InputContext.md"><code>tf.distribute.InputContext</code></a> instance where
information about batching and input replication can be accessed.

You can also use the `element_spec` property of the
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> returned by this API to query the
<a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the elements returned by the iterator. This can be used to
set the `input_signature` property of a <a href="../../tf/function.md"><code>tf.function</code></a>.

```
>>> global_batch_size = 8
>>> def dataset_fn(input_context):
...   batch_size = input_context.get_per_replica_batch_size(
...                    global_batch_size)
...   d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
...   return d.shard(
...       input_context.num_input_pipelines,
...       input_context.input_pipeline_id)
```

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> ds = strategy.experimental_distribute_datasets_from_function(dataset_fn)
```

```
>>> def train(ds):
...   @tf.function(input_signature=[ds.element_spec])
...   def step_fn(inputs):
...     # train the model with inputs
...     return inputs
```

...   for batch in ds:
...     replica_results = strategy.run(replica_fn, args=(batch,))
>>> train(ds)

IMPORTANT: The <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> returned by `dataset_fn` should have a
per-replica batch size, unlike `experimental_distribute_dataset`, which uses
the global batch size.  This may be computed using
`input_context.get_per_replica_batch_size`.


Note: The order in which the data is processed by the workers when using
<a href="../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a> is
not guaranteed. This is typically required if you are using
<a href="../../tf/distribute.md"><code>tf.distribute</code></a> to scale prediction. You can however insert an index for
each element in the batch and order outputs accordingly. Refer to [this
snippet](https://www.tensorflow.org/tutorials/distribute/input#caveats)
for an example of how to order outputs.

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
A <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1373-L1390">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>experimental_local_results(
    value
)
</code></pre>

Returns the list of all local per-replica values contained in `value`.

Note: This only returns values on the worker initiated by this client.
When using a <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> like
<a href="../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a>, each worker
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1219-L1349">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reduce(
    reduce_op, value, axis
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
<a href="../../tf/distribute/ReduceOp.md#MEAN"><code>tf.distribute.ReduceOp.MEAN</code></a>, using `axis=0` will use the correct
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L1130-L1211">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fn, args=(), kwargs=None, options=None
)
</code></pre>

Run `fn` on each replica, with the given arguments.

Executes ops specified by `fn` on each replica. If `args` or `kwargs` have
<a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, such as those produced by a
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> from
<a href="../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset</code></a> or
<a href="../../tf/distribute/Strategy.md#experimental_distribute_datasets_from_function"><code>tf.distribute.Strategy.experimental_distribute_datasets_from_function</code></a>,
when `fn` is executed on a particular replica, it will be executed with the
component of <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> that correspond to that
replica.

`fn` may call <a href="../../tf/distribute/get_replica_context.md"><code>tf.distribute.get_replica_context()</code></a> to access members such
as `all_reduce`.

All arguments in `args` or `kwargs` should either be nest of tensors or
<a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> containing tensors or composite tensors.

IMPORTANT: Depending on the implementation of <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> and
whether eager execution is enabled, `fn` may be called one or more times. If
`fn` is annotated with <a href="../../tf/function.md"><code>tf.function</code></a> or <a href="../../tf/distribute/Strategy.md#run"><code>tf.distribute.Strategy.run</code></a> is
called inside a <a href="../../tf/function.md"><code>tf.function</code></a>, eager execution is disabled and `fn` is
called once (or once per replica, if you are using MirroredStrategy) to
generate a Tensorflow graph, which will then be reused for execution with
new inputs. Otherwise, if eager execution is enabled, `fn` will be called
every step just like regular python code.

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
Merged return value of `fn` across replicas. The structure of the return
value is the same as the return value from `fn`. Each element in the
structure can either be <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a>, `Tensor`
objects, or `Tensor`s (for example, if running on a single replica).
</td>
</tr>

</table>



<h3 id="scope"><code>scope</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/distribute_lib.py#L791-L878">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>scope()
</code></pre>

Context manager to make the strategy current and distribute variables.

This method returns a context manager, and is used as follows:

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> # Variable created inside scope:
>>> with strategy.scope():
...   mirrored_variable = tf.Variable(1.)
>>> mirrored_variable
MirroredVariable:{
  0: <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
}
>>> # Variable created outside scope:
>>> regular_variable = tf.Variable(1.)
>>> regular_variable
<tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>
```

_What happens when Strategy.scope is entered?_

* `strategy` is installed in the global context as the "current" strategy.
  Inside this scope, <a href="../../tf/distribute/get_strategy.md"><code>tf.distribute.get_strategy()</code></a> will now return this
  strategy. Outside this scope, it returns the default no-op strategy.
* Entering the scope also enters the "cross-replica context". See
  <a href="../../tf/distribute/StrategyExtended.md"><code>tf.distribute.StrategyExtended</code></a> for an explanation on cross-replica and
  replica contexts.
* Variable creation inside `scope` is intercepted by the strategy. Each
  strategy defines how it wants to affect the variable creation. Sync
  strategies like `MirroredStrategy`, `TPUStrategy` and
  `MultiWorkerMiroredStrategy` create variables replicated on each replica,
  whereas `ParameterServerStrategy` creates variables on the parameter
  servers. This is done using a custom <a href="../../tf/variable_creator_scope.md"><code>tf.variable_creator_scope</code></a>.
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
* When a <a href="../../tf/keras/Model.md"><code>tf.keras.Model</code></a> is created inside a `strategy.scope`, we capture
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
  ** Creating the input datasets
  ** Defining <a href="../../tf/function.md"><code>tf.function</code></a>s that represent your training step
  ** Saving APIs such as <a href="../../tf/saved_model/save.md"><code>tf.saved_model.save</code></a>. Loading creates variables,
     so that should go inside the scope if you want to train the model in a
     distributed way.
  ** Checkpoint saving. As mentioned above - `checkpoint.restore` may
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





