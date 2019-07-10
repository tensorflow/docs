page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.triangular_solve

Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

### Aliases:

* `tf.compat.v1.linalg.triangular_solve`
* `tf.compat.v1.matrix_triangular_solve`
* `tf.compat.v2.linalg.triangular_solve`
* `tf.linalg.triangular_solve`
* `tf.matrix_triangular_solve`

``` python
tf.linalg.triangular_solve(
    matrix,
    rhs,
    lower=True,
    adjoint=False,
    name=None
)
```



Defined in generated file: `python/ops/gen_linalg_ops.py`.

<!-- Placeholder for "Used in" -->


`matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form
square matrices. If `lower` is `True` then the strictly upper triangular part
of each inner-most matrix is assumed to be zero and not accessed.
If `lower` is False then the strictly lower triangular part of each inner-most
matrix is assumed to be zero and not accessed.
`rhs` is a tensor of shape `[..., M, K]`.

The output is a tensor of shape `[..., M, K]`. If `adjoint` is
`True` then the innermost matrices in `output` satisfy matrix equations
`matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`.
If `adjoint` is `False` then the strictly then the  innermost matrices in
`output` satisfy matrix equations
`adjoint(matrix[..., i, k]) * output[..., k, j] = rhs[..., i, j]`.

#### Example:


```python

a = tf.constant([[3,  0,  0,  0],
                 [2,  1,  0,  0],
                 [1,  0,  1,  0],
                 [1,  1,  1,  1]], dtype=tf.float32)

b = tf.constant([[4],
                 [2],
                 [4],
                 [2]], dtype=tf.float32)

x = tf.linalg.triangular_solve(a, b, lower=True)
x
# <tf.Tensor: id=257, shape=(4, 1), dtype=float32, numpy=
# array([[ 1.3333334 ],
#        [-0.66666675],
#        [ 2.6666665 ],
#        [-1.3333331 ]], dtype=float32)>

# in python3 one can use `a@x`
tf.matmul(a, x)
# <tf.Tensor: id=263, shape=(4, 1), dtype=float32, numpy=
# array([[4.       ],
#        [2.       ],
#        [4.       ],
#        [1.9999999]], dtype=float32)>
```

#### Args:


* <b>`matrix`</b>: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
  Shape is `[..., M, M]`.
* <b>`rhs`</b>: A `Tensor`. Must have the same type as `matrix`.
  Shape is `[..., M, K]`.
* <b>`lower`</b>: An optional `bool`. Defaults to `True`.
  Boolean indicating whether the innermost matrices in `matrix` are
  lower or upper triangular.
* <b>`adjoint`</b>: An optional `bool`. Defaults to `False`.
  Boolean indicating whether to solve with `matrix` or its (block-wise)
           adjoint.


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `matrix`.


#### Numpy Compatibility
Equivalent to scipy.linalg.solve_triangular

