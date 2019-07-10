page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.conv_transpose

The transpose of `convolution`.

### Aliases:

* `tf.compat.v1.nn.conv_transpose`
* `tf.compat.v2.nn.conv_transpose`
* `tf.nn.conv_transpose`

``` python
tf.nn.conv_transpose(
    input,
    filters,
    output_shape,
    strides,
    padding='SAME',
    data_format=None,
    dilations=None,
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after [Deconvolutional
Networks](http://www.matthewzeiler.com/pubs/cvpr2010/cvpr2010.pdf), but is
actually the transpose (gradient) of `convolution` rather than an actual
deconvolution.

#### Args:


* <b>`input`</b>: An N+2 dimensional `Tensor` of shape
  `[batch_size] + input_spatial_shape + [in_channels]` if data_format does
  not start with "NC" (default), or
  `[batch_size, in_channels] + input_spatial_shape` if data_format starts
  with "NC". It must be one of the following types:
  `half`, `bfloat16`, `float32`, `float64`.
* <b>`filters`</b>: An N+2 dimensional `Tensor` with the same type as `input` and
  shape `spatial_filter_shape + [in_channels, out_channels]`.
* <b>`output_shape`</b>: A 1-D `Tensor` representing the output shape of the
  deconvolution op.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `N` or `N+2`.  The
  stride of the sliding window for each dimension of `input`. If a single
  value is given it is replicated in the spatial dimensions. By default
  the `N` and `C` dimensions are set to 0. The dimension order is determined
  by the value of `data_format`, see below for details.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string or None.  Specifies whether the channel dimension of
  the `input` and output is the last dimension (default, or if `data_format`
  does not start with "NC"), or the second dimension (if `data_format`
  starts with "NC").  For N=1, the valid values are "NWC" (default) and
  "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
  For N=3, the valid values are "NDHWC" (default) and "NCDHW".
* <b>`dilations`</b>: An int or list of `ints` that has length `1`, `N` or `N+2`,
  defaults to 1. The dilation factor for each dimension of`input`. If a
  single value is given it is replicated in the spatial dimensions. By
  default the `N` and `C` dimensions are set to 1. If set to k > 1, there
  will be k-1 skipped cells between each filter element on that dimension.
  The dimension order is determined by the value of `data_format`, see above
  for details.
* <b>`name`</b>: A name for the operation (optional). If not specified "conv_transpose"
  is used.


#### Returns:

A `Tensor` with the same type as `value`.
