

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.array_to_img

``` python
tf.keras.preprocessing.image.array_to_img(
    x,
    data_format=None,
    scale=True
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Converts a 3D Numpy array to a PIL Image instance.

#### Arguments:

* <b>`x`</b>: Input Numpy array.
* <b>`data_format`</b>: Image data format.
* <b>`scale`</b>: Whether to rescale image values
        to be within [0, 255].


#### Returns:

A PIL Image instance.


#### Raises:

* <b>`ImportError`</b>: if PIL is not available.
* <b>`ValueError`</b>: if invalid `x` or `data_format` is passed.