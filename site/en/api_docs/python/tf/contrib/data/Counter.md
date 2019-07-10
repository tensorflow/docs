page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.Counter

``` python
tf.contrib.data.Counter(
    start=0,
    step=1,
    dtype=tf.dtypes.int64
)
```



Defined in [`tensorflow/contrib/data/python/ops/counter.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/data/python/ops/counter.py).

Creates a `Dataset` that counts from `start` in steps of size `step`. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use `tf.data.experimental.Counter(...)`.

For example:

```python
Dataset.count() == [0, 1, 2, ...)
Dataset.count(2) == [2, 3, ...)
Dataset.count(2, 5) == [2, 7, 12, ...)
Dataset.count(0, -1) == [0, -1, -2, ...)
Dataset.count(10, -1) == [10, 9, ...)
```

#### Args:

* <b>`start`</b>: (Optional.) The starting value for the counter. Defaults to 0.
* <b>`step`</b>: (Optional.) The step size for the counter. Defaults to 1.
* <b>`dtype`</b>: (Optional.) The data type for counter elements. Defaults to
    <a href="../../../tf/dtypes#int64"><code>tf.int64</code></a>.


#### Returns:

A `Dataset` of scalar `dtype` elements.