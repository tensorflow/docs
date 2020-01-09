page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.reciprocal


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes the reciprocal of x element-wise.

### Aliases:

* `tf.compat.v1.math.reciprocal`
* `tf.compat.v1.reciprocal`
* `tf.compat.v2.math.reciprocal`


``` python
tf.math.reciprocal(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

I.e., \\(y = 1 / x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
