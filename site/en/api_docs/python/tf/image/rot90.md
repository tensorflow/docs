page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rot90

Rotate image(s) counter-clockwise by 90 degrees.

### Aliases:

* `tf.compat.v1.image.rot90`
* `tf.compat.v2.image.rot90`
* `tf.image.rot90`

``` python
tf.image.rot90(
    image,
    k=1,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`k`</b>: A scalar integer. The number of times the image is rotated by 90 degrees.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A rotated tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.