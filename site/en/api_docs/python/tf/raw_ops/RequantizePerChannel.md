description: Requantizes input with min and max values known per channel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RequantizePerChannel" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RequantizePerChannel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Requantizes input with min and max values known per channel.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RequantizePerChannel`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RequantizePerChannel(
    input, input_min, input_max, requested_output_min, requested_output_max,
    out_type=tf.dtypes.quint8, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
The original input tensor.
</td>
</tr><tr>
<td>
`input_min`
</td>
<td>
A `Tensor` of type `float32`.
The minimum value of the input tensor
</td>
</tr><tr>
<td>
`input_max`
</td>
<td>
A `Tensor` of type `float32`.
The maximum value of the input tensor.
</td>
</tr><tr>
<td>
`requested_output_min`
</td>
<td>
A `Tensor` of type `float32`.
The minimum value of the output tensor requested.
</td>
</tr><tr>
<td>
`requested_output_max`
</td>
<td>
A `Tensor` of type `float32`.
The maximum value of the output tensor requested.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to <a href="../../tf.md#quint8"><code>tf.quint8</code></a>.
The quantized type of output tensor that needs to be converted.
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

