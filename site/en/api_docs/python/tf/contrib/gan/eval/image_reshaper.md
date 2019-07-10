page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.image_reshaper

A reshaped summary image.

### Aliases:

* `tf.contrib.gan.eval.eval_utils.image_reshaper`
* `tf.contrib.gan.eval.image_reshaper`

``` python
tf.contrib.gan.eval.image_reshaper(
    images,
    num_cols=None
)
```



Defined in [`contrib/gan/python/eval/python/eval_utils_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/python/eval_utils_impl.py).

<!-- Placeholder for "Used in" -->

Returns an image that will contain all elements in the list and will be
laid out in a nearly-square tiling pattern (e.g. 11 images will lead to a
3x4 tiled image).

#### Args:


* <b>`images`</b>: Image data to summarize. Can be an RGB or grayscale image, a list of
     such images, or a set of RGB images concatenated along the depth
     dimension. The shape of each image is assumed to be [batch_size,
     height, width, depth].
* <b>`num_cols`</b>: (Optional) If provided, this is the number of columns in the final
     output image grid. Otherwise, the number of columns is determined by
     the number of images.


#### Returns:

A summary image matching the input with automatic tiling if needed.
Output shape is [1, height, width, channels].
