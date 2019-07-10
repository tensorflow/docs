page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.resize_images

Resize `images` to `size` using the specified `method`.

### Aliases:

* `tf.compat.v1.image.resize`
* `tf.compat.v1.image.resize_images`
* `tf.image.resize`
* `tf.image.resize_images`

``` python
tf.image.resize_images(
    images,
    size,
    method=ResizeMethodV1.BILINEAR,
    align_corners=False,
    preserve_aspect_ratio=False,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Resized images will be distorted if their original aspect ratio is not
the same as `size`.  To avoid distortions see
<a href="../../tf/image/resize_image_with_pad"><code>tf.compat.v1.image.resize_image_with_pad</code></a>.

`method` can be one of:

*   <b><a href="../../tf/image/ResizeMethod#BILINEAR"><code>ResizeMethod.BILINEAR</code></a></b>: [Bilinear interpolation.](
  https://en.wikipedia.org/wiki/Bilinear_interpolation)
*   <b><a href="../../tf/image/ResizeMethod#NEAREST_NEIGHBOR"><code>ResizeMethod.NEAREST_NEIGHBOR</code></a></b>: [Nearest neighbor interpolation.](
  https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
*   <b><a href="../../tf/image/ResizeMethod#BICUBIC"><code>ResizeMethod.BICUBIC</code></a></b>: [Bicubic interpolation.](
  https://en.wikipedia.org/wiki/Bicubic_interpolation)
*   <b><a href="../../tf/image/ResizeMethod#AREA"><code>ResizeMethod.AREA</code></a></b>: Area interpolation.

The return value has the same type as `images` if `method` is
<a href="../../tf/image/ResizeMethod#NEAREST_NEIGHBOR"><code>ResizeMethod.NEAREST_NEIGHBOR</code></a>. It will also have the same type as `images`
if the size of `images` can be statically determined to be the same as `size`,
because `images` is returned in this case. Otherwise, the return value has
type `float32`.

#### Args:


* <b>`images`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`size`</b>: A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The new
  size for the images.
* <b>`method`</b>: ResizeMethod.  Defaults to <a href="../../tf/image/ResizeMethod#BILINEAR"><code>ResizeMethod.BILINEAR</code></a>.
* <b>`align_corners`</b>: bool.  If True, the centers of the 4 corner pixels of the
  input and output tensors are aligned, preserving the values at the corner
  pixels. Defaults to `False`.
* <b>`preserve_aspect_ratio`</b>: Whether to preserve the aspect ratio. If this is set,
  then `images` will be resized to a size that fits in `size` while
  preserving the aspect ratio of the original image. Scales up the image if
  `size` is bigger than the current size of the `image`. Defaults to False.
* <b>`name`</b>: A name for this operation (optional).


#### Raises:


* <b>`ValueError`</b>: if the shape of `images` is incompatible with the
  shape arguments to this function
* <b>`ValueError`</b>: if `size` has invalid shape or type.
* <b>`ValueError`</b>: if an unsupported resize method is specified.


#### Returns:

If `images` was 4-D, a 4-D float Tensor of shape
`[batch, new_height, new_width, channels]`.
If `images` was 3-D, a 3-D float Tensor of shape
`[new_height, new_width, channels]`.
