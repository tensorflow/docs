page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.pool3d

3D Pooling.

### Aliases:

* `tf.compat.v1.keras.backend.pool3d`
* `tf.compat.v2.keras.backend.pool3d`
* `tf.keras.backend.pool3d`

``` python
tf.keras.backend.pool3d(
    x,
    pool_size,
    strides=(1, 1, 1),
    padding='valid',
    data_format=None,
    pool_mode='max'
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`pool_size`</b>: tuple of 3 integers.
* <b>`strides`</b>: tuple of 3 integers.
* <b>`padding`</b>: string, `"same"` or `"valid"`.
* <b>`data_format`</b>: string, `"channels_last"` or `"channels_first"`.
* <b>`pool_mode`</b>: string, `"max"` or `"avg"`.


#### Returns:

A tensor, result of 3D pooling.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither `"channels_last"` or
`"channels_first"`.
* <b>`ValueError`</b>: if `pool_mode` is neither `"max"` or `"avg"`.