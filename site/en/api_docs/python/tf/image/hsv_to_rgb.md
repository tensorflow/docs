page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.hsv_to_rgb


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/hsv_to_rgb">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_image_ops.py`



Convert one or more images from HSV to RGB.

### Aliases:

* <a href="/api_docs/python/tf/image/hsv_to_rgb"><code>tf.compat.v1.image.hsv_to_rgb</code></a>
* <a href="/api_docs/python/tf/image/hsv_to_rgb"><code>tf.compat.v2.image.hsv_to_rgb</code></a>


``` python
tf.image.hsv_to_rgb(
    images,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Outputs a tensor of the same shape as the `images` tensor, containing the RGB
value of the pixels. The output is only well defined if the value in `images`
are in `[0,1]`.

See `rgb_to_hsv` for a description of the HSV encoding.

#### Args:


* <b>`images`</b>: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `float64`.
  1-D or higher rank. HSV data to convert. Last dimension must be size 3.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `images`.
