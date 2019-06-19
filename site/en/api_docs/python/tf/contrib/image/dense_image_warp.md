

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.dense_image_warp

``` python
tf.contrib.image.dense_image_warp(
    image,
    flow,
    name='dense_image_warp'
)
```



Defined in [`tensorflow/contrib/image/python/ops/dense_image_warp.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/image/python/ops/dense_image_warp.py).

Image warping using per-pixel flow vectors.

Apply a non-linear warp to the image, where the warp is specified by a dense
flow field of offset vectors that define the correspondences of pixel values
in the output image back to locations in the  source image. Specifically, the
pixel value at output[b, j, i, c] is
images[b, j - flow[b, j, i, 0], i - flow[b, j, i, 1], c].

The locations specified by this formula do not necessarily map to an int
index. Therefore, the pixel value is obtained by bilinear
interpolation of the 4 nearest pixels around
(b, j - flow[b, j, i, 0], i - flow[b, j, i, 1]). For locations outside
of the image, we use the nearest pixel values at the image boundary.


#### Args:

* <b>`image`</b>: 4-D float `Tensor` with shape `[batch, height, width, channels]`.
* <b>`flow`</b>: A 4-D float `Tensor` with shape `[batch, height, width, 2]`.
* <b>`name`</b>: A name for the operation (optional).

  Note that image and flow can be of type tf.half, tf.float32, or tf.float64,
  and do not necessarily have to be the same type.


#### Returns:

A 4-D float `Tensor` with shape`[batch, height, width, channels]`
  and same type as input image.


#### Raises:

* <b>`ValueError`</b>: if height < 2 or width < 2 or the inputs have the wrong number
              of dimensions.