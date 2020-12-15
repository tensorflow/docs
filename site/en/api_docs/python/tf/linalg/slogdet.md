description: Computes the sign and the log of the absolute value of the determinant of

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.slogdet" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.slogdet

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the sign and the log of the absolute value of the determinant of

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.slogdet`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.slogdet(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

one or more square matrices.

The input is a tensor of shape `[N, M, M]` whose inner-most 2 dimensions
form square matrices. The outputs are two tensors containing the signs and
absolute values of the log determinants for all N input submatrices
`[..., :, :]` such that `determinant = sign*exp(log_abs_determinant)`.
The `log_abs_determinant` is computed as `det(P)*sum(log(diag(LU)))` where `LU`
is the `LU` decomposition of the input and `P` is the corresponding
permutation matrix.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
Shape is `[N, M, M]`.
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
A tuple of `Tensor` objects (sign, log_abs_determinant).
</td>
</tr>
<tr>
<td>
`sign`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr><tr>
<td>
`log_abs_determinant`
</td>
<td>
A `Tensor`. Has the same type as `input`.
</td>
</tr>
</table>

