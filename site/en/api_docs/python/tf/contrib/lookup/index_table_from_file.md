page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.index_table_from_file

Returns a lookup table that converts a string tensor into int64 IDs.

``` python
tf.contrib.lookup.index_table_from_file(
    vocabulary_file=None,
    num_oov_buckets=0,
    vocab_size=None,
    default_value=-1,
    hasher_spec=tf.contrib.lookup.FastHashSpec,
    key_dtype=tf.dtypes.string,
    name=None,
    key_column_index=TextFileIndex.WHOLE_LINE,
    value_column_index=TextFileIndex.LINE_NUMBER,
    delimiter='\t'
)
```



Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->

This operation constructs a lookup table to convert tensor of strings into
int64 IDs. The mapping can be initialized from a vocabulary file specified in
`vocabulary_file`, where the whole line is the key and the zero-based line
number is the ID.

Any lookup of an out-of-vocabulary token will return a bucket ID based on its
hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
`default_value`.
The bucket ID range is
`[vocabulary size, vocabulary size + num_oov_buckets - 1]`.

The underlying table must be initialized by calling
`session.run(tf.compat.v1.tables_initializer)` or `session.run(table.init)`
once.

To specify multi-column vocabulary files, use key_column_index and
value_column_index and delimiter.

- TextFileIndex.LINE_NUMBER means use the line number starting from zero,
  expects data type int64.
- TextFileIndex.WHOLE_LINE means use the whole line content, expects data
  type string.
- A value >=0 means use the index (starting at zero) of the split line based
  on `delimiter`.

#### Sample Usages:



If we have a vocabulary file "test.txt" with the following content:

```
emerson
lake
palmer
```

```python
features = tf.constant(["emerson", "lake", "and", "palmer"])
table = tf.lookup.index_table_from_file(
    vocabulary_file="test.txt", num_oov_buckets=1)
ids = table.lookup(features)
...
tf.compat.v1.tables_initializer().run()

ids.eval()  ==> [0, 1, 3, 2]  # where 3 is the out-of-vocabulary bucket
```

#### Args:


* <b>`vocabulary_file`</b>: The vocabulary filename, may be a constant scalar `Tensor`.
* <b>`num_oov_buckets`</b>: The number of out-of-vocabulary buckets.
* <b>`vocab_size`</b>: Number of the elements in the vocabulary, if known.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
  Defaults to -1.
* <b>`hasher_spec`</b>: A `HasherSpec` to specify the hash function to use for
  assignation of out-of-vocabulary buckets.
* <b>`key_dtype`</b>: The `key` data type.
* <b>`name`</b>: A name for this op (optional).
* <b>`key_column_index`</b>: The column index from the text file to get the `key`
  values from. The default is to use the whole line content.
* <b>`value_column_index`</b>: The column index from the text file to get the `value`
  values from. The default is to use the line number, starting from zero.
* <b>`delimiter`</b>: The delimiter to separate fields in a line.


#### Returns:

The lookup table to map a `key_dtype` `Tensor` to index `int64` `Tensor`.



#### Raises:


* <b>`ValueError`</b>: If `vocabulary_file` is not set.
* <b>`ValueError`</b>: If `num_oov_buckets` is negative or `vocab_size` is not greater
  than zero.