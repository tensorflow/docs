page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.softmax

``` python
tf.keras.activations.softmax(
    x,
    axis=-1
)
```



Defined in [`tensorflow/python/keras/activations.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/activations.py).

Softmax activation function.

#### Arguments:

* <b>`x `</b>: Input tensor.
* <b>`axis`</b>: Integer, axis along which the softmax normalization is applied.


#### Returns:

Tensor, output of softmax transformation.


#### Raises:

* <b>`ValueError`</b>: In case `dim(x) == 1`.