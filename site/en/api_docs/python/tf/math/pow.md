page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.pow


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/pow">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L434-L459">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the power of one value to another.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__pow__"><code>tf.RaggedTensor.__pow__</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__pow__"><code>tf.compat.v1.RaggedTensor.__pow__</code></a>
* <a href="/api_docs/python/tf/math/pow"><code>tf.compat.v1.math.pow</code></a>
* <a href="/api_docs/python/tf/math/pow"><code>tf.compat.v1.pow</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__pow__"><code>tf.compat.v2.RaggedTensor.__pow__</code></a>
* <a href="/api_docs/python/tf/math/pow"><code>tf.compat.v2.math.pow</code></a>
* <a href="/api_docs/python/tf/math/pow"><code>tf.compat.v2.pow</code></a>
* <a href="/api_docs/python/tf/math/pow"><code>tf.pow</code></a>


``` python
tf.math.pow(
    x,
    y,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `x` and a tensor `y`, this operation computes \\(x^y\\) for
corresponding elements in `x` and `y`. For example:

```python
x = tf.constant([[2, 2], [3, 3]])
y = tf.constant([[8, 16], [2, 3]])
tf.pow(x, y)  # [[256, 65536], [9, 27]]
```

#### Args:


* <b>`x`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`y`</b>: A `Tensor` of type `float16`, `float32`, `float64`, `int32`, `int64`,
  `complex64`, or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`.
