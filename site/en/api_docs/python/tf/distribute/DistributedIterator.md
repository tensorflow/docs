description: An iterator over <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.DistributedIterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="get_next"/>
<meta itemprop="property" content="get_next_as_optional"/>
</div>

# tf.distribute.DistributedIterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/input_lib.py#L146-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An iterator over <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

<!-- Placeholder for "Used in" -->

<a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a> is the primary mechanism for enumerating
elements of a <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>. It supports the Python
Iterator protocol, which means it can be iterated over using a for-loop or by
fetching individual elements explicitly via `get_next()`.

You can create a <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a> by calling `iter` on
a <a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a> or creating a python loop over a
<a href="../../tf/distribute/DistributedDataset.md"><code>tf.distribute.DistributedDataset</code></a>.

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
The type specification of an element of <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a>.


```
>>> global_batch_size = 16
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.from_tensors(([1.],[2])).repeat(100).batch(global_batch_size)
>>> distributed_iterator = iter(strategy.experimental_distribute_dataset(dataset))
>>> distributed_iterator.element_spec
(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
TensorSpec(shape=(None, 1), dtype=tf.int32, name=None))
```

The above example corresponds to the case where you have only one device. If
you have two devices, for example,
```python
strategy = tf.distribute.MirroredStrategy(['/gpu:0', '/gpu:1'])
```
Then the final line will print out:
```python
(PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.float32, name=None),
TensorSpec(shape=(None, 1), dtype=tf.float32, name=None)),
PerReplicaSpec(TensorSpec(shape=(None, 1), dtype=tf.int32, name=None),
TensorSpec(shape=(None, 1), dtype=tf.int32, name=None)))
```
</td>
</tr>
</table>



## Methods

<h3 id="get_next"><code>get_next</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/input_lib.py#L163-L200">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_next()
</code></pre>

Returns the next input from the iterator for all replicas.


#### Example use:



```
>>> strategy = tf.distribute.MirroredStrategy()
>>> dataset = tf.data.Dataset.range(100).batch(2)
>>> dist_dataset = strategy.experimental_distribute_dataset(dataset)
>>> dist_dataset_iterator = iter(dist_dataset)
>>> @tf.function
... def one_step(input):
...   return input
>>> step_num = 5
>>> for _ in range(step_num):
...   strategy.run(one_step, args=(dist_dataset_iterator.get_next(),))
>>> strategy.experimental_local_results(dist_dataset_iterator.get_next())
(<tf.Tensor: shape=(2,), dtype=int64, numpy=array([10, 11])>,)
```

The above example corresponds to the case where you have only one device. If
you have two devices, for example,
```python
strategy = tf.distribute.MirroredStrategy(['/gpu:0', '/gpu:1'])
```
Then the final line will print out:
```python
(<tf.Tensor: shape=(1,), dtype=int64, numpy=array([10])>,
 <tf.Tensor: shape=(1,), dtype=int64, numpy=array([11])>)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A single <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> or a <a href="../../tf/distribute/DistributedValues.md"><code>tf.distribute.DistributedValues</code></a> which contains
the next input for all replicas.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>
<tr class="alt">
<td colspan="2">
<a href="../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>: If the end of the iterator has been reached.
</td>
</tr>

</table>



<h3 id="get_next_as_optional"><code>get_next_as_optional</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/input_lib.py#L239-L271">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_next_as_optional()
</code></pre>

Returns a <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> that contains the next value for all replicas.

If the <a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a> has reached the end of the
sequence, the returned <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> will have no value.

#### Example usage:



```
>>> strategy = tf.distribute.MirroredStrategy()
>>> global_batch_size = 2
>>> steps_per_loop = 2
>>> dataset = tf.data.Dataset.range(10).batch(global_batch_size)
>>> distributed_iterator = iter(
...     strategy.experimental_distribute_dataset(dataset))
>>> def step_fn(x):
...   return x
>>> @tf.function
... def train_fn(distributed_iterator):
...   for _ in tf.range(steps_per_loop):
...     optional_data = distributed_iterator.get_next_as_optional()
...     if not optional_data.has_value():
...       break
...     tf.print(strategy.run(step_fn, args=(optional_data.get_value(),)))
>>> train_fn(distributed_iterator)
... # ([0 1],)
... # ([2 3],)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An <a href="../../tf/experimental/Optional.md"><code>tf.experimental.Optional</code></a> object representing the next value from the
<a href="../../tf/distribute/DistributedIterator.md"><code>tf.distribute.DistributedIterator</code></a> (if it has one) or no value.
</td>
</tr>

</table>



<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>






