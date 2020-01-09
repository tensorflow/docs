page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.unique

``` python
tf.data.experimental.unique()
```



Defined in [`tensorflow/python/data/experimental/ops/unique.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/data/experimental/ops/unique.py).

Creates a `Dataset` from another `Dataset`, discarding duplicates.

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