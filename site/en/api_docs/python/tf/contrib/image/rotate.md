page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.rotate

``` python
tf.contrib.image.rotate(
    images,
    angles,
    interpolation='NEAREST',
    name=None
)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/image/python/ops/image_ops.py).

Rotate image(s) counterclockwise by the passed angle(s) in radians.

#### Args:

* <b>`images`</b>: A tensor of shape (num_images, num_rows, num_columns, num_channels)
     (NHWC), (num_rows, num_columns, num_channels) (HWC), or
     (num_rows, num_columns) (HW). The rank must be statically known (the
     shape is not `TensorShape(None)`.
* <b>`angles`</b>: A scalar angle to rotate all images by, or (if images has rank 4)
     a vector of length num_images, with an angle for each image in the batch.
* <b>`interpolation`</b>: Interpolation mode. Supported values: "NEAREST", "BILINEAR".
* <b>`name`</b>: The name of the op.


#### Returns:

Image(s) with the same type and shape as `images`, rotated by the given
angle(s). Empty space due to the rotation will be filled with zeros.


#### Raises:

* <b>`TypeError`</b>: If `image` is an invalid type.