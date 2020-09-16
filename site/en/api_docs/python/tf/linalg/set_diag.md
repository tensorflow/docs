description: Returns a batched matrix tensor with new batched diagonal values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.set_diag" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.set_diag

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/array_ops.py#L2590-L2724">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a batched matrix tensor with new batched diagonal values.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.set_diag`, `tf.compat.v1.matrix_set_diag`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.set_diag(
    input, diagonal, name='set_diag', k=0, align='RIGHT_LEFT'
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
where `d = n - m`, `diag_index = k[1] - d`, and
`index_in_diag = n - max(d, 0) + offset`.

`offset` is zero except when the alignment of the diagonal is to the right.
```
offset = max_diag_len - diag_len(d) ; if (`align` in {RIGHT_LEFT, RIGHT_RIGHT}
                                           and `d >= 0`) or
                                         (`align` in {LEFT_RIGHT, RIGHT_RIGHT}
                                           and `d <= 0`)
         0                          ; otherwise
```
where `diag_len(d) = min(cols - max(d, 0), rows + min(d, 0))`.

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
tf.matrix_set_diag(input, diagonal)
  ==> [[[1, 7, 7, 7],  # Output shape: (2, 3, 4)
        [7, 2, 7, 7],
        [7, 7, 3, 7]],
       [[4, 7, 7, 7],
        [7, 5, 7, 7],
        [7, 7, 6, 7]]]

# A superdiagonal (per batch).
tf.matrix_set_diag(input, diagonal, k = 1)
  ==> [[[7, 1, 7, 7],  # Output shape: (2, 3, 4)
        [7, 7, 2, 7],
        [7, 7, 7, 3]],
       [[7, 4, 7, 7],
        [7, 7, 5, 7],
        [7, 7, 7, 6]]]

# A band of diagonals.
diagonals = np.array([[[9, 1, 0],  # Diagonal shape: (2, 4, 3)
                       [6, 5, 8],
                       [1, 2, 3],
                       [0, 4, 5]],
                      [[1, 2, 0],
                       [5, 6, 4],
                       [6, 1, 2],
                       [0, 3, 4]]])
tf.matrix_set_diag(input, diagonals, k = (-1, 2))
  ==> [[[1, 6, 9, 7],  # Output shape: (2, 3, 4)
        [4, 2, 5, 1],
        [7, 5, 3, 8]],
       [[6, 5, 1, 7],
        [3, 1, 6, 2],
        [7, 4, 2, 4]]]

# RIGHT_LEFT alignment.
diagonals = np.array([[[0, 9, 1],  # Diagonal shape: (2, 4, 3)
                       [6, 5, 8],
                       [1, 2, 3],
                       [4, 5, 0]],
                      [[0, 1, 2],
                       [5, 6, 4],
                       [6, 1, 2],
                       [3, 4, 0]]])
tf.matrix_set_diag(input, diagonals, k = (-1, 2), align="RIGHT_LEFT")
  ==> [[[1, 6, 9, 7],  # Output shape: (2, 3, 4)
        [4, 2, 5, 1],
        [7, 5, 3, 8]],
       [[6, 5, 1, 7],
        [3, 1, 6, 2],
        [7, 4, 2, 4]]]

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
A `Tensor` with rank `k + 1`, where `k >= 1`.
</td>
</tr><tr>
<td>
`diagonal`
</td>
<td>
A `Tensor` with rank `k`, when `d_lower == d_upper`, or `k + 1`,
otherwise. `k >= 1`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`k`
</td>
<td>
Diagonal offset(s). Positive value means superdiagonal, 0 refers to the
main diagonal, and negative value means subdiagonals. `k` can be a single
integer (for a single diagonal) or a pair of integers specifying the low
and high ends of a matrix band. `k[0]` must not be larger than `k[1]`.
</td>
</tr><tr>
<td>
`align`
</td>
<td>
Some diagonals are shorter than `max_diag_len` and need to be padded.
`align` is a string specifying how superdiagonals and subdiagonals should
be aligned, respectively. There are four possible alignments: "RIGHT_LEFT"
(default), "LEFT_RIGHT", "LEFT_LEFT", and "RIGHT_RIGHT". "RIGHT_LEFT"
aligns superdiagonals to the right (left-pads the row) and subdiagonals to
the left (right-pads the row). It is the packing format LAPACK uses.
cuSPARSE uses "LEFT_RIGHT", which is the opposite alignment.
</td>
</tr>
</table>

