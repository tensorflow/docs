

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.pool3d

``` python
pool3d(
    x,
    pool_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    pool_mode='max'
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

3D Pooling.

#### Arguments:

    x: Tensor or variable.
    pool_size: tuple of 3 integers.
    strides: tuple of 3 integers.
    padding: one of `"valid"`, `"same"`.
    data_format: one of `"channels_first"`, `"channels_last"`.
    pool_mode: one of `"max"`, `"avg"`.


#### Returns:

    A tensor, result of 3D pooling.


#### Raises:

    ValueError: if `data_format` is neither
        `channels_last` or `channels_first`.
    ValueError: if `pool_mode` is neither `max` or `avg`.