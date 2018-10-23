

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.conv2d_transpose

### `tf.contrib.keras.backend.conv2d_transpose`

``` python
conv2d_transpose(
    x,
    kernel,
    output_shape,
    strides=(1, 1),
    padding='valid',
    data_format=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

2D deconvolution (i.e.

transposed convolution).

#### Arguments:

    x: Tensor or variable.
    kernel: kernel tensor.
    output_shape: 1D int tensor for the output shape.
    strides: strides tuple.
    padding: string, `"same"` or `"valid"`.
    data_format: `"channels_last"` or `"channels_first"`.
        Whether to use Theano or TensorFlow data format
        for inputs/kernels/ouputs.


#### Returns:

    A tensor, result of transposed 2D convolution.


#### Raises:

    ValueError: if `data_format` is neither `channels_last` or
    `channels_first`.