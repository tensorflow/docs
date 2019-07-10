page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.greater_equal

Returns the truth value of (x >= y) element-wise.

### Aliases:

* `tf.RaggedTensor.__ge__`
* `tf.Tensor.__ge__`
* `tf.compat.v1.RaggedTensor.__ge__`
* `tf.compat.v1.Tensor.__ge__`
* `tf.compat.v1.greater_equal`
* `tf.compat.v1.math.greater_equal`
* `tf.compat.v2.RaggedTensor.__ge__`
* `tf.compat.v2.Tensor.__ge__`
* `tf.compat.v2.greater_equal`
* `tf.compat.v2.math.greater_equal`
* `tf.greater_equal`
* `tf.math.greater_equal`

``` python
tf.math.greater_equal(
    x,
    y,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

*NOTE*: <a href="../../tf/math/greater_equal"><code>math.greater_equal</code></a> supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
