robots: noindex

# tf.raw_ops.ExperimentalCSVDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>





<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ExperimentalCSVDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ExperimentalCSVDataset(
    filenames, compression_type, buffer_size, header, field_delim, use_quote_delim,
    na_value, select_cols, record_defaults, output_shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`filenames`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`buffer_size`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`header`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`field_delim`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`use_quote_delim`
</td>
<td>
A `Tensor` of type `bool`.
</td>
</tr><tr>
<td>
`na_value`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`select_cols`
</td>
<td>
A `Tensor` of type `int64`.
</td>
</tr><tr>
<td>
`record_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
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

