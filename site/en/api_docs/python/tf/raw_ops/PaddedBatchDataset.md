description: Creates a dataset that batches and pads batch_size elements from the input.

robots: noindex

# tf.raw_ops.PaddedBatchDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that batches and pads `batch_size` elements from the input.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PaddedBatchDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PaddedBatchDataset(
    input_dataset, batch_size, padded_shapes, padding_values, output_shapes,
    name=None
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
`padded_shapes`
</td>
<td>
A list of at least 1 `Tensor` objects with type `int64`.
A list of int64 tensors representing the desired padded shapes
of the corresponding output components. These shapes may be partially
specified, using `-1` to indicate that a particular dimension should be
padded to the maximum size of all batch elements.
</td>
</tr><tr>
<td>
`padding_values`
</td>
<td>
A list of `Tensor` objects.
A list of scalars containing the padding value to use for
each of the outputs.
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

