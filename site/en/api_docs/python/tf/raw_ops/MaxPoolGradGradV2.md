description: Computes second-order gradients of the maxpooling function.

robots: noindex

# tf.raw_ops.MaxPoolGradGradV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes second-order gradients of the maxpooling function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MaxPoolGradGradV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MaxPoolGradGradV2(
    orig_input, orig_output, grad, ksize, strides, padding, data_format='NHWC',
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
`orig_input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
The original input tensor.
</td>
</tr><tr>
<td>
`orig_output`
</td>
<td>
A `Tensor`. Must have the same type as `orig_input`.
The original output tensor.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must have the same type as `orig_input`.
4-D.  Gradients of gradients w.r.t. the input of `max_pool`.
</td>
</tr><tr>
<td>
`ksize`
</td>
<td>
A `Tensor` of type `int32`.
The size of the window for each dimension of the input tensor.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A `Tensor` of type `int32`.
The stride of the sliding window for each dimension of the
input tensor.
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
`data_format`
</td>
<td>
An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`.
Specify the data format of the input and output data. With the
default format "NHWC", the data is stored in the order of:
[batch, in_height, in_width, in_channels].
Alternatively, the format could be "NCHW", the data storage order of:
[batch, in_channels, in_height, in_width].
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
A `Tensor`. Has the same type as `orig_input`.
</td>
</tr>

</table>

