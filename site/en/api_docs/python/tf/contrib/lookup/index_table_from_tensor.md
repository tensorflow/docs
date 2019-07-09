page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.index_table_from_tensor

``` python
tf.contrib.lookup.index_table_from_tensor(
    mapping,
    num_oov_buckets=0,
    default_value=-1,
    hasher_spec=tf.contrib.lookup.FastHashSpec,
    dtype=tf.string,
    name=None
)
```



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/lookup/lookup_ops.py).

Returns a lookup table that converts a string tensor into int64 IDs.

This operation constructs a lookup table to convert tensor of strings into
int64 IDs. The mapping can be initialized from a string `mapping` 1-D tensor
where each element is a key and corresponding index within the tensor is the
value.

Any lookup of an out-of-vocabulary token will return a bucket ID based on its
hash if `num_oov_buckets` is greater than zero. Otherwise it is assigned the
`default_value`.
The bucket ID range is `[mapping size, mapping size + num_oov_buckets - 1]`.

The underlying table must be initialized by calling
`tf.tables_initializer.run()` or `table.init.run()` once.

Elements in `mapping` cannot have duplicates, otherwise when executing the
table initializer op, it will throw a `FailedPreconditionError`.

Sample Usages:

```python
mapping_strings = tf.constant(["emerson", "lake", "palmer"])
table = tf.contrib.lookup.index_table_from_tensor(
    mapping=mapping_strings, num_oov_buckets=1, default_value=-1)
features = tf.constant(["emerson", "lake", "and", "palmer"])
ids = table.lookup(features)
...
tf.tables_initializer().run()

ids.eval()  ==> [0, 1, 3, 2]
```

#### Args:

* <b>`mapping`</b>: A 1-D `Tensor` that specifies the mapping of keys to indices. The
    type of this object must be castable to `dtype`.
* <b>`num_oov_buckets`</b>: The number of out-of-vocabulary buckets.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
    Defaults to -1.
* <b>`hasher_spec`</b>: A `HasherSpec` to specify the hash function to use for
    assignment of out-of-vocabulary buckets.
* <b>`dtype`</b>: The type of values passed to `lookup`. Only string and integers are
    supported.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

The lookup table to map an input `Tensor` to index `int64` `Tensor`.


#### Raises:

* <b>`ValueError`</b>: If `mapping` is invalid.
* <b>`ValueError`</b>: If `num_oov_buckets` is negative.