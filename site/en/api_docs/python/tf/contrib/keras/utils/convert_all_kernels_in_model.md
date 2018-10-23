

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.utils.convert_all_kernels_in_model

### `tf.contrib.keras.utils.convert_all_kernels_in_model`

``` python
convert_all_kernels_in_model(model)
```



Defined in [`tensorflow/contrib/keras/python/keras/utils/layer_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/utils/layer_utils.py).

Converts all convolution kernels in a model from Theano to TensorFlow.

Also works from TensorFlow to Theano.

#### Arguments:

    model: target model for the conversion.