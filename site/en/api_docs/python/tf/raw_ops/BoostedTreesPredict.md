description: Runs multiple additive regression ensemble predictors on input instances and

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesPredict" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesPredict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Runs multiple additive regression ensemble predictors on input instances and

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesPredict`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesPredict(
    tree_ensemble_handle, bucketized_features, logits_dimension, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

computes the logits. It is designed to be used during prediction.
It traverses all the trees and calculates the final score for each instance.

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
</td>
</tr><tr>
<td>
`bucketized_features`
</td>
<td>
A list of at least 1 `Tensor` objects with type `int32`.
A list of rank 1 Tensors containing bucket id for each
feature.
</td>
</tr><tr>
<td>
`logits_dimension`
</td>
<td>
An `int`.
scalar, dimension of the logits, to be used for partial logits
shape.
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

