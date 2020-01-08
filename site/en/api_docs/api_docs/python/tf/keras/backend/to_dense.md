

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.to_dense

``` python
tf.keras.backend.to_dense(tensor)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py).

Converts a sparse tensor into a dense tensor and returns it.

#### Arguments:

* <b>`tensor`</b>: A tensor instance (potentially sparse).


#### Returns:

    A dense tensor.

Examples:
```python
    >>> from keras import backend as K
    >>> b = K.placeholder((2, 2), sparse=True)
    >>> print(K.is_sparse(b))
    True
    >>> c = K.to_dense(b)
    >>> print(K.is_sparse(c))
    False
```