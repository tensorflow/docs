

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.count_params

``` python
count_params(x)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

Returns the number of scalars in a Keras variable.

#### Arguments:

* <b>`x`</b>: Keras variable.


#### Returns:

    Integer, the number of scalars in `x`.

Example:
```python
    >>> kvar = K.zeros((2,3))
    >>> K.count_params(kvar)
    6
    >>> K.eval(kvar)
    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]], dtype=float32)
```