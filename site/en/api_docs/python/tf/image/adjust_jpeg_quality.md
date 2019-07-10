page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_jpeg_quality

Adjust jpeg encoding quality of an RGB image.

### Aliases:

* `tf.compat.v1.image.adjust_jpeg_quality`
* `tf.compat.v2.image.adjust_jpeg_quality`
* `tf.image.adjust_jpeg_quality`

``` python
tf.image.adjust_jpeg_quality(
    image,
    jpeg_quality,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

This is a convenience method that adjusts jpeg encoding quality of an
RGB image.

`image` is an RGB image.  The image's encoding quality is adjusted
to `jpeg_quality`.
`jpeg_quality` must be in the interval `[0, 100]`.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`jpeg_quality`</b>: Python int or Tensor of type int32.  jpeg encoding quality.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Adjusted image(s), same shape and DType as `image`.
