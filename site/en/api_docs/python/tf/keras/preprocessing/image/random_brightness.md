page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_brightness


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/random_brightness">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Performs a random brightness shift.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/image/random_brightness"><code>tf.compat.v1.keras.preprocessing.image.random_brightness</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/image/random_brightness"><code>tf.compat.v2.keras.preprocessing.image.random_brightness</code></a>


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
