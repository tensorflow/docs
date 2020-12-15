description: Receives the named tensor from send_device on recv_device.

robots: noindex

# tf.raw_ops.Recv

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Receives the named tensor from send_device on recv_device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Recv`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Recv(
    tensor_type, tensor_name, send_device, send_device_incarnation, recv_device,
    client_terminated=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor_type`
</td>
<td>
A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
</td>
</tr><tr>
<td>
`tensor_name`
</td>
<td>
A `string`. The name of the tensor to receive.
</td>
</tr><tr>
<td>
`send_device`
</td>
<td>
A `string`. The name of the device sending the tensor.
</td>
</tr><tr>
<td>
`send_device_incarnation`
</td>
<td>
An `int`. The current incarnation of send_device.
</td>
</tr><tr>
<td>
`recv_device`
</td>
<td>
A `string`. The name of the device receiving the tensor.
</td>
</tr><tr>
<td>
`client_terminated`
</td>
<td>
An optional `bool`. Defaults to `False`.
If set to true, this indicates that the node was added
to the graph as a result of a client-side feed or fetch of Tensor data,
in which case the corresponding send or recv is expected to be managed
locally by the caller.
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
A `Tensor` of type `tensor_type`.
</td>
</tr>

</table>

