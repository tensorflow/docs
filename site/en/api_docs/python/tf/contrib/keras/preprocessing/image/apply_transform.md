

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.preprocessing.image.apply_transform

### `tf.contrib.keras.preprocessing.image.apply_transform`

``` python
apply_transform(
    x,
    transform_matrix,
    channel_axis=0,
    fill_mode='nearest',
    cval=0.0
)
```



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/image.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/preprocessing/image.py).

Apply the image transformation specified by a matrix.

#### Arguments:

    x: 2D numpy array, single image.
    transform_matrix: Numpy array specifying the geometric transformation.
    channel_axis: Index of axis for channels in the input tensor.
    fill_mode: Points outside the boundaries of the input
        are filled according to the given mode
        (one of `{'constant', 'nearest', 'reflect', 'wrap'}`).
    cval: Value used for points outside the boundaries
        of the input if `mode='constant'`.


#### Returns:

    The transformed version of the input.