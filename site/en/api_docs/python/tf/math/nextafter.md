page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.nextafter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/nextafter">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Returns the next representable value of `x1` in the direction of `x2`, element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/nextafter"><code>tf.compat.v1.math.nextafter</code></a>
* <a href="/api_docs/python/tf/math/nextafter"><code>tf.compat.v2.math.nextafter</code></a>


``` python
tf.math.nextafter(
    x1,
    x2,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation returns the same result as the C++ std::nextafter function.

It can also return a subnormal number.



#### Args:


* <b>`x1`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`.
* <b>`x2`</b>: A `Tensor`. Must have the same type as `x1`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x1`.


#### Cpp Compatibility
Equivalent to C++ std::nextafter function.
