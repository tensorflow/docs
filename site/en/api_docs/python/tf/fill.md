

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.fill

### `tf.fill`

``` python
fill(
    dims,
    value,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

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

* <b>`dims`</b>: A `Tensor` of type `int32`.
    1-D. Represents the shape of the output tensor.
* <b>`value`</b>: A `Tensor`. 0-D (scalar). Value to fill the returned tensor.


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `value`.

#### numpy compatibility
    Equivalent to np.full

