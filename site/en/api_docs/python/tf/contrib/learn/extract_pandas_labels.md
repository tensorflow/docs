page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.extract_pandas_labels


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py#L123-L153">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Extract data from pandas.DataFrame for labels. (deprecated)

``` python
tf.contrib.learn.extract_pandas_labels(labels)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please access pandas data directly.

#### Args:


* <b>`labels`</b>: `pandas.DataFrame` or `pandas.Series` containing one column of
  labels to be extracted.


#### Returns:

A numpy `ndarray` of labels from the DataFrame.



#### Raises:


* <b>`ValueError`</b>: if more than one column is found or type is not int, float or
  bool.
