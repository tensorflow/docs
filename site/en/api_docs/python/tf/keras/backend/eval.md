page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.eval

Evaluates the value of a variable.

### Aliases:

* `tf.compat.v1.keras.backend.eval`
* `tf.compat.v2.keras.backend.eval`
* `tf.keras.backend.eval`

``` python
tf.keras.backend.eval(x)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A variable.


#### Returns:

A Numpy array.



#### Examples:


```python
    >>> from keras import backend as K
    >>> kvar = K.variable(np.array([[1, 2], [3, 4]]), dtype='float32')
    >>> K.eval(kvar)
    array([[ 1.,  2.],
           [ 3.,  4.]], dtype=float32)
```