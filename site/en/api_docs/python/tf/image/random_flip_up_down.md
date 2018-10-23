

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_flip_up_down

``` python
tf.image.random_flip_up_down(
    image,
    seed=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Randomly flips an image vertically (upside down).

With a 1 in 2 chance, outputs the contents of `image` flipped along the first
dimension, which is `height`.  Otherwise output the image as-is.

#### Args:

* <b>`image`</b>: A 3-D tensor of shape `[height, width, channels].`
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
    <a href="../../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.


#### Returns:

A 3-D tensor of the same type and shape as `image`.


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.