page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.ignore_errors

Creates a `Dataset` from another `Dataset` and silently ignores any errors. (deprecated)

``` python
tf.contrib.data.ignore_errors()
```



Defined in [`contrib/data/python/ops/error_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/error_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/ignore_errors"><code>tf.data.experimental.ignore_errors()</code></a>.

Use this transformation to produce a dataset that contains the same elements
as the input, but silently drops any elements that caused an error. For
example:

```python
dataset = tf.data.Dataset.from_tensor_slices([1., 2., 0., 4.])

# Computing `tf.debugging.check_numerics(1. / 0.)` will raise an
InvalidArgumentError.
dataset = dataset.map(lambda x: tf.debugging.check_numerics(1. / x, "error"))

# Using `ignore_errors()` will drop the element that causes an error.
dataset =
    dataset.apply(tf.data.experimental.ignore_errors())  # ==> { 1., 0.5, 0.2
    }
```

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
