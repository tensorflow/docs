page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sin


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes sine of x element-wise.

### Aliases:

* `tf.compat.v1.math.sin`
* `tf.compat.v1.sin`
* `tf.compat.v2.math.sin`
* `tf.compat.v2.sin`
* `tf.sin`


``` python
tf.math.sin(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  Given an input tensor, this function computes sine of every
  element in the tensor. Input range is `(-inf, inf)` and
  output range is `[-1,1]`.

>     x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10, float("inf")])
>     tf.math.sin(x) ==> [nan -0.4121185 -0.47942555 0.84147096 0.9320391 -0.87329733 -0.54402107 nan]

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
