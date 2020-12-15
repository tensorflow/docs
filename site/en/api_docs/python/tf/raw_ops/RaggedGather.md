description: Gather ragged slices from params axis 0 according to indices.

robots: noindex

# tf.raw_ops.RaggedGather

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Gather ragged slices from `params` axis `0` according to `indices`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedGather`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedGather(
    params_nested_splits, params_dense_values, indices, OUTPUT_RAGGED_RANK,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs a `RaggedTensor` output composed from `output_dense_values` and
`output_nested_splits`, such that:

```python
output.shape = indices.shape + params.shape[1:]
output.ragged_rank = indices.shape.ndims + params.ragged_rank
output[i...j, d0...dn] = params[indices[i...j], d0...dn]
```

where

* `params =
   ragged.from_nested_row_splits(params_dense_values, params_nested_splits)`
   provides the values that should be gathered.
* `indices` ia a dense tensor with dtype `int32` or `int64`, indicating which
   values should be gathered.
* `output =
   ragged.from_nested_row_splits(output_dense_values, output_nested_splits)`
   is the output tensor.

(Note: This c++ op is used to implement the higher-level python
`tf.ragged.gather` op, which also supports ragged indices.)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`params_nested_splits`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
The `nested_row_splits` tensors that define the row-partitioning for the
`params` RaggedTensor input.
</td>
</tr><tr>
<td>
`params_dense_values`
</td>
<td>
A `Tensor`.
The `flat_values` for the `params` RaggedTensor. There was a terminology change
at the python level from dense_values to flat_values, so dense_values is the
deprecated name.
</td>
</tr><tr>
<td>
`indices`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Indices in the outermost dimension of `params` of the values that should be
gathered.
</td>
</tr><tr>
<td>
`OUTPUT_RAGGED_RANK`
</td>
<td>
An `int` that is `>= 0`.
The ragged rank of the output RaggedTensor. `output_nested_splits` will contain
this number of `row_splits` tensors. This value should equal
`indices.shape.ndims + params.ragged_rank - 1`.
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
A tuple of `Tensor` objects (output_nested_splits, output_dense_values).
</td>
</tr>
<tr>
<td>
`output_nested_splits`
</td>
<td>
A list of `OUTPUT_RAGGED_RANK` `Tensor` objects with the same type as `params_nested_splits`.
</td>
</tr><tr>
<td>
`output_dense_values`
</td>
<td>
A `Tensor`. Has the same type as `params_dense_values`.
</td>
</tr>
</table>

