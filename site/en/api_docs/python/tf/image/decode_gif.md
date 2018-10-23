

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.image.decode_gif

### `tf.image.decode_gif`

``` python
decode_gif(
    contents,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Encoding and Decoding](../../../../api_guides/python/image#Encoding_and_Decoding)

Decode the first frame of a GIF-encoded image to a uint8 tensor.

GIF with frame or transparency compression are not supported
convert animated GIF from compressed to uncompressed by:

convert $src.gif -coalesce $dst.gif

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The GIF-encoded image.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor` of type `uint8`.
  4-D with shape `[num_frames, height, width, 3]`. RGB order