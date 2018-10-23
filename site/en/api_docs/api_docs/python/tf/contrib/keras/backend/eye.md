

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.eye

``` python
eye(
    size,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Instantiate an identity matrix and returns it.

#### Arguments:

    size: Integer, number of rows/columns.
    dtype: String, data type of returned Keras variable.
    name: String, name of returned Keras variable.


#### Returns:

    A Keras variable, an identity matrix.

Example:
```python
    >>> from keras import backend as K
    >>> kvar = K.eye(3)
    >>> K.eval(kvar)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]], dtype=float32)
```