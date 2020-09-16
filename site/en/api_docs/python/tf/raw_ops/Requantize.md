description: Converts the quantized input tensor into a lower-precision output.

robots: noindex

# tf.raw_ops.Requantize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Converts the quantized `input` tensor into a lower-precision `output`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Requantize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Requantize(
    input, input_min, input_max, requested_output_min, requested_output_max,
    out_type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Converts the quantized `input` tensor into a lower-precision `output`, using the
output range specified with `requested_output_min` and `requested_output_max`.

`[input_min, input_max]` are scalar floats that specify the range for the float
interpretation of the `input` data. For example, if `input_min` is -1.0f and
`input_max` is 1.0f, and we are dealing with `quint16` quantized data, then a 0
value in the 16-bit data should be interpreted as -1.0f, and a 65535 means 1.0f.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the minimum quantized input value represents.
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the maximum quantized input value represents.
</td>
</tr><tr>
<td>
`requested_output_min`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the minimum quantized output value represents.
</td>
</tr><tr>
<td>
`requested_output_max`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the maximum quantized output value represents.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`.
The type of the output. Should be a lower bit depth than Tinput.
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
A tuple of `Tensor` objects (output, output_min, output_max).
</td>
</tr>
<tr>
<td>
`output`
</td>
<td>
A `Tensor` of type `out_type`.
</td>
</tr><tr>
<td>
`output_min`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`output_max`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

