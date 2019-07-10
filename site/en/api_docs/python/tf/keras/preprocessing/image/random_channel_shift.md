page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_channel_shift

Performs a random channel shift.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.random_channel_shift`
* `tf.compat.v2.keras.preprocessing.image.random_channel_shift`
* `tf.keras.preprocessing.image.random_channel_shift`

``` python
tf.keras.preprocessing.image.random_channel_shift(
    x,
    intensity_range,
    channel_axis=0
)
```

<!-- Placeholder for "Used in" -->

# Arguments
    x: Input tensor. Must be 3D.
    intensity_range: Transformation intensity.
    channel_axis: Index of axis for channels in the input tensor.

# Returns
    Numpy image tensor.