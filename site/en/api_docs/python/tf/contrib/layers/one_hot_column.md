page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.one_hot_column


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/layers/python/layers/feature_column.py#L1289-L1300">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates an `_OneHotColumn` for a one-hot or multi-hot repr in a DNN.

``` python
tf.contrib.layers.one_hot_column(sparse_id_column)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`sparse_id_column`</b>: A _SparseColumn which is created by
  `sparse_column_with_*` or crossed_column functions. Note that `combiner`
  defined in `sparse_id_column` is ignored.


#### Returns:

An _OneHotColumn.
