page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.resize_with_crop_or_pad


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/resize_with_crop_or_pad">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L889-L1005">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Crops and/or pads an image to a target width and height.

### Aliases:

* <a href="/api_docs/python/tf/image/resize_with_crop_or_pad"><code>tf.compat.v1.image.resize_image_with_crop_or_pad</code></a>
* <a href="/api_docs/python/tf/image/resize_with_crop_or_pad"><code>tf.compat.v1.image.resize_with_crop_or_pad</code></a>
* <a href="/api_docs/python/tf/image/resize_with_crop_or_pad"><code>tf.compat.v2.image.resize_with_crop_or_pad</code></a>
* <a href="/api_docs/python/tf/image/resize_with_crop_or_pad"><code>tf.image.resize_image_with_crop_or_pad</code></a>


``` python
tf.image.resize_with_crop_or_pad(
    image,
    target_height,
    target_width
)
```



<!-- Placeholder for "Used in" -->

Resizes an image to a target width and height by either centrally
cropping the image or padding it evenly with zeros.

If `width` or `height` is greater than the specified `target_width` or
`target_height` respectively, this op centrally crops along that dimension.
If `width` or `height` is smaller than the specified `target_width` or
`target_height` respectively, this op centrally pads with 0 along that
dimension.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`target_height`</b>: Target height.
* <b>`target_width`</b>: Target width.


#### Raises:


* <b>`ValueError`</b>: if `target_height` or `target_width` are zero or negative.


#### Returns:

Cropped and/or padded image.
If `images` was 4-D, a 4-D float Tensor of shape
`[batch, new_height, new_width, channels]`.
If `images` was 3-D, a 3-D float Tensor of shape
`[new_height, new_width, channels]`.
