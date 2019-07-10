page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.divide_no_nan

Computes an unsafe divide which returns 0 if the y is zero.

### Aliases:

* `tf.compat.v1.div_no_nan`
* `tf.compat.v1.math.divide_no_nan`
* `tf.compat.v2.math.divide_no_nan`
* `tf.div_no_nan`
* `tf.math.divide_no_nan`

``` python
tf.math.divide_no_nan(
    x,
    y,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`y`</b>: A `Tensor` whose dtype is compatible with `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The element-wise value of the x divided by y.
