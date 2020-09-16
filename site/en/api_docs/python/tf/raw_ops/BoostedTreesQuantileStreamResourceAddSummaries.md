description: Add the quantile summaries to each quantile stream resource.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesQuantileStreamResourceAddSummaries" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesQuantileStreamResourceAddSummaries

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Add the quantile summaries to each quantile stream resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesQuantileStreamResourceAddSummaries`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesQuantileStreamResourceAddSummaries(
    quantile_stream_resource_handle, summaries, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that adds a list of quantile summaries to a quantile stream resource. Each
summary Tensor is rank 2, containing summaries (value, weight, min_rank, max_rank)
for a single feature.

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
`summaries`
</td>
<td>
A list of `Tensor` objects with type `float32`.
string; List of Rank 2 Tensor each containing the summaries for a single feature.
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

