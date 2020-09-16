description: Encodes a RaggedTensor into a variant Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RaggedTensorToVariant" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RaggedTensorToVariant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Encodes a `RaggedTensor` into a `variant` Tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedTensorToVariant`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedTensorToVariant(
    rt_nested_splits, rt_dense_values, batched_input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


Encodes the given `RaggedTensor` and returns a `variant` Tensor. If
`batched_input` is True, then input `RaggedTensor` is unbatched along the
zero-th dimension, each component `RaggedTensor` is encoded into a scalar
`variant` Tensor, and these are stacked to return a 1-D `variant` Tensor.
If `batched_input` is False, then the input `RaggedTensor` is encoded as is and
a scalar `variant` Tensor is returned. A `RaggedTensor` is encoded by first
creating a 1-D `variant` Tensor with `ragged_rank + 1` elements, containing the
splits and values Tensors of the `RaggedTensor`. Then the 1-D `variant` Tensor
is wrapped in a scalar `variant` Tensor. See `RaggedTensorFromVariant` for the
corresponding decoding logic.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`rt_nested_splits`
</td>
<td>
A list of `Tensor` objects with the same type in: `int32`, `int64`.
A list of one or more Tensors representing the splits of the input
`RaggedTensor`.
</td>
</tr><tr>
<td>
`rt_dense_values`
</td>
<td>
A `Tensor`.
A Tensor representing the values of the input `RaggedTensor`.
</td>
</tr><tr>
<td>
`batched_input`
</td>
<td>
A `bool`.
A `bool` denoting whether the input is a batched `RaggedTensor`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

