description: Loads a 2-D (matrix) Tensor with name old_tensor_name from the checkpoint

robots: noindex

# tf.raw_ops.LoadAndRemapMatrix

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Loads a 2-D (matrix) `Tensor` with name `old_tensor_name` from the checkpoint

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.LoadAndRemapMatrix`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.LoadAndRemapMatrix(
    ckpt_path, old_tensor_name, row_remapping, col_remapping, initializing_values,
    num_rows, num_cols, max_rows_in_memory=-1, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

at `ckpt_path` and potentially reorders its rows and columns using the
specified remappings.

Most users should use one of the wrapper initializers (such as
`tf.contrib.framework.load_and_remap_matrix_initializer`) instead of this
function directly.

The remappings are 1-D tensors with the following properties:

* `row_remapping` must have exactly `num_rows` entries. Row `i` of the output
  matrix will be initialized from the row corresponding to index
  `row_remapping[i]` in the old `Tensor` from the checkpoint.
* `col_remapping` must have either 0 entries (indicating that no column
  reordering is needed) or `num_cols` entries. If specified, column `j` of the
  output matrix will be initialized from the column corresponding to index
  `col_remapping[j]` in the old `Tensor` from the checkpoint.
* A value of -1 in either of the remappings signifies a "missing" entry. In that
  case, values from the `initializing_values` tensor will be used to fill that
  missing row or column. If `row_remapping` has `r` missing entries and
  `col_remapping` has `c` missing entries, then the following condition must be
  true:

`(r * num_cols) + (c * num_rows) - (r * c) == len(initializing_values)`

The remapping tensors can be generated using the GenerateVocabRemapping op.

As an example, with row_remapping = [1, 0, -1], col_remapping = [0, 2, -1],
initializing_values = [0.5, -0.5, 0.25, -0.25, 42], and w(i, j) representing
the value from row i, column j of the old tensor in the checkpoint, the output
matrix will look like the following:

[[w(1, 0),  w(1, 2),  0.5],
 [w(0, 0),  w(0, 2), -0.5],
 [0.25,    -0.25,      42]]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`ckpt_path`
</td>
<td>
A `Tensor` of type `string`.
Path to the TensorFlow checkpoint (version 2, `TensorBundle`) from
which the old matrix `Tensor` will be loaded.
</td>
</tr><tr>
<td>
`old_tensor_name`
</td>
<td>
A `Tensor` of type `string`.
Name of the 2-D `Tensor` to load from checkpoint.
</td>
</tr><tr>
<td>
`row_remapping`
</td>
<td>
A `Tensor` of type `int64`.
An int `Tensor` of row remappings (generally created by
`generate_vocab_remapping`).  Even if no row remapping is needed, this must
still be an index-valued Tensor (e.g. [0, 1, 2, ...]), or a shifted
index-valued `Tensor` (e.g. [8, 9, 10, ...], for partitioned `Variables`).
</td>
</tr><tr>
<td>
`col_remapping`
</td>
<td>
A `Tensor` of type `int64`.
An int `Tensor` of column remappings (generally created by
`generate_vocab_remapping`).  May be a size-0 `Tensor` if only row remapping
is to be done (e.g. column ordering is the same).
</td>
</tr><tr>
<td>
`initializing_values`
</td>
<td>
A `Tensor` of type `float32`.
A float `Tensor` containing  values to fill in for cells
in the output matrix that are not loaded from the checkpoint. Length must be
exactly the same as the number of missing / new cells.
</td>
</tr><tr>
<td>
`num_rows`
</td>
<td>
An `int` that is `>= 0`.
Number of rows (length of the 1st dimension) in the output matrix.
</td>
</tr><tr>
<td>
`num_cols`
</td>
<td>
An `int` that is `>= 1`.
Number of columns (length of the 2nd dimension) in the output matrix.
</td>
</tr><tr>
<td>
`max_rows_in_memory`
</td>
<td>
An optional `int`. Defaults to `-1`.
The maximum number of rows to load from the checkpoint at
once. If less than or equal to 0, the entire matrix will be loaded into
memory. Setting this arg trades increased disk reads for lower memory usage.
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

