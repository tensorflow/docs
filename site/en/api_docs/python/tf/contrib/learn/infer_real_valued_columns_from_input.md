page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.infer_real_valued_columns_from_input

``` python
tf.contrib.learn.infer_real_valued_columns_from_input(x)
```



Defined in [`tensorflow/contrib/learn/python/learn/estimators/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/learn/python/learn/estimators/estimator.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Creates `FeatureColumn` objects for inputs defined by input `x`. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please specify feature columns explicitly.

This interprets all inputs as dense, fixed-length float values.

#### Args:

* <b>`x`</b>: Real-valued matrix of shape [n_samples, n_features...]. Can be
     iterator that returns arrays of features.


#### Returns:

List of `FeatureColumn` objects.