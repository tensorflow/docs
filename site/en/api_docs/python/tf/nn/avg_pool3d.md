page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool3d

Performs the average pooling on the input.

### Aliases:

* `tf.compat.v1.nn.avg_pool3d`
* `tf.compat.v2.nn.avg_pool3d`
* `tf.nn.avg_pool3d`

``` python
tf.nn.avg_pool3d(
    input,
    ksize,
    strides,
    padding,
    data_format='NDHWC',
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

#### Args:


* <b>`input`</b>: A 5-D `Tensor` of shape `[batch, height, width, channels]` and type
  `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `3` or `5`. The size of
  the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `3` or `5`. The
  stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
  See the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NDHWC' and 'NCDHW' are supported.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

A `Tensor` with the same type as `value`.  The average pooled output tensor.
