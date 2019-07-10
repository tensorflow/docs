page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.max_pool2d

Performs the max pooling on the input.

### Aliases:

* `tf.compat.v1.nn.max_pool2d`
* `tf.compat.v2.nn.max_pool2d`
* `tf.nn.max_pool2d`

``` python
tf.nn.max_pool2d(
    input,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A 4-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `2` or `4`. The size of
  the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `2` or `4`. The
  stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: A string. 'NHWC', 'NCHW' and 'NCHW_VECT_C' are supported.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
