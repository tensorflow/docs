

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.layers.max_pooling3d

### `tf.layers.max_pooling3d`

``` python
max_pooling3d(
    inputs,
    pool_size,
    strides,
    padding='valid',
    data_format='channels_last',
    name=None
)
```



Defined in [`tensorflow/python/layers/pooling.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/layers/pooling.py).

Max pooling layer for 3D inputs (e.g. volumes).

#### Arguments:

* <b>`inputs`</b>: The tensor over which to pool. Must have rank 5.
* <b>`pool_size`</b>: An integer or tuple/list of 3 integers:
    (pool_depth, pool_height, pool_width)
    specifying the size of the pooling window.
    Can be a single integer to specify the same value for
    all spatial dimensions.
* <b>`strides`</b>: An integer or tuple/list of 3 integers,
    specifying the strides of the pooling operation.
    Can be a single integer to specify the same value for
    all spatial dimensions.
* <b>`padding`</b>: A string. The padding method, either 'valid' or 'same'.
    Case-insensitive.
* <b>`data_format`</b>: A string. The ordering of the dimensions in the inputs.
    `channels_last` (default) and `channels_first` are supported.
    `channels_last` corresponds to inputs with shape
    `(batch, depth, height, width, channels)` while `channels_first`
    corresponds to inputs with shape
    `(batch, channels, depth, height, width)`.
* <b>`name`</b>: A string, the name of the layer.


#### Returns:

  Output tensor.