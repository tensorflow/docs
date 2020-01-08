page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.check_numerics

### Aliases:

* `tf.check_numerics`
* `tf.debugging.check_numerics`

``` python
tf.debugging.check_numerics(
    tensor,
    message,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

Checks a tensor for NaN and Inf values.

When run, reports an `InvalidArgument` error if `tensor` has any values
that are not a number (NaN) or infinity (Inf). Otherwise, passes `tensor` as-is.

#### Args:

* <b>`tensor`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`message`</b>: A `string`. Prefix of the error message.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `tensor`.