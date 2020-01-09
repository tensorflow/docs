page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_base64


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Decode web-safe base64-encoded strings.

### Aliases:

* `tf.compat.v1.decode_base64`
* `tf.compat.v1.io.decode_base64`
* `tf.compat.v2.io.decode_base64`


``` python
tf.io.decode_base64(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Input may or may not have padding at the end. See EncodeBase64 for padding.
Web-safe means that input must use - and _ instead of + and /.

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`. Base64 strings to decode.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
