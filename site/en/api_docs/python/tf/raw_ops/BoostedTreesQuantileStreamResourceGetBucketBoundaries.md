description: Generate the bucket boundaries for each feature based on accumulated summaries.

robots: noindex

# tf.raw_ops.BoostedTreesQuantileStreamResourceGetBucketBoundaries

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generate the bucket boundaries for each feature based on accumulated summaries.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesQuantileStreamResourceGetBucketBoundaries`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesQuantileStreamResourceGetBucketBoundaries(
    quantile_stream_resource_handle, num_features, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that returns a list of float tensors for a quantile stream resource. Each
tensor is Rank 1 containing bucket boundaries for a single feature.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`quantile_stream_resource_handle`
</td>
<td>
A `Tensor` of type `resource`.
resource handle referring to a QuantileStreamResource.
</td>
</tr><tr>
<td>
`num_features`
</td>
<td>
An `int` that is `>= 0`.
inferred int; number of features to get bucket boundaries for.
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
A list of `num_features` `Tensor` objects with type `float32`.
</td>
</tr>

</table>

