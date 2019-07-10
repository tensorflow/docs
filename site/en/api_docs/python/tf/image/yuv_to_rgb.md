page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.yuv_to_rgb

Converts one or more images from YUV to RGB.

### Aliases:

* `tf.compat.v1.image.yuv_to_rgb`
* `tf.compat.v2.image.yuv_to_rgb`
* `tf.image.yuv_to_rgb`

``` python
tf.image.yuv_to_rgb(images)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the RGB
value of the pixels.
The output is only well defined if the Y value in images are in [0,1],
U and V value are in [-0.5,0.5].

#### Args:


* <b>`images`</b>: 2-D or higher rank. Image data to convert. Last dimension must be
  size 3.


#### Returns:


* <b>`images`</b>: tensor with the same shape as `images`.