page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.make_place_holder_tensors_for_base_features


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column.py#L2665-L2690">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns placeholder tensors for inference.

``` python
tf.contrib.layers.make_place_holder_tensors_for_base_features(feature_columns)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`feature_columns`</b>: An iterable containing all the feature columns. All items
  should be instances of classes derived from _FeatureColumn.


#### Returns:

A dict mapping feature keys to SparseTensors (sparse columns) or
placeholder Tensors (dense columns).
