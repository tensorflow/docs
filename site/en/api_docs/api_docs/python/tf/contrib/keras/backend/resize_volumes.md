

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.resize_volumes

``` python
resize_volumes(
    x,
    depth_factor,
    height_factor,
    width_factor,
    data_format
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Resizes the volume contained in a 5D tensor.

#### Arguments:

    x: Tensor or variable to resize.
    depth_factor: Positive integer.
    height_factor: Positive integer.
    width_factor: Positive integer.
    data_format: One of `"channels_first"`, `"channels_last"`.


#### Returns:

    A tensor.


#### Raises:

    ValueError: if `data_format` is neither
        `channels_last` or `channels_first`.