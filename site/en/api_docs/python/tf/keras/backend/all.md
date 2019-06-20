page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.all

``` python
tf.keras.backend.all(
    x,
    axis=None,
    keepdims=False
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/backend.py).

Bitwise reduction (logical AND).

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`axis`</b>: axis along which to perform the reduction.
* <b>`keepdims`</b>: whether the drop or broadcast the reduction axes.


#### Returns:

A uint8 tensor (0s and 1s).