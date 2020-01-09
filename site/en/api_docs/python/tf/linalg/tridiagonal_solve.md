page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.tridiagonal_solve


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/linalg/linalg_impl.py#L342-L502">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Solves tridiagonal systems of equations.

### Aliases:

* `tf.compat.v1.linalg.tridiagonal_solve`
* `tf.compat.v2.linalg.tridiagonal_solve`


``` python
tf.linalg.tridiagonal_solve(
    diagonals,
    rhs,
    diagonals_format='compact',
    transpose_rhs=False,
    conjugate_rhs=False,
    name=None,
    partial_pivoting=True
)
```



<!-- Placeholder for "Used in" -->

The input can be supplied in various formats: `matrix`, `sequence` and
`compact`, specified by the `diagonals_format` arg.

In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with
two inner-most dimensions representing the square tridiagonal matrices.
Elements outside of the three diagonals will be ignored.

In `sequence` format, `diagonals` are supplied as a tuple or list of three
tensors of shapes `[..., N]`, `[..., M]`, `[..., N]` representing
superdiagonals, diagonals, and subdiagonals, respectively. `N` can be either
`M-1` or `M`; in the latter case, the last element of superdiagonal and the
first element of subdiagonal will be ignored.

In `compact` format the three diagonals are brought together into one tensor
of shape `[..., 3, M]`, with last two dimensions containing superdiagonals,
diagonals, and subdiagonals, in order. Similarly to `sequence` format,
elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

The `compact` format is recommended as the one with best performance. In case
you need to cast a tensor into a compact format manually, use <a href="../../tf/gather_nd"><code>tf.gather_nd</code></a>.
An example for a tensor of shape [m, m]:

```python
rhs = tf.constant([...])
matrix = tf.constant([[...]])
m = matrix.shape[0]
dummy_idx = [0, 0]  # An arbitrary element to use as a dummy
indices = [[[i, i + 1] for i in range(m - 1)] + [dummy_idx],  # Superdiagonal
         [[i, i] for i in range(m)],                          # Diagonal
         [dummy_idx] + [[i + 1, i] for i in range(m - 1)]]    # Subdiagonal
diagonals=tf.gather_nd(matrix, indices)
x = tf.linalg.tridiagonal_solve(diagonals, rhs)
```

Regardless of the `diagonals_format`, `rhs` is a tensor of shape `[..., M]` or
`[..., M, K]`. The latter allows to simultaneously solve K systems with the
same left-hand sides and K different right-hand sides. If `transpose_rhs`
is set to `True` the expected shape is `[..., M]` or `[..., K, M]`.

The batch dimensions, denoted as `...`, must be the same in `diagonals` and
`rhs`.

The output is a tensor of the same shape as `rhs`: either `[..., M]` or
`[..., M, K]`.

The op isn't guaranteed to raise an error if the input matrix is not
invertible. <a href="../../tf/debugging/check_numerics"><code>tf.debugging.check_numerics</code></a> can be applied to the output to
detect invertibility problems.

**Note**: with large batch sizes, the computation on the GPU may be slow, if
either `partial_pivoting=True` or there are multiple right-hand sides
(`K > 1`). If this issue arises, consider if it's possible to disable pivoting
and have `K = 1`, or, alternatively, consider using CPU.

On CPU, solution is computed via Gaussian elimination with or without partial
pivoting, depending on `partial_pivoting` parameter. On GPU, Nvidia's cuSPARSE
library is used: https://docs.nvidia.com/cuda/cusparse/index.html#gtsv

#### Args:


* <b>`diagonals`</b>: A `Tensor` or tuple of `Tensor`s describing left-hand sides. The
  shape depends of `diagonals_format`, see description above. Must be
  `float32`, `float64`, `complex64`, or `complex128`.
* <b>`rhs`</b>: A `Tensor` of shape [..., M] or [..., M, K] and with the same dtype as
  `diagonals`.
* <b>`diagonals_format`</b>: one of `matrix`, `sequence`, or `compact`. Default is
  `compact`.
* <b>`transpose_rhs`</b>: If `True`, `rhs` is transposed before solving (has no effect
  if the shape of rhs is [..., M]).
* <b>`conjugate_rhs`</b>: If `True`, `rhs` is conjugated before solving.
* <b>`name`</b>:  A name to give this `Op` (optional).
* <b>`partial_pivoting`</b>: whether to perform partial pivoting. `True` by default.
  Partial pivoting makes the procedure more stable, but slower. Partial
  pivoting is unnecessary in some cases, including diagonally dominant and
  symmetric positive definite matrices (see e.g. theorem 9.12 in [1]).


#### Returns:

A `Tensor` of shape [..., M] or [..., M, K] containing the solutions.



#### Raises:


* <b>`ValueError`</b>: An unsupported type is provided as input, or when the input
tensors have incorrect shapes.

[1] Nicholas J. Higham (2002). Accuracy and Stability of Numerical Algorithms:
Second Edition. SIAM. p. 175. ISBN 978-0-89871-802-7.
