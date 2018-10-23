

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.depthwise_conv2d_native_backprop_filter

``` python
depthwise_conv2d_native_backprop_filter(
    input,
    filter_sizes,
    out_backprop,
    strides,
    padding,
    data_format='NHWC',
    name=None
)
```



Defined in `tensorflow/python/ops/gen_nn_ops.py`.

See the guide: [Neural Network > Convolution](../../../../api_guides/python/nn#Convolution)

Computes the gradients of depthwise convolution with respect to the filter.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    4-D with shape based on `data_format`.  For example, if
    `data_format` is 'NHWC' then `input` is a 4-D `[batch, in_height,
    in_width, in_channels]` tensor.
* <b>`filter_sizes`</b>: A `Tensor` of type `int32`.
    An integer vector representing the tensor shape of `filter`,
    where `filter` is a 4-D
    `[filter_height, filter_width, in_channels, depthwise_multiplier]` tensor.
* <b>`out_backprop`</b>: A `Tensor`. Must have the same type as `input`.
    4-D with shape  based on `data_format`.
    For example, if `data_format` is 'NHWC' then
    out_backprop shape is `[batch, out_height, out_width, out_channels]`.
    Gradients w.r.t. the output of the convolution.
* <b>`strides`</b>: A list of `ints`.
    The stride of the sliding window for each dimension of the input
    of the convolution.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
    The type of padding algorithm to use.
* <b>`data_format`</b>: An optional `string` from: `"NHWC", "NCHW"`. Defaults to `"NHWC"`.
    Specify the data format of the input and output data. With the
    default format "NHWC", the data is stored in the order of:
        [batch, height, width, channels].
    Alternatively, the format could be "NCHW", the data storage order of:
        [batch, channels, height, width].
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`. 4-D with shape
`[filter_height, filter_width, in_channels, out_channels]`.  Gradient w.r.t.
the `filter` input of the convolution.