description: Initializes a table from a text file.

robots: noindex

# tf.raw_ops.InitializeTableFromTextFile

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Initializes a table from a text file.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.InitializeTableFromTextFile`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.InitializeTableFromTextFile(
    table_handle, filename, key_index, value_index, vocab_size=-1, delimiter='\t',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

It inserts one key-value pair into the table for each line of the file.
The key and value is extracted from the whole line content, elements from the
split line based on `delimiter` or the line number (starting from zero).
Where to extract the key and value from a line is specified by `key_index` and
`value_index`.

- A value of -1 means use the line number(starting from zero), expects `int64`.
- A value of -2 means use the whole line content, expects `string`.
- A value >= 0 means use the index (starting at zero) of the split line based
  on `delimiter`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`table_handle`
</td>
<td>
A `Tensor` of type mutable `string`.
Handle to a table which will be initialized.
</td>
</tr><tr>
<td>
`filename`
</td>
<td>
A `Tensor` of type `string`. Filename of a vocabulary text file.
</td>
</tr><tr>
<td>
`key_index`
</td>
<td>
An `int` that is `>= -2`.
Column index in a line to get the table `key` values from.
</td>
</tr><tr>
<td>
`value_index`
</td>
<td>
An `int` that is `>= -2`.
Column index that represents information of a line to get the table
`value` values from.
</td>
</tr><tr>
<td>
`vocab_size`
</td>
<td>
An optional `int` that is `>= -1`. Defaults to `-1`.
Number of elements of the file, use -1 if unknown.
</td>
</tr><tr>
<td>
`delimiter`
</td>
<td>
An optional `string`. Defaults to `"\t"`.
Delimiter to separate fields in a line.
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

