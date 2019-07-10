page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.div_no_nan

``` python
tf.div_no_nan(
    x,
    y,
    name=None
)
```



Defined in [`tensorflow/python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/math_ops.py).

Computes an unsafe divide which returns 0 if the y is zero.

#### Args:

* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`y`</b>: A `Tensor` whose dtype is compatible with `x`.
* <b>`name`</b>: A name for the operation (optional).

#### Returns:

The element-wise value of the x divided by y.