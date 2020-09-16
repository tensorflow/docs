description: Generates a feature cross from a list of tensors, and returns it as a

robots: noindex

# tf.raw_ops.RaggedCross

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates a feature cross from a list of tensors, and returns it as a

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedCross`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedCross(
    ragged_values, ragged_row_splits, sparse_indices, sparse_values, sparse_shape,
    dense_inputs, input_order, hashed_output, num_buckets, hash_key,
    out_values_type, out_row_splits_type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
RaggedTensor.  See <a href="../../tf/ragged/cross.md"><code>tf.ragged.cross</code></a> for more details.

  Args:
    ragged_values: A list of `Tensor` objects with types from: `int64`, `string`.
      The values tensor for each RaggedTensor input.
    ragged_row_splits: A list of `Tensor` objects with types from: `int32`, `int64`.
      The row_splits tensor for each RaggedTensor input.
    sparse_indices: A list of `Tensor` objects with type `int64`.
      The indices tensor for each SparseTensor input.
    sparse_values: A list of `Tensor` objects with types from: `int64`, `string`.
      The values tensor for each SparseTensor input.
    sparse_shape: A list with the same length as `sparse_indices` of `Tensor` objects with type `int64`.
      The dense_shape tensor for each SparseTensor input.
    dense_inputs: A list of `Tensor` objects with types from: `int64`, `string`.
      The tf.Tensor inputs.
    input_order: A `string`.
      String specifying the tensor type for each input.  The `i`th character in
      this string specifies the type of the `i`th input, and is one of: 'R' (ragged),
      'D' (dense), or 'S' (sparse).  This attr is used to ensure that the crossed
      values are combined in the order of the inputs from the call to tf.ragged.cross.
    hashed_output: A `bool`.
    num_buckets: An `int` that is `>= 0`.
    hash_key: An `int`.
    out_values_type: A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int64, tf.string`.
    out_row_splits_type: A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.int32, tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_values, output_row_splits).

    output_values: A `Tensor` of type `out_values_type`.
    output_row_splits: A `Tensor` of type `out_row_splits_type`.
  