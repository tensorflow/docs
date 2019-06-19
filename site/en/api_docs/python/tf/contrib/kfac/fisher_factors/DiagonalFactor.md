page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.DiagonalFactor

## Class `DiagonalFactor`

Inherits From: [`FisherFactor`](../../../../tf/contrib/kfac/fisher_factors/FisherFactor)



Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

A base class for FisherFactors that use diagonal approximations.

A DiagonalFactor's covariance variable can be of any shape, but must contain
exactly one entry per parameter.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__()
```



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

Constructs and returns the covariance update Op.

#### Args:

* <b>`ema_decay`</b>: The exponential moving average decay (float or Tensor).

#### Returns:

An Op for updating the covariance Variable referenced by _cov.

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





