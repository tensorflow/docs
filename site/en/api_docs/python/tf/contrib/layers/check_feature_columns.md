page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.check_feature_columns


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column_ops.py#L763-L783">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Checks the validity of the set of FeatureColumns.

``` python
tf.contrib.layers.check_feature_columns(feature_columns)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`feature_columns`</b>: An iterable of instances or subclasses of FeatureColumn.


#### Raises:


* <b>`ValueError`</b>: If `feature_columns` is a dict.
* <b>`ValueError`</b>: If there are duplicate feature column keys.
