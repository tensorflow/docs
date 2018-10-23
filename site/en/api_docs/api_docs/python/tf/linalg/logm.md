

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.logm

``` python
tf.linalg.logm(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_linalg_ops.py`.

Computes the matrix logarithm of one or more square matrices:


\\(log(exp(A)) = A\\)

This op is only defined for complex matrices. If A is positive-definite and
real, then casting to a complex matrix, taking the logarithm and casting back
to a real matrix will give the correct result.

This function computes the matrix logarithm using the Schur-Parlett algorithm.
Details of the algorithm can be found in Section 11.6.2 of:
Nicholas J. Higham, Functions of Matrices: Theory and Computation, SIAM 2008.
ISBN 978-0-898716-46-7.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the exponential for all input submatrices `[..., :, :]`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
    Shape is `[..., M, M]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.