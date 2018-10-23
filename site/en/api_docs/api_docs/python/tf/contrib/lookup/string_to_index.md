

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lookup.string_to_index

``` python
string_to_index(
    tensor,
    mapping,
    default_value=-1,
    name=None
)
```



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/lookup/lookup_ops.py).

Maps `tensor` of strings into `int64` indices based on `mapping`. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed after 2017-01-07.
Instructions for updating:
This op will be removed after the deprecation date. Please switch to index_table_from_tensor and call the lookup method of the returned table.

This operation converts `tensor` of strings into `int64` indices.
The mapping is initialized from a string `mapping` tensor where each element
is a key and corresponding index within the tensor is the value.

Any entry in the input which does not have a corresponding entry in 'mapping'
(an out-of-vocabulary entry) is assigned the `default_value`

Elements in `mapping` cannot be duplicated, otherwise the initialization
will throw a FailedPreconditionError.

The underlying table must be initialized by calling
`tf.tables_initializer.run()` once.

For example:

```python
mapping_strings = tf.constant(["emerson", "lake", "palmer"])
feats = tf.constant(["emerson", "lake", "and", "palmer"])
ids = tf.contrib.lookup.string_to_index(
    feats, mapping=mapping_strings, default_value=-1)
...
tf.tables_initializer().run()

ids.eval()  ==> [0, 1, -1, 2]
```

#### Args:

* <b>`tensor`</b>: A 1-D input `Tensor` with the strings to map to indices.
* <b>`mapping`</b>: A 1-D string `Tensor` that specifies the mapping of strings to
    indices.
* <b>`default_value`</b>: The `int64` value to use for out-of-vocabulary strings.
    Defaults to -1.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

  The mapped indices. It has the same shape and tensor type (dense or sparse)
  as `tensor`.