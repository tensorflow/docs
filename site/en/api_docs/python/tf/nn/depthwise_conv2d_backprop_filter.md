description: Computes the gradients of depthwise convolution with respect to the filter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.depthwise_conv2d_backprop_filter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.depthwise_conv2d_backprop_filter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L2922-L2990">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the gradients of depthwise convolution with respect to the filter.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.depthwise_conv2d_backprop_filter`, `tf.compat.v1.nn.depthwise_conv2d_native_backprop_filter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.depthwise_conv2d_backprop_filter(
    input, filter_sizes, out_backprop, strides, padding, data_format='NHWC',
    dilations=[1, 1, 1, 1], name=None
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
A `Tensor`. Must be one of the following types: `half`, `bfloat16`,
`float32`, `float64`. 4-D with shape based on `data_format`.  For example,
if `data_format` is 'NHWC' then `input` is a 4-D `[batch, in_height,
in_width, in_channels]` tensor.
</td>
</tr><tr>
<td>
`filter_sizes`
</td>
<td>
A `Tensor` of type `int32`. An integer vector representing the
tensor shape of `filter`, where `filter` is a 4-D `[filter_height,
filter_width, in_channels, depthwise_multiplier]` tensor.
</td>
</tr><tr>
<td>
`out_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`. 4-D with shape
based on `data_format`. For example, if `data_format` is 'NHWC' then
out_backprop shape is `[batch, out_height, out_width, out_channels]`.
Gradients w.r.t. the output of the convolution.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`. The stride of the sliding window for each
dimension of the input of the convolution.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
Controls how to pad the image before applying the convolution. Can
be the string `"SAME"` or `"VALID"` indicating the type of padding
algorithm to use, or a list indicating the explicit paddings at the start
and end of each dimension. When explicit padding is used and data_format
is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
[pad_left, pad_right], [0, 0]]`. When explicit padding used and
data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
[pad_top, pad_bottom], [pad_left, pad_right]]`.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
An optional `string` from: `"NHWC", "NCHW"`. Defaults to
`"NHWC"`. Specify the data format of the input and output data. With the
default format "NHWC", the data is stored in the order of: [batch, height,
width, channels].
Alternatively, the format could be "NCHW", the data storage order of:
[batch, channels, height, width].
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D
tensor of length 4.  The dilation factor for each dimension of `input`. If
set to k > 1, there will be k-1 skipped cells between each filter element
on that dimension. The dimension order is determined by the value of
`data_format`, see above for details. Dilations in the batch and depth
dimensions must be 1.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

