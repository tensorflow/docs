

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.subtract

### `tf.subtract`

``` python
subtract(
    x,
    y,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/math_ops.py).

See the guide: [Math > Arithmetic Operators](../../../api_guides/python/math_ops#Arithmetic_Operators)

Returns x - y element-wise.

*NOTE*: `tf.subtract` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `x`.