description: Computes the reverse mode backpropagated gradient of the Cholesky algorithm.

robots: noindex

# tf.raw_ops.CholeskyGrad

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the reverse mode backpropagated gradient of the Cholesky algorithm.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CholeskyGrad`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CholeskyGrad(
    l, grad, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For an explanation see "Differentiation of the Cholesky algorithm" by
Iain Murray http://arxiv.org/abs/1602.07527.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`l`
</td>
<td>
A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
Output of batch Cholesky algorithm l = cholesky(A). Shape is `[..., M, M]`.
Algorithm depends only on lower triangular part of the innermost matrices of
this tensor.
</td>
</tr><tr>
<td>
`grad`
</td>
<td>
A `Tensor`. Must have the same type as `l`.
df/dl where f is some scalar function. Shape is `[..., M, M]`.
Algorithm depends only on lower triangular part of the innermost matrices of
this tensor.
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
A `Tensor`. Has the same type as `l`.
</td>
</tr>

</table>

