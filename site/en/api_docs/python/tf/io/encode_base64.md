page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.encode_base64


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/encode_base64">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Encode strings into web-safe base64 format.

### Aliases:

* <a href="/api_docs/python/tf/io/encode_base64"><code>tf.compat.v1.encode_base64</code></a>
* <a href="/api_docs/python/tf/io/encode_base64"><code>tf.compat.v1.io.encode_base64</code></a>
* <a href="/api_docs/python/tf/io/encode_base64"><code>tf.compat.v2.io.encode_base64</code></a>
* <a href="/api_docs/python/tf/io/encode_base64"><code>tf.encode_base64</code></a>


``` python
tf.io.encode_base64(
    input,
    pad=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Refer to the following article for more information on base64 format:
en.wikipedia.org/wiki/Base64. Base64 strings may have padding with '=' at the
end so that the encoded has length multiple of 4. See Padding section of the
link above.

Web-safe means that the encoder uses - and _ instead of + and /.

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`. Strings to be encoded.
* <b>`pad`</b>: An optional `bool`. Defaults to `False`.
  Bool whether padding is applied at the ends.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
