page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.get_output_shapes

Returns the output shapes of a `Dataset` or `Iterator`.

### Aliases:

* `tf.compat.v1.data.get_output_shapes`
* `tf.data.get_output_shapes`

``` python
tf.data.get_output_shapes(dataset_or_iterator)
```



Defined in [`python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/dataset_ops.py).

<!-- Placeholder for "Used in" -->

This utility method replaces the deprecated-in-V2
`tf.compat.v1.Dataset.output_shapes` property.

#### Args:


* <b>`dataset_or_iterator`</b>: A <a href="../../tf/data/Dataset"><code>tf.data.Dataset</code></a>, <a href="../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a>, or
  `IteratorV2`.


#### Returns:

A nested structure of <a href="../../tf/TensorShape"><code>tf.TensorShape</code></a> objects corresponding to each
component of an element of the given dataset or iterator.
