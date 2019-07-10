page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.negative

Computes numerical negative value element-wise.

### Aliases:

* `tf.RaggedTensor.__neg__`
* `tf.Tensor.__neg__`
* `tf.compat.v1.RaggedTensor.__neg__`
* `tf.compat.v1.Tensor.__neg__`
* `tf.compat.v1.math.negative`
* `tf.compat.v1.negative`
* `tf.compat.v2.RaggedTensor.__neg__`
* `tf.compat.v2.Tensor.__neg__`
* `tf.compat.v2.math.negative`
* `tf.compat.v2.negative`
* `tf.math.negative`
* `tf.negative`

``` python
tf.math.negative(
    x,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->

I.e., \\(y = -x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`
