page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nest.is_nested

Returns true if its input is a collections.Sequence (except strings).

### Aliases:

* `tf.compat.v1.nest.is_nested`
* `tf.compat.v2.nest.is_nested`
* `tf.contrib.framework.nest.is_nested`
* `tf.nest.is_nested`

``` python
tf.nest.is_nested(seq)
```



Defined in [`python/util/nest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/nest.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`seq`</b>: an input sequence.


#### Returns:

True if the sequence is a not a string and is a collections.Sequence or a
dict.
