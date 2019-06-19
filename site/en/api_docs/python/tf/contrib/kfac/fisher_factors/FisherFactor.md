

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.fisher_factors.FisherFactor

## Class `FisherFactor`





Defined in [`tensorflow/contrib/kfac/python/ops/fisher_factors.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/fisher_factors.py).

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

## Properties

<h3 id="name"><code>name</code></h3>





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

<h3 id="left_multiply_matpower"><code>left_multiply_matpower</code></h3>

``` python
left_multiply_matpower(
    x,
    exp,
    damping_func
)
```

Left multiplies 'x' by matrix power of this factor (w/ damping applied).

This calculation is essentially:
  (C + damping * I)**exp * x
where * is matrix-multiplication, ** is matrix power, I is the identity
matrix, and C is the matrix represented by this factor.

x can represent either a matrix or a vector.  For some factors, 'x' might
represent a vector but actually be stored as a 2D matrix for convenience.

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`exp`</b>: float.  The matrix exponent to use.
* <b>`damping_func`</b>: A function that computes a 0-D Tensor or a float which will
    be the damping value used.  i.e. damping = damping_func().


#### Returns:

Tensor of same shape as 'x' representing the result of the multiplication.

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

<h3 id="right_multiply_matpower"><code>right_multiply_matpower</code></h3>

``` python
right_multiply_matpower(
    x,
    exp,
    damping_func
)
```

Right multiplies 'x' by matrix power of this factor (w/ damping applied).

This calculation is essentially:
  x * (C + damping * I)**exp
where * is matrix-multiplication, ** is matrix power, I is the identity
matrix, and C is the matrix represented by this factor.

Unlike left_multiply_matpower, x will always be a matrix.

#### Args:

* <b>`x`</b>: Tensor. Represents a single vector. Shape depends on implementation.
* <b>`exp`</b>: float.  The matrix exponent to use.
* <b>`damping_func`</b>: A function that computes a 0-D Tensor or a float which will
    be the damping value used.  i.e. damping = damping_func().


#### Returns:

Tensor of same shape as 'x' representing the result of the multiplication.



