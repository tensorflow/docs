page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.unique

Creates a `Dataset` from another `Dataset`, discarding duplicates. (deprecated)

``` python
tf.contrib.data.unique()
```



Defined in [`contrib/data/python/ops/unique.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/unique.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/unique"><code>tf.data.experimental.unique()</code></a>.

Use this transformation to produce a dataset that contains one instance of
each unique element in the input. For example:

```python
dataset = tf.data.Dataset.from_tensor_slices([1, 37, 2, 37, 2, 1])

# Using `unique()` will drop the duplicate elements.
dataset = dataset.apply(tf.data.experimental.unique())  # ==> { 1, 37, 2 }
```

#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
