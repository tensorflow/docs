description: Solves one or more linear least-squares problems.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.lstsq" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.lstsq

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg_ops.py#L244-L379">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Solves one or more linear least-squares problems.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.lstsq`, `tf.compat.v1.matrix_solve_ls`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.lstsq(
    matrix, rhs, l2_regularizer=0.0, fast=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`matrix` is a tensor of shape `[..., M, N]` whose inner-most 2 dimensions
form `M`-by-`N` matrices. Rhs is a tensor of shape `[..., M, K]` whose
inner-most 2 dimensions form `M`-by-`K` matrices.  The computed output is a
`Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form `M`-by-`K`
matrices that solve the equations
`matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least squares
sense.

Below we will use the following notation for each pair of matrix and
right-hand sides in the batch:

`matrix`=\\(A \in \Re^{m \times n}\\),
`rhs`=\\(B  \in \Re^{m \times k}\\),
`output`=\\(X  \in \Re^{n \times k}\\),
`l2_regularizer`=\\(\lambda\\).

If `fast` is `True`, then the solution is computed by solving the normal
equations using Cholesky decomposition. Specifically, if \\(m \ge n\\) then
\\(X = (A^T A + \lambda I)^{-1} A^T B\\), which solves the least-squares
problem \\(X = \mathrm{argmin}_{Z \in \Re^{n \times k}} ||A Z - B||_F^2 +
\lambda ||Z||_F^2\\). If \\(m \lt n\\) then `output` is computed as
\\(X = A^T (A A^T + \lambda I)^{-1} B\\), which (for \\(\lambda = 0\\)) is
the minimum-norm solution to the under-determined linear system, i.e.
\\(X = \mathrm{argmin}_{Z \in \Re^{n \times k}} ||Z||_F^2 \\), subject to
\\(A Z = B\\). Notice that the fast path is only numerically stable when
\\(A\\) is numerically full rank and has a condition number
\\(\mathrm{cond}(A) \lt \frac{1}{\sqrt{\epsilon_{mach}}}\\) or\\(\lambda\\)
is sufficiently large.

If `fast` is `False` an algorithm based on the numerically robust complete
orthogonal decomposition is used. This computes the minimum-norm
least-squares solution, even when \\(A\\) is rank deficient. This path is
typically 6-7 times slower than the fast path. If `fast` is `False` then
`l2_regularizer` is ignored.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`matrix`
</td>
<td>
`Tensor` of shape `[..., M, N]`.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
`Tensor` of shape `[..., M, K]`.
</td>
</tr><tr>
<td>
`l2_regularizer`
</td>
<td>
0-D `double` `Tensor`. Ignored if `fast=False`.
</td>
</tr><tr>
<td>
`fast`
</td>
<td>
bool. Defaults to `True`.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
string, optional name of the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`output`
</td>
<td>
`Tensor` of shape `[..., N, K]` whose inner-most 2 dimensions form
`M`-by-`K` matrices that solve the equations
`matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]` in the least
squares sense.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`NotImplementedError`
</td>
<td>
linalg.lstsq is currently disabled for complex128
and l2_regularizer != 0 due to poor accuracy.
</td>
</tr>
</table>

