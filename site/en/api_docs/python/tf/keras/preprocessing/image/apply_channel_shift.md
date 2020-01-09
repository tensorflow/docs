page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.apply_channel_shift


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/apply_channel_shift">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Performs a channel shift.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/image/apply_channel_shift"><code>tf.compat.v1.keras.preprocessing.image.apply_channel_shift</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/image/apply_channel_shift"><code>tf.compat.v2.keras.preprocessing.image.apply_channel_shift</code></a>


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
