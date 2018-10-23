

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.resize_bilinear

``` python
tf.image.resize_bilinear(
    images,
    size,
    align_corners=False,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Resizing](../../../../api_guides/python/image#Resizing)

Resize `images` to `size` using bilinear interpolation.

Input images can be of different types but output images are always float.

#### Args:

* <b>`images`</b>: A `Tensor`. Must be one of the following types: `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `bfloat16`, `half`, `float32`, `float64`.
    4-D with shape `[batch, height, width, channels]`.
* <b>`size`</b>:  A 1-D int32 Tensor of 2 elements: `new_height, new_width`.  The
    new size for the images.
* <b>`align_corners`</b>: An optional `bool`. Defaults to `False`.
    If true, the centers of the 4 corner pixels of the input and output tensors are
    aligned, preserving the values at the corner pixels. Defaults to false.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.