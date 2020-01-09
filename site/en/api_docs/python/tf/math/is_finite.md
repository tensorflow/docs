page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.is_finite


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns which elements of x are finite.

### Aliases:

* `tf.compat.v1.debugging.is_finite`
* `tf.compat.v1.is_finite`
* `tf.compat.v1.math.is_finite`
* `tf.compat.v2.math.is_finite`


``` python
tf.math.is_finite(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->



#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


#### Numpy Compatibility
Equivalent to np.isfinite
