page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rgb_to_hsv

Converts one or more images from RGB to HSV.

### Aliases:

* `tf.compat.v1.image.rgb_to_hsv`
* `tf.compat.v2.image.rgb_to_hsv`
* `tf.image.rgb_to_hsv`

``` python
tf.image.rgb_to_hsv(
    images,
    name=None
)
```



Defined in generated file: `python/ops/gen_image_ops.py`.

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the HSV
value of the pixels. The output is only well defined if the value in `images`
are in `[0,1]`.

`output[..., 0]` contains hue, `output[..., 1]` contains saturation, and
`output[..., 2]` contains value. All HSV values are in `[0,1]`. A hue of 0
corresponds to pure red, hue 1/3 is pure green, and 2/3 is pure blue.

#### Args:


* <b>`images`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
  1-D or higher rank. RGB data to convert. Last dimension must be size 3.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `images`.
