

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.Counter

``` python
tf.contrib.data.Counter(
    start=0,
    step=1,
    dtype=tf.int64
)
```



Defined in [`tensorflow/contrib/data/python/ops/counter.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/data/python/ops/counter.py).

Creates a `Dataset` of a `step`-separated count startin from `start`.

For example:

```python
Dataset.count() == [0, 1, 2, ...)
Dataset.count(2) == [2, 3, ...)
Dataset.count(2, 5) == [2, 7, 12, ...)
Dataset.count(0, -1) == [0, -1, -2, ...)
Dataset.count(10, -1) == [10, 9, ...)
```

#### Args:

* <b>`start`</b>: starting value for count.
* <b>`step`</b>: step size.
* <b>`dtype`</b>: counter data type.


#### Returns:

A `Dataset` of scalar elements.