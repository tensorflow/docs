description: Metadata indicating how the TPU computation should be replicated.

robots: noindex

# tf.raw_ops.TPUReplicateMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Metadata indicating how the TPU computation should be replicated.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TPUReplicateMetadata`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TPUReplicateMetadata(
    num_replicas, num_cores_per_replica=1, topology='', use_tpu=(True),
    device_assignment=[], computation_shape=[], host_compute_core=[],
    padding_map=[], step_marker_location='STEP_MARK_AT_ENTRY',
    allow_soft_placement=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation holds the metadata common to operations of a `tpu.replicate()` computation subgraph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_replicas`
</td>
<td>
An `int` that is `>= 0`.
Number of replicas of the computation
</td>
</tr><tr>
<td>
`num_cores_per_replica`
</td>
<td>
An optional `int`. Defaults to `1`.
Number of cores per replica. Used for model parallelism.
</td>
</tr><tr>
<td>
`topology`
</td>
<td>
An optional `string`. Defaults to `""`.
TopologyProto indicating the topology of the TPU pod slice.
</td>
</tr><tr>
<td>
`use_tpu`
</td>
<td>
An optional `bool`. Defaults to `True`.
Whether to place the computation on the TPU.
</td>
</tr><tr>
<td>
`device_assignment`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
The assignment of devices for the computation.
</td>
</tr><tr>
<td>
`computation_shape`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
DEPRECATED. Use num_cores_per_replica instead.
</td>
</tr><tr>
<td>
`host_compute_core`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`padding_map`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
</td>
</tr><tr>
<td>
`step_marker_location`
</td>
<td>
An optional `string`. Defaults to `"STEP_MARK_AT_ENTRY"`.
</td>
</tr><tr>
<td>
`allow_soft_placement`
</td>
<td>
An optional `bool`. Defaults to `False`.
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

