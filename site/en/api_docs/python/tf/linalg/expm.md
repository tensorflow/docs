page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.expm

``` python
tf.linalg.expm(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_linalg_ops.py`.

Computes the matrix exponential of one or more square matrices:

exp(A) = \sum_{n=0}^\infty A^n/n!

The exponential is computed using a combination of the scaling and squaring
method and the Pade approximation. Details can be founds in:
Nicholas J. Higham, "The scaling and squaring method for the matrix exponential
revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the exponential for all input submatrices `[..., :, :]`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
    Shape is `[..., M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.