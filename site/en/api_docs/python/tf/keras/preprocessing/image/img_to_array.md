

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.img_to_array

``` python
tf.keras.preprocessing.image.img_to_array(
    img,
    data_format=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Converts a PIL Image instance to a Numpy array.

#### Arguments:

* <b>`img`</b>: PIL Image instance.
* <b>`data_format`</b>: Image data format.


#### Returns:

A 3D Numpy array.


#### Raises:

* <b>`ValueError`</b>: if invalid `img` or `data_format` is passed.