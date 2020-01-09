page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.dtypes.complex


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/dtypes/complex">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/math_ops.py#L463-L505">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts two real numbers to a complex number.

### Aliases:

* <a href="/api_docs/python/tf/dtypes/complex"><code>tf.compat.v1.complex</code></a>
* <a href="/api_docs/python/tf/dtypes/complex"><code>tf.compat.v1.dtypes.complex</code></a>
* <a href="/api_docs/python/tf/dtypes/complex"><code>tf.compat.v2.complex</code></a>
* <a href="/api_docs/python/tf/dtypes/complex"><code>tf.compat.v2.dtypes.complex</code></a>
* <a href="/api_docs/python/tf/dtypes/complex"><code>tf.complex</code></a>


``` python
tf.dtypes.complex(
    real,
    imag,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a tensor `real` representing the real part of a complex number, and a
tensor `imag` representing the imaginary part of a complex number, this
operation returns complex numbers elementwise of the form \\(a + bj\\), where
*a* represents the `real` part and *b* represents the `imag` part.

The input tensors `real` and `imag` must have the same shape.

#### For example:



```python
real = tf.constant([2.25, 3.25])
imag = tf.constant([4.75, 5.75])
tf.complex(real, imag)  # [[2.25 + 4.75j], [3.25 + 5.75j]]
```

#### Args:


* <b>`real`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
* <b>`imag`</b>: A `Tensor`. Must have the same type as `real`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `complex64` or `complex128`.



#### Raises:


* <b>`TypeError`</b>: Real and imag must be correct types
