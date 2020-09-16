description: Produces the average pool of the input tensor for quantized types.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.quantized_avg_pool" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.quantized_avg_pool

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Produces the average pool of the input tensor for quantized types.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.quantized_avg_pool(
    input, min_input, max_input, ksize, strides, padding, name=None
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
4-D with shape `[batch, height, width, channels]`.
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
`ksize`
</td>
<td>
A list of `ints`.
The size of the window for each dimension of the input tensor.
The length must be 4 to match the number of dimensions of the input.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`.
The stride of the sliding window for each dimension of the input
tensor.  The length must be 4 to match the number of dimensions of the input.
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
A `Tensor`. Has the same type as `input`.
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

