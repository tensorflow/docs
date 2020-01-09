page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.acosh


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/acosh">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes inverse hyperbolic cosine of x element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/acosh"><code>tf.acosh</code></a>
* <a href="/api_docs/python/tf/math/acosh"><code>tf.compat.v1.acosh</code></a>
* <a href="/api_docs/python/tf/math/acosh"><code>tf.compat.v1.math.acosh</code></a>
* <a href="/api_docs/python/tf/math/acosh"><code>tf.compat.v2.acosh</code></a>
* <a href="/api_docs/python/tf/math/acosh"><code>tf.compat.v2.math.acosh</code></a>


``` python
tf.math.acosh(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given an input tensor, the function computes inverse hyperbolic cosine of every element.
Input range is `[1, inf]`. It returns `nan` if the input lies outside the range.

```python
x = tf.constant([-2, -0.5, 1, 1.2, 200, 10000, float("inf")])
tf.math.acosh(x) ==> [nan nan 0. 0.62236255 5.9914584 9.903487 inf]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
