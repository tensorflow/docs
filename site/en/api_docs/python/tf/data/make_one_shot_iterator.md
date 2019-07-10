page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.make_one_shot_iterator

Creates a <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> for enumerating the elements of a dataset.

### Aliases:

* `tf.compat.v1.data.make_one_shot_iterator`
* `tf.data.make_one_shot_iterator`

``` python
tf.data.make_one_shot_iterator(dataset)
```



Defined in [`python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/dataset_ops.py).

<!-- Placeholder for "Used in" -->

Note: The returned iterator will be initialized automatically.
A "one-shot" iterator does not support re-initialization.

#### Args:


* <b>`dataset`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a>.


#### Returns:

A <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> over the elements of this dataset.
