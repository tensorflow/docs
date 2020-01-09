page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.igamma


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/igamma">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Compute the lower regularized incomplete Gamma function `P(a, x)`.

### Aliases:

* <a href="/api_docs/python/tf/math/igamma"><code>tf.compat.v1.igamma</code></a>
* <a href="/api_docs/python/tf/math/igamma"><code>tf.compat.v1.math.igamma</code></a>
* <a href="/api_docs/python/tf/math/igamma"><code>tf.compat.v2.math.igamma</code></a>
* <a href="/api_docs/python/tf/math/igamma"><code>tf.igamma</code></a>


``` python
tf.math.igamma(
    a,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The lower regularized incomplete Gamma function is defined as:


\\(P(a, x) = gamma(a, x) / Gamma(a) = 1 - Q(a, x)\\)

where

\\(gamma(a, x) = \\int_{0}^{x} t^{a-1} exp(-t) dt\\)

is the lower incomplete Gamma function.

Note, above `Q(a, x)` (`Igammac`) is the upper regularized complete
Gamma function.

#### Args:


* <b>`a`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`x`</b>: A `Tensor`. Must have the same type as `a`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `a`.
