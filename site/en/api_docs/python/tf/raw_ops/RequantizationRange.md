description: Computes a range that covers the actual values present in a quantized tensor.

robots: noindex

# tf.raw_ops.RequantizationRange

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes a range that covers the actual values present in a quantized tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RequantizationRange`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RequantizationRange(
    input, input_min, input_max, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a quantized tensor described by `(input, input_min, input_max)`, outputs a
range that covers the actual values present in that tensor. This op is typically
used to produce the `requested_output_min` and `requested_output_max` for
`Requantize`.

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
A tuple of `Tensor` objects (output_min, output_max).
</td>
</tr>
<tr>
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

