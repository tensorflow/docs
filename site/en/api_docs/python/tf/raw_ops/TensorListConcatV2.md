description: Concats all tensors in the list along the 0th dimension.

robots: noindex

# tf.raw_ops.TensorListConcatV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Concats all tensors in the list along the 0th dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TensorListConcatV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListConcatV2(
    input_handle, element_shape, leading_dims, element_dtype, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires that all tensors have the same shape except the first dimension.

input_handle: The input list.
element_shape: The shape of the uninitialized elements in the list. If the first
  dimension is not -1, it is assumed that all list elements have the same
  leading dim.
leading_dims: The list of leading dims of uninitialized list elements. Used if
  the leading dim of input_handle.element_shape or the element_shape input arg
  is not already set.
tensor: The concated result.
lengths: Output tensor containing sizes of the 0th dimension of tensors in the list, used for computing the gradient.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_handle`
</td>
<td>
A `Tensor` of type `variant`.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
</td>
</tr><tr>
<td>
`leading_dims`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`element_dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
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
A tuple of `Tensor` objects (tensor, lengths).
</td>
</tr>
<tr>
<td>
`tensor`
</td>
<td>
A `Tensor` of type `element_dtype`.
</td>
</tr><tr>
<td>
`lengths`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr>
</table>

