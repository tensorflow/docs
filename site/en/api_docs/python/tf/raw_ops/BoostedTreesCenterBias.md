description: Calculates the prior from the training data (the bias) and fills in the first node with the logits' prior. Returns a boolean indicating whether to continue centering.

robots: noindex

# tf.raw_ops.BoostedTreesCenterBias

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Calculates the prior from the training data (the bias) and fills in the first node with the logits' prior. Returns a boolean indicating whether to continue centering.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesCenterBias`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesCenterBias(
    tree_ensemble_handle, mean_gradients, mean_hessians, l1, l2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tree_ensemble_handle`
</td>
<td>
A `Tensor` of type `resource`.
Handle to the tree ensemble.
</td>
</tr><tr>
<td>
`mean_gradients`
</td>
<td>
A `Tensor` of type `float32`.
A tensor with shape=[logits_dimension] with mean of gradients for a first node.
</td>
</tr><tr>
<td>
`mean_hessians`
</td>
<td>
A `Tensor` of type `float32`.
A tensor with shape=[logits_dimension] mean of hessians for a first node.
</td>
</tr><tr>
<td>
`l1`
</td>
<td>
A `Tensor` of type `float32`.
l1 regularization factor on leaf weights, per instance based.
</td>
</tr><tr>
<td>
`l2`
</td>
<td>
A `Tensor` of type `float32`.
l2 regularization factor on leaf weights, per instance based.
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
A `Tensor` of type `bool`.
</td>
</tr>

</table>

