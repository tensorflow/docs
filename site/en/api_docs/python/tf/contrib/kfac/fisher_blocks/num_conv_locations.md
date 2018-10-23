

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_blocks.num_conv_locations

``` python
tf.contrib.kfac.fisher_blocks.num_conv_locations(
    input_shape,
    strides
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_blocks.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_blocks.py).

Returns the number of spatial locations a 2D Conv kernel is applied to.

#### Args:

* <b>`input_shape`</b>: list representing shape of inputs to the Conv layer.
* <b>`strides`</b>: list representing strides for the Conv kernel.


#### Returns:

A scalar |T| denoting the number of spatial locations for the Conv layer.