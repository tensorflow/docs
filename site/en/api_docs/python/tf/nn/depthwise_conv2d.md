description: Depthwise 2-D convolution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.depthwise_conv2d" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.depthwise_conv2d

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/nn_impl.py#L864-L956">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Depthwise 2-D convolution.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.depthwise_conv2d(
    input, filter, strides, padding, data_format=None, dilations=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given a 4D input tensor ('NHWC' or 'NCHW' data formats)
and a filter tensor of shape
`[filter_height, filter_width, in_channels, channel_multiplier]`
containing `in_channels` convolutional filters of depth 1, `depthwise_conv2d`
applies a different filter to each input channel (expanding from 1 channel
to `channel_multiplier` channels for each), then concatenates the results
together.  The output has `in_channels * channel_multiplier` channels.

In detail, with the default NHWC format,

    output[b, i, j, k * channel_multiplier + q] = sum_{di, dj}
         filter[di, dj, k, q] * input[b, strides[1] * i + rate[0] * di,
                                         strides[2] * j + rate[1] * dj, k]

Must have `strides[0] = strides[3] = 1`.  For the most common case of the
same horizontal and vertical strides, `strides = [1, stride, stride, 1]`.
If any value in `rate` is greater than 1, we perform atrous depthwise
convolution, in which case all values in the `strides` tensor must be equal
to 1.

#### Usage Example:



```
>>> x = np.array([
...     [1., 2.],
...     [3., 4.],
...     [5., 6.]
... ], dtype=np.float32).reshape((1, 3, 2, 1))
>>> kernel = np.array([
...     [1., 2.],
...     [3., 4]
... ], dtype=np.float32).reshape((2, 1, 1, 2))
>>> tf.nn.depthwise_conv2d(x, kernel, strides=[1, 1, 1, 1],
...                        padding='VALID').numpy()
  array([[[[10., 14.],
           [14., 20.]],
          [[18., 26.],
           [22., 32.]]]], dtype=float32)
```

```
>>> tf.nn.depthwise_conv2d(x, kernel, strides=[1, 1, 1, 1],
...                        padding=[[0, 0], [1, 0], [1, 0], [0, 0]]).numpy()
  array([[[[ 0.,  0.],
           [ 3.,  4.],
           [ 6.,  8.]],
          [[ 0.,  0.],
           [10., 14.],
           [14., 20.]],
          [[ 0.,  0.],
           [18., 26.],
           [22., 32.]]]], dtype=float32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
4-D with shape according to `data_format`.
</td>
</tr><tr>
<td>
`filter`
</td>
<td>
4-D with shape
`[filter_height, filter_width, in_channels, channel_multiplier]`.
</td>
</tr><tr>
<td>
`strides`
</td>
<td>
1-D of size 4.  The stride of the sliding window for each
dimension of `input`.
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
A 4-D `Tensor` with shape according to `data_format`.  E.g., for
"NHWC" format, shape is
`[batch, out_height, out_width, in_channels * channel_multiplier].`
</td>
</tr>

</table>

