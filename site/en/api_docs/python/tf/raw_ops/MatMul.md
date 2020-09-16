description: Multiply the matrix "a" by the matrix "b".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.MatMul" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.MatMul

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Multiply the matrix "a" by the matrix "b".

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MatMul`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MatMul(
    a, b, transpose_a=(False), transpose_b=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs must be two-dimensional matrices and the inner dimension of
"a" (after being transposed if transpose_a is true) must match the
outer dimension of "b" (after being transposed if transposed_b is
true).

*Note*: The default kernel implementation for MatMul on GPUs uses
cublas.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`a`
</td>
<td>
A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`, `int32`, `int64`, `complex64`, `complex128`.
</td>
</tr><tr>
<td>
`b`
</td>
<td>
A `Tensor`. Must have the same type as `a`.
</td>
</tr><tr>
<td>
`transpose_a`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, "a" is transposed before multiplication.
</td>
</tr><tr>
<td>
`transpose_b`
</td>
<td>
An optional `bool`. Defaults to `False`.
If true, "b" is transposed before multiplication.
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
A `Tensor`. Has the same type as `a`.
</td>
</tr>

</table>

