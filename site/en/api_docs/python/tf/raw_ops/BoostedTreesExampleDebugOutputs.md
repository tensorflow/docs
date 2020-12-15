description: Debugging/model interpretability outputs for each example.

robots: noindex

# tf.raw_ops.BoostedTreesExampleDebugOutputs

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Debugging/model interpretability outputs for each example.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesExampleDebugOutputs`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesExampleDebugOutputs(
    tree_ensemble_handle, bucketized_features, logits_dimension, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It traverses all the trees and computes debug metrics for individual examples,
such as getting split feature ids and logits after each split along the decision
path used to compute directional feature contributions.

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
scalar, dimension of the logits, to be used for constructing the protos in
examples_debug_outputs_serialized.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

