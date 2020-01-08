

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.ConvDiagonalFactor

## Class `ConvDiagonalFactor`

Inherits From: [`DiagonalFactor`](../../../../tf/contrib/kfac/fisher_factors/DiagonalFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

FisherFactor for a diagonal approx of a convolutional layer's Fisher.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    inputs,
    outputs_grads,
    filter_shape,
    strides,
    padding,
    data_format=None,
    dilations=None,
    has_bias=False
)
```

Creates a ConvDiagonalFactor object.

#### Args:

* <b>`inputs`</b>: List of Tensors of shape [batch_size, height, width, in_channels].
    Input activations to this layer.  List index is towers.
* <b>`outputs_grads`</b>: List of Tensors, each of shape [batch_size,
    height, width, out_channels], which are the gradients of the loss
    with respect to the layer's outputs.  First index is source, second
    index is tower.
* <b>`filter_shape`</b>: Tuple of 4 ints: (kernel_height, kernel_width, in_channels,
    out_channels). Represents shape of kernel used in this layer.
* <b>`strides`</b>: The stride size in this layer (1-D Tensor of length 4).
* <b>`padding`</b>: The padding in this layer (1-D of Tensor length 4).
* <b>`data_format`</b>: None or str. Format of conv2d inputs.
* <b>`dilations`</b>: None or tuple of 4 ints.
* <b>`has_bias`</b>: Python bool. If True, the layer is assumed to have a bias
    parameter in addition to its filter parameter.


#### Raises:

* <b>`ValueError`</b>: If inputs, output_grads, and filter_shape do not agree on
    in_channels or out_channels.
* <b>`ValueError`</b>: If strides, dilations are not length-4 lists of ints.
* <b>`ValueError`</b>: If data_format does not put channel last.

<h3 id="get_cholesky"><code>get_cholesky</code></h3>

``` python
get_cholesky(damping_func)
```



<h3 id="get_cholesky_inverse"><code>get_cholesky_inverse</code></h3>

``` python
get_cholesky_inverse(damping_func)
```



<h3 id="get_cov"><code>get_cov</code></h3>

``` python
get_cov()
```



<h3 id="get_cov_as_linear_operator"><code>get_cov_as_linear_operator</code></h3>

``` python
get_cov_as_linear_operator()
```



<h3 id="get_matpower"><code>get_matpower</code></h3>

``` python
get_matpower(
    exp,
    damping_func
)
```



<h3 id="instantiate_cov_variables"><code>instantiate_cov_variables</code></h3>

``` python
instantiate_cov_variables()
```

Makes the internal cov variable(s).

<h3 id="instantiate_inv_variables"><code>instantiate_inv_variables</code></h3>

``` python
instantiate_inv_variables()
```



<h3 id="make_covariance_update_op"><code>make_covariance_update_op</code></h3>

``` python
make_covariance_update_op(ema_decay)
```



<h3 id="make_inverse_update_ops"><code>make_inverse_update_ops</code></h3>

``` python
make_inverse_update_ops()
```



<h3 id="register_cholesky"><code>register_cholesky</code></h3>

``` python
register_cholesky(damping_func)
```



<h3 id="register_cholesky_inverse"><code>register_cholesky_inverse</code></h3>

``` python
register_cholesky_inverse(damping_func)
```



<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(
    exp,
    damping_func
)
```





