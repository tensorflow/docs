

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.encode_jpeg

``` python
tf.image.encode_jpeg(
    image,
    format='',
    quality=95,
    progressive=False,
    optimize_size=False,
    chroma_downsampling=True,
    density_unit='in',
    x_density=300,
    y_density=300,
    xmp_metadata='',
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Encoding and Decoding](../../../../api_guides/python/image#Encoding_and_Decoding)

JPEG-encode an image.

`image` is a 3-D uint8 Tensor of shape `[height, width, channels]`.

The attr `format` can be used to override the color format of the encoded
output.  Values can be:

*   `''`: Use a default format based on the number of channels in the image.
*   `grayscale`: Output a grayscale JPEG image.  The `channels` dimension
    of `image` must be 1.
*   `rgb`: Output an RGB JPEG image. The `channels` dimension
    of `image` must be 3.

If `format` is not specified or is the empty string, a default format is picked
in function of the number of channels in `image`:

*   1: Output a grayscale image.
*   3: Output an RGB image.

#### Args:

* <b>`image`</b>: A `Tensor` of type `uint8`.
    3-D with shape `[height, width, channels]`.
* <b>`format`</b>: An optional `string` from: `"", "grayscale", "rgb"`. Defaults to `""`.
    Per pixel image format.
* <b>`quality`</b>: An optional `int`. Defaults to `95`.
    Quality of the compression from 0 to 100 (higher is better and slower).
* <b>`progressive`</b>: An optional `bool`. Defaults to `False`.
    If True, create a JPEG that loads progressively (coarse to fine).
* <b>`optimize_size`</b>: An optional `bool`. Defaults to `False`.
    If True, spend CPU/RAM to reduce size with no quality change.
* <b>`chroma_downsampling`</b>: An optional `bool`. Defaults to `True`.
    See http://en.wikipedia.org/wiki/Chroma_subsampling.
* <b>`density_unit`</b>: An optional `string` from: `"in", "cm"`. Defaults to `"in"`.
    Unit used to specify `x_density` and `y_density`:
    pixels per inch (`'in'`) or centimeter (`'cm'`).
* <b>`x_density`</b>: An optional `int`. Defaults to `300`.
    Horizontal pixels per density unit.
* <b>`y_density`</b>: An optional `int`. Defaults to `300`.
    Vertical pixels per density unit.
* <b>`xmp_metadata`</b>: An optional `string`. Defaults to `""`.
    If not empty, embed this XMP metadata in the image header.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.