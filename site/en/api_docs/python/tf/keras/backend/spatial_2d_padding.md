page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.spatial_2d_padding

Pads the 2nd and 3rd dimensions of a 4D tensor.

### Aliases:

* `tf.compat.v1.keras.backend.spatial_2d_padding`
* `tf.compat.v2.keras.backend.spatial_2d_padding`
* `tf.keras.backend.spatial_2d_padding`

``` python
tf.keras.backend.spatial_2d_padding(
    x,
    padding=((1, 1), (1, 1)),
    data_format=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`x`</b>: Tensor or variable.
* <b>`padding`</b>: Tuple of 2 tuples, padding pattern.
* <b>`data_format`</b>: One of `channels_last` or `channels_first`.


#### Returns:

A padded 4D tensor.



#### Raises:


* <b>`ValueError`</b>: if `data_format` is neither
    `channels_last` or `channels_first`.