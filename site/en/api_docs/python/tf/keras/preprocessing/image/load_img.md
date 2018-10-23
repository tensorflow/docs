

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.load_img

``` python
tf.keras.preprocessing.image.load_img(
    path,
    grayscale=False,
    target_size=None,
    interpolation='nearest'
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Loads an image into PIL format.

#### Arguments:

* <b>`path`</b>: Path to image file
* <b>`grayscale`</b>: Boolean, whether to load the image as grayscale.
* <b>`target_size`</b>: Either `None` (default to original size)
        or tuple of ints `(img_height, img_width)`.
* <b>`interpolation`</b>: Interpolation method used to resample the image if the
        target size is different from that of the loaded image.
        Supported methods are "nearest", "bilinear", and "bicubic".
        If PIL version 1.1.3 or newer is installed, "lanczos" is also
        supported. If PIL version 3.4.0 or newer is installed, "box" and
        "hamming" are also supported. By default, "nearest" is used.


#### Returns:

A PIL Image instance.


#### Raises:

* <b>`ImportError`</b>: if PIL is not available.
* <b>`ValueError`</b>: if interpolation method is not supported.