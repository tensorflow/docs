description: Aggregates the summary of accumulated stats for the batch.

robots: noindex

# tf.raw_ops.BoostedTreesAggregateStats

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
<p>`tf.compat.v1.raw_ops.BoostedTreesAggregateStats`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesAggregateStats(
    node_ids, gradients, hessians, feature, max_splits, num_buckets, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary stats contains gradients and hessians accumulated for each node, feature dimension id and bucket.

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
`feature`
</td>
<td>
A `Tensor` of type `int32`.
int32; Rank 2 feature Tensors (shape=[batch_size, feature_dimension]).
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
int; equals to the maximum possible value of bucketized feature.
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

