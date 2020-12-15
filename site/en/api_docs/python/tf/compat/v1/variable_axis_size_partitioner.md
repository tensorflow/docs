description: Get a partitioner for VariableScope to keep shards below max_shard_bytes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.variable_axis_size_partitioner" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.variable_axis_size_partitioner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/partitioned_variables.py#L71-L154">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Get a partitioner for VariableScope to keep shards below `max_shard_bytes`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.variable_axis_size_partitioner(
    max_shard_bytes, axis=0, bytes_per_string_element=16, max_shards=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This partitioner will shard a Variable along one axis, attempting to keep
the maximum shard size below `max_shard_bytes`.  In practice, this is not
always possible when sharding along only one axis.  When this happens,
this axis is sharded as much as possible (i.e., every dimension becomes
a separate shard).

If the partitioner hits the `max_shards` limit, then each shard may end up
larger than `max_shard_bytes`. By default `max_shards` equals `None` and no
limit on the number of shards is enforced.

One reasonable value for `max_shard_bytes` is `(64 << 20) - 1`, or almost
`64MB`, to keep below the protobuf byte limit.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`max_shard_bytes`
</td>
<td>
The maximum size any given shard is allowed to be.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The axis to partition along.  Default: outermost axis.
</td>
</tr><tr>
<td>
`bytes_per_string_element`
</td>
<td>
If the `Variable` is of type string, this provides
an estimate of how large each scalar in the `Variable` is.
</td>
</tr><tr>
<td>
`max_shards`
</td>
<td>
The maximum number of shards in int created taking precedence
over `max_shard_bytes`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A partition function usable as the `partitioner` argument to
`variable_scope` and `get_variable`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If any of the byte counts are non-positive.
</td>
</tr>
</table>

