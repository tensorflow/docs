page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.grayscale_to_rgb

``` python
tf.image.grayscale_to_rgb(
    images,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/image_ops_impl.py).

Converts one or more images from Grayscale to RGB.

Outputs a tensor of the same `DType` and rank as `images`.  The size of the
last dimension of the output is 3, containing the RGB value of the pixels.

#### Args:

* <b>`images`</b>: The Grayscale tensor to convert. Last dimension must be size 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The converted grayscale image(s).