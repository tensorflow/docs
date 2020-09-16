description: Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.BoostedTreesQuantileStreamResourceDeserialize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.BoostedTreesQuantileStreamResourceDeserialize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.BoostedTreesQuantileStreamResourceDeserialize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.BoostedTreesQuantileStreamResourceDeserialize(
    quantile_stream_resource_handle, bucket_boundaries, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An op that deserializes bucket boundaries and are boundaries ready flag into current QuantileAccumulator.

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
`bucket_boundaries`
</td>
<td>
A list of at least 1 `Tensor` objects with type `float32`.
float; List of Rank 1 Tensors each containing the bucket boundaries for a feature.
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

