

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.variable

``` python
variable(
    value,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Instantiates a variable and returns it.

#### Arguments:

    value: Numpy array, initial value of the tensor.
    dtype: Tensor type.
    name: Optional name string for the tensor.


#### Returns:

    A variable instance (with Keras metadata included).

Examples:
```python
    >>> from keras import backend as K
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val, dtype='float64', name='example_var')
    >>> K.dtype(kvar)
    'float64'
    >>> print(kvar)
    example_var
    >>> kvar.eval()
    array([[ 1.,  2.],
           [ 3.,  4.]])
```