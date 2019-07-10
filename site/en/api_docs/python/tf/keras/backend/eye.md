page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.eye

Instantiate an identity matrix and returns it.

### Aliases:

* `tf.compat.v1.keras.backend.eye`
* `tf.compat.v2.keras.backend.eye`
* `tf.keras.backend.eye`

``` python
tf.keras.backend.eye(
    size,
    dtype=None,
    name=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`size`</b>: Integer, number of rows/columns.
* <b>`dtype`</b>: String, data type of returned Keras variable.
* <b>`name`</b>: String, name of returned Keras variable.


#### Returns:

A Keras variable, an identity matrix.



#### Example:


```python
    >>> from keras import backend as K
    >>> kvar = K.eye(3)
    >>> K.eval(kvar)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]], dtype=float32)
```