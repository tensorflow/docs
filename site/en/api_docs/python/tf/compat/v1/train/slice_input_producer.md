description: Produces a slice of each Tensor in tensor_list. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.slice_input_producer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.slice_input_producer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/input.py#L322-L376">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Produces a slice of each `Tensor` in `tensor_list`. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.slice_input_producer(
    tensor_list, num_epochs=None, shuffle=(True), seed=None, capacity=32,
    shared_name=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.from_tensor_slices(tuple(tensor_list)).shuffle(tf.shape(input_tensor, out_type=tf.int64)[0]).repeat(num_epochs)`. If `shuffle=False`, omit the `.shuffle(...)`.

Implemented using a Queue -- a `QueueRunner` for the Queue
is added to the current `Graph`'s `QUEUE_RUNNER` collection.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensor_list`
</td>
<td>
A list of `Tensor` objects. Every `Tensor` in
`tensor_list` must have the same size in the first dimension.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
An integer (optional). If specified, `slice_input_producer`
produces each slice `num_epochs` times before generating
an `OutOfRange` error. If not specified, `slice_input_producer` can cycle
through the slices an unlimited number of times.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean. If true, the integers are randomly shuffled within each
epoch.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An integer (optional). Seed used if shuffle == True.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
An integer. Sets the queue capacity.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
(optional). If set, this queue will be shared under the given
name across multiple sessions.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operations (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of tensors, one for each element of `tensor_list`.  If the tensor
in `tensor_list` has shape `[N, a, b, .., z]`, then the corresponding output
tensor will have shape `[a, b, ..., z]`.
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
if `slice_input_producer` produces nothing from `tensor_list`.
</td>
</tr>
</table>




#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API to ingest data under eager execution.

