page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.polyval


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/polyval">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L4084-L4123">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the elementwise value of a polynomial.

### Aliases:

* <a href="/api_docs/python/tf/math/polyval"><code>tf.compat.v1.math.polyval</code></a>
* <a href="/api_docs/python/tf/math/polyval"><code>tf.compat.v2.math.polyval</code></a>


``` python
tf.math.polyval(
    coeffs,
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

If `x` is a tensor and `coeffs` is a list n + 1 tensors, this function returns
the value of the n-th order polynomial

   p(x) = coeffs[n-1] + coeffs[n-2] * x + ...  + coeffs[0] * x**(n-1)

evaluated using Horner's method, i.e.

   p(x) = coeffs[n-1] + x * (coeffs[n-2] + ... + x * (coeffs[1] +
          x * coeffs[0]))

#### Args:


* <b>`coeffs`</b>: A list of `Tensor` representing the coefficients of the polynomial.
* <b>`x`</b>: A `Tensor` representing the variable of the polynomial.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `tensor` of the shape as the expression p(x) with usual broadcasting rules
for element-wise addition and multiplication applied.




#### Numpy Compatibility
Equivalent to numpy.polyval.
