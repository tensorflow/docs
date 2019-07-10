page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.conv3d_transpose

The transpose of `conv3d`.

### Aliases:

* `tf.compat.v1.nn.conv3d_transpose`
* `tf.nn.conv3d_transpose`

``` python
tf.nn.conv3d_transpose(
    value,
    filter=None,
    output_shape=None,
    strides=None,
    padding='SAME',
    data_format='NDHWC',
    name=None,
    input=None,
    filters=None,
    dilations=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after [Deconvolutional
Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf),
but is really the transpose (gradient) of `conv3d` rather than an actual
deconvolution.

#### Args:


* <b>`value`</b>: A 5-D `Tensor` of type `float` and shape
  `[batch, depth, height, width, in_channels]`.
* <b>`filter`</b>: A 5-D `Tensor` with the same type as `value` and shape
  `[depth, height, width, output_channels, in_channels]`.  `filter`'s
  `in_channels` dimension must match that of `value`.
* <b>`output_shape`</b>: A 1-D `Tensor` representing the output shape of the
  deconvolution op.
* <b>`strides`</b>: A list of ints. The stride of the sliding window for each
  dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
  See the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string, either `'NDHWC'` or `'NCDHW`' specifying the layout
  of the input and output tensors. Defaults to `'NDHWC'`.
* <b>`name`</b>: Optional name for the returned tensor.
* <b>`input`</b>: Alias of value.
* <b>`filters`</b>: Alias of filter.
* <b>`dilations`</b>: An int or list of `ints` that has length `1`, `3` or `5`,
  defaults to 1. The dilation factor for each dimension of`input`. If a
  single value is given it is replicated in the `D`, `H` and `W` dimension.
  By default the `N` and `C` dimensions are set to 1. If set to k > 1, there
  will be k-1 skipped cells between each filter element on that dimension.
  The dimension order is determined by the value of `data_format`, see above
  for details. Dilations in the batch and depth dimensions if a 5-d tensor
  must be 1.


#### Returns:

A `Tensor` with the same type as `value`.



#### Raises:


* <b>`ValueError`</b>: If input/output depth does not match `filter`'s shape, or if
  padding is other than `'VALID'` or `'SAME'`.