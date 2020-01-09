page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.slogdet


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/slogdet">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_linalg_ops.py`



Computes the sign and the log of the absolute value of the determinant of

### Aliases:

* <a href="/api_docs/python/tf/linalg/slogdet"><code>tf.compat.v1.linalg.slogdet</code></a>
* <a href="/api_docs/python/tf/linalg/slogdet"><code>tf.compat.v2.linalg.slogdet</code></a>


``` python
tf.linalg.slogdet(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

one or more square matrices.

The input is a tensor of shape `[N, M, M]` whose inner-most 2 dimensions
form square matrices. The outputs are two tensors containing the signs and
absolute values of the log determinants for all N input submatrices
`[..., :, :]` such that the determinant = sign*exp(log_abs_determinant).
The log_abs_determinant is computed as det(P)*sum(log(diag(LU))) where LU
is the LU decomposition of the input and P is the corresponding
permutation matrix.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
  Shape is `[N, M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (sign, log_abs_determinant).


* <b>`sign`</b>: A `Tensor`. Has the same type as `input`.
* <b>`log_abs_determinant`</b>: A `Tensor`. Has the same type as `input`.
