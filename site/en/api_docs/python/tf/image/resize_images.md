

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.resize_images

``` python
resize_images(
    images,
    size,
    method=ResizeMethod.BILINEAR,
    align_corners=False
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Resizing](../../../../api_guides/python/image#Resizing)

Resize `images` to `size` using the specified `method`.

Resized images will be distorted if their original aspect ratio is not
the same as `size`.  To avoid distortions see
<a href="../../tf/image/resize_image_with_crop_or_pad"><code>tf.image.resize_image_with_crop_or_pad</code></a>.

`method` can be one of:

*   <b>`ResizeMethod.BILINEAR`</b>: [Bilinear interpolation.](
  https://en.wikipedia.org/wiki/Bilinear_interpolation)
*   <b>`ResizeMethod.NEAREST_NEIGHBOR`</b>: [Nearest neighbor interpolation.](
  https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
*   <b>`ResizeMethod.BICUBIC`</b>: [Bicubic interpolation.](
  https://en.wikipedia.org/wiki/Bicubic_interpolation)
*   <b>`ResizeMethod.AREA`</b>: Area interpolation.

The return value has the same type as `images` if `method` is
`ResizeMethod.NEAREST_NEIGHBOR`. It will also have the same type as `images`
if the size of `images` can be statically determined to be the same as `size`,
because `images` is returned in this case. Otherwise, the return value has
type `float32`.

#### Args:

* <b>`images`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or
          3-D Tensor of shape `[height, width, channels]`.
* <b>`size`</b>: A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
        new size for the images.
* <b>`method`</b>: ResizeMethod.  Defaults to `ResizeMethod.BILINEAR`.
* <b>`align_corners`</b>: bool. If true, exactly align all 4 corners of the input and
                 output. Defaults to `false`.


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