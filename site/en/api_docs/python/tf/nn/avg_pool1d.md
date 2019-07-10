page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.avg_pool1d

Performs the average pooling on the input.

### Aliases:

* `tf.compat.v1.nn.avg_pool1d`
* `tf.compat.v2.nn.avg_pool1d`
* `tf.nn.avg_pool1d`

``` python
tf.nn.avg_pool1d(
    input,
    ksize,
    strides,
    padding,
    data_format='NWC',
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

Each entry in `output` is the mean of the corresponding size `ksize`
window in `value`.

Note internally this op reshapes and uses the underlying 2d operation.

#### Args:


* <b>`input`</b>: A 3-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1` or `3`. The size of the
  window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1` or `3`. The stride of
  the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: An optional string from: "NWC", "NCW". Defaults to "NWC".
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
