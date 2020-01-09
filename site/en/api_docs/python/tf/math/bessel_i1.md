page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.bessel_i1


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/bessel_i1">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/special_math_ops.py#L113-L134">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the Bessel i1 function of `x` element-wise.

### Aliases:

* <a href="/api_docs/python/tf/math/bessel_i1"><code>tf.compat.v1.math.bessel_i1</code></a>
* <a href="/api_docs/python/tf/math/bessel_i1"><code>tf.compat.v2.math.bessel_i1</code></a>


``` python
tf.math.bessel_i1(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Modified Bessel function of order 1.

It is preferable to use the numerically stabler function `i1e(x)` instead.

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor`. Must be one of the following types: `half`,
  `float32`, `float64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.




#### Scipy Compatibility
Equivalent to scipy.special.i1
