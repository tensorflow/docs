description: Converts a RaggedTensor into a SparseTensor with the same values.

robots: noindex

# tf.raw_ops.RaggedTensorToSparse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts a `RaggedTensor` into a `SparseTensor` with the same values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedTensorToSparse`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedTensorToSparse(
    rt_nested_splits, rt_dense_values, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

input=ragged.from_nested_row_splits(rt_dense_values, rt_nested_splits)
output=SparseTensor(indices=sparse_indices, values=sparse_values,
                    dense_shape=sparse_dense_shape)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`rt_nested_splits`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
The `row_splits` for the `RaggedTensor`.
</td>
</tr><tr>
<td>
`rt_dense_values`
</td>
<td>
A `Tensor`. The `flat_values` for the `RaggedTensor`.
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
A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_dense_shape).
</td>
</tr>
<tr>
<td>
`sparse_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A `Tensor`. Has the same type as `rt_dense_values`.
</td>
</tr><tr>
<td>
`sparse_dense_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

