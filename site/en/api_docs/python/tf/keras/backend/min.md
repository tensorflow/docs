page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.min

Minimum value in a tensor.

### Aliases:

* `tf.compat.v1.keras.backend.min`
* `tf.compat.v2.keras.backend.min`
* `tf.keras.backend.min`

``` python
tf.keras.backend.min(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to find minimum values.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
    If `keepdims` is `False`, the rank of the tensor is reduced
    by 1. If `keepdims` is `True`,
    the reduced dimension is retained with length 1.


#### Returns:

A tensor with minimum values of `x`.
