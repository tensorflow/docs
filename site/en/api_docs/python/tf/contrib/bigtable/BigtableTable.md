page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.bigtable.BigtableTable

## Class `BigtableTable`

Entry point for reading and writing data in Cloud Bigtable.



### Aliases:

* Class `tf.contrib.bigtable.BigtableTable`
* Class `tf.contrib.cloud.BigtableTable`



Defined in [`contrib/bigtable/python/ops/bigtable_api.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/bigtable/python/ops/bigtable_api.py).

<!-- Placeholder for "Used in" -->

This BigtableTable class is the Python representation of the Cloud Bigtable
table within TensorFlow. Methods on this class allow data to be read from and
written to the Cloud Bigtable service in flexible and high performance
manners.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    snapshot,
    resource
)
```






## Methods

<h3 id="keys_by_prefix_dataset"><code>keys_by_prefix_dataset</code></h3>

``` python
keys_by_prefix_dataset(prefix)
```

Retrieves the row keys matching a given prefix.


#### Args:


* <b>`prefix`</b>: All row keys that begin with `prefix` in the table will be
  retrieved.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>. containing <a href="../../../tf#string"><code>tf.string</code></a> Tensors corresponding to all
of the row keys matching that prefix.


<h3 id="keys_by_range_dataset"><code>keys_by_range_dataset</code></h3>

``` python
keys_by_range_dataset(
    start,
    end
)
```

Retrieves all row keys between start and end.

Note: it does NOT retrieve the values of columns.

#### Args:


* <b>`start`</b>: The start row key. The row keys for rows after start (inclusive)
  will be retrieved.
* <b>`end`</b>: (Optional.) The end row key. Rows up to (but not including) end will
  be retrieved. If end is None, all subsequent row keys will be retrieved.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> containing <a href="../../../tf#string"><code>tf.string</code></a> Tensors corresponding to all
of the row keys between `start` and `end`.


<h3 id="lookup_columns"><code>lookup_columns</code></h3>

``` python
lookup_columns(
    *args,
    **kwargs
)
```

Retrieves the values of columns for a dataset of keys.


#### Example usage:



```python
table = bigtable_client.table("my_table")
key_dataset = table.get_keys_prefix("imagenet")
images = key_dataset.apply(table.lookup_columns(("cf1", "image"),
                                                ("cf2", "label"),
                                                ("cf2", "boundingbox")))
training_data = images.map(parse_and_crop, num_parallel_calls=64).batch(128)
```

Alternatively, you can use keyword arguments to specify the columns to
capture. Example (same as above, rewritten):

```python
table = bigtable_client.table("my_table")
key_dataset = table.get_keys_prefix("imagenet")
images = key_dataset.apply(table.lookup_columns(
    cf1="image", cf2=("label", "boundingbox")))
training_data = images.map(parse_and_crop, num_parallel_calls=64).batch(128)
```

Note: certain `kwargs` keys are reserved, and thus, some column families
cannot be identified using the `kwargs` syntax. Instead, please use the
`args` syntax. This list includes:

  - 'name'

Note: this list can change at any time.

#### Args:


* <b>`*args`</b>: A list of tuples containing (column family, column name) pairs.
* <b>`**kwargs`</b>: Column families (keys) and column qualifiers (values).


#### Returns:

A function that can be passed to <a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a> to retrieve the
values of columns for the rows.


<h3 id="parallel_scan_prefix"><code>parallel_scan_prefix</code></h3>

``` python
parallel_scan_prefix(
    prefix,
    num_parallel_scans=None,
    probability=None,
    columns=None,
    **kwargs
)
```

Retrieves row (including values) from the Bigtable service at high speed.

Rows with row-key prefixed by `prefix` will be retrieved. This method is
similar to `scan_prefix`, but by contrast performs multiple sub-scans in
parallel in order to achieve higher performance.

Note: The dataset produced by this method is not deterministic!

Specifying the columns to retrieve for each row is done by either using
kwargs or in the columns parameter. To retrieve values of the columns "c1",
and "c2" from the column family "cfa", and the value of the column "c3"
from column family "cfb", the following datasets (`ds1`, and `ds2`) are
equivalent:

```
table = # ...
ds1 = table.parallel_scan_prefix("row_prefix", columns=[("cfa", "c1"),
                                                        ("cfa", "c2"),
                                                        ("cfb", "c3")])
ds2 = table.parallel_scan_prefix("row_prefix", cfa=["c1", "c2"], cfb="c3")
```

Note: only the latest value of a cell will be retrieved.

#### Args:


* <b>`prefix`</b>: The prefix all row keys must match to be retrieved for prefix-
  based scans.
* <b>`num_parallel_scans`</b>: (Optional.) The number of concurrent scans against the
  Cloud Bigtable instance.
* <b>`probability`</b>: (Optional.) A float between 0 (exclusive) and 1 (inclusive).
  A non-1 value indicates to probabilistically sample rows with the
  provided probability.
* <b>`columns`</b>: The columns to read. Note: most commonly, they are expressed as
  kwargs. Use the columns value if you are using column families that are
  reserved. The value of columns and kwargs are merged. Columns is a list
  of tuples of strings ("column_family", "column_qualifier").
* <b>`**kwargs`</b>: The column families and columns to read. Keys are treated as
  column_families, and values can be either lists of strings, or strings
  that are treated as the column qualifier (column name).


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returning the row keys and the cell contents.



#### Raises:


* <b>`ValueError`</b>: If the configured probability is unexpected.

<h3 id="parallel_scan_range"><code>parallel_scan_range</code></h3>

``` python
parallel_scan_range(
    start,
    end,
    num_parallel_scans=None,
    probability=None,
    columns=None,
    **kwargs
)
```

Retrieves rows (including values) from the Bigtable service.

Rows with row-keys between `start` and `end` will be retrieved. This method
is similar to `scan_range`, but by contrast performs multiple sub-scans in
parallel in order to achieve higher performance.

Note: The dataset produced by this method is not deterministic!

Specifying the columns to retrieve for each row is done by either using
kwargs or in the columns parameter. To retrieve values of the columns "c1",
and "c2" from the column family "cfa", and the value of the column "c3"
from column family "cfb", the following datasets (`ds1`, and `ds2`) are
equivalent:

```
table = # ...
ds1 = table.parallel_scan_range("row_start",
                                "row_end",
                                columns=[("cfa", "c1"),
                                         ("cfa", "c2"),
                                         ("cfb", "c3")])
ds2 = table.parallel_scan_range("row_start", "row_end",
                                cfa=["c1", "c2"], cfb="c3")
```

Note: only the latest value of a cell will be retrieved.

#### Args:


* <b>`start`</b>: The start of the range when scanning by range.
* <b>`end`</b>: (Optional.) The end of the range when scanning by range.
* <b>`num_parallel_scans`</b>: (Optional.) The number of concurrent scans against the
  Cloud Bigtable instance.
* <b>`probability`</b>: (Optional.) A float between 0 (exclusive) and 1 (inclusive).
  A non-1 value indicates to probabilistically sample rows with the
  provided probability.
* <b>`columns`</b>: The columns to read. Note: most commonly, they are expressed as
  kwargs. Use the columns value if you are using column families that are
  reserved. The value of columns and kwargs are merged. Columns is a list
  of tuples of strings ("column_family", "column_qualifier").
* <b>`**kwargs`</b>: The column families and columns to read. Keys are treated as
  column_families, and values can be either lists of strings, or strings
  that are treated as the column qualifier (column name).


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returning the row keys and the cell contents.



#### Raises:


* <b>`ValueError`</b>: If the configured probability is unexpected.

<h3 id="sample_keys"><code>sample_keys</code></h3>

``` python
sample_keys()
```

Retrieves a sampling of row keys from the Bigtable table.

This dataset is most often used in conjunction with
<a href="../../../tf/data/experimental/parallel_interleave"><code>tf.data.experimental.parallel_interleave</code></a> to construct a set of ranges for
scanning in parallel.

#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returning string row keys.


<h3 id="scan_prefix"><code>scan_prefix</code></h3>

``` python
scan_prefix(
    prefix,
    probability=None,
    columns=None,
    **kwargs
)
```

Retrieves row (including values) from the Bigtable service.

Rows with row-key prefixed by `prefix` will be retrieved.

Specifying the columns to retrieve for each row is done by either using
kwargs or in the columns parameter. To retrieve values of the columns "c1",
and "c2" from the column family "cfa", and the value of the column "c3"
from column family "cfb", the following datasets (`ds1`, and `ds2`) are
equivalent:

```
table = # ...
ds1 = table.scan_prefix("row_prefix", columns=[("cfa", "c1"),
                                               ("cfa", "c2"),
                                               ("cfb", "c3")])
ds2 = table.scan_prefix("row_prefix", cfa=["c1", "c2"], cfb="c3")
```

Note: only the latest value of a cell will be retrieved.

#### Args:


* <b>`prefix`</b>: The prefix all row keys must match to be retrieved for prefix-
  based scans.
* <b>`probability`</b>: (Optional.) A float between 0 (exclusive) and 1 (inclusive).
  A non-1 value indicates to probabilistically sample rows with the
  provided probability.
* <b>`columns`</b>: The columns to read. Note: most commonly, they are expressed as
  kwargs. Use the columns value if you are using column families that are
  reserved. The value of columns and kwargs are merged. Columns is a list
  of tuples of strings ("column_family", "column_qualifier").
* <b>`**kwargs`</b>: The column families and columns to read. Keys are treated as
  column_families, and values can be either lists of strings, or strings
  that are treated as the column qualifier (column name).


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returning the row keys and the cell contents.



#### Raises:


* <b>`ValueError`</b>: If the configured probability is unexpected.

<h3 id="scan_range"><code>scan_range</code></h3>

``` python
scan_range(
    start,
    end,
    probability=None,
    columns=None,
    **kwargs
)
```

Retrieves rows (including values) from the Bigtable service.

Rows with row-keys between `start` and `end` will be retrieved.

Specifying the columns to retrieve for each row is done by either using
kwargs or in the columns parameter. To retrieve values of the columns "c1",
and "c2" from the column family "cfa", and the value of the column "c3"
from column family "cfb", the following datasets (`ds1`, and `ds2`) are
equivalent:

```
table = # ...
ds1 = table.scan_range("row_start", "row_end", columns=[("cfa", "c1"),
                                                        ("cfa", "c2"),
                                                        ("cfb", "c3")])
ds2 = table.scan_range("row_start", "row_end", cfa=["c1", "c2"], cfb="c3")
```

Note: only the latest value of a cell will be retrieved.

#### Args:


* <b>`start`</b>: The start of the range when scanning by range.
* <b>`end`</b>: (Optional.) The end of the range when scanning by range.
* <b>`probability`</b>: (Optional.) A float between 0 (exclusive) and 1 (inclusive).
  A non-1 value indicates to probabilistically sample rows with the
  provided probability.
* <b>`columns`</b>: The columns to read. Note: most commonly, they are expressed as
  kwargs. Use the columns value if you are using column families that are
  reserved. The value of columns and kwargs are merged. Columns is a list
  of tuples of strings ("column_family", "column_qualifier").
* <b>`**kwargs`</b>: The column families and columns to read. Keys are treated as
  column_families, and values can be either lists of strings, or strings
  that are treated as the column qualifier (column name).


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> returning the row keys and the cell contents.



#### Raises:


* <b>`ValueError`</b>: If the configured probability is unexpected.

<h3 id="write"><code>write</code></h3>

``` python
write(
    dataset,
    column_families,
    columns,
    timestamp=None
)
```

Writes a dataset to the table.


#### Args:


* <b>`dataset`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> to be written to this table. It must produce
  a list of number-of-columns+1 elements, all of which must be strings.
  The first value will be used as the row key, and subsequent values will
  be used as cell values for the corresponding columns from the
  corresponding column_families and columns entries.
* <b>`column_families`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of <a href="../../../tf#string"><code>tf.string</code></a>s corresponding to the
  column names to store the dataset's elements into.
* <b>`columns`</b>: A <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of <a href="../../../tf#string"><code>tf.string</code></a>s corresponding to the column names
  to store the dataset's elements into.
* <b>`timestamp`</b>: (Optional.) An int64 timestamp to write all the values at.
  Leave as None to use server-provided timestamps.


#### Returns:

A <a href="../../../tf/Operation"><code>tf.Operation</code></a> that can be run to perform the write.



#### Raises:


* <b>`ValueError`</b>: If there are unexpected or incompatible types, or if the
  number of columns and column_families does not match the output of
  `dataset`.



