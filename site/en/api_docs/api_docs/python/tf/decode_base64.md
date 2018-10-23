

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.decode_base64

### Aliases:

* `tf.decode_base64`
* `tf.io.decode_base64`

``` python
tf.decode_base64(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_string_ops.py`.

See the guide: [Strings > Conversion](../../../api_guides/python/string_ops#Conversion)

Decode web-safe base64-encoded strings.

Input may or may not have padding at the end. See EncodeBase64 for padding.
Web-safe means that input must use - and _ instead of + and /.

#### Args:

* <b>`input`</b>: A `Tensor` of type `string`. Base64 strings to decode.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.