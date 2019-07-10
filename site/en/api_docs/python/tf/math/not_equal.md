page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.not_equal

Returns the truth value of (x != y) element-wise.

### Aliases:

* `tf.compat.v1.math.not_equal`
* `tf.compat.v1.not_equal`
* `tf.compat.v2.math.not_equal`
* `tf.compat.v2.not_equal`
* `tf.math.not_equal`
* `tf.not_equal`

``` python
tf.math.not_equal(
    x,
    y,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/not_equal"><code>math.not_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`, `complex64`, `quint8`, `qint8`, `qint32`, `string`, `bool`, `complex128`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
