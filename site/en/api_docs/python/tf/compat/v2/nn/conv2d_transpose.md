page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.nn.conv2d_transpose


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L2207-L2275">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



The transpose of `conv2d`.

``` python
tf.compat.v2.nn.conv2d_transpose(
    input,
    filters,
    output_shape,
    strides,
    padding='SAME',
    data_format='NHWC',
    dilations=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after [Deconvolutional
Networks](http://www.matthewzeiler.com/pubs/cvpr2010/cvpr2010.pdf), but is
actually the transpose (gradient) of `conv2d` rather than an actual
deconvolution.

#### Args:


* <b>`input`</b>: A 4-D `Tensor` of type `float` and shape `[batch, height, width,
  in_channels]` for `NHWC` data format or `[batch, in_channels, height,
  width]` for `NCHW` data format.
* <b>`filters`</b>: A 4-D `Tensor` with the same type as `input` and shape `[height,
  width, output_channels, in_channels]`.  `filter`'s `in_channels` dimension
  must match that of `input`.
* <b>`output_shape`</b>: A 1-D `Tensor` representing the output shape of the
  deconvolution op.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`.  The
  stride of the sliding window for each dimension of `input`. If a single
  value is given it is replicated in the `H` and `W` dimension. By default
  the `N` and `C` dimensions are set to 0. The dimension order is determined
  by the value of `data_format`, see below for details.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`dilations`</b>: An int or list of `ints` that has length `1`, `2` or `4`,
  defaults to 1. The dilation factor for each dimension of`input`. If a
  single value is given it is replicated in the `H` and `W` dimension. By
  default the `N` and `C` dimensions are set to 1. If set to k > 1, there
  will be k-1 skipped cells between each filter element on that dimension.
  The dimension order is determined by the value of `data_format`, see above
  for details. Dilations in the batch and depth dimensions if a 4-d tensor
  must be 1.
* <b>`name`</b>: Optional name for the returned tensor.


#### Returns:

A `Tensor` with the same type as `input`.



#### Raises:


* <b>`ValueError`</b>: If input/output depth does not match `filter`'s shape, or if
  padding is other than `'VALID'` or `'SAME'`.
