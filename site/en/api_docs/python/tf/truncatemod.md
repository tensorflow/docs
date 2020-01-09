page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.truncatemod


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns element-wise remainder of division. This emulates C semantics in that

### Aliases:

* `tf.compat.v1.truncatemod`
* `tf.compat.v2.truncatemod`


``` python
tf.truncatemod(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

the result here is consistent with a truncating divide. E.g. `truncate(x / y) *
y + truncate_mod(x, y) = x`.

*NOTE*: `truncatemod` supports broadcasting. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
* <b>`y`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
