

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.pool2d

``` python
pool2d(
    x,
    pool_size,
    strides=(1, 1),
    padding='valid',
    data_format=None,
    pool_mode='max'
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/backend.py).

2D Pooling.

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`pool_size`</b>: tuple of 2 integers.
* <b>`strides`</b>: tuple of 2 integers.
* <b>`padding`</b>: one of `"valid"`, `"same"`.
* <b>`data_format`</b>: one of `"channels_first"`, `"channels_last"`.
* <b>`pool_mode`</b>: one of `"max"`, `"avg"`.


#### Returns:

A tensor, result of 2D pooling.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is neither `channels_last` or
    `channels_first`.
* <b>`ValueError`</b>: if `pool_mode` is neither `max` or `avg`.