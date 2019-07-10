page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rgb_to_yuv

Converts one or more images from RGB to YUV.

### Aliases:

* `tf.compat.v1.image.rgb_to_yuv`
* `tf.compat.v2.image.rgb_to_yuv`
* `tf.image.rgb_to_yuv`

``` python
tf.image.rgb_to_yuv(images)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the YUV
value of the pixels.
The output is only well defined if the value in images are in [0,1].

#### Args:


* <b>`images`</b>: 2-D or higher rank. Image data to convert. Last dimension must be
  size 3.


#### Returns:


* <b>`images`</b>: tensor with the same shape as `images`.