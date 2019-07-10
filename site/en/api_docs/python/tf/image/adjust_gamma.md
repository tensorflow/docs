page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_gamma

``` python
tf.image.adjust_gamma(
    image,
    gamma=1,
    gain=1
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/image_ops_impl.py).

Performs Gamma Correction on the input image.

Also known as Power Law Transform. This function transforms the
input image pixelwise according to the equation `Out = In**gamma`
after scaling each pixel to the range 0 to 1.

#### Args:

* <b>`image `</b>: A Tensor.
* <b>`gamma `</b>: A scalar or tensor. Non negative real number.
* <b>`gain  `</b>: A scalar or tensor. The constant multiplier.


#### Returns:

A Tensor. Gamma corrected output image.


#### Raises:

* <b>`ValueError`</b>: If gamma is negative.

Notes:
  For gamma greater than 1, the histogram will shift towards left and
  the output image will be darker than the input image.
  For gamma less than 1, the histogram will shift towards right and
  the output image will be brighter than the input image.

References:
  [1] http://en.wikipedia.org/wiki/Gamma_correction