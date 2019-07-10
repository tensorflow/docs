page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.log_sigmoid

Computes log sigmoid of `x` element-wise.

### Aliases:

* `tf.compat.v1.log_sigmoid`
* `tf.compat.v1.math.log_sigmoid`
* `tf.compat.v2.math.log_sigmoid`
* `tf.log_sigmoid`
* `tf.math.log_sigmoid`

``` python
tf.math.log_sigmoid(
    x,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Specifically, `y = log(1 / (1 + exp(-x)))`.  For numerical stability,
we use `y = -tf.nn.softplus(-x)`.

#### Args:


* <b>`x`</b>: A Tensor with type `float32` or `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A Tensor with the same type as `x`.
