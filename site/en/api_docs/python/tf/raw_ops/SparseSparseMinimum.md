description: Returns the element-wise min of two SparseTensors.

robots: noindex

# tf.raw_ops.SparseSparseMinimum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the element-wise min of two SparseTensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseSparseMinimum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseSparseMinimum(
    a_indices, a_values, a_shape, b_indices, b_values, b_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Assumes the two SparseTensors have the same shape, i.e., no broadcasting.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, in the canonical lexicographic ordering.
</td>
</tr><tr>
<td>
`a_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  `N` non-empty values corresponding to `a_indices`.
</td>
</tr><tr>
<td>
`a_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
</td>
</tr><tr>
<td>
`b_indices`
</td>
<td>
A `Tensor` of type `int64`.
counterpart to `a_indices` for the other operand.
</td>
</tr><tr>
<td>
`b_values`
</td>
<td>
A `Tensor`. Must have the same type as `a_values`.
counterpart to `a_values` for the other operand; must be of the same dtype.
</td>
</tr><tr>
<td>
`b_shape`
</td>
<td>
A `Tensor` of type `int64`.
counterpart to `a_shape` for the other operand; the two shapes must be equal.
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
A tuple of `Tensor` objects (output_indices, output_values).
</td>
</tr>
<tr>
<td>
`output_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`output_values`
</td>
<td>
A `Tensor`. Has the same type as `a_values`.
</td>
</tr>
</table>

