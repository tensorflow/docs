page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.erf


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/erf">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes the Gauss error function of `x` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/erf"><code>tf.compat.v1.erf</code></a>
* <a href="/api_docs/python/tf/math/erf"><code>tf.compat.v1.math.erf</code></a>
* <a href="/api_docs/python/tf/math/erf"><code>tf.compat.v2.math.erf</code></a>
* <a href="/api_docs/python/tf/math/erf"><code>tf.erf</code></a>


``` python
tf.math.erf(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.erf(x.values, ...), x.dense_shape)`
