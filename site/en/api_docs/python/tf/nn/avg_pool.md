

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool

``` python
tf.nn.avg_pool(
    value,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/nn_ops.py).

See the guide: [Neural Network > Pooling](../../../../api_guides/python/nn#Pooling)

Performs the average pooling on the input.

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

#### Args:

* <b>`value`</b>: A 4-D `Tensor` of shape `[batch, height, width, channels]` and type
    `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
* <b>`ksize`</b>: A 1-D int Tensor of 4 elements.
    The size of the window for each dimension of the input tensor.
* <b>`strides`</b>: A 1-D int Tensor of 4 elements
    The stride of the sliding window for each dimension of the
    input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
    See the <a href="../../tf/nn/convolution">comment here</a>
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

A `Tensor` with the same type as `value`.  The average pooled output tensor.