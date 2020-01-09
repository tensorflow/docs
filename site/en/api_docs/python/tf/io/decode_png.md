page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_png


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/io/decode_png">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_image_ops.py`



Decode a PNG-encoded image to a uint8 or uint16 tensor.

### Aliases:

* <a href="/api_docs/python/tf/io/decode_png"><code>tf.compat.v1.image.decode_png</code></a>
* <a href="/api_docs/python/tf/io/decode_png"><code>tf.compat.v1.io.decode_png</code></a>
* <a href="/api_docs/python/tf/io/decode_png"><code>tf.compat.v2.image.decode_png</code></a>
* <a href="/api_docs/python/tf/io/decode_png"><code>tf.compat.v2.io.decode_png</code></a>
* <a href="/api_docs/python/tf/io/decode_png"><code>tf.image.decode_png</code></a>


``` python
tf.io.decode_png(
    contents,
    channels=0,
    dtype=tf.dtypes.uint8,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:



*   0: Use the number of channels in the PNG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.
*   4: output an RGBA image.

If needed, the PNG-encoded image is transformed to match the requested number
of color channels.

This op also supports decoding JPEGs and non-animated GIFs since the interface
is the same, though it is cleaner to use <a href="../../tf/io/decode_image"><code>tf.image.decode_image</code></a>.

#### Args:


* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The PNG-encoded image.
* <b>`channels`</b>: An optional `int`. Defaults to `0`.
  Number of color channels for the decoded image.
* <b>`dtype`</b>: An optional <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.uint8, tf.uint16`. Defaults to <a href="../../tf#uint8"><code>tf.uint8</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `dtype`.
