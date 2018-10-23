

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.spatial_2d_padding

``` python
tf.keras.backend.spatial_2d_padding(
    x,
    padding=((1, 1), (1, 1)),
    data_format=None
)
```



Defined in [`tensorflow/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/backend.py).

Pads the 2nd and 3rd dimensions of a 4D tensor.

#### Arguments:

* <b>`x`</b>: Tensor or variable.
* <b>`padding`</b>: Tuple of 2 tuples, padding pattern.
* <b>`data_format`</b>: One of `channels_last` or `channels_first`.


#### Returns:

A padded 4D tensor.


#### Raises:

* <b>`ValueError`</b>: if `data_format` is neither
        `channels_last` or `channels_first`.