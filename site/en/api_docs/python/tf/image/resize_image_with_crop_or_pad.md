page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.resize_image_with_crop_or_pad

``` python
tf.image.resize_image_with_crop_or_pad(
    image,
    target_height,
    target_width
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Cropping](../../../../api_guides/python/image#Cropping)

Crops and/or pads an image to a target width and height.

Resizes an image to a target width and height by either centrally
cropping the image or padding it evenly with zeros.

If `width` or `height` is greater than the specified `target_width` or
`target_height` respectively, this op centrally crops along that dimension.
If `width` or `height` is smaller than the specified `target_width` or
`target_height` respectively, this op centrally pads with 0 along that
dimension.

#### Args:

* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or
         3-D Tensor of shape `[height, width, channels]`.
* <b>`target_height`</b>: Target height.
* <b>`target_width`</b>: Target width.


#### Raises:

* <b>`ValueError`</b>: if `target_height` or `target_width` are zero or negative.


#### Returns:

Cropped and/or padded image.
If `images` was 4-D, a 4-D float Tensor of shape
`[batch, new_height, new_width, channels]`.
If `images` was 3-D, a 3-D float Tensor of shape
`[new_height, new_width, channels]`.