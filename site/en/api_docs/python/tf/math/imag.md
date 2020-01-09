page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.imag


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/imag">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L542-L572">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the imaginary part of a complex (or real) tensor.

### Aliases:

* <a href="/api_docs/python/tf/math/imag"><code>tf.compat.v1.imag</code></a>
* <a href="/api_docs/python/tf/math/imag"><code>tf.compat.v1.math.imag</code></a>
* <a href="/api_docs/python/tf/math/imag"><code>tf.compat.v2.math.imag</code></a>
* <a href="/api_docs/python/tf/math/imag"><code>tf.imag</code></a>


``` python
tf.math.imag(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation returns a tensor of type `float` that
is the imaginary part of each element in `input` considered as a complex
number. If `input` is real, a tensor of all zeros is returned.

#### For example:



```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.math.imag(x)  # [4.75, 5.75]
```

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float`, `double`,
  `complex64`, `complex128`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.
