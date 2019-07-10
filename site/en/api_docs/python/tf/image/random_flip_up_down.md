page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_flip_up_down

Randomly flips an image vertically (upside down).

### Aliases:

* `tf.compat.v1.image.random_flip_up_down`
* `tf.compat.v2.image.random_flip_up_down`
* `tf.image.random_flip_up_down`

``` python
tf.image.random_flip_up_down(
    image,
    seed=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

With a 1 in 2 chance, outputs the contents of `image` flipped along the first
dimension, which is `height`.  Otherwise output the image as-is.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
  <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.


#### Returns:

A tensor of the same type and shape as `image`.


#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.