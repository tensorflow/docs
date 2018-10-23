

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.count_params

``` python
tf.keras.backend.count_params(x)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/keras/_impl/keras/backend.py).

Returns the static number of elements in a variable or tensor.

#### Arguments:

* <b>`x`</b>: Variable or tensor.


#### Returns:

    Integer, the number of scalars in `x`.

Example:
```python
    >>> kvar = K.zeros((2,3))
    >>> K.count_params(kvar)
    6
    >>> K.eval(kvar)
    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]], dtype=float32)
```