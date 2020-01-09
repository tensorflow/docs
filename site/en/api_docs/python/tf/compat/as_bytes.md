page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_bytes


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/util/compat.py#L48-L71">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts `bytearray`, `bytes`, or unicode python input types to `bytes`.

### Aliases:

* `tf.compat.v1.compat.as_bytes`
* `tf.compat.v2.compat.as_bytes`


``` python
tf.compat.as_bytes(
    bytes_or_text,
    encoding='utf-8'
)
```



<!-- Placeholder for "Used in" -->

Uses utf-8 encoding for text by default.

#### Args:


* <b>`bytes_or_text`</b>: A `bytearray`, `bytes`, `str`, or `unicode` object.
* <b>`encoding`</b>: A string indicating the charset for encoding unicode.


#### Returns:

A `bytes` object.



#### Raises:


* <b>`TypeError`</b>: If `bytes_or_text` is not a binary or unicode string.
