

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.conv3d

``` python
conv3d(
    x,
    kernel,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    dilation_rate=(1, 1, 1)
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

3D convolution.

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`kernel`</b>: kernel tensor.
* <b>`strides`</b>: strides tuple.
* <b>`padding`</b>: string, `"same"` or `"valid"`.
* <b>`data_format`</b>: `"channels_last"` or `"channels_first"`.
        Whether to use Theano or TensorFlow data format
        for inputs/kernels/outputs.
* <b>`dilation_rate`</b>: tuple of 3 integers.


#### Returns:

A tensor, result of 3D convolution.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is neither `channels_last` or
    `channels_first`.