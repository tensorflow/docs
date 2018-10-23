

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.saturate_cast

``` python
saturate_cast(
    value,
    dtype,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/math_ops.py).

See the guide: [Tensor Transformations > Casting](../../../api_guides/python/array_ops#Casting)

Performs a safe saturating cast of `value` to `dtype`.

This function casts the input to `dtype` without applying any scaling.  If
there is a danger that values would over or underflow in the cast, this op
applies the appropriate clamping before the cast.

#### Args:

* <b>`value`</b>: A `Tensor`.
* <b>`dtype`</b>: The desired output `DType`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  `value` safely cast to `dtype`.