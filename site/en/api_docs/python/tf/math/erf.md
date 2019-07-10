page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.erf

Computes the Gauss error function of `x` element-wise.

### Aliases:

* `tf.compat.v1.erf`
* `tf.compat.v1.math.erf`
* `tf.compat.v2.math.erf`
* `tf.erf`
* `tf.math.erf`

``` python
tf.math.erf(
    x,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.erf(x.values, ...), x.dense_shape)`
