

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.compat.as_text

### `tf.compat.as_text`

``` python
as_text(
    bytes_or_text,
    encoding='utf-8'
)
```



Defined in [`tensorflow/python/util/compat.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/util/compat.py).

Returns the given argument as a unicode string.

#### Args:

* <b>`bytes_or_text`</b>: A `bytes`, `str, or `unicode` object.
* <b>`encoding`</b>: A string indicating the charset for decoding unicode.


#### Returns:

  A `unicode` (Python 2) or `str` (Python 3) object.


#### Raises:

* <b>`TypeError`</b>: If `bytes_or_text` is not a binary or unicode string.