page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.make_place_holder_tensors_for_base_features

Returns placeholder tensors for inference.

``` python
tf.contrib.layers.make_place_holder_tensors_for_base_features(feature_columns)
```



Defined in [`contrib/layers/python/layers/feature_column.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/layers/python/layers/feature_column.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`feature_columns`</b>: An iterable containing all the feature columns. All items
  should be instances of classes derived from _FeatureColumn.


#### Returns:

A dict mapping feature keys to SparseTensors (sparse columns) or
placeholder Tensors (dense columns).
