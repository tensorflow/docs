

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.check_numerics

``` python
check_numerics(
    tensor,
    message,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

See the guide: [Control Flow > Debugging Operations](../../../api_guides/python/control_flow_ops#Debugging_Operations)

Checks a tensor for NaN and Inf values.

When run, reports an `InvalidArgument` error if `tensor` has any values
that are not a number (NaN) or infinity (Inf). Otherwise, passes `tensor` as-is.

#### Args:

* <b>`tensor`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
* <b>`message`</b>: A `string`. Prefix of the error message.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `tensor`.