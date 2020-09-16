description: Reverses the operation of Batch for a single output Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Unbatch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Unbatch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Reverses the operation of Batch for a single output Tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Unbatch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Unbatch(
    batched_tensor, batch_index, id, timeout_micros, container='', shared_name='',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

An instance of Unbatch either receives an empty batched_tensor, in which case it
asynchronously waits until the values become available from a concurrently
running instance of Unbatch with the same container and shared_name, or receives
a non-empty batched_tensor in which case it finalizes all other concurrently
running instances and outputs its own element from the batch.

batched_tensor: The possibly transformed output of Batch. The size of the first
 dimension should remain unchanged by the transformations for the operation to
 work.
batch_index: The matching batch_index obtained from Batch.
id: The id scalar emitted by Batch.
unbatched_tensor: The Tensor corresponding to this execution.
timeout_micros: Maximum amount of time (in microseconds) to wait to receive the
 batched input tensor associated with a given invocation of the op.
container: Container to control resource sharing.
shared_name: Instances of Unbatch with the same container and shared_name are
 assumed to possibly belong to the same batch. If left empty, the op name will
 be used as the shared name.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`batched_tensor`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`batch_index`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`id`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`timeout_micros`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`container`
</td>
<td>
An optional `string`. Defaults to `""`.
</td>
</tr><tr>
<td>
`shared_name`
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
A `Tensor`. Has the same type as `batched_tensor`.
</td>
</tr>

</table>

