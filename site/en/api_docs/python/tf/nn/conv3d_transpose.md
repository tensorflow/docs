page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.conv3d_transpose

``` python
tf.nn.conv3d_transpose(
    value,
    filter,
    output_shape,
    strides,
    padding='SAME',
    data_format='NDHWC',
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/nn_ops.py).

See the guide: [Neural Network > Convolution](../../../../api_guides/python/nn#Convolution)

The transpose of `conv3d`.

This operation is sometimes called "deconvolution" after [Deconvolutional
Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf), but is
actually the transpose (gradient) of `conv3d` rather than an actual
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


#### Returns:

A `Tensor` with the same type as `value`.


#### Raises:

* <b>`ValueError`</b>: If input/output depth does not match `filter`'s shape, or if
    padding is other than `'VALID'` or `'SAME'`.