page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.det


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/det">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_linalg_ops.py`



Computes the determinant of one or more square matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/det"><code>tf.compat.v1.linalg.det</code></a>
* <a href="/api_docs/python/tf/linalg/det"><code>tf.compat.v1.matrix_determinant</code></a>
* <a href="/api_docs/python/tf/linalg/det"><code>tf.compat.v2.linalg.det</code></a>
* <a href="/api_docs/python/tf/linalg/det"><code>tf.matrix_determinant</code></a>


``` python
tf.linalg.det(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor containing the determinants
for all input submatrices `[..., :, :]`.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
  Shape is `[..., M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
