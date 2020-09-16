description: Sparse addition of two CSR matrices, C = alpha * A + beta * B.

robots: noindex

# tf.raw_ops.SparseMatrixAdd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Sparse addition of two CSR matrices, C = alpha * A + beta * B.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixAdd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixAdd(
    a, b, alpha, beta, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The gradients of SparseMatrixAdd outputs with respect to alpha and beta are not
currently defined (TensorFlow will return zeros for these entries).

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
A `Tensor` of type `variant`. A CSRSparseMatrix.
</td>
</tr><tr>
<td>
`alpha`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`.
A constant scalar.
</td>
</tr><tr>
<td>
`beta`
</td>
<td>
A `Tensor`. Must have the same type as `alpha`. A constant scalar.
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

