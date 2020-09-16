description: Creates a dataset that emits the records from one or more TFRecord files.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.TFRecordDataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.TFRecordDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a dataset that emits the records from one or more TFRecord files.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.TFRecordDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.TFRecordDataset(
    filenames, compression_type, buffer_size, name=None
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
A scalar or vector containing the name(s) of the file(s) to be
read.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
A `Tensor` of type `string`.
A scalar containing either (i) the empty string (no
compression), (ii) "ZLIB", or (iii) "GZIP".
</td>
</tr><tr>
<td>
`buffer_size`
</td>
<td>
A `Tensor` of type `int64`.
A scalar representing the number of bytes to buffer. A value of
0 means no buffering will be performed.
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

