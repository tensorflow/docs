description: Calculates gains for each feature and returns the best possible split information for the feature.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Calculates gains for each feature and returns the best possible split information for the feature.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesSparseCalculateBestFeatureSplit(
    node_id_range, stats_summary_indices, stats_summary_values, stats_summary_shape,
    l1, l2, tree_complexity, min_node_weight, logits_dimension,
    split_type='inequality', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

The output shapes are compatible in a way that the first dimension of all tensors are the same and equal to the number of possible split nodes for each feature.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`node_id_range`
</td>
<td>
A `Tensor` of type `int32`.
A Rank 1 tensor (shape=[2]) to specify the range [first, last) of node ids to process within `stats_summary_list`. The nodes are iterated between the two nodes specified by the tensor, as like `for node_id in range(node_id_range[0], node_id_range[1])` (Note that the last index node_id_range[1] is exclusive).
</td>
</tr><tr>
<td>
`stats_summary_indices`
</td>
<td>
A `Tensor` of type `int32`.
A Rank 2 int64 tensor of dense shape [N, 4] (N specifies the number of non-zero values) for accumulated stats summary (gradient/hessian) per node per bucket for each feature. The second dimension contains node id, feature dimension, bucket id, and stats dim.
stats dim is the sum of logits dimension and hessian dimension, hessian dimension can either be logits dimension if diagonal hessian is used, or logits dimension^2 if full hessian is used.
</td>
</tr><tr>
<td>
`stats_summary_values`
</td>
<td>
A `Tensor` of type `float32`.
A Rank 1 float tensor of dense shape [N] (N specifies the number of non-zero values), which supplies the values for each element in summary_indices.
</td>
</tr><tr>
<td>
`stats_summary_shape`
</td>
<td>
A `Tensor` of type `int32`.
A Rank 1 float tensor of dense shape [4], which specifies the dense shape of the sparse tensor, which is [num tree nodes, feature dimensions, num buckets, stats dim].
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
`tree_complexity`
</td>
<td>
A `Tensor` of type `float32`.
adjustment to the gain, per leaf based.
</td>
</tr><tr>
<td>
`min_node_weight`
</td>
<td>
A `Tensor` of type `float32`.
minimum avg of hessians in a node before required for the node to be considered for splitting.
</td>
</tr><tr>
<td>
`logits_dimension`
</td>
<td>
An `int` that is `>= 1`.
The dimension of logit, i.e., number of classes.
</td>
</tr><tr>
<td>
`split_type`
</td>
<td>
An optional `string` from: `"inequality"`. Defaults to `"inequality"`.
A string indicating if this Op should perform inequality split or equality split.
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
A tuple of `Tensor` objects (node_ids, gains, feature_dimensions, thresholds, left_node_contribs, right_node_contribs, split_with_default_directions).
</td>
</tr>
<tr>
<td>
`node_ids`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`gains`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`feature_dimensions`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`thresholds`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`left_node_contribs`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`right_node_contribs`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`split_with_default_directions`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr>
</table>

