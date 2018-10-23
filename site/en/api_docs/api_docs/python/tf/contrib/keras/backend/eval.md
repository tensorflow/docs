

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.eval

``` python
eval(x)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Evaluates the value of a variable.

#### Arguments:

    x: A variable.


#### Returns:

    A Numpy array.

Examples:
```python
    >>> from keras import backend as K
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
    >>> K.eval(kvar)
    array([[ 1.,  2.],
           [ 3.,  4.]], dtype=float32)
```