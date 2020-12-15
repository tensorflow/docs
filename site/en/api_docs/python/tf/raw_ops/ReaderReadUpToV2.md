description: Returns up to num_records (key, value) pairs produced by a Reader.

robots: noindex

# tf.raw_ops.ReaderReadUpToV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns up to `num_records` (key, value) pairs produced by a Reader.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.ReaderReadUpToV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.ReaderReadUpToV2(
    reader_handle, queue_handle, num_records, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Will dequeue from the input queue if necessary (e.g. when the
Reader needs to start reading from a new file since it has finished
with the previous file).
It may return less than `num_records` even before the last batch.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`reader_handle`
</td>
<td>
A `Tensor` of type `resource`. Handle to a `Reader`.
</td>
</tr><tr>
<td>
`queue_handle`
</td>
<td>
A `Tensor` of type `resource`.
Handle to a `Queue`, with string work items.
</td>
</tr><tr>
<td>
`num_records`
</td>
<td>
A `Tensor` of type `int64`.
number of records to read from `Reader`.
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
A tuple of `Tensor` objects (keys, values).
</td>
</tr>
<tr>
<td>
`keys`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`values`
</td>
<td>
A `Tensor` of type `string`.
</td>
</tr>
</table>

