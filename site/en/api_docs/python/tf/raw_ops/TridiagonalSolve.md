description: Solves tridiagonal systems of equations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TridiagonalSolve" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TridiagonalSolve

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Solves tridiagonal systems of equations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TridiagonalSolve`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TridiagonalSolve(
    diagonals, rhs, partial_pivoting=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

  Solves tridiagonal systems of equations.
  Supports batch dimensions and multiple right-hand sides per each left-hand
  side.
  On CPU, solution is computed via Gaussian elimination with or without partial
  pivoting, depending on `partial_pivoting` attribute. On GPU, Nvidia's cuSPARSE
  library is used: https://docs.nvidia.com/cuda/cusparse/index.html#gtsv

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`diagonals`
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
Tensor of shape `[..., 3, M]` whose innermost 2 dimensions represent the
tridiagonal matrices with three rows being the superdiagonal, diagonals, and
subdiagonals, in order. The last element of the superdiagonal and the first
element of the subdiagonal is ignored.
</td>
</tr><tr>
<td>
`rhs`
</td>
<td>
A `Tensor`. Must have the same type as `diagonals`.
Tensor of shape `[..., M, K]`, representing K right-hand sides per each
left-hand side.
</td>
</tr><tr>
<td>
`partial_pivoting`
</td>
<td>
An optional `bool`. Defaults to `True`.
Whether to apply partial pivoting. Partial pivoting makes the procedure more
stable, but slower.
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
A `Tensor`. Has the same type as `diagonals`.
</td>
</tr>

</table>

