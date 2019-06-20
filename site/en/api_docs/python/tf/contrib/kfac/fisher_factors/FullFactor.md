page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.FullFactor

## Class `FullFactor`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

FisherFactor for a full matrix representation of the Fisher of a parameter.

Note that this uses the naive "square the sum estimator", and so is applicable
to any type of parameter in principle, but has very high variance.

## Properties

<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    params_grads,
    batch_size
)
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



