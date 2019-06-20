page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.subtract

``` python
tf.subtract(
    x,
    y,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Arithmetic Operators](../../../api_guides/python/math_ops#Arithmetic_Operators)

Returns x - y element-wise.

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.