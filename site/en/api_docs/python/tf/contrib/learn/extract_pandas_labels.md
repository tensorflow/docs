page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.extract_pandas_labels

``` python
tf.contrib.learn.extract_pandas_labels(labels)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py).

Extract data from pandas.DataFrame for labels. (deprecated)

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