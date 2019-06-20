page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.polygamma

### Aliases:

* `tf.math.polygamma`
* `tf.polygamma`

``` python
tf.polygamma(
    a,
    x,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_math_ops.py`.

See the guide: [Math > Basic Math Functions](../../../api_guides/python/math_ops#Basic_Math_Functions)

Compute the polygamma function \\(\psi^{(n)} (x)\\).

The polygamma function is defined as:


\\(\psi^{(n)} (x) = \frac{d^n}{dx^n} \psi(x)\\)

where \\(\psi(x)\\) is the digamma function.

#### Args:

* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `a`.