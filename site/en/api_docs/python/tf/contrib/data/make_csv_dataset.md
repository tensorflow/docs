page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.make_csv_dataset

Reads CSV files into a dataset. (deprecated)

``` python
tf.contrib.data.make_csv_dataset(
    file_pattern,
    batch_size,
    column_names=None,
    column_defaults=None,
    label_name=None,
    select_columns=None,
    field_delim=',',
    use_quote_delim=True,
    na_value='',
    header=True,
    num_epochs=None,
    shuffle=True,
    shuffle_buffer_size=10000,
    shuffle_seed=None,
    prefetch_buffer_size=optimization.AUTOTUNE,
    num_parallel_reads=1,
    sloppy=False,
    num_rows_for_inference=100,
    compression_type=None
)
```



Defined in [`contrib/data/python/ops/readers.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/readers.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/make_csv_dataset"><code>tf.data.experimental.make_csv_dataset(...)</code></a>.

Reads CSV files into a dataset, where each element is a (features, labels)
tuple that corresponds to a batch of CSV rows. The features dictionary
maps feature column names to `Tensor`s containing the corresponding
feature data, and labels is a `Tensor` containing the batch's label data.

#### Args:


* <b>`file_pattern`</b>: List of files or patterns of file paths containing CSV
  records. See <a href="../../../tf/io/gfile/glob"><code>tf.io.gfile.glob</code></a> for pattern rules.
* <b>`batch_size`</b>: An int representing the number of records to combine
  in a single batch.
* <b>`column_names`</b>: An optional list of strings that corresponds to the CSV
  columns, in order. One per column of the input record. If this is not
  provided, infers the column names from the first row of the records.
  These names will be the keys of the features dict of each dataset element.
* <b>`column_defaults`</b>: A optional list of default values for the CSV fields. One
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
* <b>`label_name`</b>: A optional string corresponding to the label column. If
  provided, the data for this column is returned as a separate `Tensor` from
  the features dictionary, so that the dataset complies with the format
  expected by a `tf.Estimator.train` or `tf.Estimator.evaluate` input
  function.
* <b>`select_columns`</b>: An optional list of integer indices or string column
  names, that specifies a subset of columns of CSV data to select. If
  column names are provided, these must correspond to names provided in
  `column_names` or inferred from the file header lines. When this argument
  is specified, only a subset of CSV columns will be parsed and returned,
  corresponding to the columns specified. Using this results in faster
  parsing and lower memory usage. If both this and `column_defaults` are
  specified, these must have the same lengths, and `column_defaults` is
  assumed to be sorted in order of increasing column index.
* <b>`field_delim`</b>: An optional `string`. Defaults to `","`. Char delimiter to
  separate fields in a record.
* <b>`use_quote_delim`</b>: An optional bool. Defaults to `True`. If false, treats
  double quotation marks as regular characters inside of the string fields.
* <b>`na_value`</b>: Additional string to recognize as NA/NaN.
* <b>`header`</b>: A bool that indicates whether the first rows of provided CSV files
  correspond to header lines with column names, and should not be included
  in the data.
* <b>`num_epochs`</b>: An int specifying the number of times this dataset is repeated.
  If None, cycles through the dataset forever.
* <b>`shuffle`</b>: A bool that indicates whether the input should be shuffled.
* <b>`shuffle_buffer_size`</b>: Buffer size to use for shuffling. A large buffer size
  ensures better shuffling, but increases memory usage and startup time.
* <b>`shuffle_seed`</b>: Randomization seed to use for shuffling.
* <b>`prefetch_buffer_size`</b>: An int specifying the number of feature
  batches to prefetch for performance improvement. Recommended value is the
  number of batches consumed per training step. Defaults to auto-tune.
* <b>`num_parallel_reads`</b>: Number of threads used to read CSV records from files.
  If >1, the results will be interleaved.
* <b>`sloppy`</b>: If `True`, reading performance will be improved at
  the cost of non-deterministic ordering. If `False`, the order of elements
  produced is deterministic prior to shuffling (elements are still
  randomized if `shuffle=True`. Note that if the seed is set, then order
  of elements after shuffling is deterministic). Defaults to `False`.
* <b>`num_rows_for_inference`</b>: Number of rows of a file to use for type inference
  if record_defaults is not provided. If None, reads all the rows of all
  the files. Defaults to 100.
* <b>`compression_type`</b>: (Optional.) A <a href="../../../tf#string"><code>tf.string</code></a> scalar evaluating to one of
  `""` (no compression), `"ZLIB"`, or `"GZIP"`. Defaults to no compression.


#### Returns:

A dataset, where each element is a (features, labels) tuple that corresponds
to a batch of `batch_size` CSV rows. The features dictionary maps feature
column names to `Tensor`s containing the corresponding column data, and
labels is a `Tensor` containing the column data for the label column
specified by `label_name`.



#### Raises:


* <b>`ValueError`</b>: If any of the arguments is malformed.