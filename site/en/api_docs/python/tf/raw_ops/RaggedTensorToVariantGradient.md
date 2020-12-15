description: Helper used to compute the gradient for RaggedTensorToVariant.

robots: noindex

# tf.raw_ops.RaggedTensorToVariantGradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Helper used to compute the gradient for `RaggedTensorToVariant`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RaggedTensorToVariantGradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RaggedTensorToVariantGradient(
    encoded_ragged_grad, row_splits, dense_values_shape, Tvalues, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Computes the gradient for the dense_values input to the RaggedTensorToVariant
op, given the variant-encoded ragged gradients of the outputs, along with
the outer row-splits and the shape of the dense-values that were provided as
inputs to the RaggedTensorToVariant op.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`encoded_ragged_grad`
</td>
<td>
A `Tensor` of type `variant`.
A `variant` Tensor containing encoded `RaggedTensor` gradients.
</td>
</tr><tr>
<td>
`row_splits`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`.
Outermost row-splits that were used as input to the RaggedTensorToVariant op.
</td>
</tr><tr>
<td>
`dense_values_shape`
</td>
<td>
A `Tensor` of type `int32`.
Shape of the dense_values that was used as an input to the
RaggedTensorToVariant op.
</td>
</tr><tr>
<td>
`Tvalues`
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
A `Tensor` of type `Tvalues`.
</td>
</tr>

</table>

