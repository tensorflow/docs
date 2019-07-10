page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.int_shape

Returns the shape of tensor or variable as a tuple of int or None entries.

### Aliases:

* `tf.compat.v1.keras.backend.int_shape`
* `tf.compat.v2.keras.backend.int_shape`
* `tf.keras.backend.int_shape`

``` python
tf.keras.backend.int_shape(x)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.


#### Returns:

A tuple of integers (or None entries).



#### Examples:


```python
    >>> from keras import backend as K
    >>> input = K.placeholder(shape=(2, 4, 5))
    >>> K.int_shape(input)
    (2, 4, 5)
    >>> val = np.array([[1, 2], [3, 4]])
    >>> kvar = K.variable(value=val)
    >>> K.int_shape(kvar)
    (2, 2)
```