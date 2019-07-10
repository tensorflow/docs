page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_bytes

Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

### Aliases:

* `tf.compat.as_bytes`
* `tf.compat.v1.compat.as_bytes`
* `tf.compat.v2.compat.as_bytes`

``` python
tf.compat.as_bytes(
    bytes_or_text,
    encoding='utf-8'
)
```



Defined in [`python/util/compat.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/compat.py).

<!-- Placeholder for "Used in" -->

Uses utf-8 encoding for text by default.

#### Args:


* <b>`bytes_or_text`</b>: A `bytearray`, `bytes`, `str`, or `unicode` object.
* <b>`encoding`</b>: A string indicating the charset for encoding unicode.


#### Returns:

A `bytes` object.



#### Raises:


* <b>`TypeError`</b>: If `bytes_or_text` is not a binary or unicode string.