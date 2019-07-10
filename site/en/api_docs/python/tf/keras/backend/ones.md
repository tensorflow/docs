page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ones

Instantiates an all-ones variable and returns it.

### Aliases:

* `tf.compat.v1.keras.backend.ones`
* `tf.compat.v2.keras.backend.ones`
* `tf.keras.backend.ones`

``` python
tf.keras.backend.ones(
    shape,
    dtype=None,
    name=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`shape`</b>: Tuple of integers, shape of returned Keras variable.
* <b>`dtype`</b>: String, data type of returned Keras variable.
* <b>`name`</b>: String, name of returned Keras variable.


#### Returns:

A Keras variable, filled with `1.0`.
Note that if `shape` was symbolic, we cannot return a variable,
and will return a dynamically-shaped tensor instead.



#### Example:


```python
    >>> from keras import backend as K
    >>> kvar = K.ones((3,4))
    >>> K.eval(kvar)
    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]], dtype=float32)
```