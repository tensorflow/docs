page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ones_like

Instantiates an all-ones variable of the same shape as another tensor.

### Aliases:

* `tf.compat.v1.keras.backend.ones_like`
* `tf.compat.v2.keras.backend.ones_like`
* `tf.keras.backend.ones_like`

``` python
tf.keras.backend.ones_like(
    x,
    dtype=None,
    name=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Keras variable or tensor.
* <b>`dtype`</b>: String, dtype of returned Keras variable.
     None uses the dtype of x.
* <b>`name`</b>: String, name for the variable to create.


#### Returns:

A Keras variable with the shape of x filled with ones.



#### Example:


```python
    >>> from keras import backend as K
    >>> kvar = K.variable(np.random.random((2,3)))
    >>> kvar_ones = K.ones_like(kvar)
    >>> K.eval(kvar_ones)
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]], dtype=float32)
```