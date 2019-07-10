page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.local_conv2d

Apply 2D conv with un-shared weights.

### Aliases:

* `tf.compat.v1.keras.backend.local_conv2d`
* `tf.compat.v2.keras.backend.local_conv2d`
* `tf.keras.backend.local_conv2d`

``` python
tf.keras.backend.local_conv2d(
    inputs,
    kernel,
    kernel_size,
    strides,
    output_shape,
    data_format=None
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`inputs`</b>: 4D tensor with shape:
    (batch_size, filters, new_rows, new_cols)
    if data_format='channels_first'
    or 4D tensor with shape:
    (batch_size, new_rows, new_cols, filters)
    if data_format='channels_last'.
* <b>`kernel`</b>: the unshared weight for convolution,
    with shape (output_items, feature_dim, filters).
* <b>`kernel_size`</b>: a tuple of 2 integers, specifying the
    width and height of the 2D convolution window.
* <b>`strides`</b>: a tuple of 2 integers, specifying the strides
    of the convolution along the width and height.
* <b>`output_shape`</b>: a tuple with (output_row, output_col).
* <b>`data_format`</b>: the data format, channels_first or channels_last.


#### Returns:

A 4D tensor with shape:
(batch_size, filters, new_rows, new_cols)
if data_format='channels_first'
or 4D tensor with shape:
(batch_size, new_rows, new_cols, filters)
if data_format='channels_last'.
