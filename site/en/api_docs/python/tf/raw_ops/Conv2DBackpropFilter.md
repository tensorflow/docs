description: Computes the gradients of convolution with respect to the filter.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Conv2DBackpropFilter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Conv2DBackpropFilter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the gradients of convolution with respect to the filter.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Conv2DBackpropFilter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Conv2DBackpropFilter(
    input, filter_sizes, out_backprop, strides, padding, use_cudnn_on_gpu=(True),
    explicit_paddings=[], data_format='NHWC', dilations=[1, 1, 1, 1], name=None
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
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
4-D with shape `[batch, in_height, in_width, in_channels]`.
</td>
</tr><tr>
<td>
`filter_sizes`
</td>
<td>
A `Tensor` of type `int32`.
An integer vector representing the tensor shape of `filter`,
where `filter` is a 4-D
`[filter_height, filter_width, in_channels, out_channels]` tensor.
</td>
</tr><tr>
<td>
`out_backprop`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
4-D with shape `[batch, out_height, out_width, out_channels]`.
Gradients w.r.t. the output of the convolution.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`.
The stride of the sliding window for each dimension of the input
of the convolution. Must be in the same order as the dimension specified with
format.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
A `string` from: `"SAME", "VALID", "EXPLICIT"`.
The type of padding algorithm to use.
</td>
</tr><tr>
<td>
`use_cudnn_on_gpu`
</td>
<td>
An optional `bool`. Defaults to `True`.
</td>
</tr><tr>
<td>
`explicit_paddings`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
If `padding` is `"EXPLICIT"`, the list of explicit padding amounts. For the ith
dimension, the amount of padding inserted before and after the dimension is
`explicit_paddings[2 * i]` and `explicit_paddings[2 * i + 1]`, respectively. If
`padding` is not `"EXPLICIT"`, `explicit_paddings` must be empty.
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
`dilations`
</td>
<td>
An optional list of `ints`. Defaults to `[1, 1, 1, 1]`.
1-D tensor of length 4.  The dilation factor for each dimension of
`input`. If set to k > 1, there will be k-1 skipped cells between each filter
element on that dimension. The dimension order is determined by the value of
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

