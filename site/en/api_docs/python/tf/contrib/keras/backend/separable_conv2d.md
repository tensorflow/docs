

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.separable_conv2d

### `tf.contrib.keras.backend.separable_conv2d`

``` python
separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1)
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

2D convolution with separable filters.

#### Arguments:

    x: input tensor
    depthwise_kernel: convolution kernel for the depthwise convolution.
    pointwise_kernel: kernel for the 1x1 convolution.
    strides: strides tuple (length 2).
    padding: padding mode, "valid" or "same".
    data_format: data format, "channels_first" or "channels_last".
    dilation_rate: tuple of integers,
        dilation rates for the separable convolution.


#### Returns:

    Output tensor.


#### Raises:

    ValueError: if `data_format` is neither `channels_last` or
    `channels_first`.