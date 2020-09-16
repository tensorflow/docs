description: Converts a sparse representation into a dense tensor. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.sparse_to_dense" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.sparse_to_dense

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/sparse_ops.py#L1120-L1177">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a sparse representation into a dense tensor. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.sparse_to_dense(
    sparse_indices, output_shape, sparse_values, default_value=0,
    validate_indices=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Create a <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> and use <a href="../../../tf/sparse/to_dense.md"><code>tf.sparse.to_dense</code></a> instead.

Builds an array `dense` with shape `output_shape` such that

```python
# If sparse_indices is scalar
dense[i] = (i == sparse_indices ? sparse_values : default_value)

# If sparse_indices is a vector, then for each i
dense[sparse_indices[i]] = sparse_values[i]

# If sparse_indices is an n by d matrix, then for each i in [0, n)
dense[sparse_indices[i][0], ..., sparse_indices[i][d-1]] = sparse_values[i]
```

All other values in `dense` are set to `default_value`.  If `sparse_values`
is a scalar, all sparse indices are set to this single value.

Indices should be sorted in lexicographic order, and indices must not
contain any repeats. If `validate_indices` is True, these properties
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
A 0-D, 1-D, or 2-D `Tensor` of type `int32` or `int64`.
`sparse_indices[i]` contains the complete index where `sparse_values[i]`
will be placed.
</td>
</tr><tr>
<td>
`output_shape`
</td>
<td>
A 1-D `Tensor` of the same type as `sparse_indices`.  Shape
of the dense output tensor.
</td>
</tr><tr>
<td>
`sparse_values`
</td>
<td>
A 0-D or 1-D `Tensor`.  Values corresponding to each row of
`sparse_indices`, or a scalar value to be used for all sparse indices.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A 0-D `Tensor` of the same type as `sparse_values`.  Value
to set for indices not specified in `sparse_indices`.  Defaults to zero.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
A boolean value.  If True, indices are checked to make
sure they are sorted in lexicographic order and that there are no repeats.
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
Dense `Tensor` of shape `output_shape`.  Has the same type as
`sparse_values`.
</td>
</tr>

</table>

