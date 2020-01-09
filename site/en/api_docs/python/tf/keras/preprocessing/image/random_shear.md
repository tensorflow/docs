page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_shear


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/random_shear">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Performs a random spatial shear of a Numpy image tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/image/random_shear"><code>tf.compat.v1.keras.preprocessing.image.random_shear</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/image/random_shear"><code>tf.compat.v2.keras.preprocessing.image.random_shear</code></a>


``` python
tf.keras.preprocessing.image.random_shear(
    x,
    intensity,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0,
    interpolation_order=1
)
```



<!-- Placeholder for "Used in" -->

# Arguments
    x: Input tensor. Must be 3D.
    intensity: Transformation intensity in degrees.
    row_axis: Index of axis for rows in the input tensor.
    col_axis: Index of axis for columns in the input tensor.
    channel_axis: Index of axis for channels in the input tensor.
    fill_mode: Points outside the boundaries of the input
        are filled according to the given mode
        (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
    cval: Value used for points outside the boundaries
        of the input if `mode='constant'`.
    interpolation_order: int, order of spline interpolation.
        see `ndimage.interpolation.affine_transform`

# Returns
    Sheared Numpy image tensor.
