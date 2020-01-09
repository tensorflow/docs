page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.as_text


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/compat/as_text">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/compat.py#L74-L95">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts any string-like python input types to unicode.

### Aliases:

* <a href="/api_docs/python/tf/compat/as_text"><code>tf.compat.as_str</code></a>
* <a href="/api_docs/python/tf/compat/as_text"><code>tf.compat.v1.compat.as_str</code></a>
* <a href="/api_docs/python/tf/compat/as_text"><code>tf.compat.v1.compat.as_text</code></a>
* <a href="/api_docs/python/tf/compat/as_text"><code>tf.compat.v2.compat.as_str</code></a>
* <a href="/api_docs/python/tf/compat/as_text"><code>tf.compat.v2.compat.as_text</code></a>


``` python
tf.compat.as_text(
    bytes_or_text,
    encoding='utf-8'
)
```



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
