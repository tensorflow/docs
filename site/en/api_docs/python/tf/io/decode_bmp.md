page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_bmp

Decode the first frame of a BMP-encoded image to a uint8 tensor.

### Aliases:

* `tf.compat.v1.image.decode_bmp`
* `tf.compat.v1.io.decode_bmp`
* `tf.compat.v2.image.decode_bmp`
* `tf.compat.v2.io.decode_bmp`
* `tf.image.decode_bmp`
* `tf.io.decode_bmp`

``` python
tf.io.decode_bmp(
    contents,
    channels=0,
    name=None
)
```



Defined in generated file: `python/ops/gen_image_ops.py`.

<!-- Placeholder for "Used in" -->

The attr `channels` indicates the desired number of color channels for the
decoded image.

#### Accepted values are:



*   0: Use the number of channels in the BMP-encoded image.
*   3: output an RGB image.
*   4: output an RGBA image.

#### Args:


* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The BMP-encoded image.
* <b>`channels`</b>: An optional `int`. Defaults to `0`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `uint8`.
