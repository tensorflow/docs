description: A ProtocolMessage

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.ConfigProto" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="DeviceCountEntry"/>
<meta itemprop="property" content="Experimental"/>
</div>

# tf.compat.v1.ConfigProto

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/core/protobuf/config.proto">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A ProtocolMessage

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`allow_soft_placement`
</td>
<td>
`bool allow_soft_placement`
</td>
</tr><tr>
<td>
`cluster_def`
</td>
<td>
`ClusterDef cluster_def`
</td>
</tr><tr>
<td>
`device_count`
</td>
<td>
`repeated DeviceCountEntry device_count`
</td>
</tr><tr>
<td>
`device_filters`
</td>
<td>
`repeated string device_filters`
</td>
</tr><tr>
<td>
`experimental`
</td>
<td>
`Experimental experimental`
</td>
</tr><tr>
<td>
`gpu_options`
</td>
<td>
`GPUOptions gpu_options`
</td>
</tr><tr>
<td>
`graph_options`
</td>
<td>
`GraphOptions graph_options`
</td>
</tr><tr>
<td>
`inter_op_parallelism_threads`
</td>
<td>
`int32 inter_op_parallelism_threads`
</td>
</tr><tr>
<td>
`intra_op_parallelism_threads`
</td>
<td>
`int32 intra_op_parallelism_threads`
</td>
</tr><tr>
<td>
`isolate_session_state`
</td>
<td>
`bool isolate_session_state`
</td>
</tr><tr>
<td>
`log_device_placement`
</td>
<td>
`bool log_device_placement`
</td>
</tr><tr>
<td>
`operation_timeout_in_ms`
</td>
<td>
`int64 operation_timeout_in_ms`
</td>
</tr><tr>
<td>
`placement_period`
</td>
<td>
`int32 placement_period`
</td>
</tr><tr>
<td>
`rpc_options`
</td>
<td>
`RPCOptions rpc_options`
</td>
</tr><tr>
<td>
`session_inter_op_thread_pool`
</td>
<td>
`repeated ThreadPoolOptionProto session_inter_op_thread_pool`
</td>
</tr><tr>
<td>
`share_cluster_devices_in_session`
</td>
<td>
`bool share_cluster_devices_in_session`
</td>
</tr><tr>
<td>
`use_per_session_threads`
</td>
<td>
`bool use_per_session_threads`
</td>
</tr>
</table>



## Child Classes
[`class DeviceCountEntry`](../../../tf/compat/v1/ConfigProto/DeviceCountEntry.md)

[`class Experimental`](../../../tf/compat/v1/ConfigProto/Experimental.md)

