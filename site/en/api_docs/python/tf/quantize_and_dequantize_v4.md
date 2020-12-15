description: Returns the gradient of QuantizeAndDequantizeV4.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantize_and_dequantize_v4" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantize_and_dequantize_v4

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
<p>`tf.compat.v1.quantize_and_dequantize_v4`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantize_and_dequantize_v4(
    input, input_min, input_max, signed_input=(True), num_bits=8,
    range_given=(False), round_mode='HALF_TO_EVEN', narrow_range=(False), axis=-1,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is almost identical to QuantizeAndDequantizeV2, except that it returns a
gradient of 1 for inputs that are within the quantization range, or 0 otherwise.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
</td>
</tr><tr>
<td>
`signed_input`
</td>
<td>
An optional `bool`. Defaults to `True`.
</td>
</tr><tr>
<td>
`num_bits`
</td>
<td>
An optional `int`. Defaults to `8`.
</td>
</tr><tr>
<td>
`range_given`
</td>
<td>
An optional `bool`. Defaults to `False`.
</td>
</tr><tr>
<td>
`round_mode`
</td>
<td>
An optional `string` from: `"HALF_TO_EVEN", "HALF_UP"`. Defaults to `"HALF_TO_EVEN"`.
</td>
</tr><tr>
<td>
`narrow_range`
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

