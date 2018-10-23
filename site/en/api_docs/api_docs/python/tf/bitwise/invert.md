

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.bitwise.invert

``` python
invert(
    x,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_bitwise_ops.py`.

Flips all bits elementwise.

The result will have exactly those bits set, that are not set in `x`. The
computation is performed on the underlying representation of x.

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.