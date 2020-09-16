description: Dequeues a tuple of one or more tensors from the given queue.

robots: noindex

# tf.raw_ops.QueueDequeue

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Dequeues a tuple of one or more tensors from the given queue.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.QueueDequeue`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.QueueDequeue(
    handle, component_types, timeout_ms=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation has k outputs, where k is the number of components
in the tuples stored in the given queue, and output i is the ith
component of the dequeued tuple.

N.B. If the queue is empty, this operation will block until an element
has been dequeued (or 'timeout_ms' elapses, if specified).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`handle`
</td>
<td>
A `Tensor` of type mutable `string`. The handle to a queue.
</td>
</tr><tr>
<td>
`component_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
The type of each component in a tuple.
</td>
</tr><tr>
<td>
`timeout_ms`
</td>
<td>
An optional `int`. Defaults to `-1`.
If the queue is empty, this operation will block for up to
timeout_ms milliseconds.
Note: This option is not supported yet.
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
A list of `Tensor` objects of type `component_types`.
</td>
</tr>

</table>

