page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.ignore_errors

Creates a `Dataset` from another `Dataset` and silently ignores any errors.

### Aliases:

* `tf.compat.v1.data.experimental.ignore_errors`
* `tf.compat.v2.data.experimental.ignore_errors`
* `tf.data.experimental.ignore_errors`

``` python
tf.data.experimental.ignore_errors()
```



Defined in [`python/data/experimental/ops/error_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/experimental/ops/error_ops.py).

<!-- Placeholder for "Used in" -->

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
    dataset.apply(tf.data.experimental.ignore_errors())  # ==> {1., 0.5, 0.2}
```

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
