description: Concats all tensors in the list along the 0th dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TensorListConcat" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TensorListConcat

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
<p>`tf.compat.v1.raw_ops.TensorListConcat`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TensorListConcat(
    input_handle, element_dtype, element_shape=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Requires that all tensors have the same shape except the first dimension.

input_handle: The input list.
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
`element_dtype`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
An optional <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`. Defaults to `None`.
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

