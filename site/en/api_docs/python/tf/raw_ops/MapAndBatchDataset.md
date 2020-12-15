description: Creates a dataset that fuses mapping with batching.

robots: noindex

# tf.raw_ops.MapAndBatchDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that fuses mapping with batching.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.MapAndBatchDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.MapAndBatchDataset(
    input_dataset, other_arguments, batch_size, num_parallel_calls, drop_remainder,
    f, output_types, output_shapes, preserve_cardinality=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a dataset that applies `f` to the outputs of `input_dataset` and then
batches `batch_size` of them.

Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
to `batch_size * num_parallel_batches` copies of `f` in parallel.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_dataset`
</td>
<td>
A `Tensor` of type `variant`.
A variant tensor representing the input dataset.
</td>
</tr><tr>
<td>
`other_arguments`
</td>
<td>
A list of `Tensor` objects.
A list of tensors, typically values that were captured when building a closure
for `f`.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of elements to accumulate in a
batch. It determines the number of concurrent invocations of `f` that process
elements from `input_dataset` in parallel.
</td>
</tr><tr>
<td>
`num_parallel_calls`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the maximum number of parallel invocations of the `map_fn`
function. Applying the `map_fn` on consecutive input elements in parallel has
the potential to improve input pipeline throughput.
</td>
</tr><tr>
<td>
`drop_remainder`
</td>
<td>
A `Tensor` of type `bool`.
A scalar representing whether the last batch should be dropped in case its size
is smaller than desired.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
A function to apply to the outputs of `input_dataset`.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A list of `tf.DTypes` that has length `>= 1`.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`) that has length `>= 1`.
</td>
</tr><tr>
<td>
`preserve_cardinality`
</td>
<td>
An optional `bool`. Defaults to `False`.
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
A `Tensor` of type `variant`.
</td>
</tr>

</table>

