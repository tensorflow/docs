page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.flip_left_right


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L411-L429">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Flip an image horizontally (left to right).

### Aliases:

* `tf.compat.v1.image.flip_left_right`
* `tf.compat.v2.image.flip_left_right`


``` python
tf.image.flip_left_right(image)
```



### Used in the tutorials:

* [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)



Outputs the contents of `image` flipped along the width dimension.

See also `reverse()`.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.


#### Returns:

A tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.
