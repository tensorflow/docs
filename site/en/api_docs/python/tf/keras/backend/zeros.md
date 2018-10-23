

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.zeros

``` python
zeros(
    shape,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Instantiates an all-zeros variable and returns it.

#### Arguments:

* <b>`shape`</b>: Tuple of integers, shape of returned Keras variable
* <b>`dtype`</b>: String, data type of returned Keras variable
* <b>`name`</b>: String, name of returned Keras variable


#### Returns:

    A variable (including Keras metadata), filled with `0.0`.

Example:
```python
    >>> from keras import backend as K
    >>> kvar = K.zeros((3,4))
    >>> K.eval(kvar)
    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.]], dtype=float32)
```