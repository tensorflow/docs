page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.std

``` python
tf.keras.backend.std(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/backend.py).

Standard deviation of a tensor, alongside the specified axis.

#### Arguments:

* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to compute the standard deviation.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
        If `keepdims` is `False`, the rank of the tensor is reduced
        by 1. If `keepdims` is `True`,
        the reduced dimension is retained with length 1.


#### Returns:

A tensor with the standard deviation of elements of `x`.