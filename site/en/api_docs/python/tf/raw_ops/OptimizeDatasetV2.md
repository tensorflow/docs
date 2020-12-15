description: Creates a dataset by applying related optimizations to input_dataset.

robots: noindex

# tf.raw_ops.OptimizeDatasetV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset by applying related optimizations to `input_dataset`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OptimizeDatasetV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OptimizeDatasetV2(
    input_dataset, optimizations_enabled, optimizations_disabled,
    optimizations_default, output_types, output_shapes, optimization_configs=[],
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Creates a dataset by applying related optimizations to `input_dataset`.

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
`optimizations_enabled`
</td>
<td>
A `Tensor` of type `string`.
A <a href="../../tf.md#string"><code>tf.string</code></a> vector <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> identifying user enabled optimizations.
</td>
</tr><tr>
<td>
`optimizations_disabled`
</td>
<td>
A `Tensor` of type `string`.
A <a href="../../tf.md#string"><code>tf.string</code></a> vector <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> identifying user disabled optimizations.
</td>
</tr><tr>
<td>
`optimizations_default`
</td>
<td>
A `Tensor` of type `string`.
A <a href="../../tf.md#string"><code>tf.string</code></a> vector <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> identifying optimizations by default.
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
`optimization_configs`
</td>
<td>
An optional list of `strings`. Defaults to `[]`.
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

