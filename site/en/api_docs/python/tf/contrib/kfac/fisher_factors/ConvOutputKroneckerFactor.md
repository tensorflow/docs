

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.ConvOutputKroneckerFactor

## Class `ConvOutputKroneckerFactor`

Inherits From: [`InverseProvidingFactor`](../../../../tf/contrib/kfac/fisher_factors/InverseProvidingFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Kronecker factor for the output side of a convolutional layer.

Estimates E[ ds ds^T ] where s is the preactivations of a convolutional layer
given example x and ds = (d / d s) log(p(y|x, w)). Expectation is taken over
all examples and locations.

Equivalent to Gamma in https://arxiv.org/abs/1602.01407 for details. See
Section 3.1 Estimating the factors.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(outputs_grads)
```

Initializes ConvOutputKroneckerFactor.

#### Args:

* <b>`outputs_grads`</b>: list of Tensors. Each Tensor is of shape
      [batch_size, height, width, out_channels].

<h3 id="get_cov"><code>get_cov</code></h3>

``` python
get_cov()
```



<h3 id="get_damped_inverse"><code>get_damped_inverse</code></h3>

``` python
get_damped_inverse(damping)
```



<h3 id="get_eigendecomp"><code>get_eigendecomp</code></h3>

``` python
get_eigendecomp()
```

Creates or retrieves eigendecomposition of self._cov.

<h3 id="get_matpower"><code>get_matpower</code></h3>

``` python
get_matpower(
    exp,
    damping
)
```



<h3 id="instantiate_covariance"><code>instantiate_covariance</code></h3>

``` python
instantiate_covariance()
```

Instantiates the covariance Variable as the instance member _cov.

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

<h3 id="register_damped_inverse"><code>register_damped_inverse</code></h3>

``` python
register_damped_inverse(damping)
```

Registers a damped inverse needed by a FisherBlock.

This creates a variable and signals make_inverse_update_ops to make the
corresponding update op.  The variable can be read via the method
get_inverse.

#### Args:

* <b>`damping`</b>: The damping value (float or Tensor) for this factor.

<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(
    exp,
    damping
)
```

Registers a matrix power needed by a FisherBlock.

This creates a variable and signals make_inverse_update_ops to make the
corresponding update op.  The variable can be read via the method
get_matpower.

#### Args:

* <b>`exp`</b>: The exponent (float or Tensor) to raise the matrix to.
* <b>`damping`</b>: The damping value (float or Tensor).

<h3 id="reset_eigendecomp"><code>reset_eigendecomp</code></h3>

``` python
reset_eigendecomp()
```





