description: Runs a list of tensors to conditionally fill a queue to create batches. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.maybe_batch_join" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.maybe_batch_join

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/input.py#L1190-L1244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Runs a list of tensors to conditionally fill a queue to create batches. (deprecated)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.maybe_batch_join(
    tensors_list, keep_input, batch_size, capacity=32, enqueue_many=(False),
    shapes=None, dynamic_pad=(False), allow_smaller_final_batch=(False),
    shared_name=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data.md"><code>tf.data</code></a>. Use `tf.data.Dataset.interleave(...).filter(...).batch(batch_size)` (or `padded_batch(...)` if `dynamic_pad=True`).

See docstring in `batch_join` for more details.

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
`keep_input`
</td>
<td>
A `bool` Tensor.  This tensor controls whether the input is
added to the queue or not.  If it is a scalar and evaluates `True`, then
`tensors` are all added to the queue. If it is a vector and `enqueue_many`
is `True`, then each example is added to the queue only if the
corresponding value in `keep_input` is `True`. This tensor essentially
acts as a filtering mechanism.
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
inferred shapes for `tensor_list_list[i]`.
</td>
</tr><tr>
<td>
`dynamic_pad`
</td>
<td>
Boolean.  Allow variable dimensions in input shapes.
The given dimensions are padded upon dequeue so that tensors within a
batch have the same shapes.
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
(Optional) If set, this queue will be shared under the given
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
inferred from the elements of `tensor_list_list`.
</td>
</tr>
</table>

