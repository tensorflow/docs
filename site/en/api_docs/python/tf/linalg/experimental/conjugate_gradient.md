description: Conjugate gradient solver.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.experimental.conjugate_gradient" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.experimental.conjugate_gradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/linalg/sparse/conjugate_gradient.py#L34-L143">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Conjugate gradient solver.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.experimental.conjugate_gradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.experimental.conjugate_gradient(
    operator, rhs, preconditioner=None, x=None, tol=1e-05, max_iter=20,
    name='conjugate_gradient'
)
</code></pre>



<!-- Placeholder for "Used in" -->

Solves a linear system of equations `A*x = rhs` for self-adjoint, positive
definite matrix `A` and right-hand side vector `rhs`, using an iterative,
matrix-free algorithm where the action of the matrix A is represented by
`operator`. The iteration terminates when either the number of iterations
exceeds `max_iter` or when the residual norm has been reduced to `tol`
times its initial value, i.e. \\(||rhs - A x_k|| <= tol ||rhs||\\).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`operator`
</td>
<td>
A `LinearOperator` that is self-adjoint and positive definite.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A possibly batched vector of shape `[..., N]` containing the right-hand
size vector.
</td>
</tr><tr>
<td>
`preconditioner`
</td>
<td>
A `LinearOperator` that approximates the inverse of `A`.
An efficient preconditioner could dramatically improve the rate of
convergence. If `preconditioner` represents matrix `M`(`M` approximates
`A^{-1}`), the algorithm uses `preconditioner.apply(x)` to estimate
`A^{-1}x`. For this to be useful, the cost of applying `M` should be
much lower than computing `A^{-1}` directly.
</td>
</tr><tr>
<td>
`x`
</td>
<td>
A possibly batched vector of shape `[..., N]` containing the initial
guess for the solution.
</td>
</tr><tr>
<td>
`tol`
</td>
<td>
A float scalar convergence tolerance.
</td>
</tr><tr>
<td>
`max_iter`
</td>
<td>
An integer giving the maximum number of iterations.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name scope for the operation.
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
A namedtuple representing the final state with fields:
- i: A scalar `int32` `Tensor`. Number of iterations executed.
- x: A rank-1 `Tensor` of shape `[..., N]` containing the computed
solution.
- r: A rank-1 `Tensor` of shape `[.., M]` containing the residual vector.
- p: A rank-1 `Tensor` of shape `[..., N]`. `A`-conjugate basis vector.
- gamma: \\(r \dot M \dot r\\), equivalent to  \\(||r||_2^2\\) when
`preconditioner=None`.
</td>
</tr>
</table>

