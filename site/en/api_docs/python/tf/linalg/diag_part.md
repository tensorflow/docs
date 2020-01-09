page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.linalg.diag_part


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L2092-L2197">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the batched diagonal part of a batched tensor.

### Aliases:

* `tf.compat.v1.linalg.diag_part`
* `tf.compat.v1.matrix_diag_part`
* `tf.compat.v2.linalg.diag_part`


``` python
tf.linalg.diag_part(
    input,
    name='diag_part',
    k=0,
    padding_value=0
)
```



<!-- Placeholder for "Used in" -->

Returns a tensor with the `k[0]`-th to `k[1]`-th diagonals of the batched
`input`.

Assume `input` has `r` dimensions `[I, J, ..., L, M, N]`.
Let `max_diag_len` be the maximum length among all diagonals to be extracted,
`max_diag_len = min(M + min(k[1], 0), N + min(-k[0], 0))`
Let `num_diags` be the number of diagonals to extract,
`num_diags = k[1] - k[0] + 1`.

If `num_diags == 1`, the output tensor is of rank `r - 1` with shape
`[I, J, ..., L, max_diag_len]` and values:

```
diagonal[i, j, ..., l, n]
  = input[i, j, ..., l, n+y, n+x] ; when 0 <= n-y < M and 0 <= n-x < N,
    0                             ; otherwise.
```
where `y = max(-k[1], 0)`, `x = max(k[1], 0)`.

Otherwise, the output tensor has rank `r` with dimensions
`[I, J, ..., L, num_diags, max_diag_len]` with values:

```
diagonal[i, j, ..., l, m, n]
  = input[i, j, ..., l, n+y, n+x] ; when 0 <= n-y < M and 0 <= n-x < N,
    0                             ; otherwise.
```
where `d = k[1] - m`, `y = max(-d, 0)`, and `x = max(d, 0)`.

The input must be at least a matrix.

#### For example:



```
input = np.array([[[1, 2, 3, 4],  # Input shape: (2, 3, 4)
                   [5, 6, 7, 8],
                   [9, 8, 7, 6]],
                  [[5, 4, 3, 2],
                   [1, 2, 3, 4],
                   [5, 6, 7, 8]]])

# A main diagonal from each batch.
tf.matrix_diag_part(input) ==> [[1, 6, 7],  # Output shape: (2, 3)
                                [5, 2, 7]]

# A superdiagonal from each batch.
tf.matrix_diag_part(input, k = 1)
  ==> [[2, 7, 6],  # Output shape: (2, 3)
       [4, 3, 8]]

# A tridiagonal band from each batch.
tf.matrix_diag_part(input, k = (-1, 1))
  ==> [[[2, 7, 6],  # Output shape: (2, 3, 3)
        [1, 6, 7],
        [5, 8, 0]],
       [[4, 3, 8],
        [5, 2, 7],
        [1, 6, 0]]]

# Padding = 9
tf.matrix_diag_part(input, k = (1, 3), padding = 9)
  ==> [[[4, 9, 9],  # Output shape: (2, 3, 3)
        [3, 8, 9],
        [2, 7, 6]],
       [[2, 9, 9],
        [3, 4, 9],
        [4, 3, 8]]]
```

#### Args:


* <b>`input`</b>: A `Tensor` with `rank k >= 2`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`k`</b>: Diagonal offset(s). Positive value means superdiagonal, 0 refers to the
  main diagonal, and negative value means subdiagonals. `k` can be a single
  integer (for a single diagonal) or a pair of integers specifying the low
  and high ends of a matrix band. `k[0]` must not be larger than `k[1]`.
* <b>`padding_value`</b>: The value to fill the area outside the specified diagonal
  band with. Default is 0.


#### Returns:

A Tensor containing diagonals of `input`. Has the same type as `input`.
