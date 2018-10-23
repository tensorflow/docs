

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.ones

``` python
ones(
    shape,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates an all-ones tensor variable and returns it.

#### Arguments:

    shape: Tuple of integers, shape of returned Keras variable.
    dtype: String, data type of returned Keras variable.
    name: String, name of returned Keras variable.


#### Returns:

    A Keras variable, filled with `1.0`.

Example:
```python
    >>> from keras import backend as K
    >>> kvar = K.ones((3,4))
    >>> K.eval(kvar)
    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]], dtype=float32)
```