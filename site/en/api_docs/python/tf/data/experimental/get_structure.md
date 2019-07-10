page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_structure

Returns the <a href="../../../tf/data/experimental/Structure"><code>tf.data.experimental.Structure</code></a> of a `Dataset` or `Iterator`.

### Aliases:

* `tf.compat.v1.data.experimental.get_structure`
* `tf.compat.v2.data.experimental.get_structure`
* `tf.data.experimental.get_structure`

``` python
tf.data.experimental.get_structure(dataset_or_iterator)
```



Defined in [`python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/dataset_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a>, <a href="../../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a>, or
  `IteratorV2`.


#### Returns:

A <a href="../../../tf/data/experimental/Structure"><code>tf.data.experimental.Structure</code></a> representing the structure of the
elements of `dataset_or_iterator`.



#### Raises:


* <b>`TypeError`</b>: If `dataset_or_iterator` is not a dataset or iterator object.