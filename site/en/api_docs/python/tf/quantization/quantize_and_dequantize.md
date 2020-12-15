description: Quantizes then dequantizes a tensor. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.quantization.quantize_and_dequantize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.quantization.quantize_and_dequantize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/array_ops.py#L5648-L5712">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Quantizes then dequantizes a tensor. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.quantization.quantize_and_dequantize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.quantization.quantize_and_dequantize(
    input, input_min, input_max, signed_input=(True), num_bits=8,
    range_given=(False), round_mode='HALF_TO_EVEN', name=None, narrow_range=(False),
    axis=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
This Op has been deprecated, use`quantize_and_dequantize_v2` instead. To To simulate the V1 the behavior of tf.quantization.quantize_and_dequantize(...) use tf.grad_pass_through(tf.quantization.quantize_and_dequantize_v2)(...).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` to quantize and dequantize.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
If range_given=True, the minimum input value, that needs to be
represented in the quantized representation. If axis is specified, this
should be a vector of minimum values for each slice along axis.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
If range_given=True, the maximum input value that needs to be
represented in the quantized representation. If axis is specified, this
should be a vector of maximum values for each slice along axis.
</td>
</tr><tr>
<td>
`signed_input`
</td>
<td>
True if the quantization is signed or unsigned.
</td>
</tr><tr>
<td>
`num_bits`
</td>
<td>
The bitwidth of the quantization.
</td>
</tr><tr>
<td>
`range_given`
</td>
<td>
If true use `input_min` and `input_max` for the range of the
input, otherwise determine min and max from the input `Tensor`.
</td>
</tr><tr>
<td>
`round_mode`
</td>
<td>
Rounding mode when rounding from float values to quantized ones.
one of ['HALF_TO_EVEN', 'HALF_UP']
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the operation.
</td>
</tr><tr>
<td>
`narrow_range`
</td>
<td>
If true, then the absolute value of the quantized minimum
value is the same as the quantized maximum value, instead of 1 greater.
i.e. for 8 bit quantization, the minimum value is -127 instead of -128.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Integer. If specified, refers to a dimension of the input tensor, such
that quantization will be per slice along that dimension.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Each element is the result of quantizing and dequantizing the
corresponding element of `input`.
</td>
</tr>

</table>

