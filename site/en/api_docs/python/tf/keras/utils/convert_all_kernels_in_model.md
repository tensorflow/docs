page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.convert_all_kernels_in_model

``` python
tf.keras.utils.convert_all_kernels_in_model(model)
```



Defined in [`tensorflow/python/keras/utils/layer_utils.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/keras/utils/layer_utils.py).

Converts all convolution kernels in a model from Theano to TensorFlow.

Also works from TensorFlow to Theano.

#### Arguments:

* <b>`model`</b>: target model for the conversion.