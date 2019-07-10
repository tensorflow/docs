page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.learn.extract_dask_data

Extract data from dask.Series or dask.DataFrame for predictors. (deprecated)

``` python
tf.contrib.learn.extract_dask_data(data)
```



Defined in [`contrib/learn/python/learn/learn_io/dask_io.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/learn/python/learn/learn_io/dask_io.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please feed input to tf.data to support dask.

Given a distributed dask.DataFrame or dask.Series containing columns or names
for one or more predictors, this operation returns a single dask.DataFrame or
dask.Series that can be iterated over.

#### Args:


* <b>`data`</b>: A distributed dask.DataFrame or dask.Series.


#### Returns:

A dask.DataFrame or dask.Series that can be iterated over.
If the supplied argument is neither a dask.DataFrame nor a dask.Series this
operation returns it without modification.
