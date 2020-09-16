description: Output strings (e.g. filenames) to a queue for an input pipeline. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.string_input_producer" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.string_input_producer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/input.py#L205-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Output strings (e.g. filenames) to a queue for an input pipeline. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.string_input_producer(
    string_tensor, num_epochs=None, shuffle=(True), seed=None, capacity=32,
    shared_name=None, name=None, cancel_op=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.from_tensor_slices(string_tensor).shuffle(tf.shape(input_tensor, out_type=tf.int64)[0]).repeat(num_epochs)`. If `shuffle=False`, omit the `.shuffle(...)`.

Note: if `num_epochs` is not `None`, this function creates local counter
`epochs`. Use `local_variables_initializer()` to initialize local variables.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`string_tensor`
</td>
<td>
A 1-D string tensor with the strings to produce.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
An integer (optional). If specified, `string_input_producer`
produces each string from `string_tensor` `num_epochs` times before
generating an `OutOfRange` error. If not specified,
`string_input_producer` can cycle through the strings in `string_tensor`
an unlimited number of times.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean. If true, the strings are randomly shuffled within each
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
name across multiple sessions. All sessions open to the device which has
this queue will be able to access it via the shared_name. Using this in
a distributed setting means each name will only be seen by one of the
sessions which has access to this operation.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operations (optional).
</td>
</tr><tr>
<td>
`cancel_op`
</td>
<td>
Cancel op for the queue (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A queue with the output strings.  A `QueueRunner` for the Queue
is added to the current `Graph`'s `QUEUE_RUNNER` collection.
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
If the string_tensor is a null Python list.  At runtime,
will fail with an assertion if string_tensor becomes a null tensor.
</td>
</tr>
</table>




#### Eager Compatibility
Input pipelines based on Queues are not supported when eager execution is
enabled. Please use the <a href="../../../../tf/data.md"><code>tf.data</code></a> API to ingest data under eager execution.

