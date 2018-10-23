

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.image.random_shift

``` python
tf.keras.preprocessing.image.random_shift(
    x,
    wrg,
    hrg,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/preprocessing/image.py).

Performs a random spatial shift of a Numpy image tensor.

#### Arguments:

* <b>`x`</b>: Input tensor. Must be 3D.
* <b>`wrg`</b>: Width shift range, as a float fraction of the width.
* <b>`hrg`</b>: Height shift range, as a float fraction of the height.
* <b>`row_axis`</b>: Index of axis for rows in the input tensor.
* <b>`col_axis`</b>: Index of axis for columns in the input tensor.
* <b>`channel_axis`</b>: Index of axis for channels in the input tensor.
* <b>`fill_mode`</b>: Points outside the boundaries of the input
        are filled according to the given mode
        (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
* <b>`cval`</b>: Value used for points outside the boundaries
        of the input if `mode='constant'`.


#### Returns:

Shifted Numpy image tensor.