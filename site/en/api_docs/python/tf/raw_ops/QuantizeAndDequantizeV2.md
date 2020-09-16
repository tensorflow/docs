description: Quantizes then dequantizes a tensor.

robots: noindex

# tf.raw_ops.QuantizeAndDequantizeV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Quantizes then dequantizes a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QuantizeAndDequantizeV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QuantizeAndDequantizeV2(
    input, input_min, input_max, signed_input=(True), num_bits=8,
    range_given=(False), round_mode='HALF_TO_EVEN', narrow_range=(False), axis=-1,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op simulates the precision loss from the quantized forward pass by:

1. Quantizing the tensor to fixed point numbers, which should match the target
   quantization method when it is used in inference.
2. Dequantizing it back to floating point numbers for the following ops, most
   likely matmul.

There are different ways to quantize. This version uses only scaling, so 0.0
maps to 0.

From the specified 'num_bits' in the quantized output type, it determines
minimum and maximum representable quantized values.

e.g.

*   [-128, 127] for signed, num_bits = 8, or
*   [0, 255] for unsigned, num_bits = 8.

If range_given == False, the initial input_min, input_max will be determined
automatically as the minimum and maximum values in the input tensor, otherwise
the specified values of input_min, input_max are used.

Note: If the input_min, input_max are specified, they do not need to equal the
actual minimum and maximum values in the tensor. e.g. in some cases it may be
beneficial to specify these values such that the low probability extremes of the
input distribution are clipped.

This op determines the maximum scale_factor that would map the initial
[input_min, input_max] range to a range that lies within the representable
quantized range.

It determines the scale from one of input_min and input_max, then updates the
other one to maximize the representable range.

e.g.

*   if the output is signed, num_bits = 8, [input_min, input_max] = [-10.0,
    5.0]: it would use a scale_factor of -128 / -10.0 = 12.8 In this case, it
    would update input_max to be 127 / 12.8 = 9.921875
*   if the output is signed, num_bits = 8, [input_min, input_max] = [-10.0,
    10.0]: it would use a scale_factor of 127 / 10.0 = 12.7 In this case, it
    would update input_min to be 128.0 / 12.7 = -10.07874
*   if the output is unsigned, input_min is forced to be 0, and only the
    specified input_max is used.

After determining the scale_factor and updating the input range, it applies the
following to each value in the 'input' tensor.

output = round(clamp(value, input_min, input_max) * scale_factor) / scale_factor.

The above round function rounds the value based on the given round_mode.

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
Tensor to quantize and then dequantize.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
If `range_given == True`, this specifies the minimum input value that needs to
be represented, otherwise it is determined from the min value of the `input`
tensor.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
If `range_given == True`, this specifies the maximum input value that needs to
be represented, otherwise it is determined from the max value of the `input`
tensor.
</td>
</tr><tr>
<td>
`signed_input`
</td>
<td>
An optional `bool`. Defaults to `True`.
Whether the quantization is signed or unsigned. (actually this parameter should
have been called <b>`signed_output`</b>)
</td>
</tr><tr>
<td>
`num_bits`
</td>
<td>
An optional `int`. Defaults to `8`.
The bitwidth of the quantization.
</td>
</tr><tr>
<td>
`range_given`
</td>
<td>
An optional `bool`. Defaults to `False`.
Whether the range is given or should be determined from the `input` tensor.
</td>
</tr><tr>
<td>
`round_mode`
</td>
<td>
An optional `string` from: `"HALF_TO_EVEN", "HALF_UP"`. Defaults to `"HALF_TO_EVEN"`.
The 'round_mode' attribute controls which rounding tie-breaking algorithm is
used when rounding float values to their quantized equivalents. The following
rounding modes are currently supported:

*   HALF_TO_EVEN: this is the default round_mode.
*   HALF_UP: round towards positive. In this mode 7.5 rounds up to 8 and -7.5
rounds up to -7.
</td>
</tr><tr>
<td>
`narrow_range`
</td>
<td>
An optional `bool`. Defaults to `False`.
If True, then the absolute value of the quantized minimum value is the same as
the quantized maximum value, instead of 1 greater.
i.e. for 8 bit quantization, the minimum value is -127 instead of -128.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An optional `int`. Defaults to `-1`.
If specified, this axis is treated as a channel or slice axis, and a separate
quantization range is used for each channel or slice along this axis.
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

