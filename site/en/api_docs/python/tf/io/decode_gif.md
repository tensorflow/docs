page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_gif

### Aliases:

* `tf.image.decode_gif`
* `tf.io.decode_gif`

``` python
tf.io.decode_gif(
    contents,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_image_ops.py`.

Decode the first frame of a GIF-encoded image to a uint8 tensor.

GIF with frame or transparency compression are not supported
convert animated GIF from compressed to uncompressed by:

    convert $src.gif -coalesce $dst.gif

This op also supports decoding JPEGs and PNGs, though it is cleaner to use
<a href="../../tf/io/decode_image"><code>tf.image.decode_image</code></a>.

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The GIF-encoded image.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `uint8`.