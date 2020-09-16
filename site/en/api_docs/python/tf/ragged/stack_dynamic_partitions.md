description: Stacks dynamic partitions of a Tensor or RaggedTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.ragged.stack_dynamic_partitions" />
<meta itemprop="path" content="Stable" />
</div>

# tf.ragged.stack_dynamic_partitions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/ragged/ragged_array_ops.py#L536-L635">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stacks dynamic partitions of a Tensor or RaggedTensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.ragged.stack_dynamic_partitions`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.ragged.stack_dynamic_partitions(
    data, partitions, num_partitions, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a RaggedTensor `output` with `num_partitions` rows, where the row
`output[i]` is formed by stacking all slices `data[j1...jN]` such that
`partitions[j1...jN] = i`.  Slices of `data` are stacked in row-major
order.

If `num_partitions` is an `int` (not a `Tensor`), then this is equivalent to
`tf.ragged.stack(tf.dynamic_partition(data, partitions, num_partitions))`.

#### Example:

```
>>> data           = ['a', 'b', 'c', 'd', 'e']
>>> partitions     = [  3,   0,   2,   2,   3]
>>> num_partitions = 5
>>> tf.ragged.stack_dynamic_partitions(data, partitions, num_partitions)
<tf.RaggedTensor [[b'b'], [], [b'c', b'd'], [b'a', b'e'], []]>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`data`
</td>
<td>
A `Tensor` or `RaggedTensor` containing the values to stack.
</td>
</tr><tr>
<td>
`partitions`
</td>
<td>
An `int32` or `int64` `Tensor` or `RaggedTensor` specifying the
partition that each slice of `data` should be added to.
`partitions.shape` must be a prefix of `data.shape`.  Values must be
greater than or equal to zero, and less than `num_partitions`.
`partitions` is not required to be sorted.
</td>
</tr><tr>
<td>
`num_partitions`
</td>
<td>
An `int32` or `int64` scalar specifying the number of
partitions to output.  This determines the number of rows in `output`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensor (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `RaggedTensor` containing the stacked partitions.  The returned tensor
has the same dtype as `data`, and its shape is
`[num_partitions, (D)] + data.shape[partitions.rank:]`, where `(D)` is a
ragged dimension whose length is the number of data slices stacked for
each `partition`.
</td>
</tr>

</table>

