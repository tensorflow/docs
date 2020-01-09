page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.negative


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/negative">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes numerical negative value element-wise.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__neg__"><code>tf.RaggedTensor.__neg__</code></a>
* <a href="/api_docs/python/tf/Tensor#__neg__"><code>tf.Tensor.__neg__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__neg__"><code>tf.compat.v1.RaggedTensor.__neg__</code></a>
* <a href="/api_docs/python/tf/Tensor#__neg__"><code>tf.compat.v1.Tensor.__neg__</code></a>
* <a href="/api_docs/python/tf/math/negative"><code>tf.compat.v1.math.negative</code></a>
* <a href="/api_docs/python/tf/math/negative"><code>tf.compat.v1.negative</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__neg__"><code>tf.compat.v2.RaggedTensor.__neg__</code></a>
* <a href="/api_docs/python/tf/Tensor#__neg__"><code>tf.compat.v2.Tensor.__neg__</code></a>
* <a href="/api_docs/python/tf/math/negative"><code>tf.compat.v2.math.negative</code></a>
* <a href="/api_docs/python/tf/math/negative"><code>tf.compat.v2.negative</code></a>
* <a href="/api_docs/python/tf/math/negative"><code>tf.negative</code></a>


``` python
tf.math.negative(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

I.e., \\(y = -x\\).

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.negative(x.values, ...), x.dense_shape)`
