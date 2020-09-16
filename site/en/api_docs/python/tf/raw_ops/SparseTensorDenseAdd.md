description: Adds up a SparseTensor and a dense Tensor, producing a dense Tensor.

robots: noindex

# tf.raw_ops.SparseTensorDenseAdd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adds up a `SparseTensor` and a dense `Tensor`, producing a dense `Tensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseTensorDenseAdd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseTensorDenseAdd(
    a_indices, a_values, a_shape, b, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op does not require `a_indices` be sorted in standard lexicographic order.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a_indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
2-D.  The `indices` of the `SparseTensor`, with shape `[nnz, ndims]`.
</td>
</tr><tr>
<td>
`a_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  The `values` of the `SparseTensor`, with shape `[nnz]`.
</td>
</tr><tr>
<td>
`a_shape`
</td>
<td>
A `Tensor`. Must have the same type as `a_indices`.
1-D.  The `shape` of the `SparseTensor`, with shape `[ndims]`.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. Must have the same type as `a_values`.
`ndims`-D Tensor.  With shape `a_shape`.
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
A `Tensor`. Has the same type as `a_values`.
</td>
</tr>

</table>

