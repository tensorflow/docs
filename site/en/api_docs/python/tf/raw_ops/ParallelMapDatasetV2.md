description: Creates a dataset that applies f to the outputs of input_dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ParallelMapDatasetV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ParallelMapDatasetV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that applies `f` to the outputs of `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ParallelMapDatasetV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ParallelMapDatasetV2(
    input_dataset, other_arguments, num_parallel_calls, f, output_types,
    output_shapes, use_inter_op_parallelism=(True), deterministic='default',
    preserve_cardinality=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Unlike a "MapDataset", which applies `f` sequentially, this dataset invokes up
to `num_parallel_calls` copies of `f` in parallel.

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
</td>
</tr><tr>
<td>
`other_arguments`
</td>
<td>
A list of `Tensor` objects.
</td>
</tr><tr>
<td>
`num_parallel_calls`
</td>
<td>
A `Tensor` of type `int64`.
The number of concurrent invocations of `f` that process
elements from `input_dataset` in parallel.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
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
`use_inter_op_parallelism`
</td>
<td>
An optional `bool`. Defaults to `True`.
</td>
</tr><tr>
<td>
`deterministic`
</td>
<td>
An optional `string`. Defaults to `"default"`.
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

