page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.exp


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/exp">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_math_ops.py`



Computes exponential of x element-wise.  \\(y = e^x\\).

### Aliases:

* <a href="/api_docs/python/tf/math/exp"><code>tf.compat.v1.exp</code></a>
* <a href="/api_docs/python/tf/math/exp"><code>tf.compat.v1.math.exp</code></a>
* <a href="/api_docs/python/tf/math/exp"><code>tf.compat.v2.exp</code></a>
* <a href="/api_docs/python/tf/math/exp"><code>tf.compat.v2.math.exp</code></a>
* <a href="/api_docs/python/tf/math/exp"><code>tf.exp</code></a>


``` python
tf.math.exp(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

  This function computes the exponential of every element in the input tensor.
  i.e. `exp(x)` or `e^(x)`, where `x` is the input tensor.
  `e` denotes Euler's number and is approximately equal to 2.718281.
  Output is positive for any real input.

>     x = tf.constant(2.0)
>     tf.math.exp(x) ==> 7.389056
>     
>     x = tf.constant([2.0, 8.0])
>     tf.math.exp(x) ==> array([7.389056, 2980.958], dtype=float32)

  For complex numbers, the exponential value is calculated as follows:

>     e^(x+iy) = e^x * e^iy = e^x * (cos y + i sin y)

  Let's consider complex number 1+1j as an example.
  e^1 * (cos 1 + i sin 1) = 2.7182818284590 * (0.54030230586+0.8414709848j)

>     x = tf.constant(1 + 1j)
>     tf.math.exp(x) ==> 1.4686939399158851+2.2873552871788423j

#### Args:


* <b>`x`</b>: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `x`.
