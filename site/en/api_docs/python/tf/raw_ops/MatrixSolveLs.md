description: Solves one or more linear least-squares problems.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.MatrixSolveLs" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.MatrixSolveLs

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Solves one or more linear least-squares problems.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MatrixSolveLs`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MatrixSolveLs(
    matrix, rhs, l2_regularizer, fast=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

`matrix` is a tensor of shape `[..., M, N]` whose inner-most 2 dimensions
form real or complex matrices of size `[M, N]`. `Rhs` is a tensor of the same
type as `matrix` and shape `[..., M, K]`.
The output is a tensor shape `[..., N, K]` where each output matrix solves
each of the equations
`matrix[..., :, :]` * `output[..., :, :]` = `rhs[..., :, :]`
in the least squares sense.

We use the following notation for (complex) matrix and right-hand sides
in the batch:

`matrix`=\\(A \in \mathbb{C}^{m \times n}\\),
`rhs`=\\(B  \in \mathbb{C}^{m \times k}\\),
`output`=\\(X  \in \mathbb{C}^{n \times k}\\),
`l2_regularizer`=\\(\lambda \in \mathbb{R}\\).

If `fast` is `True`, then the solution is computed by solving the normal
equations using Cholesky decomposition. Specifically, if \\(m \ge n\\) then
\\(X = (A^H A + \lambda I)^{-1} A^H B\\), which solves the least-squares
problem \\(X = \mathrm{argmin}_{Z \in \Re^{n \times k} } ||A Z - B||_F^2 + \lambda ||Z||_F^2\\).
If \\(m \lt n\\) then `output` is computed as
\\(X = A^H (A A^H + \lambda I)^{-1} B\\), which (for \\(\lambda = 0\\)) is the
minimum-norm solution to the under-determined linear system, i.e.
\\(X = \mathrm{argmin}_{Z \in \mathbb{C}^{n \times k} } ||Z||_F^2 \\),
subject to \\(A Z = B\\). Notice that the fast path is only numerically stable
when \\(A\\) is numerically full rank and has a condition number
\\(\mathrm{cond}(A) \lt \frac{1}{\sqrt{\epsilon_{mach} } }\\) or \\(\lambda\\) is
sufficiently large.

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
A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
Shape is `[..., M, N]`.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A `Tensor`. Must have the same type as `matrix`.
Shape is `[..., M, K]`.
</td>
</tr><tr>
<td>
`l2_regularizer`
</td>
<td>
A `Tensor` of type `float64`. Scalar tensor.
</td>
</tr><tr>
<td>
`fast`
</td>
<td>
An optional `bool`. Defaults to `True`.
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
A `Tensor`. Has the same type as `matrix`.
</td>
</tr>

</table>



#### Numpy Compatibility
Equivalent to np.linalg.lstsq

