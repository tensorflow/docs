

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.image.random_contrast

### `tf.image.random_contrast`

``` python
random_contrast(
    image,
    lower,
    upper,
    seed=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Image Adjustments](../../../../api_guides/python/image#Image_Adjustments)

Adjust the contrast of an image by a random factor.

Equivalent to `adjust_contrast()` but uses a `contrast_factor` randomly
picked in the interval `[lower, upper]`.

#### Args:

* <b>`image`</b>: An image tensor with 3 or more dimensions.
* <b>`lower`</b>: float.  Lower bound for the random contrast factor.
* <b>`upper`</b>: float.  Upper bound for the random contrast factor.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
    [`tf.set_random_seed`](../../tf/set_random_seed)
    for behavior.


#### Returns:

  The contrast-adjusted tensor.


#### Raises:

* <b>`ValueError`</b>: if `upper <= lower` or if `lower < 0`.