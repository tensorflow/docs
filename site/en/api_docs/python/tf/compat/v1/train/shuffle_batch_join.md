description: Create batches by randomly shuffling tensors. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.shuffle_batch_join" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.shuffle_batch_join

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/input.py#L1414-L1509">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create batches by randomly shuffling tensors. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.shuffle_batch_join(
    tensors_list, batch_size, capacity, min_after_dequeue, seed=None,
    enqueue_many=(False), shapes=None, allow_smaller_final_batch=(False),
    shared_name=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.interleave(...).shuffle(min_after_dequeue).batch(batch_size)`.

The `tensors_list` argument is a list of tuples of tensors, or a list of
dictionaries of tensors.  Each element in the list is treated similarly
to the `tensors` argument of <a href="../../../../tf/compat/v1/train/shuffle_batch.md"><code>tf.compat.v1.train.shuffle_batch()</code></a>.

This version enqueues a different list of tensors in different threads.
It adds the following to the current `Graph`:

* A shuffling queue into which tensors from `tensors_list` are enqueued.
* A `dequeue_many` operation to create batches from the queue.
* A `QueueRunner` to `QUEUE_RUNNER` collection, to enqueue the tensors
  from `tensors_list`.

`len(tensors_list)` threads will be started, with thread `i` enqueuing
the tensors from `tensors_list[i]`. `tensors_list[i1][j]` must match
`tensors_list[i2][j]` in type and shape, except in the first dimension if
`enqueue_many` is true.

If `enqueue_many` is `False`, each `tensors_list[i]` is assumed
to represent a single example.  An input tensor with shape `[x, y, z]`
will be output as a tensor with shape `[batch_size, x, y, z]`.

If `enqueue_many` is `True`, `tensors_list[i]` is assumed to
represent a batch of examples, where the first dimension is indexed
by example, and all members of `tensors_list[i]` should have the
same size in the first dimension.  If an input tensor has shape `[*, x,
y, z]`, the output will have shape `[batch_size, x, y, z]`.

The `capacity` argument controls the how long the prefetching is allowed to
grow the queues.

The returned operation is a dequeue operation and will throw
<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a> if the input queue is exhausted. If this
operation is feeding another input queue, its queue runner will catch
this exception, however, if this operation is used in your main thread
you are responsible for catching this yourself.

If `allow_smaller_final_batch` is `True`, a smaller batch value than
`batch_size` is returned when the queue is closed and there are not enough
elements to fill the batch, otherwise the pending elements are discarded.
In addition, all output tensors' static shapes, as accessed via the
`shape` property will have a first `Dimension` value of `None`, and
operations that depend on fixed batch_size would fail.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tensors_list`
</td>
<td>
A list of tuples or dictionaries of tensors to enqueue.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
An integer. The new batch size pulled from the queue.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
An integer. The maximum number of elements in the queue.
</td>
</tr><tr>
<td>
`min_after_dequeue`
</td>
<td>
Minimum number elements in the queue after a
dequeue, used to ensure a level of mixing of elements.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Seed for the random shuffling within the queue.
</td>
</tr><tr>
<td>
`enqueue_many`
</td>
<td>
Whether each tensor in `tensor_list_list` is a single
example.
</td>
</tr><tr>
<td>
`shapes`
</td>
<td>
(Optional) The shapes for each example.  Defaults to the
inferred shapes for `tensors_list[i]`.
</td>
</tr><tr>
<td>
`allow_smaller_final_batch`
</td>
<td>
(Optional) Boolean. If `True`, allow the final
batch to be smaller if there are insufficient items left in the queue.
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
(Optional) A name for the operations.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list or dictionary of tensors with the same number and types as
`tensors_list[i]`.
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
If the `shapes` are not specified, and cannot be
inferred from the elements of `tensors_list`.
</td>
</tr>
</table>




#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API to ingest data under eager execution.

