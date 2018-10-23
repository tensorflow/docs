

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.kfac.fisher_factors.FisherFactor

## Class `FisherFactor`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

Base class for objects modeling factors of approximate Fisher blocks.

A FisherFactor represents part of an approximate Fisher Information matrix.
For example, one approximation to the Fisher uses the Kronecker product of two
FisherFactors A and B, F = kron(A, B). FisherFactors are composed with
FisherBlocks to construct a block-diagonal approximation to the full Fisher.

FisherFactors are backed by a single, non-trainable variable that is updated
by running FisherFactor.make_covariance_update_op(). The shape and type of
this variable is implementation specific.

Note that for blocks that aren't based on approximations, a 'factor' can
be the entire block itself, as is the case for the diagonal and full
representations.

Subclasses must implement the _compute_new_cov() method, and the _var_scope
and _cov_shape properties.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__()
```



<h3 id="get_cov"><code>get_cov</code></h3>

``` python
get_cov()
```

Get full covariance matrix.

#### Returns:

Tensor of shape [n, n]. Represents all parameter-parameter correlations
captured by this FisherFactor.

<h3 id="get_cov_var"><code>get_cov_var</code></h3>

``` python
get_cov_var()
```

Get variable backing this FisherFactor.

May or may not be the same as self.get_cov()

#### Returns:

Variable of shape self._cov_shape.

<h3 id="instantiate_covariance"><code>instantiate_covariance</code></h3>

``` python
instantiate_covariance()
```

Instantiates the covariance Variable as the instance member _cov.

<h3 id="left_multiply"><code>left_multiply</code></h3>

``` python
left_multiply(
    x,
    damping
)
```

Multiplies 'x' by the damped covariance of this factor.

Let C be the covariance matrix this factor represents, and
D = C + damping * I be its damped variant. This method calculates
matmul(D, vec(x)).

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`damping`</b>: 0-D Tensor. Damping to add to C's diagonal.


#### Returns:

Tensor of same shape as 'x'.

<h3 id="left_multiply_inverse"><code>left_multiply_inverse</code></h3>

``` python
left_multiply_inverse(
    x,
    damping
)
```

Multiplies 'x' by damped inverse of this factor.

Let C be the covariance matrix this factor represents and
E = inv(C + damping * I) be its damped inverse. This method calculates
matmul(E, vec(x)).

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`damping`</b>: 0-D Tensor. Damping to add to C's diagonal.


#### Returns:

Tensor of same shape as 'x'.

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

<h3 id="right_multiply"><code>right_multiply</code></h3>

``` python
right_multiply(
    x,
    damping
)
```

Multiplies 'x' by the damped covariance of this factor.

Let C be the covariance matrix this factor represents, and
D = C + damping * I be its damped variant. This method calculates
matmul(vec(x), D).

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`damping`</b>: 0-D Tensor. Damping to add to C's diagonal.


#### Returns:

Tensor of same shape as 'x'.

<h3 id="right_multiply_inverse"><code>right_multiply_inverse</code></h3>

``` python
right_multiply_inverse(
    x,
    damping
)
```

Multiplies 'x' by damped inverse of this factor.

Let C be the covariance matrix this factor represents and
E = inv(C + damping * I) be its damped inverse. This method calculates
matmul(vec(x), E).

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`damping`</b>: 0-D Tensor. Damping to add to C's diagonal.


#### Returns:

Tensor of same shape as 'x'.



