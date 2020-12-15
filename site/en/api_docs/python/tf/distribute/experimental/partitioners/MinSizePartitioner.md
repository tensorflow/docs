description: Partitioner that allocates a minimum size per shard.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.partitioners.MinSizePartitioner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.distribute.experimental.partitioners.MinSizePartitioner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/sharded_variable.py#L108-L159">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Partitioner that allocates a minimum size per shard.

Inherits From: [`Partitioner`](../../../../tf/distribute/experimental/partitioners/Partitioner.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.partitioners.MinSizePartitioner(
    min_shard_bytes=(256 << 10), max_shards=1, bytes_per_string=16
)
</code></pre>



<!-- Placeholder for "Used in" -->

This partitioner ensures each shard has at least `min_shard_bytes`, and tries
to allocate as many shards as possible, i.e., keeping shard size as small as
possible. The maximum number of such shards (upper bound) is given by
`max_shards`.

#### Examples:



```
>>> partitioner = MinSizePartitioner(min_shard_bytes=4, max_shards=2)
>>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
>>> [2, 1]
>>> partitioner = MinSizePartitioner(min_shard_bytes=4, max_shards=10)
>>> partitions = partitioner(tf.TensorShape([6, 1]), tf.float32)
>>> [6, 1]
>>>
>>> # use in ParameterServerStrategy
>>> # strategy = tf.distribute.experimental.ParameterServerStrategy(
>>> #   cluster_resolver=cluster_resolver, variable_partitioner=partitioner)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`min_shard_bytes`
</td>
<td>
Minimum bytes of each shard. Defaults to 256K.
</td>
</tr><tr>
<td>
`max_shards`
</td>
<td>
Upper bound on the number of shards. Defaults to 1.
</td>
</tr><tr>
<td>
`bytes_per_string`
</td>
<td>
If the partition value is of type string, this provides
an estimate of how large each string is.
</td>
</tr>
</table>



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/sharded_variable.py#L154-L159">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    shape, dtype, axis=0
)
</code></pre>

Partitions the given `shape` and returns the partition results.

Examples of a partitioner that allocates a fixed number of shards:

```python
partitioner = FixedShardsPartitioner(num_shards=2)
partitions = partitioner(tf.TensorShape([10, 3], tf.float32), axis=0)
print(partitions) # [2, 0]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
a <a href="../../../../tf/TensorShape.md"><code>tf.TensorShape</code></a>, the shape to partition.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
a `tf.dtypes.Dtype` indicating the type of the partition value.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis to partition along.  Default: outermost axis.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of integers representing the number of partitions on each axis,
where i-th value correponds to i-th axis.
</td>
</tr>

</table>





