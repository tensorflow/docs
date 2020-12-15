description: Returns the gradient of QuantizeAndDequantizeV4.

robots: noindex

# tf.raw_ops.QuantizeAndDequantizeV4Grad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the gradient of `QuantizeAndDequantizeV4`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QuantizeAndDequantizeV4Grad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QuantizeAndDequantizeV4Grad(
    gradients, input, input_min, input_max, axis=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a gradient of 1 for inputs that are within the quantization range,
or 0 otherwise.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`gradients`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must have the same type as `gradients`.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor`. Must have the same type as `gradients`.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor`. Must have the same type as `gradients`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An optional `int`. Defaults to `-1`.
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
A tuple of `Tensor` objects (input_backprop, input_min_backprop, input_max_backprop).
</td>
</tr>
<tr>
<td>
`input_backprop`
</td>
<td>
A `Tensor`. Has the same type as `gradients`.
</td>
</tr><tr>
<td>
`input_min_backprop`
</td>
<td>
A `Tensor`. Has the same type as `gradients`.
</td>
</tr><tr>
<td>
`input_max_backprop`
</td>
<td>
A `Tensor`. Has the same type as `gradients`.
</td>
</tr>
</table>

