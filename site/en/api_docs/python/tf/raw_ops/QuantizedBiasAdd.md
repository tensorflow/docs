description: Adds Tensor 'bias' to Tensor 'input' for Quantized types.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.QuantizedBiasAdd" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.QuantizedBiasAdd

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Adds Tensor 'bias' to Tensor 'input' for Quantized types.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QuantizedBiasAdd`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QuantizedBiasAdd(
    input, bias, min_input, max_input, min_bias, max_bias, out_type, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Broadcasts the values of bias on dimensions 0..N-2 of 'input'.

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
`bias`
</td>
<td>
A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
A 1D bias Tensor with size matching the last dimension of 'input'.
</td>
</tr><tr>
<td>
`min_input`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the lowest quantized input value represents.
</td>
</tr><tr>
<td>
`max_input`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the highest quantized input value represents.
</td>
</tr><tr>
<td>
`min_bias`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the lowest quantized bias value represents.
</td>
</tr><tr>
<td>
`max_bias`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the highest quantized bias value represents.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`.
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
A tuple of `Tensor` objects (output, min_out, max_out).
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
`min_out`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max_out`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

