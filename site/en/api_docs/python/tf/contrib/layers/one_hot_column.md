page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.one_hot_column

Creates an `_OneHotColumn` for a one-hot or multi-hot repr in a DNN.

``` python
tf.contrib.layers.one_hot_column(sparse_id_column)
```



Defined in [`contrib/layers/python/layers/feature_column.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/feature_column.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sparse_id_column`</b>: A _SparseColumn which is created by
  `sparse_column_with_*` or crossed_column functions. Note that `combiner`
  defined in `sparse_id_column` is ignored.


#### Returns:

An _OneHotColumn.
