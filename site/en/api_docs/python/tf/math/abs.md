page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.abs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/abs">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L245-L278">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the absolute value of a tensor.

### Aliases:

* <a href="/api_docs/python/tf/RaggedTensor#__abs__"><code>tf.RaggedTensor.__abs__</code></a>
* <a href="/api_docs/python/tf/Tensor#__abs__"><code>tf.Tensor.__abs__</code></a>
* <a href="/api_docs/python/tf/math/abs"><code>tf.abs</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__abs__"><code>tf.compat.v1.RaggedTensor.__abs__</code></a>
* <a href="/api_docs/python/tf/Tensor#__abs__"><code>tf.compat.v1.Tensor.__abs__</code></a>
* <a href="/api_docs/python/tf/math/abs"><code>tf.compat.v1.abs</code></a>
* <a href="/api_docs/python/tf/math/abs"><code>tf.compat.v1.math.abs</code></a>
* <a href="/api_docs/python/tf/RaggedTensor#__abs__"><code>tf.compat.v2.RaggedTensor.__abs__</code></a>
* <a href="/api_docs/python/tf/Tensor#__abs__"><code>tf.compat.v2.Tensor.__abs__</code></a>
* <a href="/api_docs/python/tf/math/abs"><code>tf.compat.v2.abs</code></a>
* <a href="/api_docs/python/tf/math/abs"><code>tf.compat.v2.math.abs</code></a>


``` python
tf.math.abs(
    x,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor of integer or floating-point values, this operation returns a
tensor of the same type, where each element contains the absolute value of the
corresponding element in the input.

Given a tensor `x` of complex numbers, this operation returns a tensor of type
`float32` or `float64` that is the absolute value of each element in `x`. All
elements in `x` must be complex numbers of the form \\(a + bj\\). The
absolute value is computed as \\( \sqrt{a^2 + b^2}\\).  For example:

```python
x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])
tf.abs(x)  # [5.25594902, 6.60492229]
```

#### Args:


* <b>`x`</b>: A `Tensor` or `SparseTensor` of type `float16`, `float32`, `float64`,
  `int32`, `int64`, `complex64` or `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` or `SparseTensor` the same size, type, and sparsity as `x` with
  absolute values.
Note, for `complex64` or `complex128` input, the returned `Tensor` will be
  of type `float32` or `float64`, respectively.

If `x` is a `SparseTensor`, returns
`SparseTensor(x.indices, tf.math.abs(x.values, ...), x.dense_shape)`
