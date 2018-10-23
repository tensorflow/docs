


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.sparse_column_with_keys

### `tf.contrib.layers.sparse_column_with_keys`

```
tf.contrib.layers.sparse_column_with_keys(column_name, keys, default_value=-1, combiner=None)
```


See the guide: [Layers (contrib) > Feature columns](../../../../../api_guides/python/contrib.layers#Feature_columns)

Creates a _SparseColumn with keys.

Look up logic is as follows:
lookup_id = index_of_feature_in_keys if feature in keys else default_value

#### Args:

* <b>`column_name`</b>: A string defining sparse column name.
* <b>`keys`</b>: a string list defining vocabulary.
* <b>`default_value`</b>: The value to use for out-of-vocabulary feature values.
    Default is -1.
* <b>`combiner`</b>: A string specifying how to reduce if the sparse column is
    multivalent. Currently "mean", "sqrtn" and "sum" are supported, with
    "sum" the default:
      * "sum": do not normalize features in the column
      * "mean": do l1 normalization on features in the column
      * "sqrtn": do l2 normalization on features in the column
    For more information: `tf.embedding_lookup_sparse`.


#### Returns:

  A _SparseColumnKeys with keys configuration.

Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://www.tensorflow.org/code/tensorflow/contrib/layers/python/layers/feature_column.py).

