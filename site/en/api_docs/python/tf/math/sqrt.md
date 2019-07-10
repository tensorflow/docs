page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sqrt

Computes square root of x element-wise.

### Aliases:

* `tf.compat.v1.math.sqrt`
* `tf.compat.v1.sqrt`
* `tf.compat.v2.math.sqrt`
* `tf.compat.v2.sqrt`
* `tf.math.sqrt`
* `tf.sqrt`

``` python
tf.math.sqrt(
    x,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

I.e., \\(y = \sqrt{x} = x^{1/2}\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sqrt(x.values, ...), x.dense_shape)`
