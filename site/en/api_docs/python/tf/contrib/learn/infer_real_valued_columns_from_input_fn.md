page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.infer_real_valued_columns_from_input_fn

Creates `FeatureColumn` objects for inputs defined by `input_fn`. (deprecated)

``` python
tf.contrib.learn.infer_real_valued_columns_from_input_fn(input_fn)
```



Defined in [`contrib/learn/python/learn/estimators/estimator.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/estimators/estimator.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please specify feature columns explicitly.

This interprets all inputs as dense, fixed-length float values. This creates
a local graph in which it calls `input_fn` to build the tensors, then discards
it.

#### Args:


* <b>`input_fn`</b>: Input function returning a tuple of:
    features - Dictionary of string feature name to `Tensor` or `Tensor`.
    labels - `Tensor` of label values.


#### Returns:

List of `FeatureColumn` objects.
