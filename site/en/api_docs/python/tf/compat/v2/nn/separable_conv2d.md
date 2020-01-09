page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.separable_conv2d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_impl.py#L984-L1048">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



2-D convolution with separable filters.

``` python
tf.compat.v2.nn.separable_conv2d(
    input,
    depthwise_filter,
    pointwise_filter,
    strides,
    padding,
    data_format=None,
    dilations=None,
    name=None
)
```



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

#### Args:


* <b>`input`</b>: 4-D `Tensor` with shape according to `data_format`.
* <b>`depthwise_filter`</b>: 4-D `Tensor` with shape `[filter_height, filter_width,
  in_channels, channel_multiplier]`. Contains `in_channels` convolutional
  filters of depth 1.
* <b>`pointwise_filter`</b>: 4-D `Tensor` with shape `[1, 1, channel_multiplier *
  in_channels, out_channels]`.  Pointwise filter to mix channels after
  `depthwise_filter` has convolved spatially.
* <b>`strides`</b>: 1-D of size 4.  The strides for the depthwise convolution for each
  dimension of `input`.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`.  The padding algorithm. See
  the "returns" section of <a href="../../../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: The data format for input. Either "NHWC" (default) or "NCHW".
* <b>`dilations`</b>: 1-D of size 2. The dilation rate in which we sample input values
  across the `height` and `width` dimensions in atrous convolution. If it is
  greater than 1, then all values of strides must be 1.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A 4-D `Tensor` with shape according to 'data_format'. For
  example, with data_format="NHWC", shape is [batch, out_height,
  out_width, out_channels].
