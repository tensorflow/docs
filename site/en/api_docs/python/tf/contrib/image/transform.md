page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.transform

``` python
tf.contrib.image.transform(
    images,
    transforms,
    interpolation='NEAREST',
    output_shape=None,
    name=None
)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/contrib/image/python/ops/image_ops.py).

Applies the given transform(s) to the image(s).

#### Args:

* <b>`images`</b>: A tensor of shape (num_images, num_rows, num_columns, num_channels)
     (NHWC), (num_rows, num_columns, num_channels) (HWC), or
     (num_rows, num_columns) (HW). The rank must be statically known (the
     shape is not `TensorShape(None)`.
* <b>`transforms`</b>: Projective transform matrix/matrices. A vector of length 8 or
     tensor of size N x 8. If one row of transforms is
     [a0, a1, a2, b0, b1, b2, c0, c1], then it maps the *output* point
     `(x, y)` to a transformed *input* point
     `(x', y') = ((a0 x + a1 y + a2) / k, (b0 x + b1 y + b2) / k)`,
     where `k = c0 x + c1 y + 1`. The transforms are *inverted* compared to
     the transform mapping input points to output points. Note that gradients
     are not backpropagated into transformation parameters.
* <b>`interpolation`</b>: Interpolation mode. Supported values: "NEAREST", "BILINEAR".
* <b>`output_shape`</b>: Output dimesion after the transform, [height, width].
     If None, output is the same size as input image.

* <b>`name`</b>: The name of the op.


#### Returns:

Image(s) with the same type and shape as `images`, with the given
transform(s) applied. Transformed coordinates outside of the input image
will be filled with zeros.


#### Raises:

* <b>`TypeError`</b>: If `image` is an invalid type.
* <b>`ValueError`</b>: If output shape is not 1-D int32 Tensor.