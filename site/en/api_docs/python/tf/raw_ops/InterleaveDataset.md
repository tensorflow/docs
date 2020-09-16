description: Creates a dataset that applies f to the outputs of input_dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.InterleaveDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.InterleaveDataset

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
<p>`tf.compat.v1.raw_ops.InterleaveDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.InterleaveDataset(
    input_dataset, other_arguments, cycle_length, block_length, f, output_types,
    output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Unlike MapDataset, the `f` in InterleaveDataset is expected to return
a Dataset variant, and InterleaveDataset will flatten successive
results into a single Dataset. Unlike FlatMapDataset,
InterleaveDataset will interleave sequences of up to `block_length`
consecutive elements from `cycle_length` input elements.

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

