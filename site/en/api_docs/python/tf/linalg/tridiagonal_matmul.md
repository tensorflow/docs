page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.tridiagonal_matmul


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/linalg/linalg_impl.py#L549-L636">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Multiplies tridiagonal matrix by matrix.

### Aliases:

* `tf.compat.v1.linalg.tridiagonal_matmul`
* `tf.compat.v2.linalg.tridiagonal_matmul`


``` python
tf.linalg.tridiagonal_matmul(
    diagonals,
    rhs,
    diagonals_format='compact',
    name=None
)
```



<!-- Placeholder for "Used in" -->

`diagonals` is representation of 3-diagonal NxN matrix, which depends on
`diagonals_format`.

In `matrix` format, `diagonals` must be a tensor of shape `[..., M, M]`, with
two inner-most dimensions representing the square tridiagonal matrices.
Elements outside of the three diagonals will be ignored.

If `sequence` format, `diagonals` is list or tuple of three tensors:
`[superdiag, maindiag, subdiag]`, each having shape [..., M]. Last element
of `superdiag` first element of `subdiag` are ignored.

In `compact` format the three diagonals are brought together into one tensor
of shape `[..., 3, M]`, with last two dimensions containing superdiagonals,
diagonals, and subdiagonals, in order. Similarly to `sequence` format,
elements `diagonals[..., 0, M-1]` and `diagonals[..., 2, 0]` are ignored.

The `sequence` format is recommended as the one with the best performance.

`rhs` is matrix to the right of multiplication. It has shape `[..., M, N]`.

#### Example:



```python
superdiag = tf.constant([-1, -1, 0], dtype=tf.float64)
maindiag = tf.constant([2, 2, 2], dtype=tf.float64)
subdiag = tf.constant([0, -1, -1], dtype=tf.float64)
diagonals = [superdiag, maindiag, subdiag]
rhs = tf.constant([[1, 1], [1, 1], [1, 1]], dtype=tf.float64)
x = tf.linalg.tridiagonal_matmul(diagonals, rhs, diagonals_format='sequence')
```

#### Args:


* <b>`diagonals`</b>: A `Tensor` or tuple of `Tensor`s describing left-hand sides. The
  shape depends of `diagonals_format`, see description above. Must be
  `float32`, `float64`, `complex64`, or `complex128`.
* <b>`rhs`</b>: A `Tensor` of shape [..., M, N] and with the same dtype as `diagonals`.
* <b>`diagonals_format`</b>: one of `sequence`, or `compact`. Default is `compact`.
* <b>`name`</b>:  A name to give this `Op` (optional).


#### Returns:

A `Tensor` of shape [..., M, N] containing the result of multiplication.



#### Raises:


* <b>`ValueError`</b>: An unsupported type is provided as input, or when the input
tensors have incorrect shapes.
