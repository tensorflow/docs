description: Returns a RaggedTensor containing the specified sequences of numbers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RaggedRange" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RaggedRange

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns a `RaggedTensor` containing the specified sequences of numbers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedRange`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedRange(
    starts, limits, deltas, Tsplits=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


Returns a `RaggedTensor` `result` composed from `rt_dense_values` and
`rt_nested_splits`, such that
`result[i] = range(starts[i], limits[i], deltas[i])`.

```python
(rt_nested_splits, rt_dense_values) = ragged_range(
      starts=[2, 5, 8], limits=[3, 5, 12], deltas=1)
result = tf.ragged.from_row_splits(rt_dense_values, rt_nested_splits)
print(result)
<tf.RaggedTensor [[2], [], [8, 9, 10, 11]] >
```

The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
The vector inputs must all have the same size.  Scalar inputs are broadcast
to match the size of the vector inputs.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`starts`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`, `int32`, `int64`.
The starts of each range.
</td>
</tr><tr>
<td>
`limits`
</td>
<td>
A `Tensor`. Must have the same type as `starts`.
The limits of each range.
</td>
</tr><tr>
<td>
`deltas`
</td>
<td>
A `Tensor`. Must have the same type as `starts`.
The deltas of each range.
</td>
</tr><tr>
<td>
`Tsplits`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple of `Tensor` objects (rt_nested_splits, rt_dense_values).
</td>
</tr>
<tr>
<td>
`rt_nested_splits`
</td>
<td>
A `Tensor` of type `Tsplits`.
</td>
</tr><tr>
<td>
`rt_dense_values`
</td>
<td>
A `Tensor`. Has the same type as `starts`.
</td>
</tr>
</table>

