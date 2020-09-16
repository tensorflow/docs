description: Reorders a SparseTensor into the canonical, row-major ordering.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseReorder" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseReorder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reorders a SparseTensor into the canonical, row-major ordering.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseReorder`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseReorder(
    input_indices, input_values, input_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that by convention, all sparse ops preserve the canonical ordering along
increasing dimension number. The only time ordering can be violated is during
manual manipulation of the indices and values vectors to add entries.

Reordering does not affect the shape of the SparseTensor.

If the tensor has rank `R` and `N` non-empty values, `input_indices` has
shape `[N, R]`, input_values has length `N`, and input_shape has length `R`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `N x R` matrix with the indices of non-empty values in a
SparseTensor, possibly not in canonical ordering.
</td>
</tr><tr>
<td>
`input_values`
</td>
<td>
A `Tensor`.
1-D.  `N` non-empty values corresponding to `input_indices`.
</td>
</tr><tr>
<td>
`input_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
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
A `Tensor`. Has the same type as `input_values`.
</td>
</tr>
</table>

