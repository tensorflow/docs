description: Creates a dataset that asynchronously prefetches elements from input_dataset.

robots: noindex

# tf.raw_ops.PrefetchDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that asynchronously prefetches elements from `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.PrefetchDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.PrefetchDataset(
    input_dataset, buffer_size, output_types, output_shapes, slack_period=0,
    legacy_autotune=(True), buffer_size_min=0, name=None
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
`buffer_size`
</td>
<td>
A `Tensor` of type `int64`.
The maximum number of elements to buffer in an iterator over
this dataset.
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
`slack_period`
</td>
<td>
An optional `int`. Defaults to `0`.
</td>
</tr><tr>
<td>
`legacy_autotune`
</td>
<td>
An optional `bool`. Defaults to `True`.
</td>
</tr><tr>
<td>
`buffer_size_min`
</td>
<td>
An optional `int`. Defaults to `0`.
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

