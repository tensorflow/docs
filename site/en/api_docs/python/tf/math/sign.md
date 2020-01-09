page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.sign


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/sign">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns an element-wise indication of the sign of a number.

### Aliases:

* <a href="/api_docs/python/tf/math/sign"><code>tf.compat.v1.math.sign</code></a>
* <a href="/api_docs/python/tf/math/sign"><code>tf.compat.v1.sign</code></a>
* <a href="/api_docs/python/tf/math/sign"><code>tf.compat.v2.math.sign</code></a>
* <a href="/api_docs/python/tf/math/sign"><code>tf.compat.v2.sign</code></a>
* <a href="/api_docs/python/tf/math/sign"><code>tf.sign</code></a>


``` python
tf.math.sign(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

`y = sign(x) = -1` if `x < 0`; 0 if `x == 0`; 1 if `x > 0`.

For complex numbers, `y = sign(x) = x / |x|` if `x != 0`, otherwise `y = 0`.

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.sign(x.values, ...), x.dense_shape)`
