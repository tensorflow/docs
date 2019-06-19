page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitwise.right_shift

``` python
tf.bitwise.right_shift(
    x,
    y,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_bitwise_ops.py`.

Elementwise computes the bitwise right-shift of `x` and `y`.

Performs a logical shift for unsigned integer types, and an arithmetic shift
for signed integer types.

If `y` is negative, or greater than or equal to than the width of `x` in bits
the result is implementation defined.

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.