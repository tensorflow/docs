

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.hsv_to_rgb

``` python
hsv_to_rgb(
    images,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Converting Between Colorspaces](../../../../api_guides/python/image#Converting_Between_Colorspaces)

Convert one or more images from HSV to RGB.

Outputs a tensor of the same shape as the `images` tensor, containing the RGB
value of the pixels. The output is only well defined if the value in `images`
are in `[0,1]`.

See `rgb_to_hsv` for a description of the HSV encoding.

#### Args:

* <b>`images`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    1-D or higher rank. HSV data to convert. Last dimension must be size 3.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `images`. `images` converted to RGB.