description: Flush the summaries for a quantile stream resource.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesQuantileStreamResourceFlush" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesQuantileStreamResourceFlush

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Flush the summaries for a quantile stream resource.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesQuantileStreamResourceFlush`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesQuantileStreamResourceFlush(
    quantile_stream_resource_handle, num_buckets, generate_quantiles=(False),
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that flushes the summaries for a quantile stream resource.

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
`num_buckets`
</td>
<td>
A `Tensor` of type `int64`.
int; approximate number of buckets unless using generate_quantiles.
</td>
</tr><tr>
<td>
`generate_quantiles`
</td>
<td>
An optional `bool`. Defaults to `False`.
bool; If True, the output will be the num_quantiles for each stream where the ith
entry is the ith quantile of the input with an approximation error of epsilon.
Duplicate values may be present.
If False, the output will be the points in the histogram that we got which roughly
translates to 1/epsilon boundaries and without any duplicates.
Default to False.
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

