description: Output the rows of input_tensor to a queue for an input pipeline. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.input_producer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.input_producer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/input.py#L117-L202">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Output the rows of `input_tensor` to a queue for an input pipeline. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.input_producer(
    input_tensor, element_shape=None, num_epochs=None, shuffle=(True), seed=None,
    capacity=32, shared_name=None, summary_name=None, name=None, cancel_op=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.from_tensor_slices(input_tensor).shuffle(tf.shape(input_tensor, out_type=tf.int64)[0]).repeat(num_epochs)`. If `shuffle=False`, omit the `.shuffle(...)`.

Note: if `num_epochs` is not `None`, this function creates local counter
`epochs`. Use `local_variables_initializer()` to initialize local variables.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_tensor`
</td>
<td>
A tensor with the rows to produce. Must be at least
one-dimensional. Must either have a fully-defined shape, or
`element_shape` must be defined.
</td>
</tr><tr>
<td>
`element_shape`
</td>
<td>
(Optional.) A `TensorShape` representing the shape of a
row of `input_tensor`, if it cannot be inferred.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
(Optional.) An integer. If specified `input_producer` produces
each row of `input_tensor` `num_epochs` times before generating an
`OutOfRange` error. If not specified, `input_producer` can cycle through
the rows of `input_tensor` an unlimited number of times.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
(Optional.) A boolean. If true, the rows are randomly shuffled
within each epoch.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
(Optional.) An integer. The seed to use if `shuffle` is true.
</td>
</tr><tr>
<td>
`capacity`
</td>
<td>
(Optional.) The capacity of the queue to be used for buffering
the input.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
(Optional.) If set, this queue will be shared under the given
name across multiple sessions.
</td>
</tr><tr>
<td>
`summary_name`
</td>
<td>
(Optional.) If set, a scalar summary for the current queue
size will be generated, using this name as part of the tag.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional.) A name for queue.
</td>
</tr><tr>
<td>
`cancel_op`
</td>
<td>
(Optional.) Cancel op for the queue
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A queue with the output rows.  A `QueueRunner` for the queue is
added to the current `QUEUE_RUNNER` collection of the current
graph.
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
If the shape of the input cannot be inferred from the arguments.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called with eager execution enabled.
</td>
</tr>
</table>




#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API to ingest data under eager execution.

