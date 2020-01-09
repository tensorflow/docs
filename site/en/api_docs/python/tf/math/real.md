page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.real


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/math/real">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L508-L539">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the real part of a complex (or real) tensor.

### Aliases:

* <a href="/api_docs/python/tf/math/real"><code>tf.compat.v1.math.real</code></a>
* <a href="/api_docs/python/tf/math/real"><code>tf.compat.v1.real</code></a>
* <a href="/api_docs/python/tf/math/real"><code>tf.compat.v2.math.real</code></a>
* <a href="/api_docs/python/tf/math/real"><code>tf.real</code></a>


``` python
tf.math.real(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `input`, this operation returns a tensor of type `float` that
is the real part of each element in `input` considered as a complex number.

#### For example:



```python
x = tf.constant([-2.25 + 4.75j, 3.25 + 5.75j])
tf.math.real(x)  # [-2.25, 3.25]
```

If `input` is already real, it is returned unchanged.

#### Args:


* <b>`input`</b>: A `Tensor`. Must have numeric type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32` or `float64`.
