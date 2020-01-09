page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.regression_target


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/target_column.py#L34-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a _TargetColumn for linear regression. (deprecated)

``` python
tf.contrib.layers.regression_target(
    label_name=None,
    weight_column_name=None,
    label_dimension=1
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-11-12.
Instructions for updating:
This file will be removed after the deprecation date.Please switch to third_party/tensorflow/contrib/learn/python/learn/estimators/head.py

#### Args:


* <b>`label_name`</b>: String, name of the key in label dict. Can be null if label
    is a tensor (single headed models).
* <b>`weight_column_name`</b>: A string defining feature column name representing
  weights. It is used to down weight or boost examples during training. It
  will be multiplied by the loss of the example.
* <b>`label_dimension`</b>: dimension of the target for multilabels.


#### Returns:

An instance of _TargetColumn
