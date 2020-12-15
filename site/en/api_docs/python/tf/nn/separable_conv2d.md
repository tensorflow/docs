description: 2-D convolution with separable filters.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.separable_conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.separable_conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L1075-L1146">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



2-D convolution with separable filters.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.separable_conv2d(
    input, depthwise_filter, pointwise_filter, strides, padding, data_format=None,
    dilations=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Performs a depthwise convolution that acts separately on channels followed by
a pointwise convolution that mixes channels.  Note that this is separability
between dimensions `[1, 2]` and `3`, not spatial separability between
dimensions `1` and `2`.

In detail, with the default NHWC format,

    output[b, i, j, k] = sum_{di, dj, q, r}
        input[b, strides[1] * i + di, strides[2] * j + dj, q] *
        depthwise_filter[di, dj, q, r] *
        pointwise_filter[0, 0, q * channel_multiplier + r, k]

`strides` controls the strides for the depthwise convolution only, since
the pointwise convolution has implicit strides of `[1, 1, 1, 1]`.  Must have
`strides[0] = strides[3] = 1`.  For the most common case of the same
horizontal and vertical strides, `strides = [1, stride, stride, 1]`.
If any value in `rate` is greater than 1, we perform atrous depthwise
convolution, in which case all values in the `strides` tensor must be equal
to 1.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
4-D `Tensor` with shape according to `data_format`.
</td>
</tr><tr>
<td>
`depthwise_filter`
</td>
<td>
4-D `Tensor` with shape `[filter_height, filter_width,
in_channels, channel_multiplier]`. Contains `in_channels` convolutional
filters of depth 1.
</td>
</tr><tr>
<td>
`pointwise_filter`
</td>
<td>
4-D `Tensor` with shape `[1, 1, channel_multiplier *
in_channels, out_channels]`.  Pointwise filter to mix channels after
`depthwise_filter` has convolved spatially.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
1-D of size 4.  The strides for the depthwise convolution for each
dimension of `input`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
Controls how to pad the image before applying the depthwise
convolution. Can be the string `"SAME"` or `"VALID"` indicating the type
of padding algorithm to use, or a Python list indicating the explicit
paddings at the start and end of each dimension. When explicit padding is
used and data_format is `"NHWC"`, this should be in the form `[[0, 0],
[pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit
padding used and data_format is `"NCHW"`, this should be in the form
`[[0, 0], [0, 0], [pad_top, pad_bottom], [pad_left, pad_right]]`.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
The data format for input. Either "NHWC" (default) or "NCHW".
</td>
</tr><tr>
<td>
`dilations`
</td>
<td>
1-D of size 2. The dilation rate in which we sample input values
across the `height` and `width` dimensions in atrous convolution. If it is
greater than 1, then all values of strides must be 1.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A 4-D `Tensor` with shape according to 'data_format'. For
example, with data_format="NHWC", shape is [batch, out_height,
out_width, out_channels].
</td>
</tr>

</table>

