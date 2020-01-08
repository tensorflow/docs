page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.reduce_dataset

``` python
tf.contrib.data.reduce_dataset(
    dataset,
    reducer
)
```



Defined in [`tensorflow/contrib/data/python/ops/get_single_element.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/data/python/ops/get_single_element.py).

Returns the result of reducing the `dataset` using `reducer`. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.reduce(...)`.

#### Args:

* <b>`dataset`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object.
* <b>`reducer`</b>: A <a href="../../../tf/contrib/data/Reducer"><code>tf.contrib.data.Reducer</code></a> object representing the reduce logic.


#### Returns:

A nested structure of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> objects, corresponding to the result
of reducing `dataset` using `reducer`.


#### Raises:

* <b>`TypeError`</b>: if `dataset` is not a <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> object.