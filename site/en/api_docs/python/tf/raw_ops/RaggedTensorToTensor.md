description: Create a dense tensor from a ragged tensor, possibly altering its shape.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RaggedTensorToTensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RaggedTensorToTensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Create a dense tensor from a ragged tensor, possibly altering its shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedTensorToTensor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedTensorToTensor(
    shape, values, default_value, row_partition_tensors, row_partition_types,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The `ragged_to_dense` op creates a dense tensor from a list of row partition
tensors, a value vector, and default values. If the shape is unspecified, the
minimal shape required to contain all the elements in the ragged tensor (the
natural shape) will be used. If some dimensions are left unspecified, then the
size of the natural shape is used in that dimension.

The default_value will be broadcast to the output shape. After that, the values
from the ragged tensor overwrite the default values. Note that the default_value
must have less dimensions than the value.

The row partition tensors are in the order of the dimensions.
At present, the types can be:
* "ROW_SPLITS": the row_splits tensor from the ragged tensor.
* "VALUE_ROWIDS": the value_rowids tensor from the ragged tensor.
* "FIRST_DIM_SIZE": if value_rowids is used for the first dimension, then it
  is preceded by "FIRST_DIM_SIZE".

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int64`, `int32`.
The desired shape of the the output tensor. If left unspecified (empty),
the minimal shape required to contain all the elements in the ragged tensor
(the natural shape) will be used. If some dimensions are left unspecified, then
the size of the natural shape is used in that dimension.

Note that dense dimensions cannot be modified by the shape argument. Trying to
change the size of a dense dimension will cause the op to fail.
Examples:
natural shape: [4, 5, 6]
shape: -1
output shape: [4, 5, 6]

natural shape: [4, 5, 6]
shape: [3, -1, 2]
output shape: [3, 5, 2]

natural shape: [4, 5, 6]
shape: [3, 7, 2]
output shape: [3, 7, 2]
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor`.
A 1D tensor representing the values of the ragged tensor.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
A `Tensor`. Must have the same type as `values`.
The default_value when the shape is larger than the ragged tensor. The
default_value is broadcast until it is the shape of the output tensor, and
then overwritten by values in the ragged tensor. The default value must be
compatible with this broadcast operation, and must have fewer dimensions than
the value tensor.
</td>
</tr><tr>
<td>
`row_partition_tensors`
</td>
<td>
A list of at least 1 `Tensor` objects with the same type in: `int64`, `int32`.
</td>
</tr><tr>
<td>
`row_partition_types`
</td>
<td>
A list of `strings`.
The types of the row partition tensors. At present, these can be:
* "ROW_SPLITS": the row_splits tensor from the ragged tensor.
* "VALUE_ROWIDS": the value_rowids tensor from the ragged tensor.
* "FIRST_DIM_SIZE": if value_rowids is used for the first dimension, then it
is preceeded by "FIRST_DIM_SIZE".
The tensors are in the order of the dimensions.
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
A `Tensor`. Has the same type as `values`.
</td>
</tr>

</table>

