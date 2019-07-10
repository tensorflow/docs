page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.subtract

Returns x - y element-wise.

### Aliases:

* `tf.RaggedTensor.__sub__`
* `tf.compat.v1.RaggedTensor.__sub__`
* `tf.compat.v1.math.subtract`
* `tf.compat.v1.subtract`
* `tf.compat.v2.RaggedTensor.__sub__`
* `tf.compat.v2.math.subtract`
* `tf.compat.v2.subtract`
* `tf.math.subtract`
* `tf.subtract`

``` python
tf.math.subtract(
    x,
    y,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

*NOTE*: `Subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `uint16`, `int16`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
