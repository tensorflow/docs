page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.transpose


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L587-L614">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Transpose image(s) by swapping the height and width dimension.

### Aliases:

* `tf.compat.v1.image.transpose`
* `tf.compat.v1.image.transpose_image`
* `tf.compat.v2.image.transpose`


``` python
tf.image.transpose(
    image,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

 If `image` was 4-D, a 4-D float Tensor of shape
`[batch, width, height, channels]`
 If `image` was 3-D, a 3-D float Tensor of shape
`[width, height, channels]`



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.
