page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.bitwise.invert

Flips all bits elementwise.

### Aliases:

* `tf.bitwise.invert`
* `tf.compat.v1.bitwise.invert`
* `tf.compat.v2.bitwise.invert`

``` python
tf.bitwise.invert(
    x,
    name=None
)
```



Defined in generated file: `python/ops/gen_bitwise_ops.py`.

<!-- Placeholder for "Used in" -->

The result will have exactly those bits set, that are not set in `x`. The
computation is performed on the underlying representation of x.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
