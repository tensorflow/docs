

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.TextFileIdTableInitializer

## Class `TextFileIdTableInitializer`

Inherits From: [`TextFileInitializer`](../../../tf/contrib/lookup/TextFileInitializer)



Defined in [`tensorflow/python/ops/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/lookup_ops.py).

Table initializer for string to `int64` IDs tables from a text file.

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
    key_column_index=TextFileIndex.WHOLE_LINE,
    value_column_index=TextFileIndex.LINE_NUMBER,
    vocab_size=None,
    delimiter='\t',
    name='text_file_id_table_init',
    key_dtype=tf.string
)
```

Constructs an initializer for an string-to-id table from a text file.

It populates a table that its key and value types are string and int64,
respectively. It generates one key-value pair per line.
The content of the key and value are specified by the key_index
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
* <b>`key_column_index`</b>: The column index from the text file to get the `key`
    values from. The default is to use the whole line content.
* <b>`value_column_index`</b>: The column index from the text file to get the `value`
    values from. The default is to use the line number, starting from zero.
* <b>`vocab_size`</b>: The number of elements in the file, if known.
* <b>`delimiter`</b>: The delimiter to separate fields in a line.
* <b>`name`</b>: Optional name for the op.
* <b>`key_dtype`</b>: The `key` data type.


#### Raises:

* <b>`TypeError`</b>: when the filename is empty, or when the table key and value
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



