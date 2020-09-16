description: Flush the quantile summaries from each quantile stream resource.

robots: noindex

# tf.raw_ops.BoostedTreesFlushQuantileSummaries

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Flush the quantile summaries from each quantile stream resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesFlushQuantileSummaries`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesFlushQuantileSummaries(
    quantile_stream_resource_handle, num_features, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that outputs a list of quantile summaries of a quantile stream resource.
Each summary Tensor is rank 2, containing summaries (value, weight, min_rank,
max_rank) for a single feature.

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

