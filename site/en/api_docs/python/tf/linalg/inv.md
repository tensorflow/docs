page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.inv


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/inv">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_linalg_ops.py`



Computes the inverse of one or more square invertible matrices or their

### Aliases:

* <a href="/api_docs/python/tf/linalg/inv"><code>tf.compat.v1.linalg.inv</code></a>
* <a href="/api_docs/python/tf/linalg/inv"><code>tf.compat.v1.matrix_inverse</code></a>
* <a href="/api_docs/python/tf/linalg/inv"><code>tf.compat.v2.linalg.inv</code></a>
* <a href="/api_docs/python/tf/linalg/inv"><code>tf.matrix_inverse</code></a>


``` python
tf.linalg.inv(
    input,
    adjoint=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

adjoints (conjugate transposes).

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the inverse for all input submatrices `[..., :, :]`.

The op uses LU decomposition with partial pivoting to compute the inverses.

If a matrix is not invertible there is no guarantee what the op does. It
may detect the condition and raise an exception or it may simply return a
garbage result.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
  Shape is `[..., M, M]`.
* <b>`adjoint`</b>: An optional `bool`. Defaults to `False`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
