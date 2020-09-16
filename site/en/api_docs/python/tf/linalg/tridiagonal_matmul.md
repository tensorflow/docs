description: Multiplies tridiagonal matrix by matrix.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.tridiagonal_matmul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.tridiagonal_matmul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg/linalg_impl.py#L641-L719">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Multiplies tridiagonal matrix by matrix.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.tridiagonal_matmul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.tridiagonal_matmul(
    diagonals, rhs, diagonals_format='compact', name=None
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`diagonals`
</td>
<td>
A `Tensor` or tuple of `Tensor`s describing left-hand sides. The
shape depends of `diagonals_format`, see description above. Must be
`float32`, `float64`, `complex64`, or `complex128`.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A `Tensor` of shape [..., M, N] and with the same dtype as `diagonals`.
</td>
</tr><tr>
<td>
`diagonals_format`
</td>
<td>
one of `sequence`, or `compact`. Default is `compact`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name to give this `Op` (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of shape [..., M, N] containing the result of multiplication.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
An unsupported type is provided as input, or when the input
tensors have incorrect shapes.
</td>
</tr>
</table>

