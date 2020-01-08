page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.psnr

``` python
tf.image.psnr(
    a,
    b,
    max_val,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/image_ops_impl.py).

Returns the Peak Signal-to-Noise Ratio between a and b.

This is intended to be used on signals (or images). Produces a PSNR value for
each image in batch.

The last three dimensions of input are expected to be [height, width, depth].

Example:

```python
    # Read images from file.
    im1 = tf.decode_png('path/to/im1.png')
    im2 = tf.decode_png('path/to/im2.png')
    # Compute PSNR over tf.uint8 Tensors.
    psnr1 = tf.image.psnr(im1, im2, max_val=255)

    # Compute PSNR over tf.float32 Tensors.
    im1 = tf.image.convert_image_dtype(im1, tf.float32)
    im2 = tf.image.convert_image_dtype(im2, tf.float32)
    psnr2 = tf.image.psnr(im1, im2, max_val=1.0)
    # psnr1 and psnr2 both have type tf.float32 and are almost equal.
```

#### Arguments:

* <b>`a`</b>: First set of images.
* <b>`b`</b>: Second set of images.
* <b>`max_val`</b>: The dynamic range of the images (i.e., the difference between the
    maximum the and minimum allowed values).
* <b>`name`</b>: Namespace to embed the computation in.


#### Returns:

The scalar PSNR between a and b. The returned tensor has type <a href="../../tf#float32"><code>tf.float32</code></a>
and shape [batch_size, 1].