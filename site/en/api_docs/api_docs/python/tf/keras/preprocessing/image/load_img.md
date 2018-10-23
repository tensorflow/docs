

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.load_img

``` python
load_img(
    path,
    grayscale=False,
    target_size=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Loads an image into PIL format.

#### Arguments:

* <b>`path`</b>: Path to image file
* <b>`grayscale`</b>: Boolean, whether to load the image as grayscale.
* <b>`target_size`</b>: Either `None` (default to original size)
        or tuple of ints `(img_height, img_width)`.


#### Returns:

A PIL Image instance.


#### Raises:

* <b>`ImportError`</b>: if PIL is not available.