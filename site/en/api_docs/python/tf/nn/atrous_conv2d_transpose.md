page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.atrous_conv2d_transpose


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/atrous_conv2d_transpose">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L2278-L2427">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



The transpose of `atrous_conv2d`.

### Aliases:

* <a href="/api_docs/python/tf/nn/atrous_conv2d_transpose"><code>tf.compat.v1.nn.atrous_conv2d_transpose</code></a>
* <a href="/api_docs/python/tf/nn/atrous_conv2d_transpose"><code>tf.compat.v2.nn.atrous_conv2d_transpose</code></a>


``` python
tf.nn.atrous_conv2d_transpose(
    value,
    filters,
    output_shape,
    rate,
    padding,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation is sometimes called "deconvolution" after [Deconvolutional
Networks](https://www.matthewzeiler.com/mattzeiler/deconvolutionalnetworks.pdf),
but is really the transpose (gradient) of `atrous_conv2d` rather than an
actual deconvolution.

#### Args:


* <b>`value`</b>: A 4-D `Tensor` of type `float`. It needs to be in the default `NHWC`
  format. Its shape is `[batch, in_height, in_width, in_channels]`.
* <b>`filters`</b>: A 4-D `Tensor` with the same type as `value` and shape
  `[filter_height, filter_width, out_channels, in_channels]`. `filters`'
  `in_channels` dimension must match that of `value`. Atrous convolution is
  equivalent to standard convolution with upsampled filters with effective
  height `filter_height + (filter_height - 1) * (rate - 1)` and effective
  width `filter_width + (filter_width - 1) * (rate - 1)`, produced by
  inserting `rate - 1` zeros along consecutive elements across the
  `filters`' spatial dimensions.
* <b>`output_shape`</b>: A 1-D `Tensor` of shape representing the output shape of the
  deconvolution op.
* <b>`rate`</b>: A positive int32. The stride with which we sample input values across
  the `height` and `width` dimensions. Equivalently, the rate by which we
  upsample the filter values by inserting zeros across the `height` and
  `width` dimensions. In the literature, the same parameter is sometimes
  called `input stride` or `dilation`.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
* <b>`name`</b>: Optional name for the returned tensor.


#### Returns:

A `Tensor` with the same type as `value`.



#### Raises:


* <b>`ValueError`</b>: If input/output depth does not match `filters`' shape, or if
  padding is other than `'VALID'` or `'SAME'`, or if the `rate` is less
  than one, or if the output_shape is not a tensor with 4 elements.
