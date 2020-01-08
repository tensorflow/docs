

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.extract_pointwise_conv2d_patches

``` python
tf.contrib.kfac.utils.extract_pointwise_conv2d_patches(
    inputs,
    filter_shape,
    name=None,
    data_format=None
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/utils.py).

Extract patches for a 1x1 conv2d.

#### Args:

* <b>`inputs`</b>: 4-D Tensor of shape [batch_size, height, width, in_channels].
* <b>`filter_shape`</b>: List of 4 ints. Shape of filter to apply with conv2d()
* <b>`name`</b>: None or str. Name for Op.
* <b>`data_format`</b>: None or str. Format for data. See 'data_format' in
    tf.nn.conv2d() for details.


#### Returns:

Tensor of shape [batch_size, ..spatial_input_shape..,
..spatial_filter_shape.., in_channels]


#### Raises:

* <b>`ValueError`</b>: if inputs is not 4-D.
* <b>`ValueError`</b>: if filter_shape is not [1, 1, ?, ?]
* <b>`ValueError`</b>: if data_format is not channels-last.