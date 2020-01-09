page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.cholesky


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/cholesky">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_linalg_ops.py`



Computes the Cholesky decomposition of one or more square matrices.

### Aliases:

* <a href="/api_docs/python/tf/linalg/cholesky"><code>tf.cholesky</code></a>
* <a href="/api_docs/python/tf/linalg/cholesky"><code>tf.compat.v1.cholesky</code></a>
* <a href="/api_docs/python/tf/linalg/cholesky"><code>tf.compat.v1.linalg.cholesky</code></a>
* <a href="/api_docs/python/tf/linalg/cholesky"><code>tf.compat.v2.linalg.cholesky</code></a>


``` python
tf.linalg.cholesky(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices.

The input has to be symmetric and positive definite. Only the lower-triangular
part of the input will be used for this operation. The upper-triangular part
will not be read.

The output is a tensor of the same shape as the input
containing the Cholesky decompositions for all input submatrices `[..., :, :]`.

**Note**: The gradient computation on GPU is faster for large matrices but
not for large batch dimensions when the submatrices are small. In this
case it might be faster to use the CPU.

#### Args:


* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
  Shape is `[..., M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
