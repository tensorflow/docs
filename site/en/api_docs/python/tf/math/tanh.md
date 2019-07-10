page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.tanh

Computes hyperbolic tangent of `x` element-wise.

### Aliases:

* `tf.compat.v1.math.tanh`
* `tf.compat.v1.nn.tanh`
* `tf.compat.v1.tanh`
* `tf.compat.v2.math.tanh`
* `tf.compat.v2.nn.tanh`
* `tf.compat.v2.tanh`
* `tf.math.tanh`
* `tf.nn.tanh`
* `tf.tanh`

``` python
tf.math.tanh(
    x,
    name=None
)
```



Defined in generated file: `python/ops/gen_math_ops.py`.

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.tanh(x.values, ...), x.dense_shape)`
