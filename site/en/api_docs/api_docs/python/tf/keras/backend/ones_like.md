

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.ones_like

``` python
ones_like(
    x,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

Instantiates an all-ones variable of the same shape as another tensor.

#### Arguments:

* <b>`x`</b>: Keras variable or tensor.
* <b>`dtype`</b>: String, dtype of returned Keras variable.
         None uses the dtype of x.
* <b>`name`</b>: String, name for the variable to create.


#### Returns:

    A Keras variable with the shape of x filled with ones.

Example:
```python
    >>> from keras import backend as K
    >>> kvar = K.variable(np.random.random((2,3)))
    >>> kvar_ones = K.ones_like(kvar)
    >>> K.eval(kvar_ones)
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]], dtype=float32)
```