page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_flip_left_right

``` python
tf.image.random_flip_left_right(
    image,
    seed=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Flipping, Rotating and Transposing](../../../../api_guides/python/image#Flipping_Rotating_and_Transposing)

Randomly flip an image horizontally (left to right).

With a 1 in 2 chance, outputs the contents of `image` flipped along the
second dimension, which is `width`.  Otherwise output the image as-is.

#### Args:

* <b>`image`</b>: A 3-D tensor of shape `[height, width, channels].`
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
    <a href="../../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.


#### Returns:

A 3-D tensor of the same type and shape as `image`.


#### Raises:

* <b>`ValueError`</b>: if the shape of `image` not supported.