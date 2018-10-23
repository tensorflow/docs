

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.layers.max_pooling1d

``` python
tf.layers.max_pooling1d(
    inputs,
    pool_size,
    strides,
    padding='valid',
    data_format='channels_last',
    name=None
)
```



Defined in [`tensorflow/python/layers/pooling.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/python/layers/pooling.py).

Max Pooling layer for 1D inputs.

#### Arguments:

* <b>`inputs`</b>: The tensor over which to pool. Must have rank 3.
* <b>`pool_size`</b>: An integer or tuple/list of a single integer,
    representing the size of the pooling window.
* <b>`strides`</b>: An integer or tuple/list of a single integer, specifying the
    strides of the pooling operation.
* <b>`padding`</b>: A string. The padding method, either 'valid' or 'same'.
    Case-insensitive.
* <b>`data_format`</b>: A string, one of `channels_last` (default) or `channels_first`.
    The ordering of the dimensions in the inputs.
    `channels_last` corresponds to inputs with shape
    `(batch, length, channels)` while `channels_first` corresponds to
    inputs with shape `(batch, channels, length)`.
* <b>`name`</b>: A string, the name of the layer.


#### Returns:

The output tensor, of rank 3.


#### Raises:

* <b>`ValueError`</b>: if eager execution is enabled.