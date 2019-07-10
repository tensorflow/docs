page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitwise.left_shift

Elementwise computes the bitwise left-shift of `x` and `y`.

### Aliases:

* `tf.bitwise.left_shift`
* `tf.compat.v1.bitwise.left_shift`
* `tf.compat.v2.bitwise.left_shift`

``` python
tf.bitwise.left_shift(
    x,
    y,
    name=None
)
```



Defined in generated file: `python/ops/gen_bitwise_ops.py`.

<!-- Placeholder for "Used in" -->

If `y` is negative, or greater than or equal to the width of `x` in bits the
result is implementation defined.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
