page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.flip_left_right


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/flip_left_right">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L411-L429">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Flip an image horizontally (left to right).

### Aliases:

* <a href="/api_docs/python/tf/image/flip_left_right"><code>tf.compat.v1.image.flip_left_right</code></a>
* <a href="/api_docs/python/tf/image/flip_left_right"><code>tf.compat.v2.image.flip_left_right</code></a>


``` python
tf.image.flip_left_right(image)
```



<!-- Placeholder for "Used in" -->

Outputs the contents of `image` flipped along the width dimension.

See also `reverse()`.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.


#### Returns:

A tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.
