page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.bessel_i1e


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/bessel_i1e">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes the Bessel i1e function of `x` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/bessel_i1e"><code>tf.compat.v1.math.bessel_i1e</code></a>
* <a href="/api_docs/python/tf/math/bessel_i1e"><code>tf.compat.v2.math.bessel_i1e</code></a>


``` python
tf.math.bessel_i1e(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Exponentially scaled modified Bessel function of order 0 defined as
`bessel_i1e(x) = exp(-abs(x)) bessel_i1(x)`.

This function is faster and numerically stabler than `bessel_i1(x)`.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.bessel_i1e(x.values, ...), x.dense_shape)`
