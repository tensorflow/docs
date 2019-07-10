page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.resize_volumes

Resizes the volume contained in a 5D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.resize_volumes`
* `tf.compat.v2.keras.backend.resize_volumes`
* `tf.keras.backend.resize_volumes`

``` python
tf.keras.backend.resize_volumes(
    x,
    depth_factor,
    height_factor,
    width_factor,
    data_format
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable to resize.
* <b>`depth_factor`</b>: Positive integer.
* <b>`height_factor`</b>: Positive integer.
* <b>`width_factor`</b>: Positive integer.
* <b>`data_format`</b>: One of `"channels_first"`, `"channels_last"`.


#### Returns:

A tensor.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither
    `channels_last` or `channels_first`.