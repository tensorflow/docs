

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.zeros

``` python
tf.keras.backend.zeros(
    shape,
    dtype=None,
    name=None
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Instantiates an all-zeros variable and returns it.

#### Arguments:

* <b>`shape`</b>: Tuple of integers, shape of returned Keras variable
* <b>`dtype`</b>: String, data type of returned Keras variable
* <b>`name`</b>: String, name of returned Keras variable


#### Returns:

    A variable (including Keras metadata), filled with `0.0`.
    Note that if `shape` was symbolic, we cannot return a variable,
    and will return a dynamically-shaped tensor instead.

Example:
```python
    >>> from keras import backend as K
    >>> kvar = K.zeros((3,4))
    >>> K.eval(kvar)
    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.]], dtype=float32)
```