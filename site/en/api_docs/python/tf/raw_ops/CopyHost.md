description: Copy a tensor to host.

robots: noindex

# tf.raw_ops.CopyHost

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Copy a tensor to host.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.CopyHost`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.CopyHost(
    input, tensor_name='', debug_ops_spec=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Performs CPU-to-CPU deep-copying of tensor.
N.B.: If the all downstream attached debug ops are disabled given the current
gRPC gating status, the output will simply forward the input tensor without
deep-copying. See the documentation of Debug* ops for more details.

Unlike the Copy Op, this op has HostMemory constraint on its input or output.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Input tensor.
</td>
</tr><tr>
<td>
`tensor_name`
</td>
<td>
An optional `string`. Defaults to `""`.
The name of the input tensor.
</td>
</tr><tr>
<td>
`debug_ops_spec`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
A list of debug op spec (op, url, gated_grpc) for attached debug
ops. Each element of the list has the format
<debug_op>;<grpc_url>;<gated_grpc>, wherein gated_grpc is boolean represented
as 0/1. E.g., "DebugIdentity;grpc://foo:3333;1",
"DebugIdentity;file:///tmp/tfdbg_1;0".
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

