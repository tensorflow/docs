page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool

Performs the average pooling on the input.

### Aliases:

* `tf.compat.v1.nn.avg_pool`
* `tf.compat.v1.nn.avg_pool2d`
* `tf.nn.avg_pool`
* `tf.nn.avg_pool2d`

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



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

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
