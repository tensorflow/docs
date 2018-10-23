

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.preprocess_image

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.preprocess_image`
* `tf.contrib.gan.eval.preprocess_image`

``` python
preprocess_image(
    image,
    height=INCEPTION_V3_DEFAULT_IMG_SIZE,
    width=INCEPTION_V3_DEFAULT_IMG_SIZE,
    central_fraction=0.875,
    scope=None
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Prepare one image for evaluation.

If height and width are specified it would output an image with that size by
applying resize_bilinear.

If central_fraction is specified it would crop the central fraction of the
input image.

#### Args:

* <b>`image`</b>: 3-D Tensor of image. If dtype is tf.float32 then the range should be
    [0, 1], otherwise it would converted to tf.float32 assuming that the range
    is [0, MAX], where MAX is largest positive representable number for
    int(8/16/32) data type (see `tf.image.convert_image_dtype` for details).
* <b>`height`</b>: integer
* <b>`width`</b>: integer
* <b>`central_fraction`</b>: Optional Float, fraction of the image to crop.
* <b>`scope`</b>: Optional scope for name_scope.

#### Returns:

3-D float Tensor of prepared image.