page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.crop_to_bounding_box


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L809-L886">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Crops an image to a specified bounding box.

### Aliases:

* `tf.compat.v1.image.crop_to_bounding_box`
* `tf.compat.v2.image.crop_to_bounding_box`


``` python
tf.image.crop_to_bounding_box(
    image,
    offset_height,
    offset_width,
    target_height,
    target_width
)
```



<!-- Placeholder for "Used in" -->

This op cuts a rectangular part out of `image`. The top-left corner of the
returned image is at `offset_height, offset_width` in `image`, and its
lower-right corner is at
`offset_height + target_height, offset_width + target_width`.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`offset_height`</b>: Vertical coordinate of the top-left corner of the result in
  the input.
* <b>`offset_width`</b>: Horizontal coordinate of the top-left corner of the result in
  the input.
* <b>`target_height`</b>: Height of the result.
* <b>`target_width`</b>: Width of the result.


#### Returns:

If `image` was 4-D, a 4-D float Tensor of shape
`[batch, target_height, target_width, channels]`
If `image` was 3-D, a 3-D float Tensor of shape
`[target_height, target_width, channels]`



#### Raises:


* <b>`ValueError`</b>: If the shape of `image` is incompatible with the `offset_*` or
  `target_*` arguments, or either `offset_height` or `offset_width` is
  negative, or either `target_height` or `target_width` is not positive.
