

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lookup.index_table_from_file

### `tf.contrib.lookup.index_table_from_file`

``` python
index_table_from_file(
    vocabulary_file=None,
    num_oov_buckets=0,
    vocab_size=None,
    default_value=-1,
    hasher_spec=tf.contrib.lookup.FastHashSpec,
    key_dtype=tf.string,
    name=None
)
```



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/lookup/lookup_ops.py).

Returns a lookup table that converts a string tensor into int64 IDs.

This operation constructs a lookup table to convert tensor of strings into
int64 IDs. The mapping can be initialized from a vocabulary file specified in
`vocabulary_file`, where the whole line is the key and the zero-based line
number is the ID.

Any lookup of an out-of-vocabulary token will return a bucket ID based on its
hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
`default_value`.
The bucket ID range is `[vocabulary size, vocabulary size + num_oov_buckets]`.

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
features = tf.constant(["emerson", "lake", "and", "palmer"])
table = tf.contrib.lookup.index_table_from_file(
    vocabulary_file="test.txt", num_oov_buckets=1)
ids = table.lookup(features)
...
tf.tables_initializer().run()

ids.eval()  ==> [0, 1, 3, 2]  # where 3 is the out-of-vocabulary bucket
```

#### Args:

* <b>`vocabulary_file`</b>: The vocabulary filename.
* <b>`num_oov_buckets`</b>: The number of out-of-vocabulary buckets.
* <b>`vocab_size`</b>: Number of the elements in the vocabulary, if known.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
    Defaults to -1.
* <b>`hasher_spec`</b>: A `HasherSpec` to specify the hash function to use for
    assignation of out-of-vocabulary buckets.
* <b>`key_dtype`</b>: The `key` data type.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

  The lookup table to map a `key_dtype` `Tensor` to index `int64` `Tensor`.


#### Raises:

* <b>`ValueError`</b>: If `vocabulary_file` is not set.
* <b>`ValueError`</b>: If `num_oov_buckets` is negative or `vocab_size` is not greater
    than zero.