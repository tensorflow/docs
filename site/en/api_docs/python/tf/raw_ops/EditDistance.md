description: Computes the (possibly normalized) Levenshtein Edit Distance.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.EditDistance" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.EditDistance

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Computes the (possibly normalized) Levenshtein Edit Distance.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.EditDistance`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.EditDistance(
    hypothesis_indices, hypothesis_values, hypothesis_shape, truth_indices,
    truth_values, truth_shape, normalize=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The inputs are variable-length sequences provided by SparseTensors
  (hypothesis_indices, hypothesis_values, hypothesis_shape)
and
  (truth_indices, truth_values, truth_shape).

#### The inputs are:




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`hypothesis_indices`
</td>
<td>
A `Tensor` of type `int64`.
The indices of the hypothesis list SparseTensor.
This is an N x R int64 matrix.
</td>
</tr><tr>
<td>
`hypothesis_values`
</td>
<td>
A `Tensor`.
The values of the hypothesis list SparseTensor.
This is an N-length vector.
</td>
</tr><tr>
<td>
`hypothesis_shape`
</td>
<td>
A `Tensor` of type `int64`.
The shape of the hypothesis list SparseTensor.
This is an R-length vector.
</td>
</tr><tr>
<td>
`truth_indices`
</td>
<td>
A `Tensor` of type `int64`.
The indices of the truth list SparseTensor.
This is an M x R int64 matrix.
</td>
</tr><tr>
<td>
`truth_values`
</td>
<td>
A `Tensor`. Must have the same type as `hypothesis_values`.
The values of the truth list SparseTensor.
This is an M-length vector.
</td>
</tr><tr>
<td>
`truth_shape`
</td>
<td>
A `Tensor` of type `int64`. truth indices, vector.
</td>
</tr><tr>
<td>
`normalize`
</td>
<td>
An optional `bool`. Defaults to `True`.
boolean (if true, edit distances are normalized by length of truth).

The output is:
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

