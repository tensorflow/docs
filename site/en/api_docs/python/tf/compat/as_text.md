page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_text

Converts any string-like python input types to unicode.

### Aliases:

* `tf.compat.as_str`
* `tf.compat.as_text`
* `tf.compat.v1.compat.as_str`
* `tf.compat.v1.compat.as_text`
* `tf.compat.v2.compat.as_str`
* `tf.compat.v2.compat.as_text`

``` python
tf.compat.as_text(
    bytes_or_text,
    encoding='utf-8'
)
```



Defined in [`python/util/compat.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/compat.py).

<!-- Placeholder for "Used in" -->

Returns the input as a unicode string. Uses utf-8 encoding for text
by default.

#### Args:


* <b>`bytes_or_text`</b>: A `bytes`, `str`, or `unicode` object.
* <b>`encoding`</b>: A string indicating the charset for decoding unicode.


#### Returns:

A `unicode` (Python 2) or `str` (Python 3) object.



#### Raises:


* <b>`TypeError`</b>: If `bytes_or_text` is not a binary or unicode string.