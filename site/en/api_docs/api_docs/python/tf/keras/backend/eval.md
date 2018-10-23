

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.eval

``` python
eval(x)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

Evaluates the value of a variable.

#### Arguments:

* <b>`x`</b>: A variable.


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