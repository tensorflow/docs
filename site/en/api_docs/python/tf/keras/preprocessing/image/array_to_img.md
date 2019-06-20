page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.array_to_img

``` python
tf.keras.preprocessing.image.array_to_img(
    x,
    data_format=None,
    scale=True
)
```



Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/image.py).

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