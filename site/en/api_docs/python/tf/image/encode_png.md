page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.encode_png


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/encode_png">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_image_ops.py`



PNG-encode an image.

### Aliases:

* <a href="/api_docs/python/tf/image/encode_png"><code>tf.compat.v1.image.encode_png</code></a>
* <a href="/api_docs/python/tf/image/encode_png"><code>tf.compat.v2.image.encode_png</code></a>


``` python
tf.image.encode_png(
    image,
    compression=-1,
    name=None
)
```



<!-- Placeholder for "Used in" -->

`image` is a 3-D uint8 or uint16 Tensor of shape `[height, width, channels]`
where `channels` is:

*   1: for grayscale.
*   2: for grayscale + alpha.
*   3: for RGB.
*   4: for RGBA.

The ZLIB compression level, `compression`, can be -1 for the PNG-encoder
default or a value from 0 to 9.  9 is the highest compression level, generating
the smallest output, but is slower.

#### Args:


* <b>`image`</b>: A `Tensor`. Must be one of the following types: `uint8`, `uint16`.
  3-D with shape `[height, width, channels]`.
* <b>`compression`</b>: An optional `int`. Defaults to `-1`. Compression level.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.
