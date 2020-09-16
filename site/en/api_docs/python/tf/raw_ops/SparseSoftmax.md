description: Applies softmax to a batched N-D SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.SparseSoftmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.SparseSoftmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Applies softmax to a batched N-D `SparseTensor`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.SparseSoftmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.SparseSoftmax(
    sp_indices, sp_values, sp_shape, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs represent an N-D SparseTensor  with logical shape `[..., B, C]`
(where `N >= 2`), and with indices sorted in the canonical lexicographic order.

This op is equivalent to applying the normal <a href="../../tf/nn/softmax.md"><code>tf.nn.softmax()</code></a> to each innermost
logical submatrix with shape `[B, C]`, but with the catch that *the implicitly
zero elements do not participate*.  Specifically, the algorithm is equivalent
to the following:

  (1) Applies <a href="../../tf/nn/softmax.md"><code>tf.nn.softmax()</code></a> to a densified view of each innermost submatrix
      with shape `[B, C]`, along the size-C dimension;
  (2) Masks out the original implicitly-zero locations;
  (3) Renormalizes the remaining elements.

Hence, the `SparseTensor` result has exactly the same non-zero indices and
shape.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_indices`
</td>
<td>
A `Tensor` of type `int64`.
2-D.  `NNZ x R` matrix with the indices of non-empty values in a
SparseTensor, in canonical ordering.
</td>
</tr><tr>
<td>
`sp_values`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `float64`.
1-D.  `NNZ` non-empty values corresponding to `sp_indices`.
</td>
</tr><tr>
<td>
`sp_shape`
</td>
<td>
A `Tensor` of type `int64`.
1-D.  Shape of the input SparseTensor.
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
A `Tensor`. Has the same type as `sp_values`.
</td>
</tr>

</table>

