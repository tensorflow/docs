

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.random_brightness

``` python
random_brightness(
    image,
    max_delta,
    seed=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Image Adjustments](../../../../api_guides/python/image#Image_Adjustments)

Adjust the brightness of images by a random factor.

Equivalent to `adjust_brightness()` using a `delta` randomly picked in the
interval `[-max_delta, max_delta)`.

#### Args:

* <b>`image`</b>: An image.
* <b>`max_delta`</b>: float, must be non-negative.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
    [`tf.set_random_seed`](../../tf/set_random_seed)
    for behavior.


#### Returns:

The brightness-adjusted image.


#### Raises:

* <b>`ValueError`</b>: if `max_delta` is negative.