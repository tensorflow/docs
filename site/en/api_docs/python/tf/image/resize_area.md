page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.resize_area

Resize `images` to `size` using area interpolation.

### Aliases:

* `tf.compat.v1.image.resize_area`
* `tf.image.resize_area`

``` python
tf.image.resize_area(
    images,
    size,
    align_corners=False,
    name=None
)
```



Defined in generated file: `python/ops/gen_image_ops.py`.

<!-- Placeholder for "Used in" -->

Input images can be of different types but output images are always float.

The range of pixel values for the output image might be slightly different
from the range for the input image because of limited numerical precision.
To guarantee an output range, for example `[0.0, 1.0]`, apply
<a href="../../tf/clip_by_value"><code>tf.clip_by_value</code></a> to the output.

Each output pixel is computed by first transforming the pixel's footprint into
the input tensor and then averaging the pixels that intersect the footprint. An
input pixel's contribution to the average is weighted by the fraction of its
area that intersects the footprint.  This is the same as OpenCV's INTER_AREA.

#### Args:


* <b>`images`</b>: A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `half`, `float32`, `float64`.
  4-D with shape `[batch, height, width, channels]`.
* <b>`size`</b>:  A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
  new size for the images.
* <b>`align_corners`</b>: An optional `bool`. Defaults to `False`.
  If true, the centers of the 4 corner pixels of the input and output tensors are
  aligned, preserving the values at the corner pixels. Defaults to false.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.
