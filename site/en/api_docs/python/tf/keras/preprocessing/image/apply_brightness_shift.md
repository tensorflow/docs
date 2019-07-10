page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.apply_brightness_shift

Performs a brightness shift.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.apply_brightness_shift`
* `tf.compat.v2.keras.preprocessing.image.apply_brightness_shift`
* `tf.keras.preprocessing.image.apply_brightness_shift`

``` python
tf.keras.preprocessing.image.apply_brightness_shift(
    x,
    brightness
)
```

<!-- Placeholder for "Used in" -->

# Arguments
    x: Input tensor. Must be 3D.
    brightness: Float. The new brightness value.
    channel_axis: Index of axis for channels in the input tensor.

# Returns
    Numpy image tensor.

# Raises
    ValueError if `brightness_range` isn't a tuple.