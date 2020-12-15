description: Makes the summary of accumulated stats for the batch.

robots: noindex

# tf.raw_ops.BoostedTreesMakeStatsSummary

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Makes the summary of accumulated stats for the batch.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesMakeStatsSummary`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesMakeStatsSummary(
    node_ids, gradients, hessians, bucketized_features_list, max_splits,
    num_buckets, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The summary stats contains gradients and hessians accumulated into the corresponding node and bucket for each example.

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
int32 Rank 1 Tensor containing node ids, which each example falls into for the requested layer.
</td>
</tr><tr>
<td>
`gradients`
</td>
<td>
A `Tensor` of type `float32`.
float32; Rank 2 Tensor (shape=[#examples, 1]) for gradients.
</td>
</tr><tr>
<td>
`hessians`
</td>
<td>
A `Tensor` of type `float32`.
float32; Rank 2 Tensor (shape=[#examples, 1]) for hessians.
</td>
</tr><tr>
<td>
`bucketized_features_list`
</td>
<td>
A list of at least 1 `Tensor` objects with type `int32`.
int32 list of Rank 1 Tensors, each containing the bucketized feature (for each feature column).
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

