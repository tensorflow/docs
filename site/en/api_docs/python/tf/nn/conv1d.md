

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.conv1d

``` python
tf.nn.conv1d(
    value,
    filters,
    stride,
    padding,
    use_cudnn_on_gpu=None,
    data_format=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/nn_ops.py).

See the guide: [Neural Network > Convolution](../../../../api_guides/python/nn#Convolution)

Computes a 1-D convolution given 3-D input and filter tensors. (deprecated arguments) (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
`NCHW` for data_format is deprecated, use `NCW` instead

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
`NHWC` for data_format is deprecated, use `NWC` instead

Given an input tensor of shape
  [batch, in_width, in_channels]
if data_format is "NWC", or
  [batch, in_channels, in_width]
if data_format is "NCW",
and a filter / kernel tensor of shape
[filter_width, in_channels, out_channels], this op reshapes
the arguments to pass them to conv2d to perform the equivalent
convolution operation.

Internally, this op reshapes the input tensors and invokes <a href="../../tf/nn/conv2d"><code>tf.nn.conv2d</code></a>.
For example, if `data_format` does not start with "NC", a tensor of shape
  [batch, in_width, in_channels]
is reshaped to
  [batch, 1, in_width, in_channels],
and the filter is reshaped to
  [1, filter_width, in_channels, out_channels].
The result is then reshaped back to
  [batch, out_width, out_channels]
\(where out_width is a function of the stride and padding as in conv2d\) and
returned to the caller.

#### Args:

* <b>`value`</b>: A 3D `Tensor`.  Must be of type `float16` or `float32`.
* <b>`filters`</b>: A 3D `Tensor`.  Must have the same type as `value`.
* <b>`stride`</b>: An `integer`.  The number of entries by which
    the filter is moved right at each step.
* <b>`padding`</b>: 'SAME' or 'VALID'
* <b>`use_cudnn_on_gpu`</b>: An optional `bool`.  Defaults to `True`.
* <b>`data_format`</b>: An optional `string` from `"NWC", "NCW"`.  Defaults
    to `"NWC"`, the data is stored in the order of
    [batch, in_width, in_channels].  The `"NCW"` format stores
    data as [batch, in_channels, in_width].
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.  Has the same type as input.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is invalid.