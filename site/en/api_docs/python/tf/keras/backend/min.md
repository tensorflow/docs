

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.min

``` python
tf.keras.backend.min(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/backend.py).

Minimum value in a tensor.

#### Arguments:

* <b>`x`</b>: A tensor or variable.
* <b>`axis`</b>: An integer, the axis to find minimum values.
* <b>`keepdims`</b>: A boolean, whether to keep the dimensions or not.
        If `keepdims` is `False`, the rank of the tensor is reduced
        by 1. If `keepdims` is `True`,
        the reduced dimension is retained with length 1.


#### Returns:

A tensor with miminum values of `x`.