description: Computes requantization range per channel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.RequantizationRangePerChannel" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.RequantizationRangePerChannel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes requantization range per channel.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RequantizationRangePerChannel`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RequantizationRangePerChannel(
    input, input_min, input_max, clip_value_max, name=None
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
`clip_value_max`
</td>
<td>
A `float`.
The maximum value of the output that needs to be clipped.
Example: set this to 6 for Relu6.
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

