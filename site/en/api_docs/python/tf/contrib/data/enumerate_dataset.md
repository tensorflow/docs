page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.data.enumerate_dataset

A transformation that enumerate the elements of a dataset. (deprecated)

``` python
tf.contrib.data.enumerate_dataset(start=0)
```



Defined in [`contrib/data/python/ops/enumerate_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/data/python/ops/enumerate_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../tf/data/experimental/enumerate_dataset"><code>tf.data.experimental.enumerate_dataset(...)</code></a>.

It is Similar to python's `enumerate`.
For example:

```python
# NOTE: The following examples use `{ ... }` to represent the
# contents of a dataset.
a = { 1, 2, 3 }
b = { (7, 8), (9, 10) }

# The nested structure of the `datasets` argument determines the
# structure of elements in the resulting dataset.
a.apply(tf.contrib.data.enumerate(start=5)) == { (5, 1), (6, 2), (7, 3) }
b.apply(tf.contrib.data.enumerate()) == { (0, (7, 8)), (1, (9, 10)) }
```

#### Args:


* <b>`start`</b>: A <a href="../../../tf#int64"><code>tf.int64</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing the start
  value for enumeration.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.
