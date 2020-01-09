page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.infer_real_valued_columns_from_input


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L168-L183">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates `FeatureColumn` objects for inputs defined by input `x`. (deprecated)

``` python
tf.contrib.learn.infer_real_valued_columns_from_input(x)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please specify feature columns explicitly.

This interprets all inputs as dense, fixed-length float values.

#### Args:


* <b>`x`</b>: Real-valued matrix of shape [n_samples, n_features...]. Can be
   iterator that returns arrays of features.


#### Returns:

List of `FeatureColumn` objects.
