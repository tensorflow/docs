

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.to_dense

``` python
to_dense(tensor)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Converts a sparse tensor into a dense tensor and returns it.

#### Arguments:

* <b>`tensor`</b>: A tensor instance (potentially sparse).


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