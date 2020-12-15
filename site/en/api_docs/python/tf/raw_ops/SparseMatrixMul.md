description: Element-wise multiplication of a sparse matrix with a dense tensor.

robots: noindex

# tf.raw_ops.SparseMatrixMul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Element-wise multiplication of a sparse matrix with a dense tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixMul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixMul(
    a, b, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a sparse matrix.

The dense tensor `b` may be either a scalar; otherwise `a` must be a rank-3
`SparseMatrix`; in this case `b` must be shaped `[batch_size, 1, 1]` and the
multiply operation broadcasts.

**NOTE** even if `b` is zero, the sparsity structure of the output does not
change.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
A `Tensor` of type `variant`. A CSRSparseMatrix.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. A dense tensor.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

