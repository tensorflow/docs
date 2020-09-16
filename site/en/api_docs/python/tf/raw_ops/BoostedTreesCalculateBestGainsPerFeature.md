description: Calculates gains for each feature and returns the best possible split information for the feature.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature

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
<p>`tf.compat.v1.raw_ops.BoostedTreesCalculateBestGainsPerFeature`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesCalculateBestGainsPerFeature(
    node_id_range, stats_summary_list, l1, l2, tree_complexity, min_node_weight,
    max_splits, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

The length of output lists are all of the same length, `num_features`.
The output shapes are compatible in a way that the first dimension of all tensors of all lists are the same and equal to the number of possible split nodes for each feature.

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
`stats_summary_list`
</td>
<td>
A list of at least 1 `Tensor` objects with type `float32`.
A list of Rank 3 tensor (#shape=[max_splits, bucket, 2]) for accumulated stats summary (gradient/hessian) per node per buckets for each feature. The first dimension of the tensor is the maximum number of splits, and thus not all elements of it will be used, but only the indexes specified by node_ids will be used.
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
`max_splits`
</td>
<td>
An `int` that is `>= 1`.
the number of nodes that can be split in the whole tree. Used as a dimension of output tensors.
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
A tuple of `Tensor` objects (node_ids_list, gains_list, thresholds_list, left_node_contribs_list, right_node_contribs_list).
</td>
</tr>
<tr>
<td>
`node_ids_list`
</td>
<td>
A list with the same length as `stats_summary_list` of `Tensor` objects with type `int32`.
</td>
</tr><tr>
<td>
`gains_list`
</td>
<td>
A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
</td>
</tr><tr>
<td>
`thresholds_list`
</td>
<td>
A list with the same length as `stats_summary_list` of `Tensor` objects with type `int32`.
</td>
</tr><tr>
<td>
`left_node_contribs_list`
</td>
<td>
A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
</td>
</tr><tr>
<td>
`right_node_contribs_list`
</td>
<td>
A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
</td>
</tr>
</table>

