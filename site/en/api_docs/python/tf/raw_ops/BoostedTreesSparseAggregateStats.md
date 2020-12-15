description: Aggregates the summary of accumulated stats for the batch.

robots: noindex

# tf.raw_ops.BoostedTreesSparseAggregateStats

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Aggregates the summary of accumulated stats for the batch.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesSparseAggregateStats`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesSparseAggregateStats(
    node_ids, gradients, hessians, feature_indices, feature_values, feature_shape,
    max_splits, num_buckets, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary stats contains gradients and hessians accumulated for each node, bucket and dimension id.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`node_ids`
</td>
<td>
A `Tensor` of type `int32`.
int32; Rank 1 Tensor containing node ids for each example, shape [batch_size].
</td>
</tr><tr>
<td>
`gradients`
</td>
<td>
A `Tensor` of type `float32`.
float32; Rank 2 Tensor (shape=[batch_size, logits_dimension]) with gradients for each example.
</td>
</tr><tr>
<td>
`hessians`
</td>
<td>
A `Tensor` of type `float32`.
float32; Rank 2 Tensor (shape=[batch_size, hessian_dimension]) with hessians for each example.
</td>
</tr><tr>
<td>
`feature_indices`
</td>
<td>
A `Tensor` of type `int32`.
int32; Rank 2 indices of feature sparse Tensors (shape=[number of sparse entries, 2]).
Number of sparse entries across all instances from the batch. The first value is
the index of the instance, the second is dimension of the feature. The second axis
can only have 2 values, i.e., the input dense version of Tensor can only be matrix.
</td>
</tr><tr>
<td>
`feature_values`
</td>
<td>
A `Tensor` of type `int32`.
int32; Rank 1 values of feature sparse Tensors (shape=[number of sparse entries]).
Number of sparse entries across all instances from the batch. The first value is
the index of the instance, the second is dimension of the feature.
</td>
</tr><tr>
<td>
`feature_shape`
</td>
<td>
A `Tensor` of type `int32`.
int32; Rank 1 dense shape of feature sparse Tensors (shape=[2]).
The first axis can only have 2 values, [batch_size, feature_dimension].
</td>
</tr><tr>
<td>
`max_splits`
</td>
<td>
An `int` that is `>= 1`.
int; the maximum number of splits possible in the whole tree.
</td>
</tr><tr>
<td>
`num_buckets`
</td>
<td>
An `int` that is `>= 1`.
int; equals to the maximum possible value of bucketized feature + 1.
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
A tuple of `Tensor` objects (stats_summary_indices, stats_summary_values, stats_summary_shape).
</td>
</tr>
<tr>
<td>
`stats_summary_indices`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`stats_summary_values`
</td>
<td>
A `Tensor` of type `float32`.
</td>
</tr><tr>
<td>
`stats_summary_shape`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr>
</table>

