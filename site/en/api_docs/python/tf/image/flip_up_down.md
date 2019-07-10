page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.flip_up_down

Flip an image vertically (upside down).

### Aliases:

* `tf.compat.v1.image.flip_up_down`
* `tf.compat.v2.image.flip_up_down`
* `tf.image.flip_up_down`

``` python
tf.image.flip_up_down(image)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Outputs the contents of `image` flipped along the height dimension.

See also `reverse()`.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.


#### Returns:

A tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.