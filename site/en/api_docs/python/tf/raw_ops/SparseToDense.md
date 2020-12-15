description: Converts a sparse representation into a dense tensor.

robots: noindex

# tf.raw_ops.SparseToDense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts a sparse representation into a dense tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseToDense`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseToDense(
    sparse_indices, output_shape, sparse_values, default_value,
    validate_indices=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Builds an array `dense` with shape `output_shape` such that

```
# If sparse_indices is scalar
dense[i] = (i == sparse_indices ? sparse_values : default_value)

# If sparse_indices is a vector, then for each i
dense[sparse_indices[i]] = sparse_values[i]

# If sparse_indices is an n by d matrix, then for each i in [0, n)
dense[sparse_indices[i][0], ..., sparse_indices[i][d-1]] = sparse_values[i]
```

All other values in `dense` are set to `default_value`.  If `sparse_values` is a
scalar, all sparse indices are set to this single value.

Indices should be sorted in lexicographic order, and indices must not
contain any repeats. If `validate_indices` is true, these properties
are checked during execution.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sparse_indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
0-D, 1-D, or 2-D.  `sparse_indices[i]` contains the complete
index where `sparse_values[i]` will be placed.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A `Tensor`. Must have the same type as `sparse_indices`.
1-D.  Shape of the dense output tensor.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A `Tensor`.
1-D.  Values corresponding to each row of `sparse_indices`,
or a scalar value to be used for all sparse indices.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A `Tensor`. Must have the same type as `sparse_values`.
Scalar value to set for indices not specified in
`sparse_indices`.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
An optional `bool`. Defaults to `True`.
If true, indices are checked to make sure they are sorted in
lexicographic order and that there are no repeats.
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
A `Tensor`. Has the same type as `sparse_values`.
</td>
</tr>

</table>

