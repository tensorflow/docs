

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.is_sparse

``` python
is_sparse(tensor)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Returns whether a tensor is a sparse tensor.

#### Arguments:

    tensor: A tensor instance.


#### Returns:

    A boolean.

Example:
```python
    >>> from keras import backend as K
    >>> a = K.placeholder((2, 2), sparse=False)
    >>> print(K.is_sparse(a))
    False
    >>> b = K.placeholder((2, 2), sparse=True)
    >>> print(K.is_sparse(b))
    True
```