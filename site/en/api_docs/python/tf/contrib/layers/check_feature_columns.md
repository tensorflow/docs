page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.check_feature_columns

Checks the validity of the set of FeatureColumns.

``` python
tf.contrib.layers.check_feature_columns(feature_columns)
```



Defined in [`contrib/layers/python/layers/feature_column_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/feature_column_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`feature_columns`</b>: An iterable of instances or subclasses of FeatureColumn.


#### Raises:


* <b>`ValueError`</b>: If `feature_columns` is a dict.
* <b>`ValueError`</b>: If there are duplicate feature column keys.