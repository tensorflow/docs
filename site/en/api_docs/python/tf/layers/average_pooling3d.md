page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.layers.average_pooling3d


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/layers/pooling.py#L349-L388">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Average pooling layer for 3D inputs (e.g. volumes). (deprecated)

### Aliases:

* <a href="/api_docs/python/tf/layers/average_pooling3d"><code>tf.compat.v1.layers.average_pooling3d</code></a>


``` python
tf.layers.average_pooling3d(
    inputs,
    pool_size,
    strides,
    padding='valid',
    data_format='channels_last',
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use keras.layers.AveragePooling3D instead.

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



#### Raises:


* <b>`ValueError`</b>: if eager execution is enabled.
