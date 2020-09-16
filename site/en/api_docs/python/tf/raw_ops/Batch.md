description: Batches all input tensors nondeterministically.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Batch" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Batch

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Batches all input tensors nondeterministically.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Batch`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Batch(
    in_tensors, num_batch_threads, max_batch_size, batch_timeout_micros,
    grad_timeout_micros, max_enqueued_batches=10, allowed_batch_sizes=[],
    container='', shared_name='', batching_queue='', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

When many instances of this Op are being run concurrently with the same
container/shared_name in the same device, some will output zero-shaped Tensors
and others will output Tensors of size up to max_batch_size.

All Tensors in in_tensors are batched together (so, for example, labels and
features should be batched with a single instance of this operation.

Each invocation of batch emits an `id` scalar which will be used to identify
this particular invocation when doing unbatch or its gradient.

Each op which emits a non-empty batch will also emit a non-empty batch_index
Tensor, which, is a [K, 3] matrix where each row contains the invocation's id,
start, and length of elements of each set of Tensors present in batched_tensors.

Batched tensors are concatenated along the first dimension, and all tensors in
in_tensors must have the first dimension of the same size.

in_tensors: The tensors to be batched.
num_batch_threads: Number of scheduling threads for processing batches of work.
 Determines the number of batches processed in parallel.
max_batch_size: Batch sizes will never be bigger than this.
batch_timeout_micros: Maximum number of microseconds to wait before outputting
 an incomplete batch.
allowed_batch_sizes: Optional list of allowed batch sizes. If left empty, does
 nothing. Otherwise, supplies a list of batch sizes, causing the op to pad
 batches up to one of those sizes. The entries must increase monotonically, and
 the final entry must equal max_batch_size.
grad_timeout_micros: The timeout to use for the gradient. See Unbatch.
batched_tensors: Either empty tensors or a batch of concatenated Tensors.
batch_index: If out_tensors is non-empty, has information to invert it.
container: Controls the scope of sharing of this batch.
id: always contains a scalar with a unique ID for this invocation of Batch.
shared_name: Concurrently running instances of batch in the same device with the
 same container and shared_name will batch their elements together. If left
 empty, the op name will be used as the shared name.
T: the types of tensors to be batched.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`in_tensors`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`num_batch_threads`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`max_batch_size`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`batch_timeout_micros`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`grad_timeout_micros`
</td>
<td>
An `int`.
</td>
</tr><tr>
<td>
`max_enqueued_batches`
</td>
<td>
An optional `int`. Defaults to `10`.
</td>
</tr><tr>
<td>
`allowed_batch_sizes`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
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
`batching_queue`
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
A tuple of `Tensor` objects (batched_tensors, batch_index, id).
</td>
</tr>
<tr>
<td>
`batched_tensors`
</td>
<td>
A list of `Tensor` objects. Has the same type as `in_tensors`.
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
</tr>
</table>

