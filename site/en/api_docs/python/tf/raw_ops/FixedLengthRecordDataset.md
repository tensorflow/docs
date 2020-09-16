description: Creates a dataset that emits the records from one or more binary files.

robots: noindex

# tf.raw_ops.FixedLengthRecordDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that emits the records from one or more binary files.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.FixedLengthRecordDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.FixedLengthRecordDataset(
    filenames, header_bytes, record_bytes, footer_bytes, buffer_size, name=None
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
A scalar or a vector containing the name(s) of the file(s) to be
read.
</td>
</tr><tr>
<td>
`header_bytes`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of bytes to skip at the
beginning of a file.
</td>
</tr><tr>
<td>
`record_bytes`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of bytes in each record.
</td>
</tr><tr>
<td>
`footer_bytes`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of bytes to skip at the end
of a file.
</td>
</tr><tr>
<td>
`buffer_size`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of bytes to buffer. Must be > 0.
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

