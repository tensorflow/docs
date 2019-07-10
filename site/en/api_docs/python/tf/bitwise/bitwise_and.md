page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitwise.bitwise_and

Elementwise computes the bitwise AND of `x` and `y`.

### Aliases:

* `tf.bitwise.bitwise_and`
* `tf.compat.v1.bitwise.bitwise_and`
* `tf.compat.v2.bitwise.bitwise_and`

``` python
tf.bitwise.bitwise_and(
    x,
    y,
    name=None
)
```



Defined in generated file: `python/ops/gen_bitwise_ops.py`.

<!-- Placeholder for "Used in" -->

The result will have those bits set, that are set in both `x` and `y`. The
computation is performed on the underlying representations of `x` and `y`.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
