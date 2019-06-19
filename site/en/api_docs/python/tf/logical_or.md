page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.logical_or

``` python
tf.logical_or(
    x,
    y,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_math_ops.py`.

See the guide: [Control Flow > Logical Operators](../../../api_guides/python/control_flow_ops#Logical_Operators)

Returns the truth value of x OR y element-wise.

*NOTE*: `LogicalOr` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:

* <b>`x`</b>: A `Tensor` of type `bool`.
* <b>`y`</b>: A `Tensor` of type `bool`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.