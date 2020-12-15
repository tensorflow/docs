description: Emits randomized records.

robots: noindex

# tf.raw_ops.RecordInput

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Emits randomized records.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.RecordInput`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.RecordInput(
    file_pattern, file_random_seed=301, file_shuffle_shift_ratio=0,
    file_buffer_size=10000, file_parallelism=16, batch_size=32, compression_type='',
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
`file_pattern`
</td>
<td>
A `string`. Glob pattern for the data files.
</td>
</tr><tr>
<td>
`file_random_seed`
</td>
<td>
An optional `int`. Defaults to `301`.
Random seeds used to produce randomized records.
</td>
</tr><tr>
<td>
`file_shuffle_shift_ratio`
</td>
<td>
An optional `float`. Defaults to `0`.
Shifts the list of files after the list is randomly
shuffled.
</td>
</tr><tr>
<td>
`file_buffer_size`
</td>
<td>
An optional `int`. Defaults to `10000`.
The randomization shuffling buffer.
</td>
</tr><tr>
<td>
`file_parallelism`
</td>
<td>
An optional `int`. Defaults to `16`.
How many sstables are opened and concurrently iterated over.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
An optional `int`. Defaults to `32`. The batch size.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
An optional `string`. Defaults to `""`.
The type of compression for the file. Currently ZLIB and
GZIP are supported. Defaults to none.
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
A `Tensor` of type `string`.
</td>
</tr>

</table>

