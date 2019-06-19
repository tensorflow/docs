page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.is_sparse

``` python
tf.keras.backend.is_sparse(tensor)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Returns whether a tensor is a sparse tensor.

#### Arguments:

* <b>`tensor`</b>: A tensor instance.


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