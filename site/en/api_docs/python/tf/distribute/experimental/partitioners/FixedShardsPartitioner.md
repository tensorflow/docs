description: Partitioner that allocates a fixed number of shards.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.partitioners.FixedShardsPartitioner" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.distribute.experimental.partitioners.FixedShardsPartitioner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/sharded_variable.py#L76-L104">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Partitioner that allocates a fixed number of shards.

Inherits From: [`Partitioner`](../../../../tf/distribute/experimental/partitioners/Partitioner.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.partitioners.FixedShardsPartitioner(
    num_shards
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:



```
>>> # standalone usage:
>>> partitioner = FixedShardsPartitioner(num_shards=2)
>>> partitions = partitioner(tf.TensorShape([10, 3]), tf.float32)
>>> [2, 1]
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
`num_shards`
</td>
<td>
`int`, number of shards to partition.
</td>
</tr>
</table>



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/sharded_variable.py#L100-L104">View source</a>

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





