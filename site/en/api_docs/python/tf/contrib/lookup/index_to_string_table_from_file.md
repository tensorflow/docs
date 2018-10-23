


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.lookup.index_to_string_table_from_file

### `tf.contrib.lookup.index_to_string_table_from_file`

```
tf.contrib.lookup.index_to_string_table_from_file(vocabulary_file, vocab_size=None, default_value='UNK', name=None)
```


Returns a lookup table that maps a `Tensor` of indices into strings.

This operation constructs a lookup table to map int64 indices into string
values. The table is initialized from a vocabulary file specified in
`vocabulary_file`, where the whole line is the value and the
zero-based line number is the index.

Any input which does not have a corresponding index in the vocabulary file
(an out-of-vocabulary entry) is assigned the `default_value`

The underlying table must be initialized by calling
`tf.tables_initializer.run()` or `table.init.run()` once.

Sample Usages:

If we have a vocabulary file "test.txt" with the following content:

```
emerson
lake
palmer
```

```python
indices = tf.constant([1, 5], tf.int64)
table = tf.contrib.lookup.index_to_string_from_file(
    vocabulary_file="test.txt", default_value="UNKNOWN")
values = table.lookup(indices)
...
tf.tables_initializer().run()

values.eval() ==> ["lake", "UNKNOWN"]
```

#### Args:

* <b>`vocabulary_file`</b>: The vocabulary filename.
* <b>`vocab_size`</b>: Number of the elements in the vocabulary, if known.
* <b>`default_value`</b>: The value to use for out-of-vocabulary indices.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

  The lookup table to map a string values associated to a given index `int64`
  `Tensors`.


#### Raises:

* <b>`ValueError`</b>: when `vocabulary_file` is empty.
* <b>`ValueError`</b>: when `vocab_size` is invalid.

Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/lookup/lookup_ops.py).

