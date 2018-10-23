

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.image.random_rotation

``` python
tf.keras.preprocessing.image.random_rotation(
    x,
    rg,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0
)
```



Defined in [`tensorflow/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/image.py).

Performs a random rotation of a Numpy image tensor.

#### Arguments:

* <b>`x`</b>: Input tensor. Must be 3D.
* <b>`rg`</b>: Rotation range, in degrees.
* <b>`row_axis`</b>: Index of axis for rows in the input tensor.
* <b>`col_axis`</b>: Index of axis for columns in the input tensor.
* <b>`channel_axis`</b>: Index of axis for channels in the input tensor.
* <b>`fill_mode`</b>: Points outside the boundaries of the input
        are filled according to the given mode
        (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
* <b>`cval`</b>: Value used for points outside the boundaries
        of the input if `mode='constant'`.


#### Returns:

Rotated Numpy image tensor.