page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.extract_pandas_data

``` python
tf.contrib.learn.extract_pandas_data(data)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/learn/python/learn/learn_io/pandas_io.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Extract data from pandas.DataFrame for predictors. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please access pandas data directly.

Given a DataFrame, will extract the values and cast them to float. The
DataFrame is expected to contain values of type int, float or bool.

#### Args:

* <b>`data`</b>: `pandas.DataFrame` containing the data to be extracted.


#### Returns:

A numpy `ndarray` of the DataFrame's values as floats.


#### Raises:

* <b>`ValueError`</b>: if data contains types other than int, float or bool.