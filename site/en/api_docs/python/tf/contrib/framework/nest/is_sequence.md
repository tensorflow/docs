page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.is_sequence

``` python
tf.contrib.framework.nest.is_sequence(o)
```



Defined in [`tensorflow/python/pywrap_tensorflow_internal.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/pywrap_tensorflow_internal.py).

Returns a true if its input is a collections.Sequence (except strings).

#### Args:

* <b>`seq`</b>: an input sequence.


#### Returns:

True if the sequence is a not a string and is a collections.Sequence or a
dict.