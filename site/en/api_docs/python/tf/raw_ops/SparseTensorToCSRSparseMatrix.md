description: Converts a SparseTensor to a (possibly batched) CSRSparseMatrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseTensorToCSRSparseMatrix" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseTensorToCSRSparseMatrix

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts a SparseTensor to a (possibly batched) CSRSparseMatrix.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseTensorToCSRSparseMatrix`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseTensorToCSRSparseMatrix(
    indices, values, dense_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`. SparseTensor indices.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`.
SparseTensor values.
</td>
</tr><tr>
<td>
`dense_shape`
</td>
<td>
A `Tensor` of type `int64`. SparseTensor dense shape.
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

