description: Creates a dataset that shards the input dataset.

robots: noindex

# tf.raw_ops.AutoShardDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that shards the input dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.AutoShardDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.AutoShardDataset(
    input_dataset, num_workers, index, output_types, output_shapes,
    auto_shard_policy=0, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a dataset that shards the input dataset by num_workers, returning a
sharded dataset for the index-th worker. This attempts to automatically shard
a dataset by examining the Dataset graph and inserting a shard op before the
inputs to a reader Dataset (e.g. CSVDataset, TFRecordDataset).

This dataset will throw a NotFound error if we cannot shard the dataset
automatically.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
A variant tensor representing the input dataset.
</td>
</tr><tr>
<td>
`num_workers`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of workers to distribute this dataset across.
</td>
</tr><tr>
<td>
`index`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the index of the current worker out of num_workers.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
</td>
</tr><tr>
<td>
`auto_shard_policy`
</td>
<td>
An optional `int`. Defaults to `0`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

