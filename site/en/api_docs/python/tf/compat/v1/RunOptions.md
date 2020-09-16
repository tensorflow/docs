description: A ProtocolMessage

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.RunOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="Experimental"/>
<meta itemprop="property" content="FULL_TRACE"/>
<meta itemprop="property" content="HARDWARE_TRACE"/>
<meta itemprop="property" content="NO_TRACE"/>
<meta itemprop="property" content="SOFTWARE_TRACE"/>
<meta itemprop="property" content="TraceLevel"/>
</div>

# tf.compat.v1.RunOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/core/protobuf/config.proto">
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
`debug_options`
</td>
<td>
`DebugOptions debug_options`
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
`inter_op_thread_pool`
</td>
<td>
`int32 inter_op_thread_pool`
</td>
</tr><tr>
<td>
`output_partition_graphs`
</td>
<td>
`bool output_partition_graphs`
</td>
</tr><tr>
<td>
`report_tensor_allocations_upon_oom`
</td>
<td>
`bool report_tensor_allocations_upon_oom`
</td>
</tr><tr>
<td>
`timeout_in_ms`
</td>
<td>
`int64 timeout_in_ms`
</td>
</tr><tr>
<td>
`trace_level`
</td>
<td>
`TraceLevel trace_level`
</td>
</tr>
</table>



## Child Classes
[`class Experimental`](../../../tf/compat/v1/RunOptions/Experimental.md)

## Class Variables

* `FULL_TRACE = 3` <a id="FULL_TRACE"></a>
* `HARDWARE_TRACE = 2` <a id="HARDWARE_TRACE"></a>
* `NO_TRACE = 0` <a id="NO_TRACE"></a>
* `SOFTWARE_TRACE = 1` <a id="SOFTWARE_TRACE"></a>
* `TraceLevel` <a id="TraceLevel"></a>
