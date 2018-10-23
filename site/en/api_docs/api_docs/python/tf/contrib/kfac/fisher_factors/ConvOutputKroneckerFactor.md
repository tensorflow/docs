

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.ConvOutputKroneckerFactor

## Class `ConvOutputKroneckerFactor`

Inherits From: [`InverseProvidingFactor`](../../../../tf/contrib/kfac/fisher_factors/InverseProvidingFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Kronecker factor for the output side of a convolutional layer.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(outputs_grads)
```



<h3 id="get_cov"><code>get_cov</code></h3>

``` python
get_cov()
```



<h3 id="get_eigendecomp"><code>get_eigendecomp</code></h3>

``` python
get_eigendecomp()
```



<h3 id="get_inverse"><code>get_inverse</code></h3>

``` python
get_inverse(damping)
```



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

#### Args:

* <b>`damping`</b>: The damping value (float or Tensor) for this factor.

<h3 id="register_eigendecomp"><code>register_eigendecomp</code></h3>

``` python
register_eigendecomp()
```

Registers that an eigendecomposition is needed by a FisherBlock.

<h3 id="register_matpower"><code>register_matpower</code></h3>

``` python
register_matpower(
    exp,
    damping
)
```

Registers a matrix power needed by a FisherBlock.

#### Args:

* <b>`exp`</b>: The exponent (float or Tensor) to raise the matrix to.
* <b>`damping`</b>: The damping value (float or Tensor).



