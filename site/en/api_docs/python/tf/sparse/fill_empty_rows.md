description: Fills empty rows in the input 2-D SparseTensor with a default value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.sparse.fill_empty_rows" />
<meta itemprop="path" content="Stable" />
</div>

# tf.sparse.fill_empty_rows

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/sparse_ops.py#L1874-L1938">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Fills empty rows in the input 2-D `SparseTensor` with a default value.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.sparse.fill_empty_rows`, `tf.compat.v1.sparse_fill_empty_rows`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.sparse.fill_empty_rows(
    sp_input, default_value, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This op adds entries with the specified `default_value` at index
`[row, 0]` for any row in the input that does not already have a value.

For example, suppose `sp_input` has shape `[5, 6]` and non-empty values:

    [0, 1]: a
    [0, 3]: b
    [2, 0]: c
    [3, 1]: d

Rows 1 and 4 are empty, so the output will be of shape `[5, 6]` with values:

    [0, 1]: a
    [0, 3]: b
    [1, 0]: default_value
    [2, 0]: c
    [3, 1]: d
    [4, 0]: default_value

Note that the input may have empty columns at the end, with no effect on
this op.

The output `SparseTensor` will be in row-major order and will have the
same shape as the input.

This op also returns an indicator vector such that

    empty_row_indicator[i] = True iff row i was an empty row.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`sp_input`
</td>
<td>
A `SparseTensor` with shape `[N, M]`.
</td>
</tr><tr>
<td>
`default_value`
</td>
<td>
The value to fill for empty rows, with the same type as
`sp_input.`
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name prefix for the returned tensors (optional)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`sp_ordered_output`
</td>
<td>
A `SparseTensor` with shape `[N, M]`, and with all empty
rows filled in with `default_value`.
</td>
</tr><tr>
<td>
`empty_row_indicator`
</td>
<td>
A bool vector of length `N` indicating whether each
input row was empty.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `sp_input` is not a `SparseTensor`.
</td>
</tr>
</table>

