description: Computes the matrix exponential of one or more square matrices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.linalg.expm" />
<meta itemprop="path" content="Stable" />
</div>

# tf.linalg.expm

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/linalg/linalg_impl.py#L232-L347">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the matrix exponential of one or more square matrices.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.linalg.expm`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.linalg.expm(
    input, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

$$exp(A) = \sum_{n=0}^\infty A^n/n!$$

The exponential is computed using a combination of the scaling and squaring
method and the Pade approximation. Details can be found in:
Nicholas J. Higham, "The scaling and squaring method for the matrix
exponential revisited," SIAM J. Matrix Anal. Applic., 26:1179-1193, 2005.

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
A `Tensor`. Must be `float16`, `float32`, `float64`, `complex64`, or
`complex128` with shape `[..., M, M]`.
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
the matrix exponential of the input.
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
An unsupported type is provided as input.
</td>
</tr>
</table>




#### Scipy Compatibility
Equivalent to scipy.linalg.expm

