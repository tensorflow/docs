

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.zeros

### `tf.contrib.keras.backend.zeros`

``` python
zeros(
    shape,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates an all-zeros variable and returns it.

#### Arguments:

    shape: Tuple of integers, shape of returned Keras variable
    dtype: String, data type of returned Keras variable
    name: String, name of returned Keras variable


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