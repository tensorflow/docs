description: Computes a 2-D convolution given 4-D input and filter tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Conv2D" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Conv2D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes a 2-D convolution given 4-D `input` and `filter` tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Conv2D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Conv2D(
    input, filter, strides, padding, use_cudnn_on_gpu=(True), explicit_paddings=[],
    data_format='NHWC', dilations=[1, 1, 1, 1], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given an input tensor of shape `[batch, in_height, in_width, in_channels]`
and a filter / kernel tensor of shape
`[filter_height, filter_width, in_channels, out_channels]`, this op
performs the following:

1. Flattens the filter to a 2-D matrix with shape
   `[filter_height * filter_width * in_channels, output_channels]`.
2. Extracts image patches from the input tensor to form a *virtual*
   tensor of shape `[batch, out_height, out_width,
   filter_height * filter_width * in_channels]`.
3. For each patch, right-multiplies the filter matrix and the image patch
   vector.

In detail, with the default NHWC format,

    output[b, i, j, k] =
        sum_{di, dj, q} input[b, strides[1] * i + di, strides[2] * j + dj, q] *
                        filter[di, dj, q, k]

Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
horizontal and vertices strides, `strides = [1, stride, stride, 1]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `int32`.
A 4-D tensor. The dimension order is interpreted according to the value
of `data_format`, see below for details.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
A 4-D tensor of shape
`[filter_height, filter_width, in_channels, out_channels]`
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
A list of `ints`.
1-D tensor of length 4.  The stride of the sliding window for each
dimension of `input`. The dimension order is determined by the value of
`data_format`, see below for details.
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
[batch, height, width, channels].
Alternatively, the format could be "NCHW", the data storage order of:
[batch, channels, height, width].
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

