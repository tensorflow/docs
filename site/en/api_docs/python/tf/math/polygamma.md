page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.polygamma


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Compute the polygamma function \\(\psi^{(n)}(x)\\).

### Aliases:

* `tf.compat.v1.math.polygamma`
* `tf.compat.v1.polygamma`
* `tf.compat.v2.math.polygamma`


``` python
tf.math.polygamma(
    a,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The polygamma function is defined as:


\\(\psi^{(a)}(x) = \frac{d^a}{dx^a} \psi(x)\\)

where \\(\psi(x)\\) is the digamma function.
The polygamma function is defined only for non-negative integer orders \\a\\.

#### Args:


* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `a`.
