description: Computes Quantized Rectified Linear X: min(max(features, 0), max_value)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.quantized_relu_x" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.quantized_relu_x

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.quantized_relu_x(
    features, max_value, min_features, max_features, out_type=tf.dtypes.quint8,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
</td>
</tr><tr>
<td>
`max_value`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`min_features`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the lowest quantized value represents.
</td>
</tr><tr>
<td>
`max_features`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the highest quantized value represents.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
An optional <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to <a href="../../../../tf.md#quint8"><code>tf.quint8</code></a>.
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
A tuple of `Tensor` objects (activations, min_activations, max_activations).
</td>
</tr>
<tr>
<td>
`activations`
</td>
<td>
A `Tensor` of type `out_type`.
</td>
</tr><tr>
<td>
`min_activations`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max_activations`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

