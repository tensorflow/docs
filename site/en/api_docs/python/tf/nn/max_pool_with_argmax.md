page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.max_pool_with_argmax

``` python
tf.nn.max_pool_with_argmax(
    input,
    ksize,
    strides,
    padding,
    Targmax=tf.int64,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_nn_ops.py`.

See the guide: [Neural Network > Pooling](../../../../api_guides/python/nn#Pooling)

Performs max pooling on the input and outputs both max values and indices.

The indices in `argmax` are flattened, so that a maximum value at position
`[b, y, x, c]` becomes flattened index
`((b * height + y) * width + x) * channels + c`.

The indices returned are always in `[0, height) x [0, width)` before flattening,
even if padding is involved and the mathematically correct answer is outside
(either negative or too large).  This is a bug, but fixing it is difficult to do
in a safe backwards compatible way, especially due to flattening.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    4-D with shape `[batch, height, width, channels]`.  Input to pool over.
* <b>`ksize`</b>: A list of `ints` that has length `>= 4`.
    The size of the window for each dimension of the input tensor.
* <b>`strides`</b>: A list of `ints` that has length `>= 4`.
    The stride of the sliding window for each dimension of the
    input tensor.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
    The type of padding algorithm to use.
* <b>`Targmax`</b>: An optional <a href="../../tf/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf/int64"><code>tf.int64</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (output, argmax).

* <b>`output`</b>: A `Tensor`. Has the same type as `input`.
* <b>`argmax`</b>: A `Tensor` of type `Targmax`.