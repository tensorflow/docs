page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.rint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/rint">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns element-wise integer closest to x.

### Aliases:

* <a href="/api_docs/python/tf/math/rint"><code>tf.compat.v1.math.rint</code></a>
* <a href="/api_docs/python/tf/math/rint"><code>tf.compat.v1.rint</code></a>
* <a href="/api_docs/python/tf/math/rint"><code>tf.compat.v2.math.rint</code></a>
* <a href="/api_docs/python/tf/math/rint"><code>tf.rint</code></a>


``` python
tf.math.rint(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If the result is midway between two representable values,
the even representable is chosen.
For example:

```
rint(-1.5) ==> -2.0
rint(0.5000001) ==> 1.0
rint([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]) ==> [-2., -2., -0., 0., 2., 2., 2.]
```

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
