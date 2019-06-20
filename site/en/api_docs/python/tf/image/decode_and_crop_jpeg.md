page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.decode_and_crop_jpeg

``` python
tf.image.decode_and_crop_jpeg(
    contents,
    crop_window,
    channels=0,
    ratio=1,
    fancy_upscaling=True,
    try_recover_truncated=False,
    acceptable_fraction=1,
    dct_method='',
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_image_ops.py`.

Decode and Crop a JPEG-encoded image to a uint8 tensor.

The attr `channels` indicates the desired number of color channels for the
decoded image.

Accepted values are:

*   0: Use the number of channels in the JPEG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.

If needed, the JPEG-encoded image is transformed to match the requested number
of color channels.

The attr `ratio` allows downscaling the image by an integer factor during
decoding.  Allowed values are: 1, 2, 4, and 8.  This is much faster than
downscaling the image later.


It is equivalent to a combination of decode and crop, but much faster by only
decoding partial jpeg image.

#### Args:

* <b>`contents`</b>: A `Tensor` of type `string`. 0-D.  The JPEG-encoded image.
* <b>`crop_window`</b>: A `Tensor` of type `int32`.
    1-D.  The crop window: [crop_y, crop_x, crop_height, crop_width].
* <b>`channels`</b>: An optional `int`. Defaults to `0`.
    Number of color channels for the decoded image.
* <b>`ratio`</b>: An optional `int`. Defaults to `1`. Downscaling ratio.
* <b>`fancy_upscaling`</b>: An optional `bool`. Defaults to `True`.
    If true use a slower but nicer upscaling of the
    chroma planes (yuv420/422 only).
* <b>`try_recover_truncated`</b>: An optional `bool`. Defaults to `False`.
    If true try to recover an image from truncated input.
* <b>`acceptable_fraction`</b>: An optional `float`. Defaults to `1`.
    The minimum required fraction of lines before a truncated
    input is accepted.
* <b>`dct_method`</b>: An optional `string`. Defaults to `""`.
    string specifying a hint about the algorithm used for
    decompression.  Defaults to "" which maps to a system-specific
    default.  Currently valid values are ["INTEGER_FAST",
    "INTEGER_ACCURATE"].  The hint may be ignored (e.g., the internal
    jpeg library changes to a version that does not have that specific
    option.)
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `uint8`.