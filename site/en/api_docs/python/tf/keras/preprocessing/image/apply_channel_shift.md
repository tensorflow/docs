page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.apply_channel_shift

Performs a channel shift.

### Aliases:

* `tf.compat.v1.keras.preprocessing.image.apply_channel_shift`
* `tf.compat.v2.keras.preprocessing.image.apply_channel_shift`
* `tf.keras.preprocessing.image.apply_channel_shift`

``` python
tf.keras.preprocessing.image.apply_channel_shift(
    x,
    intensity,
    channel_axis=0
)
```

<!-- Placeholder for "Used in" -->

# Arguments
    x: Input tensor. Must be 3D.
    intensity: Transformation intensity.
    channel_axis: Index of axis for channels in the input tensor.

# Returns
    Numpy image tensor.