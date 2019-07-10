page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.round

Rounds the values of a tensor to the nearest integer, element-wise.

### Aliases:

* `tf.compat.v1.math.round`
* `tf.compat.v1.round`
* `tf.compat.v2.math.round`
* `tf.compat.v2.round`
* `tf.math.round`
* `tf.round`

``` python
tf.math.round(
    x,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Rounds half to even.  Also known as bankers rounding. If you want to round
according to the current system rounding mode use tf::cint.
For example:

```python
x = tf.constant([0.9, 2.5, 2.3, 1.5, -4.5])
tf.round(x)  # [ 1.0, 2.0, 2.0, 2.0, -4.0 ]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, or `int64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of same shape and type as `x`.
