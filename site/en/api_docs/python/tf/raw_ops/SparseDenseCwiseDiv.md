description: Component-wise divides a SparseTensor by a dense Tensor.

robots: noindex

# tf.raw_ops.SparseDenseCwiseDiv

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Component-wise divides a SparseTensor by a dense Tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseDenseCwiseDiv`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseDenseCwiseDiv(
    sp_indices, sp_values, sp_shape, dense, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

*Limitation*: this Op only broadcasts the dense side to the sparse side, but not
the other direction.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
</td>
</tr><tr>
<td>
`sp_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D.  `N` non-empty values corresponding to `sp_indices`.
</td>
</tr><tr>
<td>
`sp_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
</td>
</tr><tr>
<td>
`dense`
</td>
<td>
A `Tensor`. Must have the same type as `sp_values`.
`R`-D.  The dense Tensor operand.
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
A `Tensor`. Has the same type as `sp_values`.
</td>
</tr>

</table>

