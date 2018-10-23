

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.lookup.TextFileInitializer

### `class tf.contrib.lookup.TextFileInitializer`



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/lookup/lookup_ops.py).

Table initializers from a text file.

This initializer assigns one entry in the table for each line in the file.

The key and value type of the table to initialize is given by `key_dtype` and
`value_dtype`.

The key and value content to get from each line is specified by
the `key_index` and `value_index`.
  - TextFileIndex.LINE_NUMBER means use the line number starting from zero,
    expects data type int64.
  - TextFileIndex.WHOLE_LINE means use the whole line content, expects data
    type string.
  - A value >=0 means use the index (starting at zero) of the split line based
    on `delimiter`.

For example if we have a file with the following content:

```
emerson 10
lake 20
palmer 30
```

The following snippet initializes a table with the first column as keys and
second column as values:
- emerson -> 10
- lake -> 20
- palmer -> 30

```python
table = tf.contrib.lookup.HashTable(tf.contrib.lookup.TextFileInitializer(
    "test.txt", tf.string, 0, tf.int64, 1, delimiter=" "), -1)
...
table.init.run()
```

Similarly to initialize the whole line as keys and the line number as values.
- emerson 10 -> 0
- lake 20 -> 1
- palmer 30 -> 2

```python
table = tf.contrib.lookup.HashTable(tf.contrib.lookup.TextFileInitializer(
    "test.txt", tf.string, tf.contrib.lookup.TextFileIndex.WHOLE_LINE,
    tf.int64, tf.contrib.lookup.TextFileIndex.LINE_NUMBER, delimiter=" "), -1)
...
table.init.run()
```

## Properties

<h3 id="key_dtype"><code>key_dtype</code></h3>

The expected table key dtype.

<h3 id="value_dtype"><code>value_dtype</code></h3>

The expected table value dtype.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    filename,
    key_dtype,
    key_index,
    value_dtype,
    value_index,
    vocab_size=None,
    delimiter='\t',
    name=None
)
```

Constructs a table initializer object to populate from a text file.

It generates one key-value pair per line. The type of table key and
value are specified by `key_dtype` and `value_dtype`, respectively.
Similarly the content of the key and value are specified by the key_index
and value_index.

- TextFileIndex.LINE_NUMBER means use the line number starting from zero,
  expects data type int64.
- TextFileIndex.WHOLE_LINE means use the whole line content, expects data
  type string.
- A value >=0 means use the index (starting at zero) of the split line based
  on `delimiter`.

#### Args:

* <b>`filename`</b>: The filename of the text file to be used for initialization.
    The path must be accessible from wherever the graph is initialized
    (eg. trainer or eval workers). The filename may be a scalar `Tensor`.
* <b>`key_dtype`</b>: The `key` data type.
* <b>`key_index`</b>: the index that represents information of a line to get the
    table 'key' values from.
* <b>`value_dtype`</b>: The `value` data type.
* <b>`value_index`</b>: the index that represents information of a line to get the
    table 'value' values from.'
* <b>`vocab_size`</b>: The number of elements in the file, if known.
* <b>`delimiter`</b>: The delimiter to separate fields in a line.
* <b>`name`</b>: A name for the operation (optional).


#### Raises:

* <b>`ValueError`</b>: when the filename is empty, or when the table key and value
  data types do not match the expected data types.

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(table)
```

Initializes the table from a text file.

#### Args:

* <b>`table`</b>: The table to be initialized.


#### Returns:

  The operation that initializes the table.


#### Raises:

* <b>`TypeError`</b>: when the keys and values data types do not match the table
  key and value data types.



