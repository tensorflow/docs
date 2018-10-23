

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.preprocessing.image.array_to_img

``` python
array_to_img(
    x,
    data_format=None,
    scale=True
)
```



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Converts a 3D Numpy array to a PIL Image instance.

#### Arguments:

    x: Input Numpy array.
    data_format: Image data format.
    scale: Whether to rescale image values
        to be within [0, 255].


#### Returns:

    A PIL Image instance.


#### Raises:

    ImportError: if PIL is not available.
    ValueError: if invalid `x` or `data_format` is passed.