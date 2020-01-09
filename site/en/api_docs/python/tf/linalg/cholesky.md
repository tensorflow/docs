page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.cholesky

### Aliases:

* `tf.cholesky`
* `tf.linalg.cholesky`

``` python
tf.linalg.cholesky(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_linalg_ops.py`.

See the guide: [Upgrade to TensorFlow 1.0 > Upgrading your code manually](../../../../api_guides/python/upgrade#Upgrading_your_code_manually)

Computes the Cholesky decomposition of one or more square matrices.

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

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
    Shape is `[..., M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.