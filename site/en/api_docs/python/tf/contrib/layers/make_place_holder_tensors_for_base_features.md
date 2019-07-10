page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.make_place_holder_tensors_for_base_features

``` python
tf.contrib.layers.make_place_holder_tensors_for_base_features(feature_columns)
```



Defined in [`tensorflow/contrib/layers/python/layers/feature_column.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/layers/python/layers/feature_column.py).

Returns placeholder tensors for inference.

#### Args:

* <b>`feature_columns`</b>: An iterable containing all the feature columns. All items
    should be instances of classes derived from _FeatureColumn.

#### Returns:

A dict mapping feature keys to SparseTensors (sparse columns) or
placeholder Tensors (dense columns).