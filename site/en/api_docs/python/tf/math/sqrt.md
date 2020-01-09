page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sqrt


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/sqrt">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes square root of x element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/sqrt"><code>tf.compat.v1.math.sqrt</code></a>
* <a href="/api_docs/python/tf/math/sqrt"><code>tf.compat.v1.sqrt</code></a>
* <a href="/api_docs/python/tf/math/sqrt"><code>tf.compat.v2.math.sqrt</code></a>
* <a href="/api_docs/python/tf/math/sqrt"><code>tf.compat.v2.sqrt</code></a>
* <a href="/api_docs/python/tf/math/sqrt"><code>tf.sqrt</code></a>


``` python
tf.math.sqrt(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

I.e., \\(y = \sqrt{x} = x^{1/2}\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sqrt(x.values, ...), x.dense_shape)`
