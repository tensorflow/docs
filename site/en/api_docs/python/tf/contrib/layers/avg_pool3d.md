page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.layers.avg_pool3d

``` python
tf.contrib.layers.avg_pool3d(
    inputs,
    kernel_size,
    stride=2,
    padding='VALID',
    data_format=DATA_FORMAT_NDHWC,
    outputs_collections=None,
    scope=None
)
```



Defined in [`tensorflow/contrib/layers/python/layers/layers.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/layers/python/layers/layers.py).

Adds a 3D average pooling op.

It is assumed that the pooling is done per image but not in batch or channels.

#### Args:

* <b>`inputs`</b>: A 5-D tensor of shape `[batch_size, depth, height, width, channels]`
    if `data_format` is `NDHWC`, and `[batch_size, channels, depth, height,
    width]` if `data_format` is `NCDHW`.
* <b>`kernel_size`</b>: A list of length 3: [kernel_depth, kernel_height, kernel_width]
    of the pooling kernel over which the op is computed. Can be an int if both
    values are the same.
* <b>`stride`</b>: A list of length 3: [stride_depth, stride_height, stride_width].
    Can be an int if both strides are the same. Note that presently
    both strides must have the same value.
* <b>`padding`</b>: The padding method, either 'VALID' or 'SAME'.
* <b>`data_format`</b>: A string. `NDHWC` (default) and `NCDHW` are supported.
* <b>`outputs_collections`</b>: The collections to which the outputs are added.
* <b>`scope`</b>: Optional scope for name_scope.


#### Returns:

A `Tensor` representing the results of the pooling operation.


#### Raises:

* <b>`ValueError`</b>: If `data_format` is neither `NDHWC` nor `NCDHW`.