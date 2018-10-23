


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.lookup.string_to_index_table_from_tensor

### `tf.contrib.lookup.string_to_index_table_from_tensor`

```
tf.contrib.lookup.string_to_index_table_from_tensor(mapping, num_oov_buckets=0, default_value=-1, hasher_spec=tf.contrib.lookup.FastHashSpec, name=None)
```


Returns a lookup table that converts a string tensor into int64 IDs.

This operation constructs a lookup table to convert tensor of strings into
int64 IDs. The mapping can be initialized from a string `mapping` 1-D tensor
where each element is a key and corresponding index within the tensor is the
value.

Any lookup of an out-of-vocabulary token will return a bucket ID based on its
hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
`default_value`.
The bucket ID range is `[mapping size, mapping size + num_oov_buckets]`.

The underlying table must be initialized by calling
`tf.tables_initializer.run()` or `table.init.run()` once.

Elements in `mapping` cannot have duplicates, otherwise when executing the
table initializer op, it will throw a `FailedPreconditionError`.

Sample Usages:

```python
mapping_strings = t.constant(["emerson", "lake", "palmer")
table = tf.contrib.lookup.string_to_index_table_from_tensor(
    mapping=mapping_strings, num_oov_buckets=1, default_value=-1)
features = tf.constant(["emerson", "lake", "and", "palmer"])
ids = table.lookup(features)
...
tf.tables_initializer().run()

ids.eval()  ==> [0, 1, 4, 2]
```

#### Args:

* <b>`mapping`</b>: A 1-D string `Tensor` that specifies the mapping of strings to
    indices.
* <b>`num_oov_buckets`</b>: The number of out-of-vocabulary buckets.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
    Defaults to -1.
* <b>`hasher_spec`</b>: A `HasherSpec` to specify the hash function to use for
    assignation of out-of-vocabulary buckets.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

  The lookup table to map a string `Tensor` to index `int64` `Tensor`.


#### Raises:

* <b>`ValueError`</b>: `mapping` is invalid.
* <b>`ValueError`</b>: If `num_oov_buckets` is negative.

Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.tensorflow.org/code/tensorflow/contrib/lookup/lookup_ops.py).

