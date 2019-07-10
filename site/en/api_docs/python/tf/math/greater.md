page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.greater

Returns the truth value of (x > y) element-wise.

### Aliases:

* `tf.RaggedTensor.__gt__`
* `tf.Tensor.__gt__`
* `tf.compat.v1.RaggedTensor.__gt__`
* `tf.compat.v1.Tensor.__gt__`
* `tf.compat.v1.greater`
* `tf.compat.v1.math.greater`
* `tf.compat.v2.RaggedTensor.__gt__`
* `tf.compat.v2.Tensor.__gt__`
* `tf.compat.v2.greater`
* `tf.compat.v2.math.greater`
* `tf.greater`
* `tf.math.greater`

``` python
tf.math.greater(
    x,
    y,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/greater"><code>math.greater</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
