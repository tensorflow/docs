page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.prod

Multiplies the values in a tensor, alongside the specified axis.

### Aliases:

* `tf.compat.v1.keras.backend.prod`
* `tf.compat.v2.keras.backend.prod`
* `tf.keras.backend.prod`

``` python
tf.keras.backend.prod(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to compute the product.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
    If `keepdims` is `False`, the rank of the tensor is reduced
    by 1. If `keepdims` is `True`,
    the reduced dimension is retained with length 1.


#### Returns:

A tensor with the product of elements of `x`.
