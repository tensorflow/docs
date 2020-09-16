description: Gets next element for the provided shard number.

robots: noindex

# tf.raw_ops.MultiDeviceIteratorGetNextFromShard

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Gets next element for the provided shard number.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MultiDeviceIteratorGetNextFromShard`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MultiDeviceIteratorGetNextFromShard(
    multi_device_iterator, shard_num, incarnation_id, output_types, output_shapes,
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`multi_device_iterator`
</td>
<td>
A `Tensor` of type `resource`.
A MultiDeviceIterator resource.
</td>
</tr><tr>
<td>
`shard_num`
</td>
<td>
A `Tensor` of type `int32`.
Integer representing which shard to fetch data for.
</td>
</tr><tr>
<td>
`incarnation_id`
</td>
<td>
A `Tensor` of type `int64`.
Which incarnation of the MultiDeviceIterator is running.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The type list for the return values.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
The list of shapes being produced.
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
A list of `Tensor` objects of type `output_types`.
</td>
</tr>

</table>

