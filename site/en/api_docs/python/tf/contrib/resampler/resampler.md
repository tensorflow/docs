

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.resampler.resampler

``` python
tf.contrib.resampler.resampler(
    data,
    warp,
    name='resampler'
)
```



Defined in [`tensorflow/contrib/resampler/python/ops/resampler_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/resampler/python/ops/resampler_ops.py).

Resamples input data at user defined coordinates.

The resampler currently only supports bilinear interpolation of 2D data.

#### Args:

* <b>`data`</b>: Tensor of shape `[batch_size, data_height, data_width,
    data_num_channels]` containing 2D data that will be resampled.
* <b>`warp`</b>: Tensor of minimum rank 2 containing the coordinates at which
    resampling will be performed. Since only bilinear interpolation is
    currently supported, the last dimension of the `warp` tensor must be 2.
* <b>`name`</b>: Optional name of the op.


#### Returns:

Tensor of resampled values from `data`. The output tensor shape is
determined by the shape of the warp tensor. For example, if `data` is of
shape `[batch_size, data_height, data_width, data_num_channels]` and warp of
shape `[batch_size, dim_0, ... , dim_n, 2]` the output will be of shape
`[batch_size, dim_0, ... , dim_n, data_num_channels]`.


#### Raises:

* <b>`ImportError`</b>: if the wrapper generated during compilation is not present when
  the function is called.