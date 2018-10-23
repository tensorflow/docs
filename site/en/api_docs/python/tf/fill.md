

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.fill

``` python
tf.fill(
    dims,
    value,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Constants, Sequences, and Random Values > Constant Value Tensors](../../../api_guides/python/constant_op#Constant_Value_Tensors)

Creates a tensor filled with a scalar value.

This operation creates a tensor of shape `dims` and fills it with `value`.

For example:

```
# Output tensor has shape [2, 3].
fill([2, 3], 9) ==> [[9, 9, 9]
                     [9, 9, 9]]
```

#### Args:

* <b>`dims`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
    1-D. Represents the shape of the output tensor.
* <b>`value`</b>: A `Tensor`. 0-D (scalar). Value to fill the returned tensor.


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `value`.

#### Numpy Compatibility
Equivalent to np.full

