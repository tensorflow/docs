

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.image.decode_png

### `tf.image.decode_png`

``` python
decode_png(
    contents,
    channels=None,
    dtype=None,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Encoding and Decoding](../../../../api_guides/python/image#Encoding_and_Decoding)

Decode a PNG-encoded image to a uint8 or uint16 tensor.

The attr `channels` indicates the desired number of color channels for the
decoded image.

Accepted values are:

*   0: Use the number of channels in the PNG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.
*   4: output an RGBA image.

If needed, the PNG-encoded image is transformed to match the requested number
of color channels.

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The PNG-encoded image.
* <b>`channels`</b>: An optional `int`. Defaults to `0`.
    Number of color channels for the decoded image.
* <b>`dtype`</b>: An optional `tf.DType` from: `tf.uint8, tf.uint16`. Defaults to `tf.uint8`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `dtype`. 3-D with shape `[height, width, channels]`.