page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_brightness

``` python
tf.keras.preprocessing.image.random_brightness(
    x,
    brightness_range
)
```



Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/image.py).

Performs a random adjustment of brightness of a Numpy image tensor.

#### Arguments:

* <b>`x`</b>: Input tensor. Must be 3D.
* <b>`brightness_range`</b>: Tuple of floats; range to pick a brightness value from.


#### Returns:

Brightness adjusted Numpy image tensor.


#### Raises:

* <b>`ValueError`</b>: if `brightness_range` isn't a tuple.