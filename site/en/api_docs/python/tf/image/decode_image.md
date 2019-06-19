page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.decode_image

``` python
tf.image.decode_image(
    contents,
    channels=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Encoding and Decoding](../../../../api_guides/python/image#Encoding_and_Decoding)

Convenience function for `decode_bmp`, `decode_gif`, `decode_jpeg`,
and `decode_png`.

Detects whether an image is a BMP, GIF, JPEG, or PNG, and performs the
appropriate operation to convert the input bytes `string` into a `Tensor` of
type `uint8`.

Note: `decode_gif` returns a 4-D array `[num_frames, height, width, 3]`, as
opposed to `decode_bmp`, `decode_jpeg` and `decode_png`, which return 3-D
arrays `[height, width, num_channels]`. Make sure to take this into account
when constructing your graph if you are intermixing GIF files with BMP, JPEG,
and/or PNG files.

#### Args:

* <b>`contents`</b>: 0-D `string`. The encoded image bytes.
* <b>`channels`</b>: An optional `int`. Defaults to `0`. Number of color channels for
    the decoded image.
* <b>`name`</b>: A name for the operation (optional)


#### Returns:

`Tensor` with type `uint8` with shape `[height, width, num_channels]` for
  BMP, JPEG, and PNG images and shape `[num_frames, height, width, 3]` for
  GIF images.


#### Raises:

* <b>`ValueError`</b>: On incorrect number of channels.