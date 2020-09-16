description: Generate a sharded filename. The filename is printf formatted as

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ShardedFilename" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ShardedFilename

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generate a sharded filename. The filename is printf formatted as

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ShardedFilename`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ShardedFilename(
    basename, shard, num_shards, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

   %s-%05d-of-%05d, basename, shard, num_shards.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`basename`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`shard`
</td>
<td>
A `Tensor` of type `int32`.
</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>
A `Tensor` of type `int32`.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

