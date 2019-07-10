page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.max_pool3d

Performs the max pooling on the input.

### Aliases:

* `tf.compat.v1.nn.max_pool3d`
* `tf.compat.v2.nn.max_pool3d`
* `tf.nn.max_pool3d`

``` python
tf.nn.max_pool3d(
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


#### Args:


* <b>`input`</b>: A 5-D `Tensor` of the format specified by `data_format`.
* <b>`ksize`</b>: An int or list of `ints` that has length `1`, `3` or `5`. The size of
  the window for each dimension of the input tensor.
* <b>`strides`</b>: An int or list of `ints` that has length `1`, `3` or `5`. The
  stride of the sliding window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
  the "returns" section of <a href="../../tf/nn/convolution"><code>tf.nn.convolution</code></a> for details.
* <b>`data_format`</b>: An optional string from: "NDHWC", "NCDHW". Defaults to "NDHWC".
  The data format of the input and output data. With the default format
  "NDHWC", the data is stored in the order of: [batch, in_depth, in_height,
    in_width, in_channels]. Alternatively, the format could be "NCDHW", the
  data storage order is: [batch, in_channels, in_depth, in_height,
    in_width].
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of format specified by `data_format`.
The max pooled output tensor.
