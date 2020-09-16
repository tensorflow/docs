description: Updates the tree ensemble by adding a layer to the last tree being grown

robots: noindex

# tf.raw_ops.BoostedTreesUpdateEnsembleV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Updates the tree ensemble by adding a layer to the last tree being grown

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesUpdateEnsembleV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesUpdateEnsembleV2(
    tree_ensemble_handle, feature_ids, dimension_ids, node_ids, gains, thresholds,
    left_node_contribs, right_node_contribs, split_types, max_depth, learning_rate,
    pruning_mode, logits_dimension=1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

or by starting a new tree.

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
Handle to the ensemble variable.
</td>
</tr><tr>
<td>
`feature_ids`
</td>
<td>
A list of at least 1 `Tensor` objects with type `int32`.
Rank 1 tensor with ids for each feature. This is the real id of
the feature that will be used in the split.
</td>
</tr><tr>
<td>
`dimension_ids`
</td>
<td>
A list of `Tensor` objects with type `int32`.
List of rank 1 tensors representing the dimension in each feature.
</td>
</tr><tr>
<td>
`node_ids`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `int32`.
List of rank 1 tensors representing the nodes for which this feature
has a split.
</td>
</tr><tr>
<td>
`gains`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
List of rank 1 tensors representing the gains for each of the feature's
split.
</td>
</tr><tr>
<td>
`thresholds`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `int32`.
List of rank 1 tensors representing the thesholds for each of the
feature's split.
</td>
</tr><tr>
<td>
`left_node_contribs`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
List of rank 2 tensors with left leaf contribs for each of
the feature's splits. Will be added to the previous node values to constitute
the values of the left nodes.
</td>
</tr><tr>
<td>
`right_node_contribs`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
List of rank 2 tensors with right leaf contribs for each
of the feature's splits. Will be added to the previous node values to constitute
the values of the right nodes.
</td>
</tr><tr>
<td>
`split_types`
</td>
<td>
A list with the same length as `dimension_ids` of `Tensor` objects with type `string`.
List of rank 1 tensors representing the split type for each feature.
</td>
</tr><tr>
<td>
`max_depth`
</td>
<td>
A `Tensor` of type `int32`. Max depth of the tree to build.
</td>
</tr><tr>
<td>
`learning_rate`
</td>
<td>
A `Tensor` of type `float32`.
shrinkage const for each new tree.
</td>
</tr><tr>
<td>
`pruning_mode`
</td>
<td>
A `Tensor` of type `int32`.
0-No pruning, 1-Pre-pruning, 2-Post-pruning.
</td>
</tr><tr>
<td>
`logits_dimension`
</td>
<td>
An optional `int`. Defaults to `1`.
scalar, dimension of the logits
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
The created Operation.
</td>
</tr>

</table>

