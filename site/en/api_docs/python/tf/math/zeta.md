page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.zeta

Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

### Aliases:

* `tf.compat.v1.math.zeta`
* `tf.compat.v1.zeta`
* `tf.compat.v2.math.zeta`
* `tf.math.zeta`
* `tf.zeta`

``` python
tf.math.zeta(
    x,
    q,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

The Hurwitz zeta function is defined as:


\\(\zeta(x, q) = \sum_{n=0}^{\infty} (q + n)^{-x}\\)

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`q`</b>: A `Tensor`. Must have the same type as `x`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
