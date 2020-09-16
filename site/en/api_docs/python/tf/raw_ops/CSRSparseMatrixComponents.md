description: Reads out the CSR components at batch index.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.CSRSparseMatrixComponents" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.CSRSparseMatrixComponents

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reads out the CSR components at batch `index`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CSRSparseMatrixComponents`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CSRSparseMatrixComponents(
    csr_sparse_matrix, index, type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op is meant only for debugging / testing, and its interface is not expected
to be stable.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`csr_sparse_matrix`
</td>
<td>
A `Tensor` of type `variant`.
A batched CSRSparseMatrix.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
A `Tensor` of type `int32`.
The index in `csr_sparse_matrix`'s batch.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64, tf.complex64, tf.complex128`.
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
A tuple of `Tensor` objects (row_ptrs, col_inds, values).
</td>
</tr>
<tr>
<td>
`row_ptrs`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`col_inds`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor` of type `type`.
</td>
</tr>
</table>

