description: Debug Identity V2 Op.

robots: noindex

# tf.raw_ops.DebugIdentityV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Debug Identity V2 Op.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DebugIdentityV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DebugIdentityV2(
    input, tfdbg_context_id='', op_name='', output_slot=-1, tensor_debug_mode=-1,
    debug_urls=[], circular_buffer_size=1000, tfdbg_run_id='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Provides an identity mapping from input to output, while writing the content of
the input tensor by calling DebugEventsWriter.

The semantics of the input tensor depends on tensor_debug_mode. In typical
usage, the input tensor comes directly from the user computation only when
graph_debug_mode is FULL_TENSOR (see protobuf/debug_event.proto for a
list of all the possible values of graph_debug_mode). For the other debug modes,
the input tensor should be produced by an additional op or subgraph that
computes summary information about one or more tensors.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Input tensor, non-Reference type
</td>
</tr><tr>
<td>
`tfdbg_context_id`
</td>
<td>
An optional `string`. Defaults to `""`.
A tfdbg-generated ID for the context that the op belongs to,
e.g., a concrete compiled tf.function.
</td>
</tr><tr>
<td>
`op_name`
</td>
<td>
An optional `string`. Defaults to `""`.
Optional. Name of the op that the debug op is concerned with.
Used only for single-tensor trace.
</td>
</tr><tr>
<td>
`output_slot`
</td>
<td>
An optional `int`. Defaults to `-1`.
Optional. Output slot index of the tensor that the debug op
is concerned with. Used only for single-tensor trace.
</td>
</tr><tr>
<td>
`tensor_debug_mode`
</td>
<td>
An optional `int`. Defaults to `-1`.
TensorDebugMode enum value. See debug_event.proto for details.
</td>
</tr><tr>
<td>
`debug_urls`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
List of URLs to debug targets, e.g., file:///foo/tfdbg_dump.
</td>
</tr><tr>
<td>
`circular_buffer_size`
</td>
<td>
An optional `int`. Defaults to `1000`.
</td>
</tr><tr>
<td>
`tfdbg_run_id`
</td>
<td>
An optional `string`. Defaults to `""`.
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
A `Tensor`. Has the same type as `input`.
</td>
</tr>

</table>

