page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.to_dense

Converts a sparse tensor into a dense tensor and returns it.

### Aliases:

* `tf.compat.v1.keras.backend.to_dense`
* `tf.compat.v2.keras.backend.to_dense`
* `tf.keras.backend.to_dense`

``` python
tf.keras.backend.to_dense(tensor)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`tensor`</b>: A tensor instance (potentially sparse).


#### Returns:

A dense tensor.



#### Examples:


```python
    >>> from keras import backend as K
    >>> b = K.placeholder((2, 2), sparse=True)
    >>> print(K.is_sparse(b))
    True
    >>> c = K.to_dense(b)
    >>> print(K.is_sparse(c))
    False
```