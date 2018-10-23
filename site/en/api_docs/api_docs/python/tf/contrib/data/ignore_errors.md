

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.ignore_errors

``` python
ignore_errors()
```



Defined in [`tensorflow/contrib/data/python/ops/error_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/data/python/ops/error_ops.py).

Creates a `Dataset` from another `Dataset` and silently ignores any errors.

Use this transformation to produce a dataset that contains the same elements
as the input, but silently drops any elements that caused an error. For
example:

```python
dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])

# Computing `tf.check_numerics(1. / 0.)` will raise an InvalidArgumentError.
dataset = dataset.map(lambda x: tf.check_numerics(1. / x, "error"))

# Using `ignore_errors()` will drop the element that causes an error.
dataset =
    dataset.apply(tf.contrib.data.ignore_errors())  # ==> { 1., 0.5, 0.2 }
```

#### Returns:

A `Dataset` transformation function, which can be passed to
[`tf.data.Dataset.apply`](../../../tf/data/Dataset#apply).