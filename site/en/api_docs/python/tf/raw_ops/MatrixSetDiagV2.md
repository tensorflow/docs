description: Returns a batched matrix tensor with new batched diagonal values.

robots: noindex

# tf.raw_ops.MatrixSetDiagV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns a batched matrix tensor with new batched diagonal values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MatrixSetDiagV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MatrixSetDiagV2(
    input, diagonal, k, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given `input` and `diagonal`, this operation returns a tensor with the
same shape and values as `input`, except for the specified diagonals of the
innermost matrices. These will be overwritten by the values in `diagonal`.

`input` has `r+1` dimensions `[I, J, ..., L, M, N]`. When `k` is scalar or
`k[0] == k[1]`, `diagonal` has `r` dimensions `[I, J, ..., L, max_diag_len]`.
Otherwise, it has `r+1` dimensions `[I, J, ..., L, num_diags, max_diag_len]`.
`num_diags` is the number of diagonals, `num_diags = k[1] - k[0] + 1`.
`max_diag_len` is the longest diagonal in the range `[k[0], k[1]]`,
`max_diag_len = min(M + min(k[1], 0), N + min(-k[0], 0))`

The output is a tensor of rank `k+1` with dimensions `[I, J, ..., L, M, N]`.
If `k` is scalar or `k[0] == k[1]`:

```
output[i, j, ..., l, m, n]
  = diagonal[i, j, ..., l, n-max(k[1], 0)] ; if n - m == k[1]
    input[i, j, ..., l, m, n]              ; otherwise
```

Otherwise,

```
output[i, j, ..., l, m, n]
  = diagonal[i, j, ..., l, diag_index, index_in_diag] ; if k[0] <= d <= k[1]
    input[i, j, ..., l, m, n]                         ; otherwise
```
where `d = n - m`, `diag_index = k[1] - d`, and `index_in_diag = n - max(d, 0)`.

#### For example:



```
# The main diagonal.
input = np.array([[[7, 7, 7, 7],              # Input shape: (2, 3, 4)
                   [7, 7, 7, 7],
                   [7, 7, 7, 7]],
                  [[7, 7, 7, 7],
                   [7, 7, 7, 7],
                   [7, 7, 7, 7]]])
diagonal = np.array([[1, 2, 3],               # Diagonal shape: (2, 3)
                     [4, 5, 6]])
tf.matrix_set_diag(diagonal) ==> [[[1, 7, 7, 7],  # Output shape: (2, 3, 4)
                                   [7, 2, 7, 7],
                                   [7, 7, 3, 7]],
                                  [[4, 7, 7, 7],
                                   [7, 5, 7, 7],
                                   [7, 7, 6, 7]]]

# A superdiagonal (per batch).
tf.matrix_set_diag(diagonal, k = 1)
  ==> [[[7, 1, 7, 7],  # Output shape: (2, 3, 4)
        [7, 7, 2, 7],
        [7, 7, 7, 3]],
       [[7, 4, 7, 7],
        [7, 7, 5, 7],
        [7, 7, 7, 6]]]

# A band of diagonals.
diagonals = np.array([[[1, 2, 3],  # Diagonal shape: (2, 2, 3)
                       [4, 5, 0]],
                      [[6, 1, 2],
                       [3, 4, 0]]])
tf.matrix_set_diag(diagonals, k = (-1, 0))
  ==> [[[1, 7, 7, 7],  # Output shape: (2, 3, 4)
        [4, 2, 7, 7],
        [0, 5, 3, 7]],
       [[6, 7, 7, 7],
        [3, 1, 7, 7],
        [7, 4, 2, 7]]]

```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Rank `r+1`, where `r >= 1`.
</td>
</tr><tr>
<td>
`diagonal`
</td>
<td>
A `Tensor`. Must have the same type as `input`.
Rank `r` when `k` is an integer or `k[0] == k[1]`. Otherwise, it has rank `r+1`.
`k >= 1`.
</td>
</tr><tr>
<td>
`k`
</td>
<td>
A `Tensor` of type `int32`.
Diagonal offset(s). Positive value means superdiagonal, 0 refers to the main
diagonal, and negative value means subdiagonals. `k` can be a single integer
(for a single diagonal) or a pair of integers specifying the low and high ends
of a matrix band. `k[0]` must not be larger than `k[1]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

