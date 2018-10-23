

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.preprocess_image

### Aliases:

* `tf.contrib.gan.eval.classifier_metrics.preprocess_image`
* `tf.contrib.gan.eval.preprocess_image`

``` python
tf.contrib.gan.eval.preprocess_image(
    images,
    height=INCEPTION_DEFAULT_IMAGE_SIZE,
    width=INCEPTION_DEFAULT_IMAGE_SIZE,
    scope=None
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/eval/python/classifier_metrics_impl.py).

Prepare a batch of images for evaluation.

This is the preprocessing portion of the graph from
http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz.

Note that it expects Tensors in [0, 255]. This function maps pixel values to
[-1, 1] and resizes to match the InceptionV1 network.

#### Args:

* <b>`images`</b>: 3-D or 4-D Tensor of images. Values are in [0, 255].
* <b>`height`</b>: Integer. Height of resized output image.
* <b>`width`</b>: Integer. Width of resized output image.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

3-D or 4-D float Tensor of prepared image(s). Values are in [-1, 1].