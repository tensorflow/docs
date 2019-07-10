page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_brightness

Performs a random brightness shift.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.random_brightness`
* `tf.compat.v2.keras.preprocessing.image.random_brightness`
* `tf.keras.preprocessing.image.random_brightness`

``` python
tf.keras.preprocessing.image.random_brightness(
    x,
    brightness_range
)
```

<!-- Placeholder for "Used in" -->

# Arguments
    x: Input tensor. Must be 3D.
    brightness_range: Tuple of floats; brightness range.
    channel_axis: Index of axis for channels in the input tensor.

# Returns
    Numpy image tensor.

# Raises
    ValueError if `brightness_range` isn't a tuple.