

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.ignore_errors

``` python
tf.contrib.data.ignore_errors()
```



Defined in [`tensorflow/contrib/data/python/ops/error_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/data/python/ops/error_ops.py).

See the guide: [Dataset Input Pipeline > Transformations on existing datasets](../../../../../api_guides/python/input_dataset#Transformations_on_existing_datasets)

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
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.