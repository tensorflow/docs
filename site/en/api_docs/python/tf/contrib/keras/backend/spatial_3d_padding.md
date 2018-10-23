

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.spatial_3d_padding

### `tf.contrib.keras.backend.spatial_3d_padding`

``` python
spatial_3d_padding(
    x,
    padding=((1, 1), (1, 1), (1, 1)),
    data_format=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Pads 5D tensor with zeros along the depth, height, width dimensions.

Pads these dimensions with respectively
"padding[0]", "padding[1]" and "padding[2]" zeros left and right.

For 'channels_last' data_format,
the 2nd, 3rd and 4th dimension will be padded.
For 'channels_first' data_format,
the 3rd, 4th and 5th dimension will be padded.

#### Arguments:

    x: Tensor or variable.
    padding: Tuple of 3 tuples, padding pattern.
    data_format: One of `channels_last` or `channels_first`.


#### Returns:

    A padded 5D tensor.


#### Raises:

    ValueError: if `data_format` is neither
        `channels_last` or `channels_first`.