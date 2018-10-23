

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.preprocessing.image.random_rotation

### `tf.contrib.keras.preprocessing.image.random_rotation`

``` python
random_rotation(
    x,
    rg,
    row_axis=1,
    col_axis=2,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0
)
```



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Performs a random rotation of a Numpy image tensor.

#### Arguments:

    x: Input tensor. Must be 3D.
    rg: Rotation range, in degrees.
    row_axis: Index of axis for rows in the input tensor.
    col_axis: Index of axis for columns in the input tensor.
    channel_axis: Index of axis for channels in the input tensor.
    fill_mode: Points outside the boundaries of the input
        are filled according to the given mode
        (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
    cval: Value used for points outside the boundaries
        of the input if `mode='constant'`.


#### Returns:

    Rotated Numpy image tensor.