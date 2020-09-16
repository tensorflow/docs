description: Solves systems of linear eqns A X = RHS, given Cholesky factorizations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.cholesky_solve" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.cholesky_solve

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg_ops.py#L146-L189">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.cholesky_solve`, `tf.compat.v1.linalg.cholesky_solve`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.cholesky_solve(
    chol, rhs, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

```python
# Solve 10 separate 2x2 linear systems:
A = ... # shape 10 x 2 x 2
RHS = ... # shape 10 x 2 x 1
chol = tf.linalg.cholesky(A)  # shape 10 x 2 x 2
X = tf.linalg.cholesky_solve(chol, RHS)  # shape 10 x 2 x 1
# tf.matmul(A, X) ~ RHS
X[3, :, 0]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 0]

# Solve five linear systems (K = 5) for every member of the length 10 batch.
A = ... # shape 10 x 2 x 2
RHS = ... # shape 10 x 2 x 5
...
X[3, :, 2]  # Solution to the linear system A[3, :, :] x = RHS[3, :, 2]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`chol`
</td>
<td>
A `Tensor`.  Must be `float32` or `float64`, shape is `[..., M, M]`.
Cholesky factorization of `A`, e.g. `chol = tf.linalg.cholesky(A)`.
For that reason, only the lower triangular parts (including the diagonal)
of the last two dimensions of `chol` are used.  The strictly upper part is
assumed to be zero and not accessed.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A `Tensor`, same type as `chol`, shape is `[..., M, K]`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name to give this `Op`.  Defaults to `cholesky_solve`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Solution to `A x = rhs`, shape `[..., M, K]`.
</td>
</tr>

</table>

