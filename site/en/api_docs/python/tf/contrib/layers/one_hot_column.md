

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.layers.one_hot_column

### `tf.contrib.layers.one_hot_column`

``` python
one_hot_column(sparse_id_column)
```



Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/layers/python/layers/feature_column.py).

See the guide: [Layers (contrib) > Feature columns](../../../../../api_guides/python/contrib.layers#Feature_columns)

Creates an `_OneHotColumn` for a one-hot or multi-hot repr in a DNN.

#### Args:

    sparse_id_column: A _SparseColumn which is created by
      `sparse_column_with_*`
      or crossed_column functions. Note that `combiner` defined in
      `sparse_id_column` is ignored.


#### Returns:

  An _OneHotColumn.