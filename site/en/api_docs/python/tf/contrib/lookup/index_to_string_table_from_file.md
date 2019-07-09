

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.index_to_string_table_from_file

``` python
tf.contrib.lookup.index_to_string_table_from_file(
    vocabulary_file,
    vocab_size=None,
    default_value='UNK',
    name=None,
    key_column_index=TextFileIndex.LINE_NUMBER,
    value_column_index=TextFileIndex.WHOLE_LINE,
    delimiter='\t'
)
```



Defined in [`tensorflow/python/ops/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/lookup_ops.py).

Returns a lookup table that maps a `Tensor` of indices into strings.

This operation constructs a lookup table to map int64 indices into string
values. The table is initialized from a vocabulary file specified in
`vocabulary_file`, where the whole line is the value and the
zero-based line number is the index.

Any input which does not have a corresponding index in the vocabulary file
(an out-of-vocabulary entry) is assigned the `default_value`

The underlying table must be initialized by calling
`tf.tables_initializer.run()` or `table.init.run()` once.

To specify multi-column vocabulary files, use key_column_index and
value_column_index and delimiter.

- TextFileIndex.LINE_NUMBER means use the line number starting from zero,
  expects data type int64.
- TextFileIndex.WHOLE_LINE means use the whole line content, expects data
  type string.
- A value >=0 means use the index (starting at zero) of the split line based
  on `delimiter`.

Sample Usages:

If we have a vocabulary file "test.txt" with the following content:

```
emerson
lake
palmer
```

```python
indices = tf.constant([1, 5], tf.int64)
table = tf.contrib.lookup.index_to_string_table_from_file(
    vocabulary_file="test.txt", default_value="UNKNOWN")
values = table.lookup(indices)
...
tf.tables_initializer().run()

values.eval() ==> ["lake", "UNKNOWN"]
```

#### Args:

* <b>`vocabulary_file`</b>: The vocabulary filename, may be a constant scalar `Tensor`.
* <b>`vocab_size`</b>: Number of the elements in the vocabulary, if known.
* <b>`default_value`</b>: The value to use for out-of-vocabulary indices.
* <b>`name`</b>: A name for this op (optional).
* <b>`key_column_index`</b>: The column index from the text file to get the `key`
    values from. The default is to use the line number, starting from zero.
* <b>`value_column_index`</b>: The column index from the text file to get the `value`
    values from. The default is to use the whole line content.
* <b>`delimiter`</b>: The delimiter to separate fields in a line.


#### Returns:

The lookup table to map a string values associated to a given index `int64`
`Tensors`.


#### Raises:

* <b>`ValueError`</b>: when `vocabulary_file` is empty.
* <b>`ValueError`</b>: when `vocab_size` is invalid.