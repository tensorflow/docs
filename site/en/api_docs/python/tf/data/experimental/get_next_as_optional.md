page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_next_as_optional

Returns an `Optional` that contains the next value from the iterator.

### Aliases:

* `tf.compat.v1.data.experimental.get_next_as_optional`
* `tf.compat.v2.data.experimental.get_next_as_optional`
* `tf.contrib.data.get_next_as_optional`
* `tf.data.experimental.get_next_as_optional`

``` python
tf.data.experimental.get_next_as_optional(iterator)
```



Defined in [`python/data/ops/iterator_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/data/ops/iterator_ops.py).

<!-- Placeholder for "Used in" -->

If `iterator` has reached the end of the sequence, the returned `Optional`
will have no value.

#### Args:


* <b>`iterator`</b>: A <a href="../../../tf/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> object.


#### Returns:

An `Optional` object representing the next value from the iterator (if it
has one) or no value.
