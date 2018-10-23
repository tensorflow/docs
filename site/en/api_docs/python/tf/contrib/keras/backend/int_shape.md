

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.int_shape

### `tf.contrib.keras.backend.int_shape`

``` python
int_shape(x)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Returns the shape tensor or variable as a tuple of int or None entries.

#### Arguments:

    x: Tensor or variable.


#### Returns:

    A tuple of integers (or None entries).

Examples:
```python
    >>> from keras import backend as K
    >>> input = K.placeholder(shape=(2, 4, 5))
    >>> K.int_shape(input)
    (2, 4, 5)
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val)
    >>> K.int_shape(kvar)
    (2, 2)
```