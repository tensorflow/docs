


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.layers.bucketized_column

### `tf.contrib.layers.bucketized_column`

```
tf.contrib.layers.bucketized_column(source_column, boundaries)
```


See the guide: [Layers (contrib) > Feature columns](../../../../../api_guides/python/contrib.layers#Feature_columns)

Creates a _BucketizedColumn for discretizing dense input.

#### Args:

* <b>`source_column`</b>: A _RealValuedColumn defining dense column.
* <b>`boundaries`</b>: A list of floats specifying the boundaries. It has to be sorted.


#### Returns:

  A _BucketizedColumn.


#### Raises:

* <b>`ValueError`</b>: if 'boundaries' is empty or not sorted.

Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://www.tensorflow.org/code/tensorflow/contrib/layers/python/layers/feature_column.py).

