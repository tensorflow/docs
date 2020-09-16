description: Writes the given dataset to the given file using the TFRecord format.

robots: noindex

# tf.raw_ops.DatasetToTFRecord

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Writes the given dataset to the given file using the TFRecord format.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DatasetToTFRecord`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DatasetToTFRecord(
    input_dataset, filename, compression_type, name=None
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
A variant tensor representing the dataset to write.
</td>
</tr><tr>
<td>
`filename`
</td>
<td>
A `Tensor` of type `string`.
A scalar string tensor representing the filename to use.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
A `Tensor` of type `string`.
A scalar string tensor containing either (i) the empty string (no
compression), (ii) "ZLIB", or (iii) "GZIP".
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
The created Operation.
</td>
</tr>

</table>

