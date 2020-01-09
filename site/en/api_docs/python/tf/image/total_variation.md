page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.total_variation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L2320-L2388">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Calculate and return the total variation for one or more images.

### Aliases:

* `tf.compat.v1.image.total_variation`
* `tf.compat.v2.image.total_variation`


``` python
tf.image.total_variation(
    images,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The total variation is the sum of the absolute differences for neighboring
pixel-values in the input images. This measures how much noise is in the
images.

This can be used as a loss-function during optimization so as to suppress
noise in images. If you have a batch of images, then you should calculate
the scalar loss-value as the sum:
`loss = tf.reduce_sum(tf.image.total_variation(images))`

This implements the anisotropic 2-D version of the formula described here:

https://en.wikipedia.org/wiki/Total_variation_denoising

#### Args:


* <b>`images`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`name`</b>: A name for the operation (optional).


#### Raises:


* <b>`ValueError`</b>: if images.shape is not a 3-D or 4-D vector.


#### Returns:

The total variation of `images`.

If `images` was 4-D, return a 1-D float Tensor of shape `[batch]` with the
total variation for each image in the batch.
If `images` was 3-D, return a scalar float with the total variation for
that image.
