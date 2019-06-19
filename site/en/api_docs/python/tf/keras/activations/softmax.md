page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.activations.softmax

``` python
tf.keras.activations.softmax(
    x,
    axis=-1
)
```



Defined in [`tensorflow/python/keras/activations.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/activations.py).

Softmax activation function.

#### Arguments:

* <b>`x `</b>: Tensor.
* <b>`axis`</b>: Integer, axis along which the softmax normalization is applied.


#### Returns:

Tensor, output of softmax transformation.


#### Raises:

* <b>`ValueError`</b>: In case `dim(x) == 1`.