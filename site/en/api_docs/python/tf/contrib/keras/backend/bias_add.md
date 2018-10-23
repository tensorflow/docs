

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.bias_add

### `tf.contrib.keras.backend.bias_add`

``` python
bias_add(
    x,
    bias,
    data_format=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Adds a bias vector to a tensor.

#### Arguments:

    x: Tensor or variable.
    bias: Bias tensor to add.
    data_format: Data format for 3D, 4D or 5D tensors:
        one of "channels_first", "channels_last".


#### Returns:

    Output tensor.


#### Raises:

    ValueError: In case of invalid `data_format` argument.