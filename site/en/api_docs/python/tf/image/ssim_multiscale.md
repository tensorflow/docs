page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.ssim_multiscale

Computes the MS-SSIM between img1 and img2.

### Aliases:

* `tf.compat.v1.image.ssim_multiscale`
* `tf.compat.v2.image.ssim_multiscale`
* `tf.image.ssim_multiscale`

``` python
tf.image.ssim_multiscale(
    img1,
    img2,
    max_val,
    power_factors=_MSSSIM_WEIGHTS,
    filter_size=11,
    filter_sigma=1.5,
    k1=0.01,
    k2=0.03
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

This function assumes that `img1` and `img2` are image batches, i.e. the last
three dimensions are [height, width, channels].

Note: The true SSIM is only defined on grayscale.  This function does not
perform any colorspace transform.  (If input is already YUV, then it will
compute YUV SSIM average.)

Original paper: Wang, Zhou, Eero P. Simoncelli, and Alan C. Bovik. "Multiscale
structural similarity for image quality assessment." Signals, Systems and
Computers, 2004.

#### Arguments:


* <b>`img1`</b>: First image batch.
* <b>`img2`</b>: Second image batch. Must have the same rank as img1.
* <b>`max_val`</b>: The dynamic range of the images (i.e., the difference between the
  maximum the and minimum allowed values).
* <b>`power_factors`</b>: Iterable of weights for each of the scales. The number of
  scales used is the length of the list. Index 0 is the unscaled
  resolution's weight and each increasing scale corresponds to the image
  being downsampled by 2.  Defaults to (0.0448, 0.2856, 0.3001, 0.2363,
  0.1333), which are the values obtained in the original paper.
* <b>`filter_size`</b>: Default value 11 (size of gaussian filter).
* <b>`filter_sigma`</b>: Default value 1.5 (width of gaussian filter).
* <b>`k1`</b>: Default value 0.01
* <b>`k2`</b>: Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so
  it would be better if we taken the values in range of 0< K2 <0.4).


#### Returns:

A tensor containing an MS-SSIM value for each image in batch.  The values
are in range [0, 1].  Returns a tensor with shape:
broadcast(img1.shape[:-3], img2.shape[:-3]).
