page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.cast

### Aliases:

* `tf.cast`
* `tf.dtypes.cast`

``` python
tf.dtypes.cast(
    x,
    dtype,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/math_ops.py).

Casts a tensor to a new type.

The operation casts `x` (in case of `Tensor`) or `x.values`
(in case of `SparseTensor` or `IndexedSlices`) to `dtype`.

For example:

```python
x = tf.constant([1.8, 2.2], dtype=tf.float32)
tf.cast(x, tf.int32)  # [1, 2], dtype=tf.int32
```

The operation supports data types (for `x` and `dtype`) of
`uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`,
`float16`, `float32`, `float64`, `complex64`, `complex128`, `bfloat16`.
In case of casting from complex types (`complex64`, `complex128`) to real
types, only the real part of `x` is returned. In case of casting from real
types to complex types (`complex64`, `complex128`), the imaginary part of the
returned value is set to `0`. The handling of complex types here matches the
behavior of numpy.

#### Args:

* <b>`x`</b>: A `Tensor` or `SparseTensor` or `IndexedSlices` of numeric type. It could
    be `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`,
    `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`,
    `bfloat16`.
* <b>`dtype`</b>: The destination type. The list of supported dtypes is the same as
    `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` or `IndexedSlices` with same shape as `x` and
  same type as `dtype`.


#### Raises:

* <b>`TypeError`</b>: If `x` cannot be cast to the `dtype`.