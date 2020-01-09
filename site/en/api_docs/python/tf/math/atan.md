page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.atan


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes the trignometric inverse tangent of x element-wise.

### Aliases:

* `tf.atan`
* `tf.compat.v1.atan`
* `tf.compat.v1.math.atan`
* `tf.compat.v2.atan`
* `tf.compat.v2.math.atan`


``` python
tf.math.atan(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The <a href="../../tf/math/atan"><code>tf.math.atan</code></a> operation returns the inverse of <a href="../../tf/math/tan"><code>tf.math.tan</code></a>, such that
if `y = tf.math.tan(x)` then, `x = tf.math.atan(y)`.

**Note**: The output of <a href="../../tf/math/atan"><code>tf.math.atan</code></a> will lie within the invertible range 
of tan, i.e (-pi/2, pi/2).

#### For example:



```python
# Note: [1.047, 0.785] ~= [(pi/3), (pi/4)]
x = tf.constant([1.047, 0.785])
y = tf.math.tan(x) # [1.731261, 0.99920404]

tf.math.atan(y) # [1.047, 0.785] = x
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
