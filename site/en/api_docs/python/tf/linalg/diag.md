page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.diag


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/linalg/diag">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L1944-L2078">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a batched diagonal tensor with given batched diagonal values.

### Aliases:

* <a href="/api_docs/python/tf/linalg/diag"><code>tf.compat.v1.linalg.diag</code></a>
* <a href="/api_docs/python/tf/linalg/diag"><code>tf.compat.v1.matrix_diag</code></a>
* <a href="/api_docs/python/tf/linalg/diag"><code>tf.compat.v2.linalg.diag</code></a>
* <a href="/api_docs/python/tf/linalg/diag"><code>tf.matrix_diag</code></a>


``` python
tf.linalg.diag(
    diagonal,
    name='diag',
    k=0,
    num_rows=-1,
    num_cols=-1,
    padding_value=0
)
```



<!-- Placeholder for "Used in" -->

Returns a tensor with the contents in `diagonal` as `k[0]`-th to `k[1]`-th
diagonals of a matrix, with everything else padded with `padding`. `num_rows`
and `num_cols` specify the dimension of the innermost matrix of the output. If
both are not specified, the op assumes the innermost matrix is square and
infers its size from `k` and the innermost dimension of `diagonal`. If only
one of them is specified, the op assumes the unspecified value is the smallest
possible based on other criteria.

Let `diagonal` have `r` dimensions `[I, J, ..., L, M, N]`. The output tensor
has rank `r+1` with shape `[I, J, ..., L, M, num_rows, num_cols]` when only
one diagonal is given (`k` is an integer or `k[0] == k[1]`). Otherwise, it has
rank `r` with shape `[I, J, ..., L, num_rows, num_cols]`.

The second innermost dimension of `diagonal` has double meaning. When `k` is
scalar or `k[0] == k[1]`, `M` is part of the batch size [I, J, ..., M], and
the output tensor is:

```
output[i, j, ..., l, m, n]
  = diagonal[i, j, ..., l, n-max(d_upper, 0)] ; if n - m == d_upper
    output[i, j, ..., l, m, n]                ; otherwise
```

Otherwise, `M` is treated as the number of diagonals for the matrix in the
same batch (`M = k[1]-k[0]+1`), and the output tensor is:

```
output[i, j, ..., l, m, n]
  = diagonal[i, j, ..., l, k[1]-d, n-max(d, 0)] ; if d_lower <= d <= d_upper
    input[i, j, ..., l, m, n]                   ; otherwise
```
where `d = n - m`

#### For example:



```
# The main diagonal.
diagonal = np.array([[1, 2, 3, 4],            # Input shape: (2, 4)
                     [5, 6, 7, 8]])
tf.matrix_diag(diagonal) ==> [[[1, 0, 0, 0],  # Output shape: (2, 4, 4)
                               [0, 2, 0, 0],
                               [0, 0, 3, 0],
                               [0, 0, 0, 4]],
                              [[5, 0, 0, 0],
                               [0, 6, 0, 0],
                               [0, 0, 7, 0],
                               [0, 0, 0, 8]]]

# A superdiagonal (per batch).
diagonal = np.array([[1, 2, 3],  # Input shape: (2, 3)
                     [4, 5, 6]])
tf.matrix_diag(diagonal, k = 1)
  ==> [[[0, 1, 0, 0],  # Output shape: (2, 4, 4)
        [0, 0, 2, 0],
        [0, 0, 0, 3],
        [0, 0, 0, 0]],
       [[0, 4, 0, 0],
        [0, 0, 5, 0],
        [0, 0, 0, 6],
        [0, 0, 0, 0]]]

# A band of diagonals.
diagonals = np.array([[[1, 2, 3],  # Input shape: (2, 2, 3)
                       [4, 5, 0]],
                      [[6, 7, 9],
                       [9, 1, 0]]])
tf.matrix_diag(diagonals, k = (-1, 0))
  ==> [[[1, 0, 0],  # Output shape: (2, 3, 3)
        [4, 2, 0],
        [0, 5, 3]],
       [[6, 0, 0],
        [9, 7, 0],
        [0, 1, 9]]]

# Rectangular matrix.
diagonal = np.array([1, 2])  # Input shape: (2)
tf.matrix_diag(diagonal, k = -1, num_rows = 3, num_cols = 4)
  ==> [[0, 0, 0, 0],  # Output shape: (3, 4)
       [1, 0, 0, 0],
       [0, 2, 0, 0]]

# Rectangular matrix with inferred num_cols and padding = 9.
tf.matrix_diag(diagonal, k = -1, num_rows = 3, padding = 9)
  ==> [[9, 9],  # Output shape: (3, 2)
       [1, 9],
       [9, 2]]
```

#### Args:


* <b>`diagonal`</b>: A `Tensor` with `rank k >= 1`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`k`</b>: Diagonal offset(s). Positive value means superdiagonal, 0 refers to the
  main diagonal, and negative value means subdiagonals. `k` can be a single
  integer (for a single diagonal) or a pair of integers specifying the low
  and high ends of a matrix band. `k[0]` must not be larger than `k[1]`.
* <b>`num_rows`</b>: The number of rows of the output matrix. If it is not provided,
  the op assumes the output matrix is a square matrix and infers the matrix
  size from `d_lower`, `d_upper`, and the innermost dimension of `diagonal`.
* <b>`num_cols`</b>: The number of columns of the output matrix. If it is not provided,
  the op assumes the output matrix is a square matrix and infers the matrix
  size from `d_lower`, `d_upper`, and the innermost dimension of `diagonal`.
* <b>`padding_value`</b>: The value to fill the area outside the specified diagonal
  band with. Default is 0.


#### Returns:

A Tensor. Has the same type as `diagonal`.
