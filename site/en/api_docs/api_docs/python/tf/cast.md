

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.cast

``` python
tf.cast(
    x,
    dtype,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Casts a tensor to a new type.

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor`) to `dtype`.

For example:

```python
x = tf.constant([1.8, 2.2], dtype=tf.float32)
tf.cast(x, tf.int32)  # [1, 2], dtype=tf.int32
```

The operation supports data types (for `x` and `dtype`) of
`uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `float16`, `float32`,
`float64`, `complex64`, `complex128`, `bfloat16`. In case of casting from
complex types (`complex64`, `complex128`) to real types, only the real part
of `x` is returned. In case of casting from real types to complex types
(`complex64`, `complex128`), the imaginary part of the returned value is set
to `0`. The handling of complex types here matches the behavior of numpy.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor` of numeric type. It could be
    `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`,
    `float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
* <b>`dtype`</b>: The destination type. The list of supported dtypes is the same
    as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` with same shape as `x` and
  same type as `dtype`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `dtype`.