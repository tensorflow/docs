page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.extract_convolution_patches

``` python
tf.contrib.kfac.utils.extract_convolution_patches(
    inputs,
    filter_shape,
    padding,
    strides=None,
    dilation_rate=None,
    name=None,
    data_format=None
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/utils.py).

Extracts inputs to each output coordinate in tf.nn.convolution.

This is a generalization of tf.extract_image_patches() to tf.nn.convolution(),
where the number of spatial dimensions may be something other than 2.

Assumes,
- First dimension of inputs is batch_size
- Convolution filter is applied to all input channels.

#### Args:

* <b>`inputs`</b>: Tensor of shape [batch_size, ..spatial_image_shape..,
    ..spatial_filter_shape.., in_channels]. Inputs to tf.nn.convolution().
* <b>`filter_shape`</b>: List of ints. Shape of filter passed to tf.nn.convolution().
* <b>`padding`</b>: string. Padding method. One of "VALID", "SAME".
* <b>`strides`</b>: None or list of ints. Strides along spatial dimensions.
* <b>`dilation_rate`</b>: None or list of ints. Dilation along spatial dimensions.
* <b>`name`</b>: None or str. Name of Op.
* <b>`data_format`</b>: None or str. Format of data.


#### Returns:

Tensor of shape [batch_size, ..spatial_image_shape..,
  ..spatial_filter_shape.., in_channels]


#### Raises:

* <b>`ValueError`</b>: If data_format does not put channel last.
* <b>`ValueError`</b>: If inputs and filter disagree on in_channels.