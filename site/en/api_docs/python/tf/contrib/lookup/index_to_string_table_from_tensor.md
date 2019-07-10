page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.index_to_string_table_from_tensor

``` python
tf.contrib.lookup.index_to_string_table_from_tensor(
    mapping,
    default_value='UNK',
    name=None
)
```



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/lookup/lookup_ops.py).

Returns a lookup table that maps a `Tensor` of indices into strings.

This operation constructs a lookup table to map int64 indices into string
values. The mapping is initialized from a string `mapping` 1-D `Tensor` where
each element is a value and the corresponding index within the tensor is the
key.

Any input which does not have a corresponding index in 'mapping'
(an out-of-vocabulary entry) is assigned the `default_value`

The underlying table must be initialized by calling
`session.run(tf.tables_initializer)` or `session.run(table.init)` once.

Elements in `mapping` cannot have duplicates, otherwise when executing the
table initializer op, it will throw a `FailedPreconditionError`.

Sample Usages:

```python
mapping_string = tf.constant(["emerson", "lake", "palmer"])
indices = tf.constant([1, 5], tf.int64)
table = tf.contrib.lookup.index_to_string_table_from_tensor(
    mapping_string, default_value="UNKNOWN")
values = table.lookup(indices)
...
tf.tables_initializer().run()

values.eval() ==> ["lake", "UNKNOWN"]
```

#### Args:

* <b>`mapping`</b>: A 1-D string `Tensor` that specifies the strings to map from
    indices.
* <b>`default_value`</b>: The value to use for out-of-vocabulary indices.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

The lookup table to map a string values associated to a given index `int64`
`Tensors`.


#### Raises:

* <b>`ValueError`</b>: when `mapping` is not set.