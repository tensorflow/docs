description: Creates a dataset that applies f to the outputs of input_dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.LegacyParallelInterleaveDatasetV2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.LegacyParallelInterleaveDatasetV2

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
<p>`tf.compat.v1.raw_ops.LegacyParallelInterleaveDatasetV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LegacyParallelInterleaveDatasetV2(
    input_dataset, other_arguments, cycle_length, block_length,
    buffer_output_elements, prefetch_input_elements, f, output_types, output_shapes,
    deterministic='default', name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The resulting dataset is similar to the `InterleaveDataset`, with the exception
that if retrieving the next value from a dataset would cause the requester to
block, it will skip that input dataset. This dataset is especially useful
when loading data from a variable-latency datastores (e.g. HDFS, GCS), as it
allows the training step to proceed so long as some data is available.

!! WARNING !! This dataset is not deterministic!

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
`cycle_length`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`block_length`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`buffer_output_elements`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`prefetch_input_elements`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`f`
</td>
<td>
A function decorated with @Defun.
A function mapping elements of `input_dataset`, concatenated with
`other_arguments`, to a Dataset variant that contains elements matching
`output_types` and `output_shapes`.
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
`deterministic`
</td>
<td>
An optional `string`. Defaults to `"default"`.
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

