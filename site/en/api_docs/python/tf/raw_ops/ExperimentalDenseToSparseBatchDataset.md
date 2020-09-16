description: Creates a dataset that batches input elements into a SparseTensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.ExperimentalDenseToSparseBatchDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.ExperimentalDenseToSparseBatchDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that batches input elements into a SparseTensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ExperimentalDenseToSparseBatchDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ExperimentalDenseToSparseBatchDataset(
    input_dataset, batch_size, row_shape, output_types, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


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
A handle to an input dataset. Must have a single component.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of elements to accumulate in a
batch.
</td>
</tr><tr>
<td>
`row_shape`
</td>
<td>
A `Tensor` of type `int64`.
A vector representing the dense shape of each row in the produced
SparseTensor. The shape may be partially specified, using `-1` to indicate
that a particular dimension should use the maximum size of all batch elements.
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

