

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.ssim

``` python
tf.image.ssim(
    img1,
    img2,
    max_val
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/image_ops_impl.py).

Computes SSIM index between img1 and img2.

This function is based on the standard SSIM implementation from:
Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image
quality assessment: from error visibility to structural similarity. IEEE
transactions on image processing.

Note: The true SSIM is only defined on grayscale.  This function does not
perform any colorspace transform.  (If input is already YUV, then it will
compute YUV SSIM average.)

Details:
  - 11x11 Gaussian filter of width 1.5 is used.
  - k1 = 0.01, k2 = 0.03 as in the original paper.

The image sizes must be at least 11x11 because of the filter size.

Example:

```python
    # Read images from file.
    im1 = tf.decode_png('path/to/im1.png')
    im2 = tf.decode_png('path/to/im2.png')
    # Compute SSIM over tf.uint8 Tensors.
    ssim1 = tf.image.ssim(im1, im2, max_val=255)

    # Compute SSIM over tf.float32 Tensors.
    im1 = tf.image.convert_image_dtype(im1, tf.float32)
    im2 = tf.image.convert_image_dtype(im2, tf.float32)
    ssim2 = tf.image.ssim(im1, im2, max_val=1.0)
    # ssim1 and ssim2 both have type tf.float32 and are almost equal.
```

#### Args:

* <b>`img1`</b>: First image batch.
* <b>`img2`</b>: Second image batch.
* <b>`max_val`</b>: The dynamic range of the images (i.e., the difference between the
    maximum the and minimum allowed values).


#### Returns:

A tensor containing an SSIM value for each image in batch.  Returned SSIM
values are in range (-1, 1], when pixel values are non-negative. Returns
a tensor with shape: broadcast(img1.shape[:-3], img2.shape[:-3]).