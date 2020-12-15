description: The gradient operator for the SparseAdd op.

robots: noindex

# tf.raw_ops.SparseAddGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



The gradient operator for the SparseAdd op.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseAddGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseAddGrad(
    backprop_val_grad, a_indices, b_indices, sum_indices, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The SparseAdd op calculates A + B, where A, B, and the sum are all represented
as `SparseTensor` objects.  This op takes in the upstream gradient w.r.t.
non-empty values of the sum, and outputs the gradients w.r.t. the non-empty
values of A and B.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`backprop_val_grad`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
1-D with shape `[nnz(sum)]`.  The gradient with respect to
the non-empty values of the sum.
</td>
</tr><tr>
<td>
`a_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  The `indices` of the `SparseTensor` A, size `[nnz(A), ndims]`.
</td>
</tr><tr>
<td>
`b_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  The `indices` of the `SparseTensor` B, size `[nnz(B), ndims]`.
</td>
</tr><tr>
<td>
`sum_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  The `indices` of the sum `SparseTensor`, size
`[nnz(sum), ndims]`.
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
A tuple of `Tensor` objects (a_val_grad, b_val_grad).
</td>
</tr>
<tr>
<td>
`a_val_grad`
</td>
<td>
A `Tensor`. Has the same type as `backprop_val_grad`.
</td>
</tr><tr>
<td>
`b_val_grad`
</td>
<td>
A `Tensor`. Has the same type as `backprop_val_grad`.
</td>
</tr>
</table>

