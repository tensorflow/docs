page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.max_pool2d

``` python
tf.contrib.layers.max_pool2d(
    inputs,
    kernel_size,
    stride=2,
    padding='VALID',
    data_format=DATA_FORMAT_NHWC,
    outputs_collections=None,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/layers/python/layers/layers.py).

See the guide: [Layers (contrib) > Higher level ops for building neural network layers](../../../../../api_guides/python/contrib.layers#Higher_level_ops_for_building_neural_network_layers)

Adds a 2D Max Pooling op.

It is assumed that the pooling is done per image but not in batch or channels.

#### Args:

* <b>`inputs`</b>: A 4-D tensor of shape `[batch_size, height, width, channels]` if
    `data_format` is `NHWC`, and `[batch_size, channels, height, width]` if
    `data_format` is `NCHW`.
* <b>`kernel_size`</b>: A list of length 2: [kernel_height, kernel_width] of the
    pooling kernel over which the op is computed. Can be an int if both
    values are the same.
* <b>`stride`</b>: A list of length 2: [stride_height, stride_width].
    Can be an int if both strides are the same. Note that presently
    both strides must have the same value.
* <b>`padding`</b>: The padding method, either 'VALID' or 'SAME'.
* <b>`data_format`</b>: A string. `NHWC` (default) and `NCHW` are supported.
* <b>`outputs_collections`</b>: The collections to which the outputs are added.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A `Tensor` representing the results of the pooling operation.


#### Raises:

* <b>`ValueError`</b>: If `data_format` is neither `NHWC` nor `NCHW`.
* <b>`ValueError`</b>: If 'kernel_size' is not a 2-D list