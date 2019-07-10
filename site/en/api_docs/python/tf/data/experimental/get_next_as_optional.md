page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.get_next_as_optional

### Aliases:

* `tf.contrib.data.get_next_as_optional`
* `tf.data.experimental.get_next_as_optional`

``` python
tf.data.experimental.get_next_as_optional(iterator)
```



Defined in [`tensorflow/python/data/ops/iterator_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/ops/iterator_ops.py).

Returns an `Optional` that contains the next value from the iterator.

If `iterator` has reached the end of the sequence, the returned `Optional`
will have no value.

#### Args:

* <b>`iterator`</b>: A <a href="../../../tf/data/Iterator"><code>tf.data.Iterator</code></a> object.


#### Returns:

An `Optional` object representing the next value from the iterator (if it
has one) or no value.