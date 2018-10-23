

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.learn.extract_dask_data

### `tf.contrib.learn.extract_dask_data`

``` python
extract_dask_data(data)
```



Defined in [`tensorflow/contrib/learn/python/learn/learn_io/dask_io.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/learn/python/learn/learn_io/dask_io.py).

See the guide: [Learn (contrib) > Input processing](../../../../../api_guides/python/contrib.learn#Input_processing)

Extract data from dask.Series or dask.DataFrame for predictors.

Given a distributed dask.DataFrame or dask.Series containing columns or names
for one or more predictors, this operation returns a single dask.DataFrame or
dask.Series that can be iterated over.

#### Args:

* <b>`data`</b>: A distributed dask.DataFrame or dask.Series.


#### Returns:

  A dask.DataFrame or dask.Series that can be iterated over.
  If the supplied argument is neither a dask.DataFrame nor a dask.Series this
  operation returns it without modification.