


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.compat.as_bytes

### `tf.compat.as_bytes`

```
tf.compat.as_bytes(bytes_or_text, encoding='utf-8')
```

### `tf.compat.as_str`

```
tf.compat.as_str(bytes_or_text, encoding='utf-8')
```


Converts either bytes or unicode to `bytes`, using utf-8 encoding for text.

#### Args:

* <b>`bytes_or_text`</b>: A `bytes`, `str`, or `unicode` object.
* <b>`encoding`</b>: A string indicating the charset for encoding unicode.


#### Returns:

  A `bytes` object.


#### Raises:

* <b>`TypeError`</b>: If `bytes_or_text` is not a binary or unicode string.

Defined in [`tensorflow/python/util/compat.py`](https://www.tensorflow.org/code/tensorflow/python/util/compat.py).

