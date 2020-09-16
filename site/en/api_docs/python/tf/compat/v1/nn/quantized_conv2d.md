description: Computes a 2D convolution given quantized 4D input and filter tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.quantized_conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.quantized_conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes a 2D convolution given quantized 4D input and filter tensors.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.quantized_conv2d(
    input, filter, min_input, max_input, min_filter, max_filter, strides, padding,
    out_type=tf.dtypes.qint32, dilations=[1, 1, 1, 1], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs are quantized tensors where the lowest value represents the real
number of the associated minimum, and the highest represents the maximum.
This means that you can only interpret the quantized output in the same way, by
taking the returned minimum and maximum values into account.

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
`filter`
</td>
<td>
A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
filter's input_depth dimension must match input's depth dimensions.
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
`min_filter`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the lowest quantized filter value represents.
</td>
</tr><tr>
<td>
`max_filter`
</td>
<td>
A `Tensor` of type `float32`.
The float value that the highest quantized filter value represents.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`.
The stride of the sliding window for each dimension of the input
tensor.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A `string` from: `"SAME", "VALID"`.
The type of padding algorithm to use.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
An optional <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to <a href="../../../../tf.md#qint32"><code>tf.qint32</code></a>.
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1]`.
1-D tensor of length 4.  The dilation factor for each dimension of
`input`. If set to k > 1, there will be k-1 skipped cells between each
filter element on that dimension. The dimension order is determined by the
value of `data_format`, see above for details. Dilations in the batch and
depth dimensions must be 1.
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
A tuple of `Tensor` objects (output, min_output, max_output).
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
`min_output`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`max_output`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr>
</table>

