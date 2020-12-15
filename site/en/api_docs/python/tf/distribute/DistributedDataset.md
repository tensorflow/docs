description: Represents a dataset distributed among devices and machines.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.DistributedDataset" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__iter__"/>
</div>

# tf.distribute.DistributedDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/input_lib.py#L285-L486">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a dataset distributed among devices and machines.

<!-- Placeholder for "Used in" -->

A <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> could be thought of as a "distributed"
dataset. When you use <a href="../../tf/distribute.md"><code>tf.distribute</code></a> API to scale training to multiple
devices or machines, you also need to distribute the input data, which leads
to a <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> instance, instead of a
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance in the non-distributed case. In TF 2.x,
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> objects are Python iterables.

Note: <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> instances are *not* of type
<a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a>. It only supports two usages we will mention below:
iteration and `element_spec`. We don't support any other APIs to transform or
inspect the dataset.

There are two APIs to create a <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> object:
<a href="../../tf/distribute/Strategy.md#experimental_distribute_dataset"><code>tf.distribute.Strategy.experimental_distribute_dataset(dataset)</code></a>and
<a href="../../tf/distribute/Strategy.md#distribute_datasets_from_function"><code>tf.distribute.Strategy.distribute_datasets_from_function(dataset_fn)</code></a>.
*When to use which?* When you have a <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance, and the
regular batch splitting (i.e. re-batch the input <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance
with a new batch size that is equal to the global batch size divided by the
number of replicas in sync) and autosharding (i.e. the
<a href="../../tf/data/experimental/AutoShardPolicy.md"><code>tf.data.experimental.AutoShardPolicy</code></a> options) work for you, use the former
API. Otherwise, if you are *not* using a canonical <a href="../../tf/data/Dataset.md"><code>tf.data.Dataset</code></a> instance,
or you would like to customize the batch splitting or sharding, you can wrap
these logic in a `dataset_fn` and use the latter API. Both API handles
prefetch to device for the user. For more details and examples, follow the
links to the APIs.


There are two main usages of a `DistributedDataset` object:

1. Iterate over it to generate the input for a single device or multiple
devices, which is a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> instance. To do this,
you can:

  * use a pythonic for-loop construct:

    ```
    >>> global_batch_size = 4
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> dataset = tf.data.Dataset.from_tensors(([1.],[1.])).repeat(4).batch(global_batch_size)
    >>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
    >>> @tf.function
    ... def train_step(input):
    ...   features, labels = input
    ...   return labels - 0.3 * features
    >>> for x in dist_dataset:
    ...   # train_step trains the model using the dataset elements
    ...   loss = strategy.run(train_step, args=(x,))
    ...   print("Loss is", loss)
    Loss is PerReplica:{
      0: tf.Tensor(
    [[0.7]
     [0.7]], shape=(2, 1), dtype=float32),
      1: tf.Tensor(
    [[0.7]
     [0.7]], shape=(2, 1), dtype=float32)
    }
    ```

    Placing the loop inside a <a href="../../tf/function.md"><code>tf.function</code></a> will give a performance boost.
    However `break` and `return` are currently not supported if the loop is
    placed inside a <a href="../../tf/function.md"><code>tf.function</code></a>. We also don't support placing the loop
    inside a <a href="../../tf/function.md"><code>tf.function</code></a> when using
    <a href="../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> or
    <a href="../../tf/distribute/experimental/TPUStrategy.md"><code>tf.distribute.experimental.TPUStrategy</code></a> with multiple workers.

  * use `__iter__` to create an explicit iterator, which is of type
    <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a>

    ```
    >>> global_batch_size = 4
    >>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
    >>> train_dataset = tf.data.Dataset.from_tensors(([1.],[1.])).repeat(50).batch(global_batch_size)
    >>> train_dist_dataset = strategy.experimental_distribute_dataset(train_dataset)
    >>> @tf.function
    ... def distributed_train_step(dataset_inputs):
    ...   def train_step(input):
    ...     loss = tf.constant(0.1)
    ...     return loss
    ...   per_replica_losses = strategy.run(train_step, args=(dataset_inputs,))
    ...   return strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses,axis=None)
    >>> EPOCHS = 2
    >>> STEPS = 3
    >>> for epoch in range(EPOCHS):
    ...   total_loss = 0.0
    ...   num_batches = 0
    ...   dist_dataset_iterator = iter(train_dist_dataset)
    ...   for _ in range(STEPS):
    ...     total_loss += distributed_train_step(next(dist_dataset_iterator))
    ...     num_batches += 1
    ...   average_train_loss = total_loss / num_batches
    ...   template = ("Epoch {}, Loss: {:.4f}")
    ...   print (template.format(epoch+1, average_train_loss))
    Epoch 1, Loss: 0.2000
    Epoch 2, Loss: 0.2000
    ```


  To achieve a performance improvement, you can also wrap the `strategy.run`
  call with a <a href="../../tf/range.md"><code>tf.range</code></a> inside a <a href="../../tf/function.md"><code>tf.function</code></a>. This runs multiple steps in a
  <a href="../../tf/function.md"><code>tf.function</code></a>. Autograph will convert it to a <a href="../../tf/while_loop.md"><code>tf.while_loop</code></a> on the worker.
  However, it is less flexible comparing with running a single step inside
  <a href="../../tf/function.md"><code>tf.function</code></a>. For example, you cannot run things eagerly or arbitrary
  python code within the steps.


2. Inspect the <a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the data generated by `DistributedDataset`.

  <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> generates
  <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> as input to the devices. If you pass the
  input to a <a href="../../tf/function.md"><code>tf.function</code></a> and would like to specify the shape and type of
  each Tensor argument to the function, you can pass a <a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> object to
  the `input_signature` argument of the <a href="../../tf/function.md"><code>tf.function</code></a>. To get the
  <a href="../../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> of the input, you can use the `element_spec` property of the
  <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> or <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a>
  object.

  For example:

  ```
  >>> global_batch_size = 4
  >>> epochs = 1
  >>> steps_per_epoch = 1
  >>> mirrored_strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
  >>> dataset = tf.data.Dataset.from_tensors(([2.])).repeat(100).batch(global_batch_size)
  >>> dist_dataset = mirrored_strategy.experimental_distribute_dataset(dataset)
  >>> @tf.function(input_signature=[dist_dataset.element_spec])
  ... def train_step(per_replica_inputs):
  ...   def step_fn(inputs):
  ...     return tf.square(inputs)
  ...   return mirrored_strategy.run(step_fn, args=(per_replica_inputs,))
  >>> for _ in range(epochs):
  ...   iterator = iter(dist_dataset)
  ...   for _ in range(steps_per_epoch):
  ...     output = train_step(next(iterator))
  ...     print(output)
  PerReplica:{
    0: tf.Tensor(
  [[4.]
   [4.]], shape=(2, 1), dtype=float32),
    1: tf.Tensor(
  [[4.]
   [4.]], shape=(2, 1), dtype=float32)
  }
  ```


Visit the [tutorial](https://www.tensorflow.org/tutorials/distribute/input)
on distributed input for more examples and caveats.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`element_spec`
</td>
<td>
The type specification of an element of this <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.


```
>>> global_batch_size = 16
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> dataset = tf.data.Dataset.from_tensors(([1.],[2])).repeat(100).batch(global_batch_size)
>>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
>>> dist_dataset.element_spec
(PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
TensorSpec(shape=(None, 1), dtype=tf.float32, name=None)),
PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.int32, name=None),
TensorSpec(shape=(None, 1), dtype=tf.int32, name=None)))
```
</td>
</tr>
</table>



## Methods

<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/input_lib.py#L434-L456">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>

Creates an iterator for the <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

The returned iterator implements the Python Iterator protocol.

#### Example usage:



```
>>> global_batch_size = 4
>>> strategy = tf.distribute.MirroredStrategy(["GPU:0", "GPU:1"])
>>> dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4]).repeat().batch(global_batch_size)
>>> distributed_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> print(next(distributed_iterator))
PerReplica:{
  0: tf.Tensor([1 2], shape=(2,), dtype=int32),
  1: tf.Tensor([3 4], shape=(2,), dtype=int32)
}
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a> instance for the given
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> object to enumerate over the
distributed data.
</td>
</tr>

</table>





