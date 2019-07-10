page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.conv2d

Computes a 2-D convolution given 4-D `input` and `filters` tensors.

``` python
tf.compat.v2.nn.conv2d(
    input,
    filters,
    strides,
    padding,
    data_format='NHWC',
    dilations=None,
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

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

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types:
  `half`, `bfloat16`, `float32`, `float64`.
  A 4-D tensor. The dimension order is interpreted according to the value
  of `data_format`, see below for details.
* <b>`filters`</b>: A `Tensor`. Must have the same type as `input`.
  A 4-D tensor of shape
  `[filter_height, filter_width, in_channels, out_channels]`
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`.  The
  stride of the sliding window for each dimension of `input`. If a single
  value is given it is replicated in the `H` and `W` dimension. By default
  the `N` and `C` dimensions are set to 1. The dimension order is determined
  by the value of `data_format`, see below for details.
* <b>`padding`</b>: Either the `string` `"SAME"` or `"VALID"` indicating the type of
  padding algorithm to use, or a list indicating the explicit paddings at
  the start and end of each dimension. When explicit padding is used and
  data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
  pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
  and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
  [pad_top, pad_bottom], [pad_left, pad_right]]`.
* <b>`data_format`</b>: An optional `string` from: `"NHWC", "NCHW"`.
  Defaults to `"NHWC"`.
  Specify the data format of the input and output data. With the
  default format "NHWC", the data is stored in the order of:
      [batch, height, width, channels].
  Alternatively, the format could be "NCHW", the data storage order of:
      [batch, channels, height, width].
* <b>`dilations`</b>: An int or list of `ints` that has length `1`, `2` or `4`,
  defaults to 1. The dilation factor for each dimension of`input`. If a
  single value is given it is replicated in the `H` and `W` dimension. By
  default the `N` and `C` dimensions are set to 1. If set to k > 1, there
  will be k-1 skipped cells between each filter element on that dimension.
  The dimension order is determined by the value of `data_format`, see above
  for details. Dilations in the batch and depth dimensions if a 4-d tensor
  must be 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
