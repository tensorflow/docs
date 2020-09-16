description: Convert CSV records to tensors. Each column maps to one tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.io.decode_csv" />
<meta itemprop="path" content="Stable" />
</div>

# tf.io.decode_csv

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/parsing_ops.py#L982-L1039">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Convert CSV records to tensors. Each column maps to one tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.io.decode_csv(
    records, record_defaults, field_delim=',', use_quote_delim=(True), na_value='',
    select_cols=None, name=None
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
A list of `Tensor` objects with specific types.
Acceptable types are `float32`, `float64`, `int32`, `int64`, `string`.
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
Additional string to recognize as NA/NaN.
</td>
</tr><tr>
<td>
`select_cols`
</td>
<td>
Optional sorted list of column indices to select. If specified,
only this subset of columns will be parsed and returned.
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
Each tensor will have the same shape as records.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If any of the arguments is malformed.
</td>
</tr>
</table>

