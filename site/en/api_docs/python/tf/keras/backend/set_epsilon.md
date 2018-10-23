

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.set_epsilon

``` python
set_epsilon(value)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Sets the value of the fuzz factor used in numeric expressions.

#### Arguments:

* <b>`value`</b>: float. New value of epsilon.

Example:
```python
    >>> from keras import backend as K
    >>> K.epsilon()
    1e-08
    >>> K.set_epsilon(1e-05)
    >>> K.epsilon()
    1e-05
```