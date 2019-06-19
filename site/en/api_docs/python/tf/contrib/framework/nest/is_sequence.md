page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.is_sequence

``` python
tf.contrib.framework.nest.is_sequence(seq)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/util/nest.py).

Returns a true if its input is a collections.Sequence (except strings).

#### Args:

* <b>`seq`</b>: an input sequence.


#### Returns:

True if the sequence is a not a string and is a collections.Sequence or a
dict.