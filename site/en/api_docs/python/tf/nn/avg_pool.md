page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/nn/avg_pool">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L3542-L3583">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs the average pooling on the input.

### Aliases:

* <a href="/api_docs/python/tf/nn/avg_pool"><code>tf.compat.v1.nn.avg_pool</code></a>
* <a href="/api_docs/python/tf/nn/avg_pool"><code>tf.compat.v1.nn.avg_pool2d</code></a>
* <a href="/api_docs/python/tf/nn/avg_pool"><code>tf.nn.avg_pool2d</code></a>


``` python
tf.nn.avg_pool(
    value,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None,
    input=None
)
```



<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

#### Args:


* <b>`value`</b>: A 4-D `Tensor` of shape `[batch, height, width, channels]` and type
  `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `2` or `4`. The size of
  the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`. The
  stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
  See the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`name`</b>: Optional name for the operation.
* <b>`input`</b>: Alias for value.


#### Returns:

A `Tensor` with the same type as `value`.  The average pooled output tensor.
