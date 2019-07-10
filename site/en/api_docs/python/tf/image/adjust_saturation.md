page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_saturation

Adjust saturation of RGB images.

### Aliases:

* `tf.compat.v1.image.adjust_saturation`
* `tf.compat.v2.image.adjust_saturation`
* `tf.image.adjust_saturation`

``` python
tf.image.adjust_saturation(
    image,
    saturation_factor,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

This is a convenience method that converts RGB images to float
representation, converts them to HSV, add an offset to the saturation channel,
converts back to RGB and then back to the original data type. If several
adjustments are chained it is advisable to minimize the number of redundant
conversions.

`image` is an RGB image or images.  The image saturation is adjusted by
converting the images to HSV and multiplying the saturation (S) channel by
`saturation_factor` and clipping. The images are then converted back to RGB.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`saturation_factor`</b>: float. Factor to multiply the saturation by.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Adjusted image(s), same shape and DType as `image`.
