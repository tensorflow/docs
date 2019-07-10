page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.grayscale_to_rgb

Converts one or more images from Grayscale to RGB.

### Aliases:

* `tf.compat.v1.image.grayscale_to_rgb`
* `tf.compat.v2.image.grayscale_to_rgb`
* `tf.image.grayscale_to_rgb`

``` python
tf.image.grayscale_to_rgb(
    images,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same `DType` and rank as `images`.  The size of the
last dimension of the output is 3, containing the RGB value of the pixels.
The input images' last dimension must be size 1.

#### Args:


* <b>`images`</b>: The Grayscale tensor to convert. Last dimension must be size 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The converted grayscale image(s).
