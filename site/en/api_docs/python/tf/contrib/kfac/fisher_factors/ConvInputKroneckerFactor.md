page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.ConvInputKroneckerFactor

## Class `ConvInputKroneckerFactor`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Kronecker factor for the input side of a convolutional layer.

Estimates E[ a a^T ] where a is the inputs to a convolutional layer given
example x. Expectation is taken over all examples and locations.

Equivalent to Omega in https://arxiv.org/abs/1602.01407 for details. See
Section 3.1 Estimating the factors.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    inputs,
    filter_shape,
    padding,
    strides=None,
    dilation_rate=None,
    data_format=None,
    extract_patches_fn=None,
    has_bias=False,
    sub_sample_inputs=None,
    sub_sample_patches=None
)
```

Initializes ConvInputKroneckerFactor.

#### Args:

* <b>`inputs`</b>: List of Tensors of shape [batch_size, ..spatial_input_size..,
    in_channels]. Inputs to layer. List index is tower.
* <b>`filter_shape`</b>: List of ints. Contains [..spatial_filter_size..,
    in_channels, out_channels]. Shape of convolution kernel.
* <b>`padding`</b>: str. Padding method for layer. "SAME" or "VALID".
* <b>`strides`</b>: List of ints or None. Contains [..spatial_filter_strides..] if
    'extract_patches_fn' is compatible with tf.nn.convolution(), else
    [1, ..spatial_filter_strides, 1].
* <b>`dilation_rate`</b>: List of ints or None. Rate for dilation along each spatial
    dimension if 'extract_patches_fn' is compatible with
    tf.nn.convolution(), else [1, ..spatial_dilation_rates.., 1].
* <b>`data_format`</b>: str or None. Format of input data.
* <b>`extract_patches_fn`</b>: str or None. Name of function that extracts image
    patches. One of "extract_convolution_patches", "extract_image_patches",
    "extract_pointwise_conv2d_patches".
* <b>`has_bias`</b>: bool. If True, append 1 to in_channel.
* <b>`sub_sample_inputs`</b>: `bool`. If True, then subsample the inputs from which
    the image patches are extracted. (Default: None)
* <b>`sub_sample_patches`</b>: `bool`, If `True` then subsample the extracted
    patches.(Default: None)

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



<h3 id="get_eigendecomp"><code>get_eigendecomp</code></h3>

``` python
get_eigendecomp()
```

Creates or retrieves eigendecomposition of self._cov.

<h3 id="get_inverse"><code>get_inverse</code></h3>

``` python
get_inverse(damping_func)
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

Makes the internal "inverse" variable(s).

<h3 id="make_covariance_update_op"><code>make_covariance_update_op</code></h3>

``` python
make_covariance_update_op(ema_decay)
```

Constructs and returns the covariance update Op.

#### Args:

* <b>`ema_decay`</b>: The exponential moving average decay (float or Tensor).

#### Returns:

An Op for updating the covariance Variable referenced by _cov.

<h3 id="make_inverse_update_ops"><code>make_inverse_update_ops</code></h3>

``` python
make_inverse_update_ops()
```

Create and return update ops corresponding to registered computations.

<h3 id="register_cholesky"><code>register_cholesky</code></h3>

``` python
register_cholesky(damping_func)
```

Registers a Cholesky factor to be maintained and served on demand.

This creates a variable and signals make_inverse_update_ops to make the
corresponding update op.  The variable can be read via the method
get_cholesky.

#### Args:

* <b>`damping_func`</b>: A function that computes a 0-D Tensor or a float which will
    be the damping value used.  i.e. damping = damping_func().

<h3 id="register_cholesky_inverse"><code>register_cholesky_inverse</code></h3>

``` python
register_cholesky_inverse(damping_func)
```

Registers an inverse Cholesky factor to be maintained/served on demand.

This creates a variable and signals make_inverse_update_ops to make the
corresponding update op.  The variable can be read via the method
get_cholesky_inverse.

#### Args:

* <b>`damping_func`</b>: A function that computes a 0-D Tensor or a float which will
    be the damping value used.  i.e. damping = damping_func().

<h3 id="register_inverse"><code>register_inverse</code></h3>

``` python
register_inverse(damping_func)
```



<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(
    exp,
    damping_func
)
```

Registers a matrix power to be maintained and served on demand.

This creates a variable and signals make_inverse_update_ops to make the
corresponding update op.  The variable can be read via the method
get_matpower.

#### Args:

* <b>`exp`</b>: float.  The exponent to use in the matrix power.
* <b>`damping_func`</b>: A function that computes a 0-D Tensor or a float which will
    be the damping value used.  i.e. damping = damping_func().



