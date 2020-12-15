description: Computes the matrix square root of one or more square matrices:

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.sqrtm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.sqrtm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the matrix square root of one or more square matrices:

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.matrix_square_root`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.sqrtm`, `tf.compat.v1.matrix_square_root`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.sqrtm(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

matmul(sqrtm(A), sqrtm(A)) = A

The input matrix should be invertible. If the input matrix is real, it should
have no eigenvalues which are real and negative (pairs of complex conjugate
eigenvalues are allowed).

The matrix square root is computed by first reducing the matrix to
quasi-triangular form with the real Schur decomposition. The square root
of the quasi-triangular matrix is then computed directly. Details of
the algorithm can be found in: Nicholas J. Higham, "Computing real
square roots of a real matrix", Linear Algebra Appl., 1987.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the matrix square root for all input submatrices `[..., :, :]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
Shape is `[..., M, M]`.
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

