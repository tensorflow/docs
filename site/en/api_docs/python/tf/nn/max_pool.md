

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.nn.max_pool

### `tf.nn.max_pool`

``` python
max_pool(
    value,
    ksize,
    strides,
    padding,
    data_format='NHWC',
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/nn_ops.py).

See the guide: [Neural Network > Pooling](../../../../api_guides/python/nn#Pooling)

Performs the max pooling on the input.

#### Args:

* <b>`value`</b>: A 4-D `Tensor` with shape `[batch, height, width, channels]` and
    type `tf.float32`.
* <b>`ksize`</b>: A list of ints that has length >= 4.  The size of the window for
    each dimension of the input tensor.
* <b>`strides`</b>: A list of ints that has length >= 4.  The stride of the sliding
    window for each dimension of the input tensor.
* <b>`padding`</b>: A string, either `'VALID'` or `'SAME'`. The padding algorithm.
    See the [comment here](../../tf/nn/convolution)
* <b>`data_format`</b>: A string. 'NHWC' and 'NCHW' are supported.
* <b>`name`</b>: Optional name for the operation.


#### Returns:

  A `Tensor` with type `tf.float32`.  The max pooled output tensor.