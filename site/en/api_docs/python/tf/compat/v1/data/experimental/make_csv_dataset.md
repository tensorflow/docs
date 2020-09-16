description: Reads CSV files into a dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.experimental.make_csv_dataset" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.data.experimental.make_csv_dataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/data/experimental/ops/readers.py#L561-L589">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Reads CSV files into a dataset.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.data.experimental.make_csv_dataset(
    file_pattern, batch_size, column_names=None, column_defaults=None,
    label_name=None, select_columns=None, field_delim=',', use_quote_delim=(True),
    na_value='', header=(True), num_epochs=None, shuffle=(True),
    shuffle_buffer_size=10000, shuffle_seed=None, prefetch_buffer_size=None,
    num_parallel_reads=None, sloppy=(False), num_rows_for_inference=100,
    compression_type=None, ignore_errors=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Reads CSV files into a dataset, where each element is a (features, labels)
tuple that corresponds to a batch of CSV rows. The features dictionary
maps feature column names to `Tensor`s containing the corresponding
feature data, and labels is a `Tensor` containing the batch's label data.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`file_pattern`
</td>
<td>
List of files or patterns of file paths containing CSV
records. See <a href="../../../../../tf/io/gfile/glob.md"><code>tf.io.gfile.glob</code></a> for pattern rules.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
An int representing the number of records to combine
in a single batch.
</td>
</tr><tr>
<td>
`column_names`
</td>
<td>
An optional list of strings that corresponds to the CSV
columns, in order. One per column of the input record. If this is not
provided, infers the column names from the first row of the records.
These names will be the keys of the features dict of each dataset element.
</td>
</tr><tr>
<td>
`column_defaults`
</td>
<td>
A optional list of default values for the CSV fields. One
item per selected column of the input record. Each item in the list is
either a valid CSV dtype (float32, float64, int32, int64, or string), or a
`Tensor` with one of the aforementioned types. The tensor can either be
a scalar default value (if the column is optional), or an empty tensor (if
the column is required). If a dtype is provided instead of a tensor, the
column is also treated as required. If this list is not provided, tries
to infer types based on reading the first num_rows_for_inference rows of
files specified, and assumes all columns are optional, defaulting to `0`
for numeric values and `""` for string values. If both this and
`select_columns` are specified, these must have the same lengths, and
`column_defaults` is assumed to be sorted in order of increasing column
index.
</td>
</tr><tr>
<td>
`label_name`
</td>
<td>
A optional string corresponding to the label column. If
provided, the data for this column is returned as a separate `Tensor` from
the features dictionary, so that the dataset complies with the format
expected by a `tf.Estimator.train` or `tf.Estimator.evaluate` input
function.
</td>
</tr><tr>
<td>
`select_columns`
</td>
<td>
An optional list of integer indices or string column
names, that specifies a subset of columns of CSV data to select. If
column names are provided, these must correspond to names provided in
`column_names` or inferred from the file header lines. When this argument
is specified, only a subset of CSV columns will be parsed and returned,
corresponding to the columns specified. Using this results in faster
parsing and lower memory usage. If both this and `column_defaults` are
specified, these must have the same lengths, and `column_defaults` is
assumed to be sorted in order of increasing column index.
</td>
</tr><tr>
<td>
`field_delim`
</td>
<td>
An optional `string`. Defaults to `","`. Char delimiter to
separate fields in a record.
</td>
</tr><tr>
<td>
`use_quote_delim`
</td>
<td>
An optional bool. Defaults to `True`. If false, treats
double quotation marks as regular characters inside of the string fields.
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
`header`
</td>
<td>
A bool that indicates whether the first rows of provided CSV files
correspond to header lines with column names, and should not be included
in the data.
</td>
</tr><tr>
<td>
`num_epochs`
</td>
<td>
An int specifying the number of times this dataset is repeated.
If None, cycles through the dataset forever.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
A bool that indicates whether the input should be shuffled.
</td>
</tr><tr>
<td>
`shuffle_buffer_size`
</td>
<td>
Buffer size to use for shuffling. A large buffer size
ensures better shuffling, but increases memory usage and startup time.
</td>
</tr><tr>
<td>
`shuffle_seed`
</td>
<td>
Randomization seed to use for shuffling.
</td>
</tr><tr>
<td>
`prefetch_buffer_size`
</td>
<td>
An int specifying the number of feature
batches to prefetch for performance improvement. Recommended value is the
number of batches consumed per training step. Defaults to auto-tune.
</td>
</tr><tr>
<td>
`num_parallel_reads`
</td>
<td>
Number of threads used to read CSV records from files.
If >1, the results will be interleaved. Defaults to `1`.
</td>
</tr><tr>
<td>
`sloppy`
</td>
<td>
If `True`, reading performance will be improved at
the cost of non-deterministic ordering. If `False`, the order of elements
produced is deterministic prior to shuffling (elements are still
randomized if `shuffle=True`. Note that if the seed is set, then order
of elements after shuffling is deterministic). Defaults to `False`.
</td>
</tr><tr>
<td>
`num_rows_for_inference`
</td>
<td>
Number of rows of a file to use for type inference
if record_defaults is not provided. If None, reads all the rows of all
the files. Defaults to 100.
</td>
</tr><tr>
<td>
`compression_type`
</td>
<td>
(Optional.) A <a href="../../../../../tf.md#string"><code>tf.string</code></a> scalar evaluating to one of
`""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no compression.
</td>
</tr><tr>
<td>
`ignore_errors`
</td>
<td>
(Optional.) If `True`, ignores errors with CSV file parsing,
such as malformed data or empty lines, and moves on to the next valid
CSV record. Otherwise, the dataset raises an error and stops processing
when encountering any invalid records. Defaults to `False`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A dataset, where each element is a (features, labels) tuple that corresponds
to a batch of `batch_size` CSV rows. The features dictionary maps feature
column names to `Tensor`s containing the corresponding column data, and
labels is a `Tensor` containing the column data for the label column
specified by `label_name`.
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

