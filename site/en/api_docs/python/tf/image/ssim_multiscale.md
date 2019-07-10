page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.ssim_multiscale

``` python
tf.image.ssim_multiscale(
    img1,
    img2,
    max_val,
    power_factors=_MSSSIM_WEIGHTS
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/image_ops_impl.py).

Computes the MS-SSIM between img1 and img2.

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


#### Returns:

A tensor containing an MS-SSIM value for each image in batch.  The values
are in range [0, 1].  Returns a tensor with shape:
broadcast(img1.shape[:-3], img2.shape[:-3]).