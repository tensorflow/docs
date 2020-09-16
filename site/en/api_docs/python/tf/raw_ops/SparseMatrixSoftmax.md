description: Calculates the softmax of a CSRSparseMatrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseMatrixSoftmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseMatrixSoftmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Calculates the softmax of a CSRSparseMatrix.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseMatrixSoftmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseMatrixSoftmax(
    logits, type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Calculate the softmax of the innermost dimensions of a SparseMatrix.

Missing values are treated as `-inf` (i.e., logits of zero probability); and
the output has the same sparsity structure as the input (though missing values
in the output may now be treated as having probability zero).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`logits`
</td>
<td>
A `Tensor` of type `variant`. A CSRSparseMatrix.
</td>
</tr><tr>
<td>
`type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64`.
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

