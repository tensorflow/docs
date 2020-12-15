description: Computes the matrix logarithm of one or more square matrices:

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.logm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.logm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the matrix logarithm of one or more square matrices:

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.logm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.logm(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


\\(log(exp(A)) = A\\)

This op is only defined for complex matrices. If A is positive-definite and
real, then casting to a complex matrix, taking the logarithm and casting back
to a real matrix will give the correct result.

This function computes the matrix logarithm using the Schur-Parlett algorithm.
Details of the algorithm can be found in Section 11.6.2 of:
Nicholas J. Higham, Functions of Matrices: Theory and Computation, SIAM 2008.
ISBN 978-0-898716-46-7.

The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
form square matrices. The output is a tensor of the same shape as the input
containing the exponential for all input submatrices `[..., :, :]`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
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

