description: Convert CSV records to tensors. Each column maps to one tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.DecodeCSV" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.DecodeCSV

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Convert CSV records to tensors. Each column maps to one tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.DecodeCSV`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.DecodeCSV(
    records, record_defaults, field_delim=',', use_quote_delim=(True), na_value='',
    select_cols=[], name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

RFC 4180 format is expected for the CSV records.
(https://tools.ietf.org/html/rfc4180)
Note that we allow leading and trailing spaces with int or float field.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`records`
</td>
<td>
A `Tensor` of type `string`.
Each string is a record/row in the csv and all records should have
the same format.
</td>
</tr><tr>
<td>
`record_defaults`
</td>
<td>
A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
One tensor per column of the input record, with either a
scalar default value for that column or an empty vector if the column is
required.
</td>
</tr><tr>
<td>
`field_delim`
</td>
<td>
An optional `string`. Defaults to `","`.
char delimiter to separate fields in a record.
</td>
</tr><tr>
<td>
`use_quote_delim`
</td>
<td>
An optional `bool`. Defaults to `True`.
If false, treats double quotation marks as regular
characters inside of the string fields (ignoring RFC 4180, Section 2,
Bullet 5).
</td>
</tr><tr>
<td>
`na_value`
</td>
<td>
An optional `string`. Defaults to `""`.
Additional string to recognize as NA/NaN.
</td>
</tr><tr>
<td>
`select_cols`
</td>
<td>
An optional list of `ints`. Defaults to `[]`.
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
A list of `Tensor` objects. Has the same type as `record_defaults`.
</td>
</tr>

</table>

