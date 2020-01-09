page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.igammac


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Compute the upper regularized incomplete Gamma function `Q(a, x)`.

### Aliases:

* `tf.compat.v1.igammac`
* `tf.compat.v1.math.igammac`
* `tf.compat.v2.math.igammac`


``` python
tf.math.igammac(
    a,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The upper regularized incomplete Gamma function is defined as:

\\(Q(a, x) = Gamma(a, x) / Gamma(a) = 1 - P(a, x)\\)

where

\\(Gamma(a, x) = int_{x}^{\infty} t^{a-1} exp(-t) dt\\)

is the upper incomplete Gama function.

Note, above `P(a, x)` (`Igamma`) is the lower regularized complete
Gamma function.

#### Args:


* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `a`.
