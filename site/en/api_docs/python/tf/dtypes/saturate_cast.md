page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.saturate_cast

Performs a safe saturating cast of `value` to `dtype`.

### Aliases:

* `tf.compat.v1.dtypes.saturate_cast`
* `tf.compat.v1.saturate_cast`
* `tf.compat.v2.dtypes.saturate_cast`
* `tf.compat.v2.saturate_cast`
* `tf.dtypes.saturate_cast`
* `tf.saturate_cast`

``` python
tf.dtypes.saturate_cast(
    value,
    dtype,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

This function casts the input to `dtype` without applying any scaling.  If
there is a danger that values would over or underflow in the cast, this op
applies the appropriate clamping before the cast.

#### Args:


* <b>`value`</b>: A `Tensor`.
* <b>`dtype`</b>: The desired output `DType`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

`value` safely cast to `dtype`.
