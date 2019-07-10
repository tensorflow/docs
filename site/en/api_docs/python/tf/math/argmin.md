page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.argmin

### Aliases:

* `tf.argmin`
* `tf.math.argmin`

``` python
tf.math.argmin(
    input,
    axis=None,
    name=None,
    dimension=None,
    output_type=tf.dtypes.int64
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/math_ops.py).

Returns the index with the smallest value across axes of a tensor. (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dimension)`. They will be removed in a future version.
Instructions for updating:
Use the `axis` argument instead

Note that in case of ties the identity of the return value is not guaranteed.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
* <b>`axis`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    int32 or int64, must be in the range `[-rank(input), rank(input))`.
    Describes which axis of the input Tensor to reduce across. For vectors,
    use axis = 0.
* <b>`output_type`</b>: An optional <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../../tf/dtypes#int64"><code>tf.int64</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `output_type`.