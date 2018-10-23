

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.bias_add

``` python
bias_add(
    x,
    bias,
    data_format=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Adds a bias vector to a tensor.

#### Arguments:

    x: Tensor or variable.
    bias: Bias tensor to add.
    data_format: string, `"channels_last"` or `"channels_first"`.


#### Returns:

    Output tensor.


#### Raises:

    ValueError: In one of the two cases below:
                1. invalid `data_format` argument.
                2. invalid bias shape.
                   the bias should be either a vector or
                   a tensor with ndim(x) - 1 dimension