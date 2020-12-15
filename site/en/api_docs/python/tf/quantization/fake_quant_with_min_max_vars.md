description: Fake-quantize the 'inputs' tensor of type float via global float scalars

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.fake_quant_with_min_max_vars" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.fake_quant_with_min_max_vars

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Fake-quantize the 'inputs' tensor of type float via global float scalars

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.fake_quant_with_min_max_vars`, `tf.compat.v1.quantization.fake_quant_with_min_max_vars`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.fake_quant_with_min_max_vars(
    inputs, min, max, num_bits=8, narrow_range=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Fake-quantize the `inputs` tensor of type float via global float scalars
`min` and `max` to `outputs` tensor of same shape as `inputs`.

Attributes

*   `[min; max]` define the clamping range for the `inputs` data.
*   `inputs` values are quantized into the quantization range (
`[0; 2^num_bits - 1]` when `narrow_range` is false and `[1; 2^num_bits - 1]`
when it is true) and then de-quantized and output as floats in `[min; max]`
interval.
*   `num_bits` is the bitwidth of the quantization; between 2 and 16, inclusive.

Before quantization, `min` and `max` values are adjusted with the following
logic.
It is suggested to have `min <= 0 <= max`. If `0` is not in the range of values,
the behavior can be unexpected:

*   If `0 < min < max`: `min_adj = 0` and `max_adj = max - min`.
*   If `min < max < 0`: `min_adj = min - max` and `max_adj = 0`.
*   If `min <= 0 <= max`: `scale = (max - min) / (2^num_bits - 1) `,
`min_adj = scale * round(min / scale)` and `max_adj = max + min_adj - min`.

This operation has a gradient and thus allows for training `min` and `max`
values.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max`
</td>
<td>
A `Tensor` of type `float32`.
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
`narrow_range`
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

