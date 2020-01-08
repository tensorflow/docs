page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_jpeg_quality

``` python
tf.image.adjust_jpeg_quality(
    image,
    jpeg_quality,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/image_ops_impl.py).

Adjust jpeg encoding quality of an RGB image.

This is a convenience method that adjusts jpeg encoding quality of an
RGB image.

`image` is an RGB image.  The image's encoding quality is adjusted
to `jpeg_quality`.
`jpeg_quality` must be in the interval `[0, 100]`.

#### Args:

* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`jpeg_quality`</b>: int.  jpeg encoding quality.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Adjusted image(s), same shape and DType as `image`.