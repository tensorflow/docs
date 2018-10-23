

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.backend.to_dense

### `tf.contrib.keras.backend.to_dense`

``` python
to_dense(tensor)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/backend.py).

Converts a sparse tensor into a dense tensor and returns it.

#### Arguments:

    tensor: A tensor instance (potentially sparse).


#### Returns:

    A dense tensor.

Examples:
```python
    >>> from keras import backend as K
    >>> b = K.placeholder((2, 2), sparse=True)
    >>> print(K.is_sparse(b))
    True
    >>> c = K.to_dense(b)
    >>> print(K.is_sparse(c))
    False
```