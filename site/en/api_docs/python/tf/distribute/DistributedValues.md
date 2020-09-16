description: Base class for representing distributed values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.DistributedValues" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.distribute.DistributedValues

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/values.py#L59-L170">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for representing distributed values.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.DistributedValues(
    values
)
</code></pre>



<!-- Placeholder for "Used in" -->

A subclass instance of DistributedValues is created when creating variables
within a distribution strategy, iterating a `tf.Dataset` or through
`strategy.run`.  This base class should never be instantiated
directly.  DistributedValues contains a value per replica.  Depending on
the subclass, the values could either be synced on update, synced on demand,
or never synced.

DistributedValues can be reduced to obtain single value across replicas,
as input into `run` or the per replica values inspected
using `experimental_local_results`.

#### Example usage:



1. Created from Dataset:

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.from_tensor_slices([5., 6., 7., 8.]).batch(2)
>>> dataset_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> distributed_values = next(dataset_iterator)
```

2. Returned by `run`:

```
>>> strategy = tf.distribute.MirroredStrategy()
>>> @tf.function
... def run():
...   ctx = tf.distribute.get_replica_context()
...   return ctx.replica_id_in_sync_group
>>> distributed_values = strategy.run(run)
```

3. As input into `run`:
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.from_tensor_slices([5., 6., 7., 8.]).batch(2)
>>> dataset_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> distributed_values = next(dataset_iterator)
>>> @tf.function
... def run(input):
...   return input + 1.0
>>> updated_value = strategy.run(run,
...                                              args=(distributed_values,))

4. Reduce value
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.from_tensor_slices([5., 6., 7., 8.]).batch(2)
>>> dataset_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> distributed_values = next(dataset_iterator)
>>> reduced_value = strategy.reduce(tf.distribute.ReduceOp.SUM,
...                                 distributed_values,
...                                 axis = 0)

5. Inspect per replica values.
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.from_tensor_slices([5., 6., 7., 8.]).batch(2)
>>> dataset_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> per_replica_values = strategy.experimental_local_results(
...    distributed_values)
>>> per_replica_values
(<tf.Tensor: shape=(2,), dtype=float32,
 numpy=array([5., 6.], dtype=float32)>,)

