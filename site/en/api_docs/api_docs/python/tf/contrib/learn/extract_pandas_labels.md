

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.learn.extract_pandas_labels

``` python
extract_pandas_labels(labels)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Extract data from pandas.DataFrame for labels.

#### Args:

* <b>`labels`</b>: `pandas.DataFrame` or `pandas.Series` containing one column of
    labels to be extracted.


#### Returns:

A numpy `ndarray` of labels from the DataFrame.


#### Raises:

* <b>`ValueError`</b>: if more than one column is found or type is not int, float or
    bool.