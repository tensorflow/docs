page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_gamma

``` python
tf.image.adjust_gamma(
    image,
    gamma=1,
    gain=1
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Image Adjustments](../../../../api_guides/python/image#Image_Adjustments)

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