page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.from_variant

Constructs a dataset from the given variant and structure.

### Aliases:

* `tf.compat.v1.data.experimental.from_variant`
* `tf.compat.v2.data.experimental.from_variant`
* `tf.data.experimental.from_variant`

``` python
tf.data.experimental.from_variant(
    variant,
    structure
)
```



Defined in [`python/data/ops/dataset_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/dataset_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`variant`</b>: A scalar <a href="../../../tf#variant"><code>tf.variant</code></a> tensor representing a dataset.
* <b>`structure`</b>: A <a href="../../../tf/data/experimental/Structure"><code>tf.data.experimental.Structure</code></a> object representing the
  structure of each element in the dataset.


#### Returns:

A <a href="../../../tf/data/Dataset"><code>tf.data.Dataset</code></a> instance.
