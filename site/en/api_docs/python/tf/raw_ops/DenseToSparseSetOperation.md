description: Applies set operation along last dimension of Tensor and SparseTensor.

robots: noindex

# tf.raw_ops.DenseToSparseSetOperation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies set operation along last dimension of `Tensor` and `SparseTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DenseToSparseSetOperation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DenseToSparseSetOperation(
    set1, set2_indices, set2_values, set2_shape, set_operation,
    validate_indices=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

See SetOperationOp::SetOperationFromContext for values of `set_operation`.

Input `set2` is a `SparseTensor` represented by `set2_indices`, `set2_values`,
and `set2_shape`. For `set2` ranked `n`, 1st `n-1` dimensions must be the same
as `set1`. Dimension `n` contains values in a set, duplicates are allowed but
ignored.

If `validate_indices` is `True`, this op validates the order and range of `set2`
indices.

Output `result` is a `SparseTensor` represented by `result_indices`,
`result_values`, and `result_shape`. For `set1` and `set2` ranked `n`, this
has rank `n` and the same 1st `n-1` dimensions as `set1` and `set2`. The `nth`
dimension contains the result of `set_operation` applied to the corresponding
`[0...n-1]` dimension of `set`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`set1`
</td>
<td>
A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
`Tensor` with rank `n`. 1st `n-1` dimensions must be the same as `set2`.
Dimension `n` contains values in a set, duplicates are allowed but ignored.
</td>
</tr><tr>
<td>
`set2_indices`
</td>
<td>
A `Tensor` of type `int64`.
2D `Tensor`, indices of a `SparseTensor`. Must be in row-major
order.
</td>
</tr><tr>
<td>
`set2_values`
</td>
<td>
A `Tensor`. Must have the same type as `set1`.
1D `Tensor`, values of a `SparseTensor`. Must be in row-major
order.
</td>
</tr><tr>
<td>
`set2_shape`
</td>
<td>
A `Tensor` of type `int64`.
1D `Tensor`, shape of a `SparseTensor`. `set2_shape[0...n-1]` must
be the same as the 1st `n-1` dimensions of `set1`, `result_shape[n]` is the
max set size across `n-1` dimensions.
</td>
</tr><tr>
<td>
`set_operation`
</td>
<td>
A `string`.
</td>
</tr><tr>
<td>
`validate_indices`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A tuple of `Tensor` objects (result_indices, result_values, result_shape).
</td>
</tr>
<tr>
<td>
`result_indices`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`result_values`
</td>
<td>
A `Tensor`. Has the same type as `set1`.
</td>
</tr><tr>
<td>
`result_shape`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

