page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.load_img


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/image/load_img">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Loads an image into PIL format.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/image/load_img"><code>tf.compat.v1.keras.preprocessing.image.load_img</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/image/load_img"><code>tf.compat.v2.keras.preprocessing.image.load_img</code></a>


``` python
tf.keras.preprocessing.image.load_img(
    path,
    grayscale=False,
    color_mode='rgb',
    target_size=None,
    interpolation='nearest'
)
```



<!-- Placeholder for "Used in" -->

# Arguments
    path: Path to image file.
    grayscale: DEPRECATED use `color_mode="grayscale"`.
    color_mode: One of "grayscale", "rgb", "rgba". Default: "rgb".
        The desired image format.
    target_size: Either `None` (default to original size)
        or tuple of ints `(img_height, img_width)`.
    interpolation: Interpolation method used to resample the image if the
        target size is different from that of the loaded image.
        Supported methods are "nearest", "bilinear", and "bicubic".
        If PIL version 1.1.3 or newer is installed, "lanczos" is also
        supported. If PIL version 3.4.0 or newer is installed, "box" and
        "hamming" are also supported. By default, "nearest" is used.

# Returns
    A PIL Image instance.

# Raises
    ImportError: if PIL is not available.
    ValueError: if interpolation method is not supported.
