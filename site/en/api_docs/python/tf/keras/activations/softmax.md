

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.activations.softmax

``` python
softmax(
    x,
    axis=-1
)
```



Defined in [`tensorflow/python/keras/_impl/keras/activations.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/activations.py).

Softmax activation function.

#### Arguments:

* <b>`x `</b>: Tensor.
* <b>`axis`</b>: Integer, axis along which the softmax normalization is applied.


#### Returns:

Tensor, output of softmax transformation.


#### Raises:

* <b>`ValueError`</b>: In case `dim(x) == 1`.