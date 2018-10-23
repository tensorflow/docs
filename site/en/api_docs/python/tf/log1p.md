

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.log1p

``` python
tf.log1p(
    x,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_math_ops.py`.

See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Computes natural logarithm of (1 + x) element-wise.

I.e., \\(y = \log_e (1 + x)\\).

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.