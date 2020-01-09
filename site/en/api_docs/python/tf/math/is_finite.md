page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.is_finite


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/is_finite">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns which elements of x are finite.

### Aliases:

* <a href="/api_docs/python/tf/math/is_finite"><code>tf.compat.v1.debugging.is_finite</code></a>
* <a href="/api_docs/python/tf/math/is_finite"><code>tf.compat.v1.is_finite</code></a>
* <a href="/api_docs/python/tf/math/is_finite"><code>tf.compat.v1.math.is_finite</code></a>
* <a href="/api_docs/python/tf/math/is_finite"><code>tf.compat.v2.math.is_finite</code></a>
* <a href="/api_docs/python/tf/math/is_finite"><code>tf.debugging.is_finite</code></a>
* <a href="/api_docs/python/tf/math/is_finite"><code>tf.is_finite</code></a>


``` python
tf.math.is_finite(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->



#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.


#### Numpy Compatibility
Equivalent to np.isfinite
