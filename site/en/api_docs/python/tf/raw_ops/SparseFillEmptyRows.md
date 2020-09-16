description: Fills empty rows in the input 2-D SparseTensor with a default value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseFillEmptyRows" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseFillEmptyRows

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Fills empty rows in the input 2-D `SparseTensor` with a default value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseFillEmptyRows`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseFillEmptyRows(
    indices, values, dense_shape, default_value, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The input `SparseTensor` is represented via the tuple of inputs
(`indices`, `values`, `dense_shape`).  The output `SparseTensor` has the
same `dense_shape` but with indices `output_indices` and values
`output_values`.

This op inserts a single entry for every row that doesn't have any values.
The index is created as `[row, 0, ..., 0]` and the inserted value
is `default_value`.

For example, suppose `sp_input` has shape `[5, 6]` and non-empty values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

Rows 1 and 4 are empty, so the output will be of shape `[5, 6]` with values:

    [0, 1]: a
    [0, 3]: b
    [1, 0]: default_value
    [2, 0]: c
    [3, 1]: d
    [4, 0]: default_value

The output `SparseTensor` will be in row-major order and will have the
same shape as the input.

This op also returns an indicator vector shaped `[dense_shape[0]]` such that

    empty_row_indicator[i] = True iff row i was an empty row.

And a reverse index map vector shaped `[indices.shape[0]]` that is used during
backpropagation,

    reverse_index_map[j] = out_j s.t. indices[j, :] == output_indices[out_j, :]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D. the indices of the sparse tensor.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`. 1-D. the values of the sparse tensor.
</td>
</tr><tr>
<td>
`dense_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D. the shape of the sparse tensor.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A `Tensor`. Must have the same type as `values`.
0-D. default value to insert into location `[row, 0, ..., 0]`
for rows missing from the input sparse tensor.
output indices: 2-D. the indices of the filled sparse tensor.
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
A tuple of `Tensor` objects (output_indices, output_values, empty_row_indicator, reverse_index_map).
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
A `Tensor`. Has the same type as `values`.
</td>
</tr><tr>
<td>
`empty_row_indicator`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`reverse_index_map`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

