page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.separable_conv2d

``` python
tf.keras.backend.separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1)
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/backend.py).

2D convolution with separable filters.

#### Arguments:

* <b>`x`</b>: input tensor
* <b>`depthwise_kernel`</b>: convolution kernel for the depthwise convolution.
* <b>`pointwise_kernel`</b>: kernel for the 1x1 convolution.
* <b>`strides`</b>: strides tuple (length 2).
* <b>`padding`</b>: string, `"same"` or `"valid"`.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.
* <b>`dilation_rate`</b>: tuple of integers,
        dilation rates for the separable convolution.


#### Returns:

Output tensor.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is neither `channels_last` or
    `channels_first`.