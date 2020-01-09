page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.infer_real_valued_columns_from_input_fn


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/estimators/estimator.py#L147-L165">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates `FeatureColumn` objects for inputs defined by `input_fn`. (deprecated)

``` python
tf.contrib.learn.infer_real_valued_columns_from_input_fn(input_fn)
```



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
