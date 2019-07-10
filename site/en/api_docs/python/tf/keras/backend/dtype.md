page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.dtype

Returns the dtype of a Keras tensor or variable, as a string.

### Aliases:

* `tf.compat.v1.keras.backend.dtype`
* `tf.compat.v2.keras.backend.dtype`
* `tf.keras.backend.dtype`

``` python
tf.keras.backend.dtype(x)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

String, dtype of `x`.



#### Examples:


```python
    >>> from keras import backend as K
    >>> K.dtype(K.placeholder(shape=(2,4,5)))
    'float32'
    >>> K.dtype(K.placeholder(shape=(2,4,5), dtype='float32'))
    'float32'
    >>> K.dtype(K.placeholder(shape=(2,4,5), dtype='float64'))
    'float64'
    # Keras variable
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]))
    >>> K.dtype(kvar)
    'float32'
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
    >>> K.dtype(kvar)
    'float32'
```