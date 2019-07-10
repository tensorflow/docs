page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.solve

Solves systems of linear equations.

### Aliases:

* `tf.compat.v1.linalg.solve`
* `tf.compat.v1.matrix_solve`
* `tf.compat.v2.linalg.solve`
* `tf.linalg.solve`
* `tf.matrix_solve`

``` python
tf.linalg.solve(
    matrix,
    rhs,
    adjoint=False,
    name=None
)
```



Defined in generated file: `python/ops/gen_linalg_ops.py`.

<!-- Placeholder for "Used in" -->

`Matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. `Rhs` is a tensor of shape `[..., M, K]`. The `output` is
a tensor shape `[..., M, K]`.  If `adjoint` is `False` then each output matrix
satisfies `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`.
If `adjoint` is `True` then each output matrix satisfies
`adjoint(matrix[..., :, :]) * output[..., :, :] = rhs[..., :, :]`.

#### Args:


* <b>`matrix`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
  Shape is `[..., M, M]`.
* <b>`rhs`</b>: A `Tensor`. Must have the same type as `matrix`.
  Shape is `[..., M, K]`.
* <b>`adjoint`</b>: An optional `bool`. Defaults to `False`.
  Boolean indicating whether to solve with `matrix` or its (block-wise)
  adjoint.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `matrix`.
